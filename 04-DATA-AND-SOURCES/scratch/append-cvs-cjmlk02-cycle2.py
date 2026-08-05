#!/usr/bin/env python3
"""Append CJ-MLK-02 Cycle 2 (2026-08-05 12:59 MYT) CVS claims to evidence register."""
import csv

REGISTER = "/home/p62operator/.openclaw/workspace-mlk/03-VERIFICATION/CVS-EVIDENCE-REGISTER.csv"

# 20 fields: claim_id,workstream,claim,source_name,source_type,source_url,source_date,
#   evidence_type,tier,validation_status,confidence_score,authority,traceability,recency,
#   consistency,completeness,issue_gap,owner,action_required,last_reviewed
rows = [
    ["CVS-MLK-109","MLK",
     "Mas Ermieyati Samsudin's BERSATU membership was suspended for 2 terms (6 years) in March 2026 for violating the party constitution and code of conduct; she shared the suspension notice via her Instagram. She remains Ketua Srikandi BERSATU.",
     "Berita Harian + Harian Metro","Mainstream news (L4), two corroborating outlets",
     "https://www.bharian.com.my/berita/nasional/2026/03/1519440/mas-ermieyati-digantung-keahlian-bersatu-2-penggal",
     "2026-03","Party Discipline","T1","Verified","9","1","2","2","2","2",
     "Both articles antibot-blocked for full text; key facts from search snippets. Verifies prior Wikipedia signal.","CJMLK02","Human review can confirm full article text","2026-08-05"],
    ["CVS-MLK-110","MLK",
     "Mas Ermieyati Samsudin is confirmed as PAC Chairman of the 15th Parliament as of Feb-Jul 2026 (PAC proceeding 4 Feb 2026, report tabled 8 Jul 2026), despite her March 2026 BERSATU suspension — confirming parliamentary appointment is not removed by party suspension.",
     "Portal Rasmi Parlimen Malaysia","Official parliamentary record (L1)",
     "https://www.parlimen.gov.my/ipms/eps/2026-07-08/DR.22.2026%20-%20DR22.2026.pdf",
     "2026-07-08","Institutional Status","T1","Verified","10","2","2","2","2","2",
     "Full committee list in official PAC report PDF names her as Chairman.","CJMLK02","None","2026-08-05"],
    ["CVS-MLK-111","MLK",
     "Under Mas Ermieyati's chairmanship, the PAC tabled 6 reports in 2026 (as of 16 Jul 2026): cooking oil subsidies (KPDN DR.27/2026), govt vehicle concessions (MOF DR.23/2026), TLDM LCS vessels (MINDEF DR.22/2026), public airports (MOF/Transport/MAHB DR.20/2026), health insurance premiums (MOF/Health/BNM DR.12/2026), FELCRA palm oil procurement (KKDW DR.9/2026).",
     "Portal Rasmi Parlimen Malaysia","Official parliamentary record (L1)",
     "https://parlimen.gov.my/pac/publication-details.html?id=66",
     "2026-07-16","Oversight Agenda","T1","Verified","10","2","2","2","2","2",
     "Authoritative answer to PIR-04 scrutiny targets.","CJMLK02","None","2026-08-05"],
    ["CVS-MLK-112","MLK",
     "On 8 July 2026, the PAC under Mas Ermieyati tabled DR.22/2026 with 6 recommendations directing MINDEF and MOF to maintain strict financial discipline, no additional funds, and keep the LCS (Littoral Combat Ship) project cost under the RM11.22 billion ceiling for all 5 TLDM vessels. Cross-POI: PAC scrutiny of Adly Zahari's MINDEF flagship procurement.",
     "NST + Berita Harian","Mainstream news (L4), EN+BM corroborating",
     "https://www.nst.com.my/news/nation/2026/07/1483481/pac-demands-strict-oversight-financial-discipline-rm1122bil-lcs-project",
     "2026-07-08","Oversight Action","T1","Verified","9","1","2","2","2","2",
     "Corroborates L1 PAC report PDF DR.22/2026.","CJMLK02","None","2026-08-05"],
    ["CVS-MLK-113","MLK",
     "As Timbalan Menteri Pertahanan, Adly Zahari acknowledged in Dewan Rakyat (Oct 2025) that ATM has capability gaps in electronic warfare, medium/long-range layered air defence, Counter-UAS systems, and AI/automation in C2; announced DIPKN implementation and UAV Anka-S acquisition.",
     "Air Times News Network","Secondary media (L4)",
     "https://www.airtimes.my/2025/10/06/mindef-akui-masih-wujud-jurang-keupayaan-pertahanan-moden-adly/",
     "2025-10-06","Policy Statement","T2","Partially Verified","7","1","2","2","2","2",
     "Single L4 source reporting parliamentary reply; corroboration via parlimen.gov.my Hansard possible.","CJMLK02","Corroborate via Hansard Oct 2025","2026-08-05"],
    ["CVS-MLK-114","MLK",
     "On 6 February 2026, Adly Zahari announced in Dewan Rakyat the Pelan Transformasi PERHEBAT 2026-2035, a 10-year plan to develop ATM veterans/retirees as high-quality workforce, with 62+ industry partnerships (incl. Lembaga Tabung Angkatan Tentera) and alignment to Ekonomi MADANI and RMK13/14. Answered question from Dato' Sri Ikmal Hisham (Tanah Merah).",
     "Air Times News Network","Secondary media (L4)",
     "https://www.airtimes.my/2026/02/06/mindef-sasar-tenaga-kerja-berkualiti-melalui-pelan-transformasi-perhebat/",
     "2026-02-06","Policy Initiative","T2","Partially Verified","7","1","2","2","2","2",
     "Single L4 source; corroboration via Hansard 6 Feb 2026 possible.","CJMLK02","Corroborate via Hansard Feb 2026","2026-08-05"],
    ["CVS-MLK-115","MLK",
     "Adly Zahari is the incumbent Timbalan Menteri Pertahanan with an office at Pejabat Timbalan Menteri Pertahanan (MINDEF HQ), staffed with military advisers from the Army (Col Norhidayat, Penasihat Ketenteraan), Air Force/TUDM (Mejar Mohd Fadzil), and Navy/TLDM (Lt Kdr Mohd Izuan) — tri-service advisory structure.",
     "MINDEF Official Directory","Official government directory (L1)",
     "https://direktori.mod.gov.my/mindef/category/pejabat-timbalan-menteri-pertahanan",
     "2026-08-05","Institutional Status","T1","Verified","9","2","2","2","2","1",
     "Tri-service aide structure relevant to deputy's cross-service oversight incl. TLDM LCS.","CJMLK02","None","2026-08-05"],
    ["CVS-MLK-116","MLK",
     "Adam Adli bin Abd Halim is confirmed incumbent Timbalan Menteri Pendidikan Tinggi and MP for P137 Hang Tuah Jaya, Melaka (PH), per Parliament's official MP database (last updated 03/08/2026); office at Kementerian Pendidikan Tinggi, Putrajaya.",
     "Portal Rasmi Parlimen Malaysia","Official parliamentary record (L1)",
     "https://www.parlimen.gov.my/profile-ahli.html?uweb=dr&id=4176",
     "2026-08-03","Institutional Status","T1","Verified","10","2","2","2","2","2",
     "Updated 2 days before collection.","CJMLK02","None","2026-08-05"],
    ["CVS-MLK-117","MLK",
     "On 9 February 2026, Deputy Higher Education Minister Adam Adli received a memorandum outside Parliament from 40+ students (30+ groups, Liga Mahasiswa Malaysia) calling for AUKU abolition and promised 'necessary, appropriate and required steps'; the ministry had stated the prior week it had no plans to abolish AUKU entirely (amended 8 times).",
     "Free Malaysia Today","Independent media (L4)",
     "https://www.freemalaysiatoday.com/category/nation/2026/02/09/adam-vows-to-do-whats-necessary-as-students-seek-abolition-of-auku",
     "2026-02-09","Policy Position","T2","Partially Verified","7","1","2","2","2","2",
     "Single L4 source; corroborated by Sinar Harian UMANY 18 Dec 2025 demand.","CJMLK02","None","2026-08-05"],
    ["CVS-MLK-118","MLK",
     "On 18 December 2025, UMANY urged newly-appointed Deputy Higher Education Minister Adam Adli (replacing Datuk Mustapha Sakmud) to abolish AUKU and PTPTN and implement free higher education, citing his own history as a student activist prosecuted under AUKU.",
     "Sinar Harian","Mainstream media (L4)",
     "https://www.sinarharian.com.my/article/760987/berita/nasional/umany-gesa-adam-adli-mansuhkan-auku-dan-ptptn",
     "2025-12-18","Policy Demand","T2","Partially Verified","7","1","2","2","2","2",
     "Corroborated by FMT 9 Feb 2026 follow-up.","CJMLK02","None","2026-08-05"],
    ["CVS-MLK-119","MLK",
     "Adam Adli replaced Datuk Mustapha Sakmud as Timbalan Menteri Pendidikan Tinggi in the Dec 2025 cabinet reshuffle by PM Anwar Ibrahim, moving from Timbalan Menteri Belia dan Sukan; became Acting PKR Melaka chairman (memangku) Dec 2025.",
     "Sinar Harian + Wikipedia BM","Mainstream (L4) + Wikipedia (L5)",
     "https://ms.wikipedia.org/wiki/Adam_Adli_Abdul_Halim",
     "2025-12-17","Succession","T2","Verified","8","1","2","2","2","2",
     "Predecessor name (Mustapha Sakmud) new detail vs prior cycle; L1 parliament profile corroborates current status.","CJMLK02","None","2026-08-05"],
    ["CVS-MLK-120","MLK",
     "As PAC Chairman, Mas Ermieyati led a working visit to the Malaysia-Thailand border (Rantau Panjang, Kelantan) and called further witnesses in the PAC's cooking oil subsidy investigation under KPDN, finding management unsatisfactory and 2 companies without halal certs packing subsidised oil — culminating in DR.27/2026 (16 Jul 2026).",
     "Harian Metro + Malaysiakini","Mainstream + independent (L4), two corroborating",
     "https://www.malaysiakini.com/news/779858",
     "2025-09","Oversight Action","T2","Verified","8","1","2","2","2","1",
     "Corroborated by L1 PAC report DR.27/2026.","CJMLK02","None","2026-08-05"],
]

# Read existing, then append with \r\n line endings
with open(REGISTER, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, lineterminator="\r\n")
    for r in rows:
        writer.writerow(r)

print(f"Appended {len(rows)} claims (CVS-MLK-109 to CVS-MLK-{108+len(rows)})")

# Verify
with open(REGISTER, "r", encoding="utf-8") as f:
    total = sum(1 for _ in f)
print(f"Register now has {total} lines (1 header + {total-1} data rows)")
