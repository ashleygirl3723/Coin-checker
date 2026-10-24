# 🪙 Coin Checker

Snap a coin, get an instant read: error, key date, silver, or face value.
Built with Streamlit + a vision-capable AI model. Triage, not an appraisal —
big potential finds still deserve PCGS/NGC grading.

## Run it locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy it free (GitHub + Streamlit Cloud)

1. Create a repo at github.com called `coin-checker` and push this folder:
   ```bash
   git init && git add . && git commit -m "Coin Checker v1"
   git branch -M main && git remote add origin git@github.com:ashleygirl3723/coin-checker.git
   git push -u origin main
   ```
2. Go to share.streamlit.io → New app → pick the `coin-checker` repo, `app.py`.
3. Settings → Secrets, add your key:
   ```toml
   OPENROUTER_API_KEY = "paste-your-key-here"
   ```
   Free key, no card: openrouter.ai/keys
4. Deploy, then flip **Settings → Sharing → Public** so it opens without a login.

On your phone's browser the app can use the camera directly — that's the whole point.

## How it works

- **📸 Check a coin**: photo (camera or upload) → AI reads denomination, date,
  mint mark, and anything odd → matched against `coin_data.py` (valuable errors,
  key dates, silver rules) → verdict: 🔥 jackpot / 👀 worth a look / 🪙 face value.
- **⌨️ Manual lookup**: no photo or key needed — describe the coin, same database.
- **📖 Error guide**: doubled die vs machine doubling, off-center, clips, cuds…
  plus the 60-second screening rules (scale test, magnet test).
- **🕘 History**: past checks saved on the server.

## Files

- `app.py` — the Streamlit app
- `coin_data.py` — the curated coin database, glossary, screening rules
  (values are approximate circulated-market ranges; they move — edit freely)

## Honest limits

- A photo can't certify a coin. Lighting, angle, and wear fool AI the same way
  they fool eyes. Treat every 🔥 as "get this authenticated," not "you're rich."
- Never clean a coin that might be valuable — cleaning kills the premium.
