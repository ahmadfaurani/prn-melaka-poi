#!/usr/bin/env python3
"""CVS Evidence Register Appender — CJ-MLK-03 Cycle 6 (8 Aug 2026 11:19 MYT)
Logs 22 new claims (CVS-MLK-406 to CVS-MLK-427) to the evidence register.
"""
import csv
import os
from datetime import datetime

REGISTER = "/home/p62operator/.openclaw/workspace-mlk/03-VERIFICATION/CVS-EVIDENCE-REGISTER.csv"
REVIEW_DATE = "2026-08-08"
OWNER = "CJ-MLK-03"

# 20-field schema
# claim_id,workstream,claim,source_name,source_type,source_url,source_date,evidence_type,tier,validation_status,confidence_score,authority,traceability,recency,consistency,completeness,issue_gap,owner,action_required,last_reviewed

claims = [
    # CVS-MLK-406: BERSAMA candidates Aug 15
    ("CVS-MLK-406","MLK","BERSAMA (Rafizi Ramli) will announce Melaka state election candidates on August 15 2026; preparations in final stage; election not yet called",
     "Free Malaysia Today","L4 News","https://www.freemalaysiatoday.com","2026-08-08","Electoral Timeline","T2","Verified",8,1,1,2,2,2,
     "Homepage summary; individual article URL not extracted; Aug 15 also = PKR Congress in Melaka",OWNER,"Corroborate with direct BERSAMA statement",REVIEW_DATE),

    # CVS-MLK-407: Mohamad Hasan no official discussions
    ("CVS-MLK-407","MLK","Mohamad Hasan (Tok Mat/UMNO Deputy President) says no official BN-PN discussions yet for Melaka; preliminary negotiations conducted; seat distribution to top leadership",
     "Utusan Malaysia","L4 News","https://www.utusan.com.my/berita/politik","2026-08-08","Coalition Negotiation","T2","Verified",7,1,1,2,2,1,
     "CONTRADICTS Hadi Aug 7 'begun' claim; BN-aligned source",OWNER,"Corroborate; note BN bias",REVIEW_DATE),

    # CVS-MLK-408: T5 negotiation status dispute
    ("CVS-MLK-408","MLK","[DISPUTED] BN-PN Melaka negotiation status — Hadi (PAS) says negotiations begun (7 Aug); Mohamad Hasan (BN) says no official discussions yet (8 Aug)",
     "Malay Mail + Utusan","L4 News (conflicting)","https://www.utusan.com.my/berita/politik","2026-08-08","Coalition Dispute","T5","Disputed",5,1,1,2,1,1,
     "Two coalition leaders characterize negotiation status differently; power asymmetry (PAS eager BN cautious)",OWNER,"Escalation — resolve with joint statement or official confirmation",REVIEW_DATE),

    # CVS-MLK-409: Hamzah WAWASAN no rift
    ("CVS-MLK-409","MLK","Hamzah Zainuddin (WAWASAN president) says no rift in BN-PN relationship — first direct WAWASAN statement on coalition",
     "Utusan Malaysia","L4 News","https://www.utusan.com.my/berita/politik","2026-08-08","Coalition Position","T2","Verified",7,1,1,2,2,1,
     "Places WAWASAN firmly in PN/BN-PN orbit; resolves auto-approved suggestion #1 WAWASAN alignment",OWNER,"None — key WAWASAN alignment data point",REVIEW_DATE),

    # CVS-MLK-410: Azmin Ali Bersatu PN not jeopardized
    ("CVS-MLK-410","MLK","Mohamed Azmin Ali says Bersatu's membership in PN is not jeopardized — second Bersatu leader disputing Hadi's auto-exit claim (after Muhyiddin cycle 5)",
     "Utusan + Astro Awani","L4 News (2 outlets)","https://www.utusan.com.my/berita/politik","2026-08-08","Coalition Dispute","T2","Verified",7,1,1,2,2,1,
     "Updates T5 CVS-MLK-357; now 2 Bersatu leaders dispute; Azmin role in Bersatu vs PN complex",OWNER,"None — T5 tracking",REVIEW_DATE),

    # CVS-MLK-411: Bersatu Selangor attacks Hadi
    ("CVS-MLK-411","MLK","Bersatu Selangor accused Abdul Hadi of sidelining the PN Chairman (Muhyiddin) — state-level pushback against Hadi's unilateral declarations",
     "Utusan Malaysia","L4 News","https://www.utusan.com.my/berita/politik","2026-08-08","Internal Dispute","T2","Verified",6,1,1,2,1,1,
     "Dispute escalating to divisional level; Bersatu state wing publicly attacking PAS president",OWNER,"Monitor escalation",REVIEW_DATE),

    # CVS-MLK-412: PAS open to Bersatu leaders
    ("CVS-MLK-412","MLK","PAS is open to accepting BERSATU leaders who wish to join the party — PAS courting Bersatu defectors directly (not via coalition)",
     "Harakahdaily","L4 (party newspaper)","https://harakahdaily.net","2026-08-07","Party Strategy","T2","Verified",7,1,1,2,2,1,
     "MAJOR — PAS courting Bersatu defectors; relevant to Mas Ermieyati trajectory (could defect to PAS instead of WAWASAN); party-aligned source",OWNER,"Monitor for named defections",REVIEW_DATE),

    # CVS-MLK-413: Hadi constitutional argument
    ("CVS-MLK-413","MLK","Hadi's constitutional argument: BERSATU's position in PN is voided (gugur) if they form another coalition — legal basis for auto-exit claim",
     "Harakahdaily","L4 (party newspaper)","https://harakahdaily.net","2026-08-07","Constitutional Argument","T2","Verified",7,1,1,2,2,1,
     "Provides legal basis for CVS-MLK-357 T5; Bersatu disputes interpretation; PN constitution not publicly available",OWNER,"Obtain PN constitution text to verify",REVIEW_DATE),

    # CVS-MLK-414: PAS masih runding
    ("CVS-MLK-414","MLK","PAS masih runding (still negotiating) for Melaka PRN in efforts toward unity — PAS-side confirmation of ongoing negotiations (Marang Aug 7)",
     "Harakahdaily","L4 (party newspaper)","https://harakahdaily.net","2026-08-07","Negotiation Status","T2","Verified",7,1,1,2,2,1,
     "Consistent with Hadi Aug 7 declaration; 'runding' ongoing not concluded",OWNER,"None",REVIEW_DATE),

    # CVS-MLK-415: PAS belum buat keputusan
    ("CVS-MLK-415","MLK","PAS belum buat keputusan (has not made a decision) on cooperation for Melaka PRN (Kota Bharu Aug 7) — different venue from Marang statement",
     "Harakahdaily","L4 (party newspaper)","https://harakahdaily.net","2026-08-07","Negotiation Status","T2","Verified",7,1,1,2,2,1,
     "Consistent with CVS-MLK-414 (negotiating but not decided); different PAS figure/venue",OWNER,"None",REVIEW_DATE),

    # CVS-MLK-416: NS exco sworn in
    ("CVS-MLK-416","MLK","NS BN-PN exco sworn in at Istana Besar Seri Menanti: 8 new faces + 2 PN assemblymen in 10-member exco; MB Ismail Lasim heads 3 portfolios; PN satisfied (Hadi); Jalaluddin warns against slander",
     "Utusan + Astro Awani","L4 News (2 outlets)","https://www.utusan.com.my/berita/politik","2026-08-08","Governance Event","T2","Verified",8,1,1,2,2,2,
     "First BN-PN state administration; template for Melaka; dual-source corroborated",OWNER,"None — template confirmed",REVIEW_DATE),

    # CVS-MLK-417: Razlan Rafii NS formula reference
    ("CVS-MLK-417","MLK","Razlan Rafii (UMNO MKT) says NS BN-PN seat-sharing formula can be reference for upcoming elections to avoid Malay vote split — first explicit BN endorsement of NS model",
     "Astro Awani","L4 News","https://www.astroawani.com/berita-politik","2026-08-07","Coalition Strategy","T2","Verified",7,1,1,2,2,1,
     "First BN-side statement endorsing NS formula as template; Razlan is UMNO Supreme Council member",OWNER,"None",REVIEW_DATE),

    # CVS-MLK-418: Blue wave 122 seats (T3 analytical)
    ("CVS-MLK-418","MLK","[ASSESSMENT] Ilham Centre chief Hisommudin Bakar projects BN-PN 'blue wave' could sweep 122 PRU16 seats in Peninsular Malaysia alone",
     "Free Malaysia Today","L4 News (analyst quote)","https://www.freemalaysiatoday.com","2026-08-08","Analytical Projection","T3","Inferred",6,1,1,2,1,1,
     "Analytical (T3); contradicts 'BN-PN berliku' assessment; PRU16 not PRN Melaka but reflects coalition perceived strength",OWNER,"Human review — analytical",REVIEW_DATE),

    # CVS-MLK-419: PRU16 PH strengthening (T3 analytical)
    ("CVS-MLK-419","MLK","[ASSESSMENT] PRU16 analysts: PH expected to strengthen ahead of PRU16 (late 2027?) benefiting from post-3-PRN period; BN-PN alignment described as berliku (complicated) and challenging",
     "Utusan + Astro Awani","L4 News (analyst)","https://www.utusan.com.my/berita/politik","2026-08-08","Analytical Assessment","T3","Inferred",6,1,1,2,1,1,
     "Analytical (T3); contradicts Ilham Centre 'blue wave' (CVS-MLK-418); T5 analytical disagreement on PRU16 prospects",OWNER,"Human review — analytical",REVIEW_DATE),

    # CVS-MLK-420: Bersatu Terengganu crisis
    ("CVS-MLK-420","MLK","Bersatu Terengganu crisis: 3 senior leaders resigned including Datuk Razali Idris — affects Bersatu state-level structure",
     "Utusan + Astro Awani","L4 News (2 outlets)","https://www.utusan.com.my/berita/politik","2026-08-08","Party Crisis","T2","Verified",7,1,1,2,2,1,
     "Compounds Bersatu weakness; dual-source; Terengganu not Melaka but affects party national strength",OWNER,"None",REVIEW_DATE),

    # CVS-MLK-421: Hadi Aug 8 column
    ("CVS-MLK-421","MLK","Hadi's Aug 8 column: 'DAP memimpin PH menyambung kerja penjajah hapuskan Melayu Islam' — claims DAP leads PH in continuing colonial work to eliminate Malay Muslims",
     "Harakahdaily","L4 (party newspaper)","https://harakahdaily.net","2026-08-08","Ideological Position","T2","Verified",7,1,1,2,2,1,
     "Hadi president's column; timed day of PH meeting; reinforces BN-PN Malay unity framing against PH; party-aligned",OWNER,"None — ideological framing",REVIEW_DATE),

    # CVS-MLK-422: PH-Bersatu Selangor collaboration
    ("CVS-MLK-422","MLK","PH and Bersatu Selangor exploring potential collaboration again; Selangor opposition position remains unchanged",
     "Utusan Malaysia","L4 News","https://www.utusan.com.my/berita/politik","2026-08-08","Coalition Dynamics","T2","Partially Verified",6,1,1,2,1,1,
     "Selangor-specific not Melaka; but creates PH-Bersatu realignment precedent; detail limited",OWNER,"Monitor for Melaka implications",REVIEW_DATE),

    # CVS-MLK-423: DAP delegates debate
    ("CVS-MLK-423","MLK","DAP delegates debate staying in government: Ganabatirau (Klang MP) says leaving affirms perception DAP can't deliver promises; DAP faces catch-22",
     "Free Malaysia Today","L4 News","https://www.freemalaysiatoday.com","2026-08-08","Internal Party Debate","T2","Verified",7,1,1,2,2,1,
     "DAP internal debate affects PH national posture; connects to Adly/Amanah Melaka positioning",OWNER,"None",REVIEW_DATE),

    # CVS-MLK-424: Asyraf Wajdi defers
    ("CVS-MLK-424","MLK","Asyraf Wajdi Dusuki (PAS VP) defers seat distribution decisions to top leadership of both coalitions — identifies negotiation structure",
     "Utusan Malaysia","L4 News","https://www.utusan.com.my/berita/politik","2026-08-08","Negotiation Structure","T2","Verified",7,1,1,2,2,1,
     "Top leadership = BN (Zahid/Ab Rauf) + PN (Hadi/Tuan Ibrahim); PAS VP not making seat claims himself",OWNER,"None",REVIEW_DATE),

    # CVS-MLK-425: BERSAMA not NS focus Melaka
    ("CVS-MLK-425","MLK","BERSAMA announced not contesting Negeri Sembilan PRN focusing instead on Melaka PRN (July 15 2026)",
     "Astro Awani","L4 News","https://www.astroawani.com/search?q=melaka+pilihan+raya+negeri","2026-07-15","Strategic Decision","T2","Verified",8,1,2,1,2,2,
     "Corroborates Wikipedia content; BERSAMA factor ONLY in Melaka among 3 state elections; direct source",OWNER,"None — corroboration",REVIEW_DATE),

    # CVS-MLK-426: Assessment WAWASAN alignment
    ("CVS-MLK-426","MLK","[ASSESSMENT] WAWASAN (Hamzah Zainuddin) is firmly in PN/BN-PN orbit — Hamzah's 'no rift' statement + PN component status (CVS-MLK-188) + Yadzil Bemban incumbent (CVS-MLK-189) all align",
     "Analytical synthesis (CJ-MLK-03)","L5 AI-derived","","2026-08-08","Analytical","T3","Inferred",6,1,1,2,2,1,
     "Resolves auto-approved suggestion #1 WAWASAN alignment; WAWASAN does NOT follow Bersatu to IPR",OWNER,"Human review — analytical",REVIEW_DATE),

    # CVS-MLK-427: Assessment negotiation status T5
    ("CVS-MLK-427","MLK","[ASSESSMENT] BN-PN negotiation status T5 reflects power asymmetry: PAS (Hadi) eager to signal progress to press 16-seat claim; BN (Mohamad Hasan) cautious to preserve 'defend 21' position and control narrative",
     "Analytical synthesis (CJ-MLK-03)","L5 AI-derived","","2026-08-08","Analytical","T3","Inferred",5,1,1,2,1,0,
     "Analytical interpretation of CVS-MLK-408 T5; not factual",OWNER,"Human review — analytical",REVIEW_DATE),
]

# Append to CSV
fieldnames = [
    "claim_id","workstream","claim","source_name","source_type","source_url","source_date",
    "evidence_type","tier","validation_status","confidence_score","authority","traceability",
    "recency","consistency","completeness","issue_gap","owner","action_required","last_reviewed"
]

with open(REGISTER, "a", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    for c in claims:
        row = dict(zip(fieldnames, c))
        writer.writerow(row)

print(f"Appended {len(claims)} claims (CVS-MLK-406 to CVS-MLK-427) to {REGISTER}")

# Verify
with open(REGISTER, "r", encoding="utf-8") as f:
    total = sum(1 for _ in f) - 1  # minus header
print(f"Register now has {total} total claims")
