#!/usr/bin/env python3
"""Append CJ-MLK-02 cycle 6 CVS claims to the evidence register.
Uses csv.writer for correct quoting/escaping. Idempotency: skips if last claim already >= CVS-MLK-329."""
import csv, os, sys

REGISTER = "/home/p62operator/.openclaw/workspace-mlk/03-VERIFICATION/CVS-EVIDENCE-REGISTER.csv"

# Detect existing max claim id to avoid duplicate appends
existing_ids = set()
max_num = 0
if os.path.exists(REGISTER):
    with open(REGISTER, newline='', encoding='utf-8') as f:
        for row in csv.reader(f):
            if row and row[0].startswith("CVS-MLK-"):
                existing_ids.add(row[0])
                try:
                    n = int(row[0].split('-')[-1])
                    if n > max_num:
                        max_num = n
                except ValueError:
                    pass

if any(f"CVS-MLK-{n}" in existing_ids for n in range(329, 344)):
    print(f"SKIP: some cycle-6 claims already present (max existing={max_num}). No append.")
    sys.exit(0)

# 20-field schema
# claim_id,workstream,claim,source_name,source_type,source_url,source_date,
# evidence_type,tier,validation_status,confidence_score,authority,traceability,
# recency,consistency,completeness,issue_gap,owner,action_required,last_reviewed
rows = [
["CVS-MLK-329","CJ-MLK-02","PKR National Congress 2026 confirmed for 15-16 August 2026 at MITC Ayer Keroh Melaka; ~2500 delegates + 3000 observers (5500 total); theme 'Memugar Reformasi Membina MADANI'; Anwar officiates; AMK/Wanita conferences 14 Aug. RESOLVES T5 CVS-MLK-322 (Aug 15-16 authoritative; original Jun 25-28 rescheduled).","Astro Awani/Bernama + NST + The Malaysia Press + Sinar Harian + PKR site (multiple)","L4","https://content.astroawani.com/berita-politik/keadilan-anjur-kongres-nasional-2026-di-melaka-pada-15-16-ogos","2026-08-05","News report (multiple L4)","T2","Verified","8","1","2","2","2","1","Resolves T5 CVS-MLK-322; aggregated from 5+ independent sources","CJ-MLK-02","None — T5 resolved","2026-08-07"],
["CVS-MLK-330","CJ-MLK-02","PKR National Congress 2026 originally scheduled 25-28 June 2026 (4 days) announced 25 Jan 2026 by PKR Info Chief Datuk Fahmi Fadzil after MPP meeting; subsequently rescheduled to 15-16 August 2026.","The Malaysian Reserve","L4","https://themalaysianreserve.com/2026/01/25/pkr-to-hold-national-congress-in-melaka-from-june-25-28/","2026-01-25","News report","T2","Verified","7","1","2","1","2","1","Contextual; explains T5 origin (rescheduling)","CJ-MLK-02","None","2026-08-07"],
["CVS-MLK-331","CJ-MLK-02","PKR Congress 2026 full program: theme 'Memugar Reformasi Membina MADANI'; 16 debaters (economy/education/politics); Bill Kayong award to 5 families; foreign diplomats US/China/Japan/Australia; on-site gov services (JPN Imigresen PDRM ROS); Karnival Rahmah Mega by KPDN Melaka; Congress Director Saifuddin Shafi Muhammad.","Astro Awani + The Malaysia Press + NST","L4","https://themalaysiapress.com/2026/08/06/kongres-nasional-pkr-2026-himpun-5500-perwakilan-pemerhati-di-melaka/","2026-08-06","News report","T2","Verified","8","1","2","2","2","1","Congress 8 days from collection date; forward-monitor Adam Adli participation","CJ-MLK-02","None","2026-08-07"],
["CVS-MLK-332","CJ-MLK-02","Adly Zahari (Timbalan Menteri Pertahanan) stated in Dewan Rakyat (13 Jul 2026) LCS-1 delivery target end-2026 maintained despite West Asia conflict; LCS progress 78.1% (31 May 2026) vs 85.21% target (7.11% behind); built at BNS Lumut; question by Datuk Awang Hashim (PN-Pendang).","Malaysia Gazette","L4","https://malaysiagazette.com/2026/07/13/konflik-asia-barat-tidak-jejas-penyerahan-lcs-hujung-tahun-ini-mindef/","2026-07-13","News report (Dewan Rakyat statement)","T2","Verified","7","1","2","2","2","0","Adly LCS response surfaced (closes cycle-5 suggestion 2a); Dewan Rakyat Q&A not direct PAC response","CJ-MLK-02","None","2026-08-07"],
["CVS-MLK-333","CJ-MLK-02","Government implementing Dasar Industri Pertahanan Negara — current focus MRO (maintenance/repair/overhaul) expanding to high-tech (satellites drones defence systems) with G2G cooperation for tech transfer (Adly Zahari Dewan Rakyat 13 Jul 2026).","Malaysia Gazette","L4","https://malaysiagazette.com/2026/07/13/konflik-asia-barat-tidak-jejas-penyerahan-lcs-hujung-tahun-ini-mindef/","2026-07-13","News report (Dewan Rakyat statement)","T2","Verified","7","1","2","2","2","0","Operationalises CVS-MLK-305 (Khaled Nordin local defence industry policy); no Melaka-specific implementation yet","CJ-MLK-02","None","2026-08-07"],
["CVS-MLK-334","CJ-MLK-02","Government strengthening national radar system via new procurement to monitor 3 strategic zones — Sulu Sea South China Sea and Selat Melaka (Straits of Malacca); radar as strategic asset for border surveillance/sovereignty (Adly Zahari Dewan Rakyat 13 Jul 2026) — MELAKA NEXUS.","Malaysia Gazette","L4","https://malaysiagazette.com/2026/07/13/konflik-asia-barat-tidak-jejas-penyerahan-lcs-hujung-tahun-ini-mindef/","2026-07-13","News report (Dewan Rakyat statement)","T2","Verified","7","1","2","2","2","0","MELAKA NEXUS — Selat Melaka named strategic radar zone","CJ-MLK-02","None","2026-08-07"],
["CVS-MLK-335","CJ-MLK-02","PAC (chair Mas Ermieyati) announced 2 Mar 2026 it will begin proceedings on 3 issues from LKAN 1/2026: (1) UKM management/governance; (2) R&D&C&I national programme under MOF (performance deficit waste loss of intellectual assets); (3) Pelaburan Hartanah Berhad (PHB) management/governance.","Astro Awani/Bernama","L4","https://www.astroawani.com/berita-malaysia/lkan-pac-akan-mulakan-prosiding-ke-atas-ukm-dua-lagi-isu","2026-03-02","News report (Bernama)","T2","Verified","7","1","2","1","2","1","Originating announcement; execution tracked July 2026 (CVS-MLK-336/337)","CJ-MLK-02","None","2026-08-07"],
["CVS-MLK-336","CJ-MLK-02","Mas Ermieyati (PAC Chair) chaired PAC proceedings on national R&D&C&I programme under MOF subdivided into Bil. 4(b) and Bil. 4(e) of 2026 (July 2026 period; exact dates unconfirmed).","Parliament of Malaysia official Facebook + Instagram","L2","https://www.facebook.com/ParlimenMY/","2026-07-xx","Official parliament social media","T2","Verified","6","2","1","1","2","0","Exact proceeding dates unconfirmed (Facebook/Instagram blocked extraction); date caveat [UNCONFIRMED]","CJ-MLK-02","Confirm exact proceeding dates","2026-08-07"],
["CVS-MLK-337","CJ-MLK-02","Mas Ermieyati (PAC Chair) chaired PAC proceeding Bil. 3(b)&(c)/2026 on Pelaburan Hartanah Berhad (PHB) at Bilik Jawatankuasa 1 Bangunan Parlimen Malaysia on 21 July 2026; YB Teresa Kok present.","Parliament of Malaysia official Instagram","L2","https://www.instagram.com/p/DbDqBZulFN-/","2026-07-21","Official parliament social media","T2","Verified","7","2","1","2","2","0","Instagram login-walled; content from search snippet","CJ-MLK-02","None","2026-08-07"],
["CVS-MLK-338","CJ-MLK-02","As of 16 Jul 2026 eFishery/KWAP investment issue NOT yet in PAC proceedings; PAC (Mas Ermieyati) will discuss whether to investigate after finishing existing proceedings; KWAP allegedly defrauded by eFishery (manipulated financial reports); SPRM investigating (international cooperation phase 29 Jul 2026); Anwar defended due-diligence (co-investors Temasek SoftBank 42XFund Northstar).","Utusan Malaysia + Harian Metro","L4","https://www.utusan.com.my/nasional/2026/07/pac-pertimbang-siasat-pelaburan-kwap-dalam-efishery/","2026-07-16","News report","T2","Verified","7","1","2","2","2","0","Most likely next formal PAC proceeding; SPRM parallel probe may precede","CJ-MLK-02","Monitor for formal PAC proceeding opening","2026-08-07"],
["CVS-MLK-339","CJ-MLK-02","Adam Adli (Timbalan Menteri Pendidikan Tinggi) disclosed in Dewan Rakyat (10 Feb 2026) that 417158 PTPTN borrowers are in default; RM77.5B total disbursed; 4.26M students served; only 0.7% of defaulters (high-income meeting criteria) face travel bans; 13000 students in free-education initiative.","Says.com + Harian Metro + Sinar Harian + 1media","L4","https://says.com/my/seismik/berita/adam-adli-dedah-ada-lebih-400000-peminjam-kini-masih-culas-bayar-ptptn","2026-02-10","News report (Dewan Rakyat statement)","T2","Verified","7","1","2","1","2","1","Baseline parliamentary-performance item; Feb 2026 (recency 1)","CJ-MLK-02","None","2026-08-07"],
["CVS-MLK-340","CJ-MLK-02","Adly bin Zahari is Deputy Minister of Defence (Timbalan Menteri Pertahanan) MP for P135 Alor Gajah (Melaka) PH — confirmed by official Parliament of Malaysia profile (updated 05/08/2026) and MINDEF directory; in role since 10 Dec 2022.","Parliament of Malaysia (L1)","L1","https://www.parlimen.gov.my/opsearchbi2/profile-ahli.html?uweb=dr&id=4174&lang=en","2026-08-05","Official govt website","T2","Verified","7","2","2","2","2","2","AI-capped T2/score 7 per Rule 6; L1 source eligible for human review to T1/score 9","CJ-MLK-02","Human review for T1 upgrade (L1 source)","2026-08-07"],
["CVS-MLK-341","CJ-MLK-02","Adam Adli bin Abd Halim is Timbalan Menteri Pendidikan Tinggi (Deputy Minister of Higher Education) MP for P137 Hang Tuah Jaya (Melaka) PH — confirmed by official Parliament of Malaysia profile (updated 05/08/2026); appointed Dec 2025 reshuffle (replaced Mustapha Sakmud).","Parliament of Malaysia (L1)","L1","https://www.parlimen.gov.my/opsearchbi2/profile-ahli.html?uweb=dr&id=4176&lang=en","2026-08-05","Official govt website","T2","Verified","7","2","2","2","2","2","AI-capped T2/score 7 per Rule 6; L1 source eligible for human review to T1/score 9; resolves PIR-11 ministerial-prospects (already deputy minister)","CJ-MLK-02","Human review for T1 upgrade (L1 source)","2026-08-07"],
["CVS-MLK-342","CJ-MLK-02","Mas Ermieyati resigned as BERSATU Masjid Tanah division chief + Bersatu Srikandi (Women) chief with 39 committee members (Feb 2026) citing loss of confidence in president Muhyiddin (post Hamzah Zainudin dismissal as deputy president); division committee dissolved; wave of departures across Perak (Tanjung Malim Bukit Gantang Bagan Serai) and Sarawak (Bintulu 110 members).","Scoop + NST + The Vibes + Malay Mail","L4","https://www.scoop.my/news/282319/mas-ermieyati-39-committee-members-quit-bersatu-amid-crisis-of-confidence-in-muhyiddin/","2026-02-19","News report","T2","Verified","7","1","2","1","2","1","Cross-ref existing capture PIR09-KEYSTONE-mas-ermieyati-quits; resolves cycle-5 T5 CVS-MLK-239 (Srikandi role); exact BERSATU membership status (member vs ex-member) ambiguous","CJ-MLK-02","None — PIR-04 context (PAC chair political standing)","2026-08-07"],
["CVS-MLK-343","CJ-MLK-02","PAC presented 6 statements (DR.22-27/2026) in Dewan Rakyat during Mesyuarat Kedua Penggal Keempat Parlimen Ke-15; continuing various proceedings to ensure financial governance transparency/accountability.","Berita Harian","L4","https://www.bharian.com.my/berita/nasional/2026/07/1588934/pac-bentang-enam-penyata-di-dewan-rakyat","2026-07-xx","News report","T2","Verified","6","1","2","1","2","0","Corroborates L1 PAC reports page (DR.22-27/2026); article body blocked (antibot); session context added","CJ-MLK-02","None","2026-08-07"],
]

with open(REGISTER, 'a', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    for r in rows:
        cid = r[0]
        if cid in existing_ids:
            continue
        w.writerow(r)
        print(f"APPENDED {cid}")

print(f"Done. {len(rows)} rows processed. Max existing before: {max_num}")
