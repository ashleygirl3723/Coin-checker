"""
Coin Checker — snap a coin, find out if it's worth something.

How it works:
  1. Take a photo (or upload one) of a coin, front and back if you can.
  2. The AI reads the denomination, date, mint mark, and anything odd.
  3. The app matches what it sees against a curated database of valuable
     error coins, key dates, and silver coins — and gives you a verdict.

What it is NOT: a certified appraisal. It's triage. If it flags a possible
jackpot, don't clean the coin — get it authenticated/graded (PCGS / NGC).

Run it:
  pip install -r requirements.txt
  streamlit run app.py

Deploy free: see README.md (GitHub + Streamlit Cloud, same as her other apps).
"""

import base64
import io
import json
import os
import re
from datetime import datetime

import streamlit as st
from openai import OpenAI
from PIL import Image

from coin_data import DATA, GLOSSARY, SCREENING_RULES

# ---------------------------------------------------------------------------
# Settings
# ---------------------------------------------------------------------------
PROVIDERS = {
    "OpenRouter (free models, no card)": "https://openrouter.ai/api/v1",
    "OpenAI": "https://api.openai.com/v1",
}
DEFAULT_MODEL = "google/gemma-4-26b-a4b-it:free"  # free, sees images
HISTORY_FILE = "history.json"
MAX_IMAGE_SIDE = 1568

VISION_SYSTEM = """You are a coin-reading assistant. Look at the coin photo(s) and
return ONLY a JSON object, no other text, with these fields:
{
  "denomination": "cent" | "nickel" | "dime" | "quarter" | "half dollar" | "dollar" | "unknown",
  "year": "YYYY" or "unknown",
  "mint_mark": "P" | "D" | "S" | "W" | "none" | "unknown",
  "side_shown": "obverse" | "reverse" | "both" | "unknown",
  "legible": true | false,
  "anomalies": ["short plain-English notes about anything odd: doubling, missing details, off-center, wrong color, clips, extra metal, etc."],
  "surface_notes": "one line on condition: wear, shine, corrosion, damage",
  "confidence": "high" | "medium" | "low",
  "read_notes": "one line: what you could and couldn't make out"
}
Be honest: if the photo is blurry or the date is unreadable, say so with
"unknown" and low confidence rather than guessing. Never invent a date."""

ANOMALY_OPTIONS = [
    "doubling on letters/date",
    "letters or details look doubled but flat/shelf-like",
    "off-center / part of design missing",
    "wrong color for its year",
    "sticks to a magnet (or doesn't, when it should)",
    "bite or clip missing from edge",
    "coin wider than normal, no rim",
    "extra metal / blob / crack lines",
    "looks silvery (possible silver)",
    "mint mark looks doubled or odd",
    "design looks rotated / misaligned",
    "other weirdness",
]

# ---------------------------------------------------------------------------
# History helpers
# ---------------------------------------------------------------------------
def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE) as f:
                return json.load(f)
        except Exception:
            return []
    return []


def save_entry(entry):
    history = load_history()
    history.insert(0, entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)


# ---------------------------------------------------------------------------
# Image helpers
# ---------------------------------------------------------------------------
def shrink(img):
    w, h = img.size
    if max(w, h) > MAX_IMAGE_SIDE:
        scale = MAX_IMAGE_SIDE / max(w, h)
        img = img.resize((int(w * scale), int(h * scale)))
    return img


def image_part(img):
    buf = io.BytesIO()
    shrink(img).save(buf, format="JPEG", quality=85)
    b64 = base64.b64encode(buf.getvalue()).decode()
    return {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}}


def pil_from_uploads(files):
    images = []
    for f in files:
        try:
            images.append(Image.open(f).convert("RGB"))
        except Exception:
            pass
    return images


# ---------------------------------------------------------------------------
# The matcher — AI read (or manual entry) vs the coin database
# ---------------------------------------------------------------------------
def _norm_year(y):
    if y is None:
        return None
    m = re.search(r"((?:17|18|19|20)\d{2})", str(y))
    return int(m.group(1)) if m else None


STOPWORDS = {
    "the", "and", "for", "with", "are", "from", "that", "this", "was", "were",
    "has", "have", "but", "you", "your", "its", "all", "any", "can", "may",
    "when", "which", "while", "than", "then", "them", "they", "their", "there",
    "these", "those", "into", "over", "under", "such", "like", "just", "also",
    "only", "very", "more", "most", "many", "much", "well", "still", "even",
    "ever", "each", "every", "both", "between", "through", "during", "before",
    "after", "above", "below", "out", "about", "onto", "upon", "within",
    "without", "one", "two", "coin", "coins", "some", "look", "looks",
    "normal", "common", "regular", "usual", "typical", "standard",
}


def _keywords(text):
    return set(re.findall(r"[a-z]{3,}", (text or "").lower())) - STOPWORDS


def _denom_match(entry, denom):
    d = entry.get("denomination")
    if d is None:
        return True  # entry applies to any denomination
    ds = [d] if isinstance(d, str) else (d or [])
    return bool(denom) and denom in ds


def _year_status(entry, year):
    """'match' | 'mismatch' | 'unknown' (no usable year) | 'any' (entry has no year bounds)."""
    exact = entry.get("year")
    lo, hi = entry.get("year_min"), entry.get("year_max")
    if exact is not None:
        if year is None:
            return "unknown"
        return "match" if year == exact else "mismatch"
    if lo is not None or hi is not None:
        if year is None:
            return "unknown"
        if lo is not None and year < lo:
            return "mismatch"
        if hi is not None and year > hi:
            return "mismatch"
        return "match"
    return "any"


def match_coin(denomination, year, mint_mark, anomalies):
    """Score every database entry against what we know. Returns sorted hits."""
    year = _norm_year(year)
    mint = (mint_mark or "").upper().strip() or None
    if mint == "NONE":
        mint = "none"
    if mint == "UNKNOWN":
        mint = None  # unreadable mint stays permissive
    denom = (denomination or "").lower().strip() or None
    if denom == "unknown":
        denom = None
    anomaly_words = _keywords(" ".join(anomalies or []))

    hits = []
    for entry in DATA:
        score = 0
        reasons = []
        needs = 4

        # Denomination — a different denomination rules the entry out
        if entry.get("denomination") is None:
            score += 1
            reasons.append("any denomination")
        elif _denom_match(entry, denom):
            score += 3
            reasons.append("denomination")
        elif denom is None:
            needs = 6
            reasons.append("denomination unconfirmed")
        else:
            continue

        # Year
        ystat = _year_status(entry, year)
        if ystat == "match":
            score += 3
            reasons.append(f"year {year}")
        elif ystat == "any":
            if year is not None:
                score += 1
        elif ystat == "unknown":
            needs = 6
            reasons.append("date unconfirmed — verify the date")
        else:  # mismatch: this entry can't be the coin
            continue

        # Mint mark — a known, conflicting mint mark rules the entry out
        if entry["mint"] is not None and mint is not None:
            if mint.lower() in [m.lower() for m in entry["mint"]]:
                score += 2
                reasons.append(f"mint {mint}")
            else:
                continue

        # Visual keyword overlap (stopwords removed).
        # Error entries need SOMETHING odd actually observed — no flagging
        # jackpots on perfectly ordinary coins.
        overlap = anomaly_words & _keywords(entry["look_for"])
        if entry["category"] == "error" and not overlap:
            continue
        if overlap:
            score += min(len(overlap), 3)
            reasons.append("visual match: " + ", ".join(sorted(overlap)[:4]))

        if score >= needs:
            hits.append({"entry": entry, "score": score, "reasons": reasons})
    hits.sort(key=lambda h: (h["entry"]["heat"] == "jackpot", h["score"]), reverse=True)
    return hits


def silver_note(denomination, year):
    """Quick melt-value flags that don't need the database."""
    year = _norm_year(year)
    denom = (denomination or "").lower()
    notes = []
    if year and denom in ("dime", "quarter", "half dollar", "dollar"):
        if year <= 1964:
            notes.append("Dated 1964 or earlier — that's 90% silver, worth well above face value for melt alone.")
        elif denom == "half dollar" and 1965 <= year <= 1970:
            notes.append("1965-1970 half dollar — 40% silver, worth above face value.")
    if year and denom == "nickel" and 1942 <= year <= 1945:
        notes.append("1942-1945 nickel — check for a LARGE mint mark above Monticello on the back. If it's there, it's a 35% silver war nickel.")
    if year == 1943 and denom == "cent":
        notes.append("1943 cent: most are steel (magnetic, worth little). If yours is copper-colored and NOT magnetic, stop — that may be the six-figure one.")
    return notes


def verdict_block(coin_desc, hits, notes):
    jackpots = [h for h in hits if h["entry"]["heat"] == "jackpot"]
    if hits and hits[0]["entry"].get("replica_only"):
        st.info(f"## 🪙 Almost certainly a replica — {coin_desc}")
        st.markdown("Only 5 genuine 1913 Liberty nickels exist, all in museums or major collections. "
                    "One in a coin jar is a novelty copy — fun, but not valuable.")
    elif jackpots:
        st.success(f"## 🔥 Possible jackpot — {coin_desc}")
        st.markdown("**Do not clean it. Do not spend it.** A real one in this group can be worth serious money — "
                    "authentication/grading (PCGS or NGC) is the next step.")
    elif hits:
        st.warning(f"## 👀 Worth a closer look — {coin_desc}")
        st.markdown("Something about this coin lines up with coins that carry a premium. "
                    "Check the details below against your coin before you get excited.")
    else:
        st.info(f"## 🪙 Looks like face value — {coin_desc}")
        st.markdown("Nothing in the database matched. Most pocket change lands here — "
                    "but the silver notes below are still worth a glance.")
    for h in hits:
        e = h["entry"]
        with st.expander(f"{'🔥' if e['heat'] == 'jackpot' else '👀'} {e['name']} — "
                          f"about ${e['value_low']:,}–${e['value_high']:,} ({e['value_note']})"):
            st.markdown(f"**Look for:** {e['look_for']}")
            st.caption(f"Matched on: {', '.join(h['reasons'])} · Category: {e['category']}")
    if notes:
        st.subheader("Silver / melt notes")
        for n in notes:
            st.markdown(f"- {n}")


# ---------------------------------------------------------------------------
# Page
# ---------------------------------------------------------------------------
st.set_page_config(page_title="Coin Checker", page_icon="🪙", layout="centered")
st.title("🪙 Coin Checker")
st.caption("Snap a coin, get an instant read: error, key date, silver, or face value.")

st.warning("Coin Checker is **triage, not an appraisal**. It flags coins worth a second look — "
           "it can't certify anything from a photo. Big potential finds deserve PCGS/NGC grading. "
           "And never clean a coin that might be valuable.")

# --- Sidebar: brain ---
st.sidebar.subheader("The brain")
provider_label = st.sidebar.selectbox("Provider", list(PROVIDERS.keys()))
base_url = PROVIDERS[provider_label]
api_key = st.sidebar.text_input("API key", type="password",
                                help="Pasted here it lives only in this session. On Streamlit Cloud, use Settings → Secrets instead.")
api_key = api_key or st.secrets.get("OPENROUTER_API_KEY") or st.secrets.get("OPENAI_API_KEY") or os.environ.get("OPENROUTER_API_KEY") or os.environ.get("OPENAI_API_KEY")
model = st.sidebar.text_input("Model", value=DEFAULT_MODEL,
                              help="Any vision-capable chat model on the provider. Free OpenRouter options that see images: google/gemma-4-26b-a4b-it:free, nvidia/nemotron-3.5-super-vl:free, openrouter/free.")
st.sidebar.caption("🔒 Photos are sent to the AI provider for analysis.")

st.sidebar.divider()
st.sidebar.subheader("Quick screening rules")
for rule in SCREENING_RULES:
    st.sidebar.markdown(f"- {rule}")

tab_photo, tab_manual, tab_guide, tab_history = st.tabs(
    ["📸 Check a coin", "⌨️ Manual lookup", "📖 Error guide", "🕘 History"])


def run_check(images, denomination, year, mint_mark, anomalies, source_label):
    """Call the vision model (if photos given), match, render, save."""
    read = None
    if images:
        if not api_key:
            st.error("Add your API key in the sidebar first — the app can't see without it. (Free OpenRouter key: openrouter.ai/keys)")
            return
        parts = [{"type": "text", "text": "Read this coin. Return ONLY the JSON object."}]
        for img in images:
            parts.append(image_part(img))
        try:
            with st.spinner("Reading the coin…"):
                client = OpenAI(api_key=api_key, base_url=base_url)
                reply = client.chat.completions.create(
                    model=model,
                    messages=[{"role": "system", "content": VISION_SYSTEM},
                              {"role": "user", "content": parts}],
                )
            raw = reply.choices[0].message.content
            m = re.search(r"\{.*\}", raw, re.DOTALL)
            read = json.loads(m.group(0)) if m else json.loads(raw)
            denomination = read.get("denomination") or denomination
            year = read.get("year") or year
            mint_mark = read.get("mint_mark") or mint_mark
            anomalies = (anomalies or []) + (read.get("anomalies") or [])
        except Exception as e:
            st.error(f"The AI couldn't read the photo: {e}")
            st.caption("Tip: retake with the coin filling the frame, in bright indirect light, both sides.")
            return

    coin_desc = " ".join(x for x in [str(year) if year and str(year) != "unknown" else "",
                                     str(mint_mark) if mint_mark and str(mint_mark) not in ("unknown", "none") else "",
                                     denomination if denomination and denomination != "unknown" else "coin"] if x).strip() or "this coin"
    hits = match_coin(denomination, year, mint_mark, anomalies)
    notes = silver_note(denomination, year)

    if read:
        with st.expander("What the AI saw in your photo"):
            st.json(read)

    verdict_block(coin_desc, hits, notes)

    save_entry({
        "time": datetime.now().strftime("%b %d, %I:%M %p"),
        "source": source_label,
        "coin": coin_desc,
        "denomination": denomination, "year": str(year), "mint": str(mint_mark),
        "anomalies": anomalies,
        "hits": [h["entry"]["name"] for h in hits],
        "top_heat": hits[0]["entry"]["heat"] if hits else "face",
    })


# ---------------------------------------------------------------------------
# Tab 1: photo check
# ---------------------------------------------------------------------------
with tab_photo:
    st.markdown("Photograph the **front and back** — the more of the frame the coin fills, the better the read.")
    col1, col2 = st.columns(2)
    with col1:
        cam = st.camera_input("Take a photo")
    with col2:
        uploads = st.file_uploader("Or upload photos", type=["png", "jpg", "jpeg"],
                                   accept_multiple_files=True)
    extra = st.text_input("Anything odd you've noticed? (optional)",
                          placeholder="e.g. the letters look doubled, edge looks clipped")
    images = []
    if cam:
        images.append(Image.open(cam).convert("RGB"))
    images += pil_from_uploads(uploads or [])
    if images:
        st.image(images, width=220, caption=["photo"] * len(images))
    if st.button("Check this coin", type="primary", use_container_width=True, key="photo_go"):
        if not images:
            st.warning("Take or upload a photo first.")
        else:
            run_check(images, None, None, None, [extra] if extra.strip() else [], "photo")

# ---------------------------------------------------------------------------
# Tab 2: manual lookup (no photo / no key needed)
# ---------------------------------------------------------------------------
with tab_manual:
    st.markdown("No photo? No API key? Describe the coin and check it against the database directly.")
    mcol1, mcol2, mcol3 = st.columns(3)
    with mcol1:
        mdenom = st.selectbox("Denomination",
                              ["cent", "nickel", "dime", "quarter", "half dollar", "dollar"])
    with mcol2:
        myear = st.text_input("Year", placeholder="e.g. 1955")
    with mcol3:
        mmint = st.selectbox("Mint mark", ["unknown", "none", "P", "D", "S", "W"])
    manom = st.multiselect("Anything odd about it?", ANOMALY_OPTIONS)
    if st.button("Look it up", type="primary", use_container_width=True, key="manual_go"):
        run_check([], mdenom, myear, mmint, manom, "manual")

# ---------------------------------------------------------------------------
# Tab 3: error guide
# ---------------------------------------------------------------------------
with tab_guide:
    st.subheader("Know your errors")
    for term, desc in GLOSSARY.items():
        with st.expander(term):
            st.markdown(desc)
    st.subheader("Before you spend it — 60-second screening")
    for i, rule in enumerate(SCREENING_RULES, 1):
        st.markdown(f"**{i}.** {rule}")

# ---------------------------------------------------------------------------
# Tab 4: history
# ---------------------------------------------------------------------------
with tab_history:
    history = load_history()
    if not history:
        st.caption("Nothing checked yet — your checks will land here.")
    else:
        for h in history:
            icon = {"jackpot": "🔥", "look": "👀"}.get(h.get("top_heat"), "🪙")
            with st.expander(f"{icon} {h['time']} — {h['coin']}"):
                st.caption(f"via {h.get('source', '?')}")
                if h.get("anomalies"):
                    st.markdown("**Noted:** " + "; ".join(h["anomalies"]))
                if h["hits"]:
                    st.markdown("**Flagged:** " + "; ".join(h["hits"]))
                else:
                    st.markdown("No database matches — face value.")
        if st.button("Clear history"):
            if os.path.exists(HISTORY_FILE):
                os.remove(HISTORY_FILE)
            st.rerun()
