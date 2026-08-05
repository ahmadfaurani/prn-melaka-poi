#!/usr/bin/env python3
"""Append CVS claims for CJ-MLK-02 cycle 3 (2026-08-06 01:15 MYT) to evidence register."""
import csv, os

REGISTER = "/home/p62operator/.openclaw/workspace-mlk/03-VERIFICATION/CVS-EVIDENCE-REGISTER.csv"
LAST_REVIEWED = "2026-08-06"
OWNER = "CJMLK02"

# 12 new claims: CVS-MLK-168 to CVS-MLK-179
rows = [
    ["CVS-MLK-168","MLK","On 8 April 2026, Timbalan Menteri Pertahanan Adly Zahari personally officiated the launch of the Ikhtiar Autisme Angkatan Tentera Malaysia (IA-ATM) programme at PPDK Umi Kem Terendak Melaka — his second site visit after Pangkalan TLDM Lumut Perak. RESOLVES cycle-2 Melaka-base agency gap.","Kementerian Pertahanan Malaysia (mod.gov.my)","Official government website (L1)","https://www.mod.gov.my/index.php/media2/berita/timbalan-menteri-pertahanan-sempurnakan-majlis-peluncuran-program-ikhtiar-autisme-angkatan-tentera-malaysia-ia-atm-di-pusat-pemulihan-dalam-komuniti-ppdk-umi-kem-terendak-melaka","2026-04-08","Institutional Visit","T1","Verified","10","2","2","2","2","2","None — L1 official; corroborated by Utusan L4",OWNER,"None",LAST_REVIEWED],
    ["CVS-MLK-169","MLK","The IA-ATM programme cost RM528000 total (RM2200/participant) funded by Lembaga Tabung Haji with 12 Nasom-designed modules and 10 children per PPDK at PPDK Umi Kem Terendak Melaka and PPDK Lautan Kasih Pangkalan TLDM Lumut; senior military attended incl Panglima Armada Barat.","Utusan Malaysia","Mainstream media (L4)","https://www.utusan.com.my/nasional/2026/04/mindef-lancar-program-ikhtiar-autisme-untuk-anak-tentera","2026-04-07","Programme Detail","T1","Verified","9","1","2","2","2","2","Corroborates L1 mod.gov.my; financial+programme detail",OWNER,"None",LAST_REVIEWED],
    ["CVS-MLK-170","MLK","Adly Zahari attended DSA-NATSEC 2026 (19-23 Apr 2026 MITEC KL) as Defence Deputy Minister alongside Minister Khaled Nordin and tri-service chiefs; record 1456 exhibitors/63 countries 368 Malaysian companies DIPN targeting 30% local component ICP documents worth RM1.4B.","BERNAMA","National news agency (L2)","https://www.bernama.com/en/general/news.php?id=2546622","2026-04-19","Defence Industry Event","T1","Verified","9","2","2","2","2","1","Adly present; connects to DIPKN (CVS-MLK-113)",OWNER,"None",LAST_REVIEWED],
    ["CVS-MLK-171","MLK","MINDEF signed 24 contracts and ICPs valued at RM3.54 billion (12 contracts + 4 LOIs RM1.01B + 8 ICPs RM1.40B) at DSA/NATSEC 2026 on 22 April 2026 with Adly Zahari Khaled Nordin and KSU Datuk Lokman Hakim Ali present.","BernamaBiz","National news agency business (L2)","https://www.bernamabiz.com/news.php?id=2548193","2026-04-22","Procurement Output","T1","Verified","9","2","2","2","2","1","KSU Lokman Hakim = PAC LCS witness (DR.22/2026); procurement freeze link",OWNER,"None",LAST_REVIEWED],
    ["CVS-MLK-172","MLK","MINDEF froze all procurement consideration processes for 2-3 months earlier in 2026 due to unavoidable circumstances per Defence Minister Khaled Nordin at DSA2026; impacted number of contracts signed.","BernamaBiz","National news agency (L2)","https://www.bernamabiz.com/news.php?id=2548193","2026-04-22","Procurement Policy","T2","Partially Verified","7","2","2","2","2","0","Freeze cause unspecified; possible link to PAC LCS directive",OWNER,"Corroborate freeze rationale vs PAC directive",LAST_REVIEWED],
    ["CVS-MLK-173","MLK","At DSA2026 Adly Zahari received courtesy visit from Azerbaijan Deputy Minister of Defence Industry Mehman Bakhishov and held bilateral meeting on defence science technology and industry cooperation.","Adly Zahari Official Facebook","Social media official page (L5)","https://www.facebook.com/AdlyZahariOfficial/posts/semalam-di-defence-services-asia-dsa-2026-saya-menerima-kunjungan-hormat-tyt-meh/1489024472583048/","2026-04-21","Defence Diplomacy","T2","Partially Verified","5","1","1","2","1","0","L5 snippet; attendance corroborated by L2 Bernama; bilateral detail single-source",OWNER,"Corroboration via MOFA/BERNAMA",LAST_REVIEWED],
    ["CVS-MLK-174","MLK","On 17 March 2026 Adly Zahari delivered Eminent Speaker Executive Talk titled Malaysia's National Defence Policy The Foundation of Its National Power in a Competitive Age at Kursus Ketahanan Negara 7/2026 Maktab Ketahanan Nasional.","Kementerian Pertahanan Official Facebook","Social media official page (L5)","https://www.facebook.com/KementerianPertahanan/posts/kuala-lumpur-17-mac-2026-timbalan-menteri-pertahanan-yb-adly-bin-zahari-telah-me/1366805385484056/","2026-03-17","Policy Statement","T2","Partially Verified","6","1","1","2","2","0","L5 snippet only; official MINDEF page; full text blocked",OWNER,"Corroboration via MINDEF news or MKN record",LAST_REVIEWED],
    ["CVS-MLK-175","MLK","PAC 2026 publications page (L1) confirms 6 reports tabled under Mas Ermieyati with official PDF URLs: DR.27 cooking oil 16 Jul DR.23 govt vehicles 9 Jul DR.22 LCS 8 Jul DR.20 airports 1 Jul DR.12 health insurance 24 Jun DR.9 FELCRA 3 Mar. PDFs exceed extract size limit and parlimen.gov.my unreachable via curl.","Portal Rasmi Parlimen Malaysia","Official parliamentary record (L1)","https://parlimen.gov.my/pac/publication-details.html?id=66","2026-08-06","Oversight Agenda","T1","Verified","10","2","2","2","2","2","Agenda confirmed; PDF text extraction pending technical blocker",OWNER,"Retry PDF extraction via different network/extractor",LAST_REVIEWED],
    ["CVS-MLK-176","MLK","On 17 June 2026 Adam Adli (Timbalan Menteri Pendidikan Tinggi) announced three concrete PTPTN reforms: targeted repayment by ability income-contingent repayment and travel restrictions now income-based (RM6000+ threshold) not blanket; denied U-turn on PTPTN principles. Also confirmed MPP PKR member.","MalaysiaPost","Secondary media (L4)","https://malaysiapost.com.my/2026/06/17/isu-ptptn-saya-tak-pernah-u-turn-adam-adli/","2026-06-17","Policy Output","T2","Partially Verified","7","1","2","2","2","0","Concrete 2026 higher-ed policy output; single L4; corroborate via Hansard/MOHE",OWNER,"Corroborate via Hansard or MOHE official",LAST_REVIEWED],
    ["CVS-MLK-177","MLK","On 16-17 Dec 2025 UMNO MKT member Puad Zarkashi challenged newly-appointed Deputy Higher Ed Minister Adam Adli (who replaced Datuk Mustapha Sakmud) to fulfill student-activist pledge to abolish PTPTN; netizens echoed demand illustrating activist-to-officeholder tension.","The Rakyat Insight + MalaysiaGazette + mediatelus","Mainstream media (L4) 3 outlets","https://therakyatinsight.com/puad-cabar-adam-adli-dah-jadi-timbalan-menteri-berani-hapus-ptptn/","2025-12-17","Political Pressure","T2","Verified","8","1","2","2","2","1","Three corroborating outlets; spelling variant Mustapha/Mustafa",OWNER,"None",LAST_REVIEWED],
    ["CVS-MLK-178","MLK","Dec 2025 cabinet reshuffle promoted 6 deputy ministers to full ministers incl Datuk Mustafa Sakmud from Tim. Pendidikan Tinggi to Menteri JPM Sabah/Sarawak; Adam Adli filled vacated Deputy Higher Ed slot transferring from Deputy Youth & Sports. PM Anwar announced 11-portfolio reshuffle.","Harian Metro / BERNAMA","National news agency (L2)","https://www.hmetro.com.my/mutakhir/2025/12/1300636/rombakan-kabinet-6-timbalan-menteri-naik-pangkat-satu-muka-baharu","2025-12-16","Cabinet Reshuffle","T1","Verified","9","2","2","2","2","1","Confirms Adam Adli succession; 6-deputy-promotion pattern = ministerial prospect signal",OWNER,"None",LAST_REVIEWED],
    ["CVS-MLK-179","MLK","Adam Adli Abdul Halim confirmed as Ahli Majlis Pimpinan Pusat (MPP) PKR — central leadership council membership — in addition to Timbalan Menteri Pendidikan Tinggi and MP Hang Tuah Jaya as of June 2026.","MalaysiaPost","Secondary media (L4)","https://malaysiapost.com.my/2026/06/17/isu-ptptn-saya-tak-pernah-u-turn-adam-adli/","2026-06-17","Party Position","T2","Partially Verified","7","1","2","2","2","0","Party-leadership advancement alongside ministerial role; single L4",OWNER,"Corroborate via PKR official",LAST_REVIEWED],
]

header = ["claim_id","workstream","claim","source_name","source_type","source_url","source_date","evidence_type","tier","validation_status","confidence_score","authority","traceability","recency","consistency","completeness","issue_gap","owner","action_required","last_reviewed"]

# Read existing, append new (preserve existing)
existing = []
with open(REGISTER, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for r in reader:
        existing.append(r)

# Verify header matches
assert existing[0] == header, f"Header mismatch: {existing[0]}"

# Check last claim_id
last_id = existing[-1][0] if len(existing) > 1 else "(none)"
print(f"Existing rows: {len(existing)-1} data rows (last: {last_id})")

# Append
with open(REGISTER, "a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)

print(f"Appended {len(rows)} new claims (CVS-MLK-168 to CVS-MLK-179)")

# Verify
with open(REGISTER, "r", encoding="utf-8") as f:
    total = sum(1 for _ in f) - 1
print(f"Total claims in register now: {total}")
