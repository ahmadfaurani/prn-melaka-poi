#!/usr/bin/env python3
"""CJ-MLK-01 Cycle 5 — Append 11 new CVS claims to evidence register."""
import csv, os, sys

REGISTER = os.path.expanduser("~/.openclaw/workspace-mlk/03-VERIFICATION/CVS-EVIDENCE-REGISTER.csv")
FIELDS = [
    "claim_id","workstream","claim","source_name","source_type","source_url","source_date",
    "evidence_type","tier","validation_status","confidence_score",
    "authority","traceability","recency","consistency","completeness",
    "issue_gap","owner","action_required","last_reviewed"
]
TODAY = "2026-08-07"

new_claims = [
    # CVS-MLK-289: Zahid 21-seat defense
    {"claim_id":"CVS-MLK-289","workstream":"CJ-MLK-01","claim":"Ahmad Zahid Hamidi (BN Chairman/DPM) stated BN will not share its 21 won DUN seats in Melaka with any party; CM Ab Rauf committed to defending all 21 seats; seat negotiations remain open for other arrangements",
     "source_name":"Kosmo Digital","source_type":"L4","source_url":"https://www.kosmo.com.my/2026/08/06/kerusi-dimenangi-bn-di-melaka-kekal-milik-bn-ahmad-zahid/","source_date":"2026-08-06",
     "evidence_type":"News report of political statement","tier":"T2","validation_status":"Verified","confidence_score":"8",
     "authority":"1","traceability":"2","recency":"2","consistency":"2","completeness":"1",
     "issue_gap":"21 vs 20 DUN discrepancy vs cycle 4 reporting; may reflect by-election gain","owner":"CJ-MLK-01","action_required":"Corroboration of exact DUN count","last_reviewed":TODAY},

    # CVS-MLK-290: Ab Rauf PH vacancies unfilled
    {"claim_id":"CVS-MLK-290","workstream":"CJ-MLK-01","claim":"Ab Rauf Yusoh announced Melaka state government will not appoint replacements for political vacancies left by PH representatives until PRN; remaining administration term 'not long'; delivered at WRUR program in Merlimau (Akmal's constituency)",
     "source_name":"Kosmo Digital","source_type":"L4","source_url":"https://www.kosmo.com.my/2026/07/17/kekosongan-jawatan-ph-dibiar-hingga-prn-rauf/","source_date":"2026-07-17",
     "evidence_type":"News report of CM statement","tier":"T2","validation_status":"Verified","confidence_score":"8",
     "authority":"1","traceability":"2","recency":"1","consistency":"2","completeness":"2",
     "issue_gap":"None","owner":"CJ-MLK-01","action_required":"None","last_reviewed":TODAY},

    # CVS-MLK-291: Ab Rauf DAP "bernikah tidak berakad"
    {"claim_id":"CVS-MLK-291","workstream":"CJ-MLK-01","claim":"Ab Rauf Yusoh revealed BN never formed a formal coalition government with DAP in Melaka; relationship was only 'semangat persefahaman' (spirit of understanding) from Putrajaya; DAP exit 'like married without solemnization, divorced without talak'; governance continues unaffected",
     "source_name":"Kosmo Digital","source_type":"L4","source_url":"https://www.kosmo.com.my/2026/07/14/dap-keluar-umpama-bernikah-tidak-berakad-bercerai-tidak-bertalak-ab-rauf/","source_date":"2026-07-14",
     "evidence_type":"News report of CM press conference","tier":"T2","validation_status":"Verified","confidence_score":"9",
     "authority":"1","traceability":"2","recency":"1","consistency":"2","completeness":"2",
     "issue_gap":"None — direct quote, specific location (Seri Negeri)","owner":"CJ-MLK-01","action_required":"None","last_reviewed":TODAY},

    # CVS-MLK-292: Constitutional deadline 30 Dec 2026
    {"claim_id":"CVS-MLK-292","workstream":"CJ-MLK-01","claim":"Ab Rauf Yusoh stated DUN Melaka term ends 30 December 2026 (constitutional deadline); Melaka will not follow Johor/NS dissolution timing; will send machinery to help Johor/NS PRN before deciding Melaka timing; 'belum mendapat ilham' on dissolution date",
     "source_name":"Kosmo Digital","source_type":"L4","source_url":"https://www.kosmo.com.my/2026/06/06/dun-melaka-kekal-tidak-ikut-rentak-johor-negeri-sembilan/","source_date":"2026-06-06",
     "evidence_type":"News report of CM statement","tier":"T2","validation_status":"Verified","confidence_score":"8",
     "authority":"1","traceability":"2","recency":"1","consistency":"2","completeness":"2",
     "issue_gap":"None","owner":"CJ-MLK-01","action_required":"None","last_reviewed":TODAY},

    # CVS-MLK-293: Akmal "Aku ABU" — no faction alignment
    {"claim_id":"CVS-MLK-293","workstream":"CJ-MLK-01","claim":"Dr Akmal Saleh at UMNO 80th Anniversary Convention (2 May 2026) declared 'I am not Zahid's boy, not Tok Mat's boy, not Khairy's boy — I am ABU (Aku Budak UMNO)'; explicitly denied alignment with any individual leader; positioned as party loyalist independent of factions",
     "source_name":"Kosmo Digital","source_type":"L4","source_url":"https://www.kosmo.com.my/2026/05/02/aku-abu-aku-budak-umno/","source_date":"2026-05-02",
     "evidence_type":"News report of convention speech","tier":"T2","validation_status":"Verified","confidence_score":"9",
     "authority":"1","traceability":"2","recency":"1","consistency":"2","completeness":"2",
     "issue_gap":"None — direct quote at named event","owner":"CJ-MLK-01","action_required":"None","last_reviewed":TODAY},

    # CVS-MLK-294: Akmal go-solo advocacy
    {"claim_id":"CVS-MLK-294","workstream":"CJ-MLK-01","claim":"Dr Akmal Saleh (20 May 2026) urged UMNO to contest solo in ALL state and general elections; invoked religious framing ('Allah tunjukkan perangai sebenar') and royal institution defense ('titah Sultan diperlekehkan oleh kerana babi'); said Johor solo decision must apply to all states",
     "source_name":"Kosmo Digital","source_type":"L4","source_url":"https://www.kosmo.com.my/2026/05/20/sedikit-demi-sedikit-allah-tunjukkan-perangai-sebenar-mereka/","source_date":"2026-05-20",
     "evidence_type":"News report of political statement","tier":"T2","validation_status":"Verified","confidence_score":"8",
     "authority":"1","traceability":"2","recency":"1","consistency":"2","completeness":"1",
     "issue_gap":"Go-solo position was later overruled by BN-PN coalitions in Johor/NS","owner":"CJ-MLK-01","action_required":"None","last_reviewed":TODAY},

    # CVS-MLK-295: Zahid endorses Tabung Haji no-compromise
    {"claim_id":"CVS-MLK-295","workstream":"CJ-MLK-01","claim":"Ahmad Zahid Hamidi (6 Aug) formally endorsed no-compromise position on Tabung Haji RCI findings — those found guilty of mismanagement must face consequences; responds to Khairy's call for no action; RCI presentation confirmed 11 Aug in Dewan Rakyat; MACC CFO testimony ongoing 7+ hours",
     "source_name":"Kosmo Digital","source_type":"L4","source_url":"https://www.kosmo.com.my/2026/08/06/bn-umno-tidak-kompromi-penyelewengan-th-ahmad-zahid/","source_date":"2026-08-06",
     "evidence_type":"News report of DPM statement","tier":"T2","validation_status":"Verified","confidence_score":"9",
     "authority":"1","traceability":"2","recency":"2","consistency":"2","completeness":"2",
     "issue_gap":"None — Akmal's 23 Jul advocacy now party policy (14-day cycle)","owner":"CJ-MLK-01","action_required":"None","last_reviewed":TODAY},

    # CVS-MLK-296: Ismail Sabri charged
    {"claim_id":"CVS-MLK-296","workstream":"CJ-MLK-01","claim":"Former PM Datuk Seri Ismail Sabri Yaakob to be charged 7 Aug 2026 in Sessions Court KL (Judge Suzana Hussin) for asset declaration; RM170M cash + RM7M gold (16kg) seized; investigation from Feb 2025 detention of 4 senior officers; largest anti-corruption case vs former UMNO PM",
     "source_name":"Kosmo Digital","source_type":"L4","source_url":"https://www.kosmo.com.my/2026/08/06/ismail-sabri-didakwa-esok/","source_date":"2026-08-06",
     "evidence_type":"News report of court proceedings","tier":"T2","validation_status":"Verified","confidence_score":"8",
     "authority":"1","traceability":"2","recency":"2","consistency":"2","completeness":"1",
     "issue_gap":"Specific charges not yet known at reporting time","owner":"CJ-MLK-01","action_required":"Monitor charges filed 7 Aug","last_reviewed":TODAY},

    # CVS-MLK-297: PRN Melaka expected next month
    {"claim_id":"CVS-MLK-297","workstream":"CJ-MLK-01","claim":"Multiple sources (AMK/PKR Youth, ILHAM Centre analysts, Astro Awani) reference PRN Melaka as expected next month (September 2026); Parti Kancil (Rafizi Ramli) announcing intent to contest PRN Melaka; AMK accuses Rafizi of splitting PH votes to benefit UMNO",
     "source_name":"Astro Awani","source_type":"L4","source_url":"https://www.astroawani.com/berita-politik/rafizi-hipokrit-masuk-prn-melaka-bantu-umno-pecah-undi-ph-amk","source_date":"2026-08-06",
     "evidence_type":"News report + analyst commentary","tier":"T2","validation_status":"Partially Verified","confidence_score":"7",
     "authority":"1","traceability":"2","recency":"2","consistency":"2","completeness":"1",
     "issue_gap":"'Bulan hadapan' is journalistic inference, not official dissolution announcement","owner":"CJ-MLK-01","action_required":"None","last_reviewed":TODAY},

    # CVS-MLK-298: Kongres PKR 2026 confirmed details
    {"claim_id":"CVS-MLK-298","workstream":"CJ-MLK-01","claim":"Kongres Nasional PKR 2026 confirmed for 15-16 August 2026 at Melaka International Trade Centre (MITC) Ayer Keroh Melaka; ~2500 delegates and ~3000 observers expected; Nurul Izzah resigns as PKR Deputy President (focusing on studies); MPP grants leave until after congress",
     "source_name":"Astro Awani","source_type":"L4","source_url":"https://www.astroawani.com/berita-politik","source_date":"2026-08-06",
     "evidence_type":"News index aggregation","tier":"T2","validation_status":"Verified","confidence_score":"8",
     "authority":"1","traceability":"2","recency":"2","consistency":"2","completeness":"1",
     "issue_gap":"Aggregated from index page, not individual article URLs","owner":"CJ-MLK-01","action_required":"None","last_reviewed":TODAY},

    # CVS-MLK-299: ILHAM Centre analysis + UMNO assembly + Mustapa
    {"claim_id":"CVS-MLK-299","workstream":"CJ-MLK-01","claim":"ILHAM Centre analysis (6 Aug): BN-PN cooperation risks eroding UMNO dominance (only 23 Parliament seats); 52% young Malay voters remain PH blind spot; 'politik dinosaur' primordial sentiments persist; Perhimpunan Agung UMNO 2026 starts 9 September; Mustapa Mohamed returned to UMNO June but won't contest PRU16 to give way to young leaders",
     "source_name":"Astro Awani","source_type":"L4","source_url":"https://www.astroawani.com/berita-politik","source_date":"2026-08-06",
     "evidence_type":"News index aggregation + analyst statements","tier":"T2","validation_status":"Partially Verified","confidence_score":"7",
     "authority":"1","traceability":"2","recency":"2","consistency":"2","completeness":"1",
     "issue_gap":"Multiple items aggregated; individual article URLs not extracted","owner":"CJ-MLK-01","action_required":"None","last_reviewed":TODAY},
]

def main():
    rows = []
    if os.path.exists(REGISTER):
        with open(REGISTER, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            fieldnames = reader.fieldnames or FIELDS
    else:
        fieldnames = FIELDS

    existing_ids = {r.get("claim_id","") for r in rows}
    appended = 0
    for claim in new_claims:
        cid = claim["claim_id"]
        if cid in existing_ids:
            print(f"SKIP (exists): {cid}")
            continue
        row = {fn: claim.get(fn,"") for fn in fieldnames}
        rows.append(row)
        appended += 1
        print(f"APPEND: {cid} — {claim['claim'][:80]}...")

    with open(REGISTER, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nDone. Appended {appended} claims. Register total: {len(rows)} rows.")

if __name__ == "__main__":
    main()
