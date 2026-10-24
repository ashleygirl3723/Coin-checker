"""
Coin Checker dataset — valuable US error coins, key dates, and the error glossary.

Built from auction records (PCGS/NGC, Heritage/Stack's/GreatCollections),
Greysheet and dealer guides, 2024-2026 market, circulated grades.
Values are approximate and move — verify big finds against sold listings
and get $1k+ coins authenticated by PCGS or NGC.

Entry fields: denomination (str or list, None = any), year (int or None),
year_min/year_max (optional bounds), mint (list or None = any),
name, look_for (plain-language visual description, also keyword-matched),
value_low/value_high (USD), value_note, heat ("jackpot"|"look"),
category ("error"|"key_date"|"silver"), replica_only (optional).
"""

DATA = [
    {
        "denomination": "cent",
        "year": 1955,
        "mint": [
            "none"
        ],
        "name": "1955 Doubled Die Obverse (DDO)",
        "look_for": "Front of coin: every letter looks doubled with a bold raised ghost image right beside it, especially the date, LIBERTY, and IN GOD WE TRUST. Visible without magnification. No mintmark (Philadelphia).",
        "value_low": 1500,
        "value_high": 3000,
        "value_note": "Circulated XF-AU. Mint-state red examples reach $15k+; record $320,625 (Feb 2025).",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "cent",
        "year": 1969,
        "mint": [
            "S"
        ],
        "name": "1969-S Doubled Die Obverse",
        "look_for": "Dramatic raised doubling on the date, LIBERTY, and IN GOD WE TRUST. Small S mintmark under the date. Beware: the most counterfeited modern cent; authentication required.",
        "value_low": 3000,
        "value_high": 15000,
        "value_note": "Only ~100 known. Even worn examples are five figures when authenticated; auction record $126,500.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "cent",
        "year": 1972,
        "mint": [
            "none"
        ],
        "name": "1972 Doubled Die Obverse",
        "look_for": "Bold doubling in LIBERTY, IN GOD WE TRUST, and the date, visible without a loupe. No mintmark (Philadelphia).",
        "value_low": 10,
        "value_high": 50,
        "value_note": "Circulated. Mint-state examples $75-$300+.",
        "heat": "look",
        "category": "error"
    },
    {
        "denomination": "cent",
        "year": 1995,
        "mint": [
            "none"
        ],
        "name": "1995 Doubled Die Obverse",
        "look_for": "Strong raised doubling in LIBERTY and the date on the front. No mintmark (Philadelphia).",
        "value_low": 20,
        "value_high": 75,
        "value_note": "Circulated. Mint-state $75-$200.",
        "heat": "look",
        "category": "error"
    },
    {
        "denomination": "cent",
        "year": 1943,
        "mint": [
            "none",
            "D",
            "S"
        ],
        "name": "1943 Copper (Bronze) Cent",
        "look_for": "A normal copper-colored penny dated 1943 (all 1943 cents should be grey steel). Does NOT stick to a magnet. Weighs 3.11 grams. Check for altered dates (1945/1948/1949 with the 5/8/9 re-cut) and copper-plated steel fakes.",
        "value_low": 150000,
        "value_high": 900000,
        "value_note": "Only ~20-40 known. 1943-D is unique and sold privately for $1.7M; Philly examples $200k-$500k+.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "cent",
        "year": 1944,
        "mint": [
            "none",
            "D",
            "S"
        ],
        "name": "1944 Steel Cent",
        "look_for": "A grey, steel-colored penny dated 1944 (all 1944 cents should be copper). STICKS to a magnet. Weighs about 2.7 grams.",
        "value_low": 75000,
        "value_high": 400000,
        "value_note": "A handful known. Top examples $373,750 (2008); 1944-S sold $1.1M.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "cent",
        "year": 1982,
        "mint": [
            "D"
        ],
        "name": "1982-D Small Date Copper (transitional)",
        "look_for": "Dated 1982 with a D mintmark and a SMALL, delicate date. Weighs 3.11 grams (copper) instead of the normal 2.5 grams (zinc). Weigh it - that is the test.",
        "value_low": 5000,
        "value_high": 20000,
        "value_note": "Only 2 confirmed. The transitional rarity of the copper-to-zinc switch.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "cent",
        "year": 1983,
        "mint": [
            "none",
            "D"
        ],
        "name": "1983 Copper (transitional)",
        "look_for": "A 1983 penny weighing 3.11 grams (copper planchet) instead of 2.5 grams (zinc). Looks identical to a normal cent - the scale is the only giveaway.",
        "value_low": 10000,
        "value_high": 20000,
        "value_note": "Only a few found; one 1983-D certified by PCGS. Values $15k-$20k+.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "cent",
        "year": 1992,
        "mint": [
            "none"
        ],
        "name": "1992 Close AM",
        "look_for": "Back of coin: in the word AMERICA, the A and M are almost touching at their bases (normal 1992 cents have a wide gap). No mintmark. Only 3 authenticated.",
        "value_low": 2000,
        "value_high": 10000,
        "value_note": "Circulated finds start ~$2,000; mint-state to $25,850 at auction. Powerball odds - but check anyway.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "cent",
        "year": 1992,
        "mint": [
            "D"
        ],
        "name": "1992-D Close AM",
        "look_for": "Same as above: A and M nearly touching on the reverse, with a D mintmark under the date. Only 15 found since 1993.",
        "value_low": 500,
        "value_high": 3000,
        "value_note": "Mint-state $2,100-$12,250; record $51,000.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "cent",
        "year": 1999,
        "mint": [
            "none"
        ],
        "name": "1999 Wide AM",
        "look_for": "Back of coin: a clear VISIBLE GAP between the A and M in AMERICA on a normal circulation penny (1999 circulation cents should have Close AM). The FG initials sit unusually close to the Memorial building. No mintmark.",
        "value_low": 100,
        "value_high": 4500,
        "value_note": "Circulated $100+; top grades to $4,500. 1998 and 2000 Wide AM varieties exist too, worth less ($20-$300).",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "cent",
        "year": 1970,
        "mint": [
            "S"
        ],
        "name": "1970-S Small Date",
        "look_for": "Delicate, small date numerals: the top of the 7 is level with the 0, and the inner curl of the 9 points toward the 7. S mintmark under the date.",
        "value_low": 10,
        "value_high": 40,
        "value_note": "Circulated. Scarcer than the common 1970-S Large Date.",
        "heat": "look",
        "category": "error"
    },
    {
        "denomination": "cent",
        "year": 1990,
        "mint": [
            "none"
        ],
        "name": "1990 No-S Proof Cent",
        "look_for": "Mirror-shiny proof penny (from a proof set, never circulation) dated 1990 with NO S mintmark under the date where one should be.",
        "value_low": 3000,
        "value_high": 10000,
        "value_note": "Only ~200 exist. Auction record ~$9,988.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "cent",
        "year": 1983,
        "mint": [
            "none"
        ],
        "name": "1983 Doubled Die Reverse",
        "look_for": "Back of coin: strong doubling on ONE CENT and on the columns (pillars) of the Lincoln Memorial.",
        "value_low": 100,
        "value_high": 300,
        "value_note": "Circulated.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "cent",
        "year": 1984,
        "mint": [
            "none"
        ],
        "name": "1984 Doubled Ear",
        "look_for": "Lincoln's earlobe on the front is clearly doubled - a second lobe or notch hanging below the ear.",
        "value_low": 50,
        "value_high": 200,
        "value_note": "Circulated.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "cent",
        "year": 1960,
        "mint": [
            "none"
        ],
        "name": "1960 Small Date",
        "look_for": "Small, delicate date numerals (compare against a 1960 large date). No mintmark.",
        "value_low": 20,
        "value_high": 75,
        "value_note": "Circulated. Scarcest of the 1960 date-size varieties.",
        "heat": "look",
        "category": "error"
    },
    {
        "denomination": "cent",
        "year": 1964,
        "mint": [
            "S"
        ],
        "name": "1964 SMS Lincoln Cent",
        "look_for": "Satin-like special finish with razor-sharp strike and squared rims. Note: these NEVER entered circulation - only a few dozen exist from a special 1964 test striking (Eva Adams estate). A worn 'shiny' 1964 penny is not this.",
        "value_low": 2000,
        "value_high": 15000,
        "value_note": "Dozens known. MS68RD examples five figures+.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "nickel",
        "year": 2000,
        "mint": [
            "P"
        ],
        "name": "2000-P Jefferson Nickel Mule (two obverses)",
        "look_for": "Jefferson's portrait on BOTH sides of the coin - a nickel struck with two front dies. One of the rarest modern mules.",
        "value_low": 25000,
        "value_high": 100000,
        "value_note": "A handful known. Mules typically $25k-$100k.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "nickel",
        "year": 1943,
        "mint": [
            "P"
        ],
        "name": "1943-P 3 Over 2 Nickel (overdate)",
        "look_for": "In the date, the 3 is punched over a 2 - look closely at the 3 for the ghost of a 2 underneath. Large P mintmark above Monticello (war nickel).",
        "value_low": 25,
        "value_high": 300,
        "value_note": "Circulated $25+; uncirculated to $300.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "nickel",
        "year": 1942,
        "mint": [
            "D"
        ],
        "name": "1942-D D Over Horizontal D (repunched mintmark)",
        "look_for": "Under magnification the D mintmark shows a second D punched sideways/horizontally underneath it.",
        "value_low": 40,
        "value_high": 600,
        "value_note": "Circulated $40-$90; uncirculated $250-$600+.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "dime",
        "year": 1982,
        "mint": [
            "none"
        ],
        "name": "1982 No-P Roosevelt Dime",
        "look_for": "A 1982 dime with NO P mintmark above the date (Philadelphia forgot the punch on some dies). 1982 was the first year Philly used a P on dimes, so a blank spot above the date is the tell. Strong strikes worth more than weak ones.",
        "value_low": 30,
        "value_high": 300,
        "value_note": "Circulated $30-$150; uncirculated $125-$800. THE circulation-find error dime.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "dime",
        "year": 1975,
        "mint": [
            "none"
        ],
        "name": "1975 No-S Proof Dime",
        "look_for": "Mirror-shiny proof dime dated 1975 with NO S mintmark above the date. Only found in proof sets - never in pocket change.",
        "value_low": 300000,
        "value_high": 500000,
        "value_note": "Only 2 confirmed. Record $349,600-$456,000. A legend, not a circulation find.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "dime",
        "year": 1968,
        "mint": [
            "none"
        ],
        "name": "1968 No-S Proof Dime",
        "look_for": "Mirror-shiny proof dime dated 1968 missing its S mintmark above the date.",
        "value_low": 10000,
        "value_high": 30000,
        "value_note": "Proof sets only. High demand, tiny supply.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "dime",
        "year": 1942,
        "mint": [
            "none"
        ],
        "name": "1942/41 Mercury Dime Overdate",
        "look_for": "Inside the 2 of the date you can see the ghost of a 1 underneath - a 1941 die re-punched as 1942. Winged Liberty head design, no mintmark.",
        "value_low": 250,
        "value_high": 700,
        "value_note": "Good-Fine $278-$540 wholesale. A major variety - authenticate before buying.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "dime",
        "year": 1942,
        "mint": [
            "D"
        ],
        "name": "1942/41-D Mercury Dime Overdate",
        "look_for": "Same ghost-1-inside-the-2 overdate, with a D mintmark on the reverse.",
        "value_low": 300,
        "value_high": 700,
        "value_note": "Good-Fine $325-$625 wholesale.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "dime",
        "year": 1965,
        "mint": [
            "none"
        ],
        "name": "1965 Dime Struck on Silver Planchet",
        "look_for": "A 1965 dime that is solid silver: silvery-grey edge with NO copper stripe, weighs 2.5 grams (same as silver dimes). 1965 dimes should be clad.",
        "value_low": 3000,
        "value_high": 8000,
        "value_note": "Transitional error from the 1964-1965 silver-to-clad switch. A few known.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "quarter",
        "year": 2004,
        "mint": [
            "D"
        ],
        "name": "2004-D Wisconsin Extra Leaf - HIGH Leaf",
        "look_for": "Back shows cow, cheese wheel, and corn. An EXTRA leaf sticks UP from the corn husk, clearly separated from the normal leaves. D mintmark on front.",
        "value_low": 65,
        "value_high": 2000,
        "value_note": "Circulated $50-$100; uncirculated $160-$200; top grades $1,000+ (record $2,530).",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "quarter",
        "year": 2004,
        "mint": [
            "D"
        ],
        "name": "2004-D Wisconsin Extra Leaf - LOW Leaf",
        "look_for": "Same Wisconsin corn reverse, but the extra leaf droops DOWNWARD along the husk. D mintmark on front.",
        "value_low": 50,
        "value_high": 1500,
        "value_note": "Circulated $50-$100; uncirculated ~$160.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "quarter",
        "year": 2005,
        "mint": [
            "P"
        ],
        "name": "2005-P Minnesota Doubled Die (Extra Tree)",
        "look_for": "Back shows Minnesota with evergreen trees: a GHOST EXTRA TREE appears doubled beside the normal trees, often floating right of the state outline. Needs a loupe in circulated grades.",
        "value_low": 5,
        "value_high": 100,
        "value_note": "Many minor varieties $5+; bold, visible ones to $100-$200 in uncirculated.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "quarter",
        "year": 1999,
        "mint": [
            "P"
        ],
        "name": "1999-P Delaware 'Spitting Horse'",
        "look_for": "Back shows Caesar Rodney on horseback: a raised die-crack line runs from the horse's mouth, looking like the horse is spitting.",
        "value_low": 10,
        "value_high": 500,
        "value_note": "Typical $10-$20; dramatic examples $500+.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "quarter",
        "year": 1999,
        "mint": [
            "P"
        ],
        "name": "1999-P Georgia Off-Center Strike (example)",
        "look_for": "The whole design is shifted to one side, leaving a blank crescent of metal, yet the date is still visible. Dramatic examples worth far more.",
        "value_low": 100,
        "value_high": 1000,
        "value_note": "Off-center errors are priced by how dramatic and how much date shows: hundreds to thousands.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "quarter",
        "year": 1965,
        "mint": [
            "none"
        ],
        "name": "1965 Quarter Struck on Silver Planchet",
        "look_for": "A 1965 quarter with a solid silver-grey edge (no copper stripe), weighing 6.25 grams. 1965 quarters should be clad.",
        "value_low": 3000,
        "value_high": 10000,
        "value_note": "Transitional error from the silver-to-clad switch. Very few known.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "dollar",
        "year": 2000,
        "mint": [
            "P"
        ],
        "name": "(2000-P) Sacagawea / Quarter Mule",
        "look_for": "A gold-colored dollar-size coin with Washington's QUARTER portrait on one side and the Sacagawea flying-eagle dollar design on the other. No date visible on either side. Total face value $1.25 - the most famous US mule.",
        "value_low": 100000,
        "value_high": 225000,
        "value_note": "~20 known. Record $194,062 (Jan 2024). Beware glued-together 'magician coin' fakes.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "dollar",
        "year": 2000,
        "mint": [
            "P"
        ],
        "name": "Cheerios 2000-P Sacagawea Dollar",
        "look_for": "A 2000-P Sacagawea dollar where the eagle's TAIL FEATHERS have sharp, deeply cut raised center veins (structured, almost 3D look). Normal ones have smooth, flat feathers. Only from General Mills Cheerios promo packs.",
        "value_low": 1000,
        "value_high": 35000,
        "value_note": "~100 confirmed of 5,500 promo coins. The tail-feather detail is the diagnostic.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "dollar",
        "year": 2000,
        "mint": [
            "P"
        ],
        "name": "2000-P 'Wounded Eagle' Sacagawea Dollar",
        "look_for": "A raised die-crack line slashes diagonally across the eagle's breast on the reverse, like the bird was speared.",
        "value_low": 145,
        "value_high": 2000,
        "value_note": "Under 200 confirmed. Circulated/low-MS $145-$500; high grades to $8,000.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "dollar",
        "year": 1999,
        "mint": [
            "P"
        ],
        "name": "1999-P Susan B. Anthony Struck on Sacagawea Planchet",
        "look_for": "A Susan B. Anthony dollar design but struck on a GOLDEN-colored planchet (Sacagawea dollar blank) instead of the normal silvery clad. 1999-P only.",
        "value_low": 7000,
        "value_high": 16000,
        "value_note": "A few known. Heritage sales $7,700-$16,100. Wrong-planchet showpiece.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": None,
        "year": None,
        "mint": None,
        "name": "Broadstrike (any denomination)",
        "look_for": "Coin is spread wider than normal with the design running off the edge and no raised rim - struck outside its retaining collar.",
        "value_low": 20,
        "value_high": 300,
        "value_note": "Common minor errors $20+; dramatic or on silver coins more.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": None,
        "year": None,
        "mint": None,
        "name": "Clipped Planchet (any denomination)",
        "look_for": "A neat curved 'bite' missing from the coin's edge, as if punched out - the metal flows smoothly into the clip, not a rough cut (post-mint damage looks torn).",
        "value_low": 10,
        "value_high": 150,
        "value_note": "Priced by clip size; large or multiple clips worth more.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": None,
        "year": None,
        "mint": None,
        "name": "Wrong Planchet (any denomination)",
        "look_for": "Right design but wrong metal/size/weight: e.g. a cent struck on a dime blank (silvery, smaller), or a coin that fails the weight or magnet test for its date.",
        "value_low": 200,
        "value_high": 5000,
        "value_note": "Cent-on-dime-blank $200+; dramatic mismatches reach thousands.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": None,
        "year": None,
        "mint": None,
        "name": "Double Denomination (any)",
        "look_for": "Two denominations on one coin: e.g. cent design struck over an already-struck dime, so you see parts of both coins overlapping.",
        "value_low": 200,
        "value_high": 4000,
        "value_note": "Eye-catching and popular; e.g. SBA dollar on struck cent sold $3,904.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": None,
        "year": None,
        "mint": None,
        "name": "Cud / Major Die Break (any denomination)",
        "look_for": "A raised blob of metal on the rim where part of the design is missing - the die itself broke and metal filled the gap. (Thin raised lines elsewhere are just die cracks, worth much less.)",
        "value_low": 5,
        "value_high": 150,
        "value_note": "Small cuds $5+; large rim cuds obliterating design to $150+.",
        "heat": "jackpot",
        "category": "error"
    },
    {
        "denomination": "cent",
        "year": 1909,
        "mint": [
            "S"
        ],
        "name": "1909-S VDB Lincoln Cent",
        "look_for": "First-year Lincoln cent: small S mintmark under the date, and V.D.B. (designer Victor David Brenner) initials on the BOTTOM of the reverse. Wheat ears reverse. The most counterfeited US coin - authentication essential.",
        "value_low": 700,
        "value_high": 2000,
        "value_note": "Heavily worn ~$700; MS-63 ~$1,800. Mintage only 484,000.",
        "heat": "jackpot",
        "category": "key_date"
    },
    {
        "denomination": "cent",
        "year": 1914,
        "mint": [
            "D"
        ],
        "name": "1914-D Lincoln Cent",
        "look_for": "D mintmark under the date on a wheat-ear cent. Mintage just 1,193,000.",
        "value_low": 175,
        "value_high": 300,
        "value_note": "Good ~$175-$200; VF ~$250. High grades soar past $10k.",
        "heat": "jackpot",
        "category": "key_date"
    },
    {
        "denomination": "cent",
        "year": 1931,
        "mint": [
            "S"
        ],
        "name": "1931-S Lincoln Cent",
        "look_for": "S mintmark under the date; only 866,000 minted during the Depression.",
        "value_low": 80,
        "value_high": 160,
        "value_note": "Circulated $80-$160; finest known $43,200 (Aug 2025).",
        "heat": "jackpot",
        "category": "key_date"
    },
    {
        "denomination": "cent",
        "year": 1877,
        "mint": [
            "none"
        ],
        "name": "1877 Indian Head Cent",
        "look_for": "Indian/princess head portrait with feathered headdress, dated 1877. Key date of the series; mintage 852,500.",
        "value_low": 700,
        "value_high": 3000,
        "value_note": "Well-worn ~$700; high grades into five figures.",
        "heat": "jackpot",
        "category": "key_date"
    },
    {
        "denomination": "cent",
        "year": 1922,
        "mint": [
            "none"
        ],
        "name": "1922 No-D (Plain) Lincoln Cent",
        "look_for": "A 1922 penny with NO D mintmark (Denver was the only mint striking cents that year). Best variety: sharp strong reverse with weak obverse; the first 2 of the date weaker than the second 2, and TRUST sharply struck.",
        "value_low": 600,
        "value_high": 6000,
        "value_note": "Strong Reverse Die Pair 2 is the prize; weak-reverse examples worth less.",
        "heat": "jackpot",
        "category": "key_date"
    },
    {
        "denomination": "cent",
        "year": 1909,
        "mint": [
            "S"
        ],
        "name": "1909-S Indian Head Cent",
        "look_for": "Indian head design dated 1909 with an S mintmark on the reverse under the wreath.",
        "value_low": 300,
        "value_high": 1200,
        "value_note": "Low-mintage final-year Indian cent.",
        "heat": "jackpot",
        "category": "key_date"
    },
    {
        "denomination": "dime",
        "year": 1916,
        "mint": [
            "D"
        ],
        "name": "1916-D Mercury Dime",
        "look_for": "Winged Liberty head dime dated 1916 with a small D mintmark on the REVERSE, lower left by the fasces. Mintage only 264,000. One of the most counterfeited coins (fake D added) - authenticate.",
        "value_low": 1000,
        "value_high": 7500,
        "value_note": "Good ~$1,000+; XF $7,500; record $207,000.",
        "heat": "jackpot",
        "category": "key_date"
    },
    {
        "denomination": "dime",
        "year": 1921,
        "mint": [
            "none"
        ],
        "name": "1921 Mercury Dime",
        "look_for": "Winged Liberty dime dated 1921, no mintmark. Low postwar mintage 1,230,000.",
        "value_low": 60,
        "value_high": 600,
        "value_note": "Good ~$60; XF ~$595.",
        "heat": "jackpot",
        "category": "key_date"
    },
    {
        "denomination": "dime",
        "year": 1921,
        "mint": [
            "D"
        ],
        "name": "1921-D Mercury Dime",
        "look_for": "Winged Liberty dime dated 1921 with D mintmark on reverse. Mintage 1,080,000.",
        "value_low": 90,
        "value_high": 725,
        "value_note": "Good ~$90; XF ~$725.",
        "heat": "jackpot",
        "category": "key_date"
    },
    {
        "denomination": "quarter",
        "year": 1932,
        "mint": [
            "D"
        ],
        "name": "1932-D Washington Quarter",
        "look_for": "First-year Washington quarter with a D mintmark on the REVERSE below the eagle. Mintage 436,000. Beware added-D fakes on Philadelphia coins.",
        "value_low": 200,
        "value_high": 2000,
        "value_note": "Average circulated ~$207; MS65 $21,000+; record $143,750.",
        "heat": "jackpot",
        "category": "key_date"
    },
    {
        "denomination": "quarter",
        "year": 1932,
        "mint": [
            "S"
        ],
        "name": "1932-S Washington Quarter",
        "look_for": "First-year Washington quarter with an S mintmark on the reverse below the eagle. Mintage 408,000.",
        "value_low": 60,
        "value_high": 400,
        "value_note": "Nicely circulated $60-$65; record $45,500.",
        "heat": "jackpot",
        "category": "key_date"
    },
    {
        "denomination": "nickel",
        "year": 1950,
        "mint": [
            "D"
        ],
        "name": "1950-D Jefferson Nickel",
        "look_for": "D mintmark on the reverse right of Monticello. Mintage only 2,630,030 - many were hoarded, so circulated ones still turn up.",
        "value_low": 2.5,
        "value_high": 8,
        "value_note": "Circulated $2.50-$5; uncirculated $8-$20.",
        "heat": "look",
        "category": "key_date"
    },
    {
        "denomination": "nickel",
        "year": 1939,
        "mint": [
            "D"
        ],
        "name": "1939-D Jefferson Nickel",
        "look_for": "D mintmark right of Monticello; mintage 3,514,000.",
        "value_low": 2,
        "value_high": 12,
        "value_note": "Good-Fine $2-$4; EF+ $6.50-$12.",
        "heat": "look",
        "category": "key_date"
    },
    {
        "denomination": "nickel",
        "year": 1913,
        "mint": [
            "none"
        ],
        "name": "1913 Liberty Head Nickel",
        "look_for": "Liberty head (not buffalo) nickel dated 1913. ONLY 5 EXIST - all in museums or major collections. If you think you found one in change, it is a novelty copy.",
        "value_low": 3000000,
        "value_high": 5000000,
        "value_note": "One sold for $4.5M+. Included so the checker can say 'impossible - it is a replica.'",
        "heat": "jackpot",
        "category": "key_date",
        "replica_only": True
    },
    {
        "denomination": "quarter",
        "year": 2019,
        "mint": [
            "W"
        ],
        "name": "2019-W Quarter (West Point, any design)",
        "look_for": "Modern America the Beautiful quarter with a W mintmark on the front, just right of Washington's ponytail ribbon. Only 2 million per design vs 100M+ for P/D.",
        "value_low": 10,
        "value_high": 45,
        "value_note": "Circulated $10-$20; uncirculated $25-$45; MS65 $30-$80 by design.",
        "heat": "look",
        "category": "key_date"
    },
    {
        "denomination": "quarter",
        "year": 2020,
        "mint": [
            "W"
        ],
        "name": "2020-W V75 Quarter (West Point)",
        "look_for": "W mintmark by the ponytail PLUS a tiny V75 privy mark on the front (75th anniversary of WWII's end). Only 2 million per design.",
        "value_low": 15,
        "value_high": 65,
        "value_note": "Circulated $15-$30; uncirculated $35-$65; MS67+ to thousands.",
        "heat": "look",
        "category": "key_date"
    },
    {
        "denomination": "dollar",
        "year": 1921,
        "mint": [
            "none"
        ],
        "name": "1921 High-Relief Peace Dollar",
        "look_for": "Liberty head dollar dated 1921 with a distinctly HIGH, sculptural relief - the design stands much taller off the surface than later flat Peace dollars.",
        "value_low": 100,
        "value_high": 400,
        "value_note": "First and only high-relief year. Circulated $100-$200; uncirculated $250-$400+.",
        "heat": "jackpot",
        "category": "key_date"
    },
    {
        "denomination": "dime",
        "year": 1964,
        "mint": None,
        "name": "90% Silver Dime (any date 1964 or earlier)",
        "look_for": "Any Roosevelt (1946-1964) or Mercury (1916-1945) dime: solid silver-grey edge with NO copper stripe. 90% silver, 2.5 grams.",
        "value_low": 3,
        "value_high": 5,
        "value_note": "Melt value moves with silver spot (Oct 2026: roughly $4). Worn examples trade near melt.",
        "heat": "look",
        "category": "silver",
        "year_max": 1964
    },
    {
        "denomination": "quarter",
        "year": 1964,
        "mint": None,
        "name": "90% Silver Quarter (any date 1964 or earlier)",
        "look_for": "Any Washington quarter dated 1964 or earlier: solid silver-grey edge, no copper stripe. 90% silver, 6.25 grams.",
        "value_low": 8,
        "value_high": 12,
        "value_note": "Melt value moves with silver spot (Oct 2026: roughly $10).",
        "heat": "look",
        "category": "silver",
        "year_max": 1964
    },
    {
        "denomination": "half dollar",
        "year": 1964,
        "mint": None,
        "name": "1964 90% Silver Kennedy Half Dollar",
        "look_for": "1964 Kennedy half: solid silver edge, 90% silver, 12.5 grams. The ONLY year of 90% silver Kennedy halves.",
        "value_low": 17,
        "value_high": 25,
        "value_note": "Melt value moves with silver spot (Oct 2026: roughly $20).",
        "heat": "look",
        "category": "silver"
    },
    {
        "denomination": "half dollar",
        "year": 1965,
        "mint": None,
        "name": "40% Silver Kennedy Half (1965-1970)",
        "look_for": "Kennedy half dated 1965-1970: edge shows a faint copper stripe but the coin is 40% silver (silver-clad). Weighs 11.5 grams.",
        "value_low": 5,
        "value_high": 9,
        "value_note": "Melt moves with silver spot (Oct 2026: roughly $7). 1970-D only in mint sets.",
        "heat": "look",
        "category": "silver",
        "year_min": 1965,
        "year_max": 1970
    },
    {
        "denomination": "nickel",
        "year": 1943,
        "mint": None,
        "name": "35% Silver War Nickel (1942-1945)",
        "look_for": "Jefferson nickel 1942-1945 with a BIG P, D, or S mintmark stamped ABOVE Monticello on the reverse (the only nickels with the mark there). Slightly darker grey color; 35% silver. Note: regular 1942 nickels without the big mark are NOT silver.",
        "value_low": 2,
        "value_high": 3.5,
        "value_note": "Melt moves with silver spot (Oct 2026: roughly $2.50). Always check the reverse mintmark position.",
        "heat": "look",
        "category": "silver",
        "year_min": 1942,
        "year_max": 1945
    },
    {
        "denomination": "cent",
        "year": 1943,
        "mint": None,
        "name": "1943 Steel Cent (common)",
        "look_for": "Grey steel penny dated 1943 that STICKS to a magnet. This is the NORMAL 1943 cent - worth cents, not dollars. The valuable one is the copper 1943 (see error entry).",
        "value_low": 0.1,
        "value_high": 0.5,
        "value_note": "Worth 10-50 cents. Do not confuse with the $100k+ copper error.",
        "heat": "look",
        "category": "key_date"
    }
]

GLOSSARY = {
    "Doubled die (the valuable kind)": "TRUE doubled die (hub doubling): the DIE itself was made wrong - the hub pressed the design twice at a slight offset when the die was created. Every coin struck from that die shows the SAME doubling. Visual: a raised, rounded ghost image sitting side-by-side with the main letter, both images the same height, often with a little 'notch' where they split. VALUABLE.",
    "Machine doubling (worthless)": "Machine doubling (strike doubling, worthless): the die was fine, but it bounced or shifted as it struck THIS one coin, shaving metal sideways. Visual: a FLAT, shelf-like step cut into one side of the letter, lower than the main letter, looking scraped rather than raised. Adds NO value - this is the #1 thing mistaken for a doubled die. Rule of thumb: raised and rounded = doubled die; flat and shelf-like = machine doubling.",
    "Off-center strike": "Off-center strike: the blank was misaligned when struck, so the design sits shifted to one side with a blank crescent of metal showing. Value depends on how dramatic the shift is and whether the date is still visible - date-visible dramatic examples are worth hundreds to thousands.",
    "Broadstrike": "Broadstrike: the coin was struck outside its retaining collar, so metal spread wider than normal - the coin looks slightly larger with the design running off the edge and no raised rim.",
    "Clipped planchet": "Clipped planchet: the blank was mis-cut from the metal strip, so a neat curved 'bite' is missing from the edge. Genuine clips show smooth metal flow into the clip; torn or rough edges mean post-mint damage (worthless).",
    "Wrong planchet": "Wrong planchet: the coin was struck on a blank meant for another denomination - e.g. a cent design on a dime blank (silvery, smaller, lighter). Check weight, size, color, and the magnet test.",
    "Die crack / cud": "Die crack / cud: a crack in the die leaves a thin RAISED line on the coin (die crack, minor value); when a piece of the die breaks off at the rim, metal fills the gap leaving a raised BLOB that obliterates part of the design (a cud - worth real money on the rim).",
    "Repunched mint mark": "Repunched mintmark (RPM): the mintmark was punched into the die twice at slightly different positions, so under magnification you see a doubled or shadowed mint letter (e.g. D over horizontal D). Minor RPMs are a few dollars; strong ones more.",
    "Die clash": "Die clash: the obverse and reverse dies struck each other with no blank between them, transferring faint ghost outlines of one side's design onto the other side's die - then onto coins. Look for faint mirrored shapes that don't belong.",
    "Struck-through": "Struck-through: something (grease, cloth, metal fragment) got between the die and the blank, leaving a blank patch, smear, or embedded texture on the coin. Grease strikes are common and cheap; struck-through-metal or cloth commands more.",
    "Rotated die": "Rotated die: the reverse is rotated relative to the obverse (US coins should align at 180 degrees, coin-turn). Minor rotations are common; dramatic rotations (90+ degrees) carry premiums.",
    "Proof vs business strike": "Proof vs business strike: proofs are special collector coins struck with polished dies - mirror-like fields, frosted devices, razor-sharp details, sold in sets, never meant for circulation. Business strikes are normal pocket-change coins. A shiny business strike is NOT a proof; proofs have a distinct mirror finish and squared rims.",
    "Mint marks": "P = Philadelphia, D = Denver, S = San Francisco, W = West Point. On Lincoln cents the mark sits under the date; on Jefferson nickels it has moved around over the years; on Mercury dimes and Washington quarters it is on the reverse. No mark usually means Philadelphia (before 1980, Philadelphia used no mark on most coins).",
    "Don't clean coins": "NEVER clean a potentially valuable coin. Cleaning destroys collector value instantly \u2014 a cleaned rare coin can lose most of its premium. Handle by the edges."
}

SCREENING_RULES = [
    "POST-1982 ZINC CENTS: copper-plated zinc, worth 1 cent unless they carry a listed error/variety. No mintmark + 1992/1999 date = check the AM spacing.",
    "PRE-1982 COPPER CENTS (except 1943): 95% copper, 3.11 g. Worth ~3 cents in melt to dealers - save them, but don't expect riches unless the date is on the key/error list.",
    "CLAD DIMES/QUARTERS 1965+: face value unless silver (solid silver edge), a W mintmark (2019-2020 quarters), or a listed error. 1965-1967 have no mintmarks at all - that's normal.",
    "WEIGHT TEST: copper cent 3.11 g vs zinc cent 2.5 g. A kitchen scale reading 3.1 on a 1982-D small date or 1983 cent = stop and authenticate. Silver dime 2.5 g / quarter 6.25 g with NO copper stripe on edge = silver.",
    "MAGNET TEST: 1943 cents SHOULD stick (steel). A 1943 that does NOT stick = possible $100k+ copper error. A 1944 that DOES stick = possible $100k+ steel error. No other US cent should stick.",
    "EDGE CHECK: look at the coin's edge. Silver coins (1964 and earlier dimes/quarters/halves) show a solid silver-grey edge; clad coins show a brown copper stripe sandwich.",
    "DOUBLING CHECK: raised, rounded ghost image = doubled die (valuable). Flat, shelf-like step = machine doubling (worthless). When in doubt, assume machine doubling.",
    "NEVER CLEAN a coin you suspect is valuable - cleaning destroys most of the premium. Handle by the edges.",
    "IF IT SEEMS TOO GOOD: 1909-S VDB, 1914-D, 1916-D dime, and 1932-D/S quarters are among the most counterfeited US coins (added mintmarks, altered dates). Anything worth $100+ deserves PCGS/NGC authentication before you buy or sell.",
    "MOST COMMON REALITY: wheat cents 1934-1958 are 3-10 cents; common-date silver is melt; everything else modern and normal is face value. The money is in the specific dates and errors above.",
    "When in doubt, check SOLD listings on eBay for the exact coin \u2014 asking prices lie, sold prices tell the truth."
]

SILVER_NOTE = "Melt reference (Oct 2026, ~$48/oz silver): 90% dime 0.0715 oz, 90% quarter 0.179 oz, 90% half 0.3575 oz, 35% war nickel 0.0563 oz, 40% half 0.1479 oz. Melt USD = ounces x current silver spot."
