#!/usr/bin/env python3
"""Append CJ-MLK-03 cycle 4 claims (CVS-MLK-200 to 212) to the evidence register."""
import csv
import os

REGISTER = "/home/p62operator/.openclaw/workspace-mlk/03-VERIFICATION/CVS-EVIDENCE-REGISTER.csv"

FIELDS = [
    "claim_id","workstream","claim","source_name","source_type","source_url",
    "source_date","evidence_type","tier","validation_status","confidence_score",
    "authority","traceability","recency","consistency","completeness",
    "issue_gap","owner","action_required","last_reviewed"
]

# source_url shortcuts
GNEWS_EQUAL = "https://news.google.com/search?q=%22PN+likely+to+demand+equal+share+of+seats+in+Melaka+polls%22&hl=en"
GNEWS_SOLO = "https://news.google.com/search?q=%22BN+keeping+solo+option+open+in+Melaka%22&hl=en"
FMT_SEARCH1 = "https://www.freemalaysiatoday.com/?s=PN+Melaka+seats"
GNEWS_BROAD = "https://news.google.com/search?q=Melaka+PRN+2026+BN+PN+PH&hl=en"
GNEWS_RAIS = "https://news.google.com/search?q=%22Rais+Yatim%22+Melaka+PN+police+candidate&hl=en"
GNEWS_STAB = "https://news.google.com/search?q=%22stab+in+the+back%22+Amanah+BN+PN+Melaka&hl=en"
GNEWS_BERSATU = "https://news.google.com/search?q=Bersatu+Melaka+strategizing+PRN+meeting+direction&hl=en"
WIKI_MAS = "https://ms.wikipedia.org/wiki/Mas_Ermieyati_Samsudin"
GNEWS_TRP = "https://news.google.com/search?q=%22What+BN-PN+Must+Do%22+PAS-Led+States+alliance&hl=en"
SYNTH = "CJ-MLK-03 collection agent synthesis"

rows = [
    ["CVS-MLK-248","MLK","PN likely to demand an equal share of seats in the Melaka state election (~14 of 28 DUN seats), per analyst","Free Malaysia Today (Google News MY)","Secondary report",GNEWS_EQUAL,"2026-08-06","Position","T2","Partially Verified","6","1","1","2","1","1","Named analyst unidentified; FMT full article text not extracted (Google News redirect)","CJMLK03","Corroboration","2026-08-06"],
    ["CVS-MLK-249","MLK","BN keeping the solo (no formal PN pact) option open for the Melaka state election, per analyst","Free Malaysia Today (Google News MY)","Secondary report",GNEWS_SOLO,"2026-08-04","Position","T2","Partially Verified","6","1","1","2","2","1","Named analyst unidentified; FMT full article text not extracted","CJMLK03","Corroboration","2026-08-06"],
    ["CVS-MLK-250","MLK","Zahid Hamidi announced BN will defend all 21 Melaka state seats and remains open to a PN understanding (Negeri Sembilan model), conveyed via Ab Rauf Yusoh","Free Malaysia Today (site search + Google News MY)","Secondary report",FMT_SEARCH1,"2026-08-06","Position","T2","Partially Verified","7","1","1","2","2","1","Exact FMT article date not isolated; full text not extracted","CJMLK03","Corroboration","2026-08-06"],
    ["CVS-MLK-251","MLK","PN to field Rais Yatim's son and a former Melaka deputy police chief as PRN Melaka candidates","Free Malaysia Today BM (Google News MY)","Secondary report",GNEWS_RAIS,"2026-07-16","Candidate","T2","Partially Verified","6","1","1","1","1","1","Specific DUN seats for these candidates unknown; candidate names not fully extracted","CJMLK03","Corroboration","2026-08-06"],
    ["CVS-MLK-252","MLK","PAS (Tuan Ibrahim) ready for talks on extending BN-PN cooperation to Melaka and federal level","Newswav (Google News MY)","Secondary report",GNEWS_STAB,"2026-08-03","Position","T2","Partially Verified","7","1","1","2","2","1","Tuan Ibrahim vs Hadi nuance unresolved (Hadi more cautious); full article text not extracted","CJMLK03","Corroboration","2026-08-06"],
    ["CVS-MLK-253","MLK","Melaka Opposition Leader (Mohd Yadzil Yaakub, WAWASAN/PN) expects formal BN-PN electoral pact talks for Melaka soon","Newswav (Google News MY)","Secondary report",GNEWS_STAB,"2026-08-03","Position","T2","Partially Verified","7","1","1","2","2","1","Full article text not extracted; Yadzil attribution inferred from Opposition Leader role","CJMLK03","Corroboration","2026-08-06"],
    ["CVS-MLK-254","MLK","Azalina: BN-Perikatan alliance is not fixed; cooperation depends on the political landscape in each state","Newswav (Google News MY)","Secondary report",GNEWS_STAB,"2026-08-03","Position","T2","Partially Verified","7","1","1","2","2","1","Azalina exact role/title to confirm; full article text not extracted","CJMLK03","Corroboration","2026-08-06"],
    ["CVS-MLK-255","MLK","An Amanah leader calls BN-PN cooperation a stab in the back — PH opposes the emerging pact","Newswav (Google News MY)","Secondary report",GNEWS_STAB,"2026-08-03","Position","T2","Partially Verified","7","1","1","2","2","1","Named Amanah leader unidentified; full article text not extracted","CJMLK03","Corroboration","2026-08-06"],
    ["CVS-MLK-256","MLK","Bersatu Melaka begins strategizing for the PRN with a meeting (~5 Aug 2026) to determine direction","Free Malaysia Today BM (Google News MY)","Secondary report",GNEWS_BROAD,"2026-08-04","Operational","T2","Partially Verified","6","1","1","2","2","1","~5 Aug meeting outcome unknown; full article text not extracted","CJMLK03","Corroboration","2026-08-06"],
    ["CVS-MLK-257","MLK","An Amanah VP states that race- and religion-based politics are unsustainable (~2 Aug 2026)","The Vibes (Google News MY)","Secondary report",GNEWS_STAB,"2026-08-02","Position","T2","Partially Verified","7","1","1","2","2","1","Confirm Amanah VP is Adly Zahari; corroborates CVS-MLK-191","CJMLK03","Corroboration","2026-08-06"],
    ["CVS-MLK-258","MLK","Wikipedia BM still lists Mas Ermieyati as Chief of Srikandi BERSATU (since 4 Oct 2024) and does not reflect the 10 Mar 2026 membership suspension — T5 dispute is a source-currency lag","Wikipedia Bahasa Melayu","AI-generated/Reference",WIKI_MAS,"2026-08-06","Position","T3","Inferred","6","0","2","2","1","1","T5 source-currency lag; BERSATU official clarification on Srikandi post scope needed","CJMLK03","Human review","2026-08-06"],
    ["CVS-MLK-259","MLK","Negeri Sembilan state election results: BN 18, PH 11, PN 7 (BN-PN 25/36 two-thirds majority) — the Melaka BN-PN negotiation template","TRP/FMT/The Edge cluster (Google News MY)","Secondary report",GNEWS_TRP,"2026-08-01","Result","T2","Verified","8","1","1","2","2","2","None — reference model confirmed by multiple outlets","CJMLK03","None","2026-08-06"],
    ["CVS-MLK-260","MLK","ASSESSMENT: PN's equal-share seat demand (~14) is roughly 2x the NS-proportional allocation (~7-8); the gap (~6-7 seats) defines the BN-PN Melaka negotiation tension","CJ-MLK-03 analyst synthesis","AI analytical",SYNTH,"2026-08-06","Analytical","T3","Inferred","6","1","2","2","2","0","Analytical assessment derived from CVS-MLK-248/249/259; requires human review","CJMLK03","Human review","2026-08-06"],
]

# Verify all rows have 20 fields
for i, r in enumerate(rows):
    assert len(r) == 20, f"Row {i} ({r[0]}) has {len(r)} fields, expected 20"

# Check existing last claim_id to avoid duplicates
existing_ids = set()
if os.path.exists(REGISTER):
    with open(REGISTER, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cid = (row.get("claim_id") or "").strip()
            if cid:
                existing_ids.add(cid)

new_rows = [r for r in rows if r[0] not in existing_ids]
print(f"Total new claims to append: {len(new_rows)} (of {len(rows)} prepared)")
print(f"Existing claim_ids in register: {len(existing_ids)}")
if existing_ids:
    print(f"Last existing: {sorted(existing_ids)[-1]}")

# Append
with open(REGISTER, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    for r in new_rows:
        writer.writerow(r)

print(f"Appended {len(new_rows)} rows to {REGISTER}")
print("New claim_ids:", [r[0] for r in new_rows])
