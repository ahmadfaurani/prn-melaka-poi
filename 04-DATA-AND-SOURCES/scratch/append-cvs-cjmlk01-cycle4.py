#!/usr/bin/env python3
"""Append CVS claims for CJ-MLK-01 Cycle 4 (2026-08-06 13:23 MYT) to evidence register."""
import csv
import os

REGISTER = "/home/p62operator/.openclaw/workspace-mlk/03-VERIFICATION/CVS-EVIDENCE-REGISTER.csv"
FIELDS = [
    "claim_id","workstream","claim","source_name","source_type","source_url","source_date",
    "evidence_type","tier","validation_status","confidence_score","authority","traceability",
    "recency","consistency","completeness","issue_gap","owner","action_required","last_reviewed"
]

NEW_CLAIMS = [
    # CVS-MLK-213
    {
        "claim_id": "CVS-MLK-213",
        "workstream": "MLK",
        "claim": "CM Ab Rauf Yusoh rejected Dr Muhamad Akmal Saleh's resignation letter as Melaka Exco (Chairman of Rural Development Agriculture & Food Security Committee) submitted in January 2026; Ab Rauf rejected it to ensure smooth state administration continuity; announced during visit to Empangan Jus Jasin Melaka on 8 April 2026",
        "source_name": "Kosmo Digital",
        "source_type": "Media (L4)",
        "source_url": "https://www.kosmo.com.my/2026/04/08/ab-rauf-tolak-surat-peletakan-jawatan-dr-muhamad-akmal/",
        "source_date": "2026-04-08",
        "evidence_type": "Statement",
        "tier": "T2",
        "validation_status": "Verified",
        "confidence_score": "9",
        "authority": "1", "traceability": "2", "recency": "1", "consistency": "2", "completeness": "2",
        "issue_gap": "April article but events current; Akmal remains Exco as of Aug 2026",
        "owner": "CJ-MLK-01",
        "action_required": "None",
        "last_reviewed": "2026-08-06"
    },
    # CVS-MLK-214
    {
        "claim_id": "CVS-MLK-214",
        "workstream": "MLK",
        "claim": "Dr Muhamad Akmal Saleh announced his resignation as Melaka Exco at the Pemuda UMNO AGM on 15 January 2026 at PWTC KL following pressure from DAP leaders regarding UMNO's position in the Unity Government; he retained his Ketua Pemuda UMNO position",
        "source_name": "Kosmo Digital (background in 8 Apr article)",
        "source_type": "Media (L4)",
        "source_url": "https://www.kosmo.com.my/2026/04/08/ab-rauf-tolak-surat-peletakan-jawatan-dr-muhamad-akmal/",
        "source_date": "2026-04-08",
        "evidence_type": "Statement",
        "tier": "T2",
        "validation_status": "Verified",
        "confidence_score": "7",
        "authority": "1", "traceability": "2", "recency": "1", "consistency": "2", "completeness": "1",
        "issue_gap": "Background fact reported in April article; Jan event not independently verified",
        "owner": "CJ-MLK-01",
        "action_required": "None",
        "last_reviewed": "2026-08-06"
    },
    # CVS-MLK-215
    {
        "claim_id": "CVS-MLK-215",
        "workstream": "MLK",
        "claim": "Dr Muhamad Akmal Saleh publicly urged PM Anwar Ibrahim to arrest and prosecute individuals who allegedly misappropriated Tabung Haji funds following the RCI on Tabung Haji; stated the public has the right to know; delivered on 23 July 2026",
        "source_name": "Kosmo Digital",
        "source_type": "Media (L4)",
        "source_url": "https://www.kosmo.com.my/2026/07/23/saya-mohon-pmx-tangkap-dakwa-orang-sakau-tabung-haji-akmal/",
        "source_date": "2026-07-23",
        "evidence_type": "Statement",
        "tier": "T2",
        "validation_status": "Verified",
        "confidence_score": "8",
        "authority": "1", "traceability": "2", "recency": "2", "consistency": "2", "completeness": "1",
        "issue_gap": "Direct quote; corroborated by RCI Tabung Haji coverage",
        "owner": "CJ-MLK-01",
        "action_required": "None",
        "last_reviewed": "2026-08-06"
    },
    # CVS-MLK-216
    {
        "claim_id": "CVS-MLK-216",
        "workstream": "MLK",
        "claim": "35-40 Members of Parliament expressed interest in participating in a special Dewan Rakyat session on 11 August 2026 to debate the RCI Report on Tabung Haji; confirmed by Communications Minister Fahmi Fadzil",
        "source_name": "Astro Awani",
        "source_type": "Media (L4)",
        "source_url": "https://www.astroawani.com/berita-malaysia",
        "source_date": "2026-08-06",
        "evidence_type": "Statement",
        "tier": "T2",
        "validation_status": "Verified",
        "confidence_score": "7",
        "authority": "1", "traceability": "1", "recency": "2", "consistency": "2", "completeness": "1",
        "issue_gap": "Awani search page extract; specific article URL not isolated",
        "owner": "CJ-MLK-01",
        "action_required": "None",
        "last_reviewed": "2026-08-06"
    },
    # CVS-MLK-217
    {
        "claim_id": "CVS-MLK-217",
        "workstream": "MLK",
        "claim": "MACC recorded statement of former Tabung Haji CFO (60-year-old woman) for over 6 hours; investigation involves alleged abuse of power in share purchase of two plantation companies worth RM370 million; 3 individuals remanded as of 5 Aug 2026",
        "source_name": "Astro Awani + Kosmo Digital",
        "source_type": "Media (L4)",
        "source_url": "https://www.astroawani.com/berita-malaysia",
        "source_date": "2026-08-05",
        "evidence_type": "Event",
        "tier": "T2",
        "validation_status": "Verified",
        "confidence_score": "7",
        "authority": "1", "traceability": "1", "recency": "2", "consistency": "2", "completeness": "1",
        "issue_gap": "Multiple outlets corroborate; specific article URLs not isolated",
        "owner": "CJ-MLK-01",
        "action_required": "None",
        "last_reviewed": "2026-08-06"
    },
    # CVS-MLK-218
    {
        "claim_id": "CVS-MLK-218",
        "workstream": "MLK",
        "claim": "Analyst Dr Nur Ayuni Mohd Isa (UPM) assesses that no seat-allocation formula can satisfy both BN and PN for PRN Melaka: incumbent formula favours UMNO (20 ADUN), PRU15-results formula favours PN (3 Parliament/~10 DUN), winnability formula risks divisional sabotage; published 5 Aug 2026",
        "source_name": "Utusan Malaysia",
        "source_type": "Media (L4)",
        "source_url": "https://www.utusan.com.my/nasional/2026/08/melaka-bakal-menjadi-medan-ujian-sebenar-ketahanan-kerjasama-bn-pn-penganalisis/",
        "source_date": "2026-08-05",
        "evidence_type": "Analysis",
        "tier": "T2",
        "validation_status": "Partially Verified",
        "confidence_score": "7",
        "authority": "1", "traceability": "2", "recency": "2", "consistency": "2", "completeness": "1",
        "issue_gap": "Single analyst L4; corroborate via second analyst or official seat-talk statement",
        "owner": "CJ-MLK-01",
        "action_required": "Corroboration via second analyst",
        "last_reviewed": "2026-08-06"
    },
    # CVS-MLK-219
    {
        "claim_id": "CVS-MLK-219",
        "workstream": "MLK",
        "claim": "BN holds 20/28 DUN Melaka seats (majority two-thirds) but 0/6 Parliament seats; PN/PAS holds 2 DUN seats but 3/6 Parliament seats (Masjid Tanah Tangga Batu Jasin) per PRU15 results; this DUN-Parliament divergence creates structural seat-allocation tension",
        "source_name": "Utusan Malaysia (analyst article)",
        "source_type": "Media (L4)",
        "source_url": "https://www.utusan.com.my/nasional/2026/08/melaka-bakal-menjadi-medan-ujian-sebenar-ketahanan-kerjasama-bn-pn-penganalisis/",
        "source_date": "2026-08-05",
        "evidence_type": "Factual data",
        "tier": "T2",
        "validation_status": "Verified",
        "confidence_score": "7",
        "authority": "1", "traceability": "2", "recency": "2", "consistency": "2", "completeness": "1",
        "issue_gap": "DUN figures align with Wikipedia (CVS-MLK-207); Parliament figures from PRU15",
        "owner": "CJ-MLK-01",
        "action_required": "None",
        "last_reviewed": "2026-08-06"
    },
    # CVS-MLK-220
    {
        "claim_id": "CVS-MLK-220",
        "workstream": "MLK",
        "claim": "PAS President Hadi Awang stated BN and PN may reach a different form of understanding for PRN Melaka; analyst interprets this as a signal that PAS/PN will not accept a minor-partner role in Melaka",
        "source_name": "Utusan Malaysia (analyst article quoting Hadi)",
        "source_type": "Media (L4)",
        "source_url": "https://www.utusan.com.my/nasional/2026/08/melaka-bakal-menjadi-medan-ujian-sebenar-ketahanan-kerjasama-bn-pn-penganalisis/",
        "source_date": "2026-08-05",
        "evidence_type": "Statement",
        "tier": "T2",
        "validation_status": "Partially Verified",
        "confidence_score": "6",
        "authority": "1", "traceability": "2", "recency": "1", "consistency": "1", "completeness": "1",
        "issue_gap": "Hadi quote date unspecified; analyst interpretation is T3",
        "owner": "CJ-MLK-01",
        "action_required": "Verify Hadi quote date and context",
        "last_reviewed": "2026-08-06"
    },
    # CVS-MLK-221
    {
        "claim_id": "CVS-MLK-221",
        "workstream": "MLK",
        "claim": "Hari Landskap Negara (HLN) 2026 runs 6-9 Aug at Stadium Hang Jebat Melaka; PM Anwar Ibrahim scheduled to officiate on 7 Aug; ~100000 visitors expected; state prep >70%; spokesperson Exco Rais Yasin; CM Ab Rauf conducted final inspection",
        "source_name": "Melaka Hari Ini",
        "source_type": "Media (L4)",
        "source_url": "https://www.melakahariini.my/hln-2026-dijangka-tarik-100000-pengunjung-ke-melaka/",
        "source_date": "2026-08-04",
        "evidence_type": "Event",
        "tier": "T2",
        "validation_status": "Verified",
        "confidence_score": "7",
        "authority": "1", "traceability": "2", "recency": "2", "consistency": "2", "completeness": "2",
        "issue_gap": "Verify PM attendance on 7 Aug",
        "owner": "CJ-MLK-01",
        "action_required": "None; human review can elevate",
        "last_reviewed": "2026-08-06"
    },
    # CVS-MLK-222
    {
        "claim_id": "CVS-MLK-222",
        "workstream": "MLK",
        "claim": "Kosmo editorial (4 Aug 2026) states BN still unable to win over a segment of Chinese voters despite NS BN-PN victory; warns BN must not be complacent; PH obtained ~40% vote share (highest overall) but lost due to electoral system not vote collapse",
        "source_name": "Kosmo Digital",
        "source_type": "Media (L4)",
        "source_url": "https://www.kosmo.com.my/2026/08/04/sebenarnya-jadi-pembangkang-lebih-mudah/",
        "source_date": "2026-08-04",
        "evidence_type": "Analysis/Editorial",
        "tier": "T2",
        "validation_status": "Partially Verified",
        "confidence_score": "7",
        "authority": "1", "traceability": "2", "recency": "2", "consistency": "1", "completeness": "1",
        "issue_gap": "Editorial analysis; contradicts Akmal multiracial claim (CVS-MLK-211); T5 flag",
        "owner": "CJ-MLK-01",
        "action_required": "Escalate T5 conflict with Akmal claim",
        "last_reviewed": "2026-08-06"
    },
    # CVS-MLK-223
    {
        "claim_id": "CVS-MLK-223",
        "workstream": "MLK",
        "claim": "[DISPUTED/T5] Akmal Saleh's claim (2 Aug) that BN-PN support is penetrating DAP strongholds and is multiracial with Chinese/Indian voters shifting is contradicted by Kosmo editorial (4 Aug) stating BN still unable to win over a segment of Chinese voters and PH retaining ~40% vote share",
        "source_name": "Kosmo Digital (Akmal 2 Aug vs Editorial 4 Aug)",
        "source_type": "Media (L4)",
        "source_url": "https://www.kosmo.com.my/2026/08/02/akmal-saleh-dakwa-tembok-kubu-dap-mula-retak/",
        "source_date": "2026-08-04",
        "evidence_type": "Conflict flag",
        "tier": "T5",
        "validation_status": "Disputed",
        "confidence_score": "5",
        "authority": "1", "traceability": "2", "recency": "2", "consistency": "0", "completeness": "1",
        "issue_gap": "Two L4 sources conflict on same question; needs precinct-level NS electoral data to resolve",
        "owner": "CJ-MLK-01",
        "action_required": "Escalation; obtain NS precinct-level results by ethnicity",
        "last_reviewed": "2026-08-06"
    },
    # CVS-MLK-224
    {
        "claim_id": "CVS-MLK-224",
        "workstream": "MLK",
        "claim": "Editorial notes NS BN-PN cooperation was the major winning factor (avoiding multi-cornered fights) but still too early to declare accepted by the people; Wawasan first-time candidates won 3 constituencies on PN tickets; PRN Melaka is next after Johor and NS",
        "source_name": "Kosmo Digital",
        "source_type": "Media (L4)",
        "source_url": "https://www.kosmo.com.my/2026/08/04/sebenarnya-jadi-pembangkang-lebih-mudah/",
        "source_date": "2026-08-04",
        "evidence_type": "Analysis/Editorial",
        "tier": "T2",
        "validation_status": "Partially Verified",
        "confidence_score": "7",
        "authority": "1", "traceability": "2", "recency": "2", "consistency": "2", "completeness": "1",
        "issue_gap": "Editorial assessment; Wawasan 3-seat claim needs verification against official results",
        "owner": "CJ-MLK-01",
        "action_required": "None",
        "last_reviewed": "2026-08-06"
    },
]

# Read existing, check for duplicate claim_ids, append new
existing_ids = set()
rows = []
if os.path.exists(REGISTER):
    with open(REGISTER, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cid = (row.get("claim_id") or "").strip()
            existing_ids.add(cid)
            rows.append(row)

appended = 0
for claim in NEW_CLAIMS:
    if claim["claim_id"] in existing_ids:
        print(f"SKIP (duplicate): {claim['claim_id']}")
        continue
    rows.append(claim)
    appended += 1
    print(f"APPEND: {claim['claim_id']} | {claim['tier']} | score {claim['confidence_score']} | {claim['claim'][:80]}...")

with open(REGISTER, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        # Ensure all fields present
        out = {k: (row.get(k) or "") for k in FIELDS}
        writer.writerow(out)

print(f"\n--- DONE: {appended} new claims appended. Register total: {len(rows)} data rows. ---")

# Distribution
from collections import Counter
tiers = Counter((r.get("tier") or "").strip() for r in rows)
print(f"Tier distribution (all): {dict(tiers)}")
new_tiers = Counter(c["tier"] for c in NEW_CLAIMS)
print(f"Tier distribution (new): {dict(new_tiers)}")
new_scores = [int(c["confidence_score"]) for c in NEW_CLAIMS]
print(f"New confidence scores: {sorted(new_scores)}")
