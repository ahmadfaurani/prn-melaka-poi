# PRN Melaka — POI Intelligence Workstream Framework

**Workstream:** PRN Melaka — Person of Interest (POI) Intelligence Collection
**HCR:** Pending assignment
**Created:** 2026-08-04 (MYT)
**Classification:** TLP:AMBER
**Director:** DAF (Head of Intelligence, Aras Integrasi)
**Authority:** Director-approved 2026-08-04 — all 15 PIRs approved for data collection

---

## 1. Purpose

Intelligence collection workstream targeting 9 Melaka-based political figures (POIs) across three coalitions: BN/UMNO (3), PN/Bersatu+PAS (3), PH/Amanah+PKR (3). The workstream operates 15 Priority Intelligence Requirements (PIRs) covering governance dynamics, federal-state power relationships, electoral strategy, defence portfolios, parliamentary oversight, coalition negotiations, and grassroots mobilization.

## 2. POI Roster

| # | Name | Coalition | Role | Tier |
|---|------|-----------|------|------|
| 1 | Ab Rauf Yusoh | BN/UMNO | Ketua Menteri Melaka | T1 — Executive |
| 2 | Dr Muhamad Akmal Saleh | BN/UMNO | ADUN Merlimau; Ketua Pemuda UMNO Malaysia | T1 — Organizational |
| 3 | Adly Zahari | PH/Amanah | AP Alor Gajah; Timbalan Menteri Pertahanan | T1 — Federal Executive |
| 4 | Datuk Mas Ermieyati Samsudin | PN/Bersatu | AP Masjid Tanah; Pengerusi PAC Parlimen | T1 — Parliamentary |
| 5 | Adam Adli Abd Halim | PH/PKR | AP Hang Tuah Jaya | T2 — Rising |
| 6 | Zulkifli Ismail | PN/PAS | AP Jasin; Pesuruhjaya PAS Melaka | T2 — Organizational |
| 7 | Mohd Noor Helmy Abdul Halem | BN/UMNO | ADUN Duyong; Timbalan EXCO Melaka | T2 — State EXCO |
| 8 | Shamsul Iskandar @ Yusre Mohd Akin | PKR | Bekas AP Bukit Katil | T3 — Status uncertain |
| 9 | Bakri Jamaluddin | PN/PAS | AP Tangga Batu (uncertain) | T3 — Verification needed |

## 3. PIR Summary

- **Critical:** 5 (PIR-01 through PIR-05)
- **High:** 6 (PIR-06 through PIR-11)
- **Medium:** 4 (PIR-12 through PIR-15)
- **Total:** 15 PIRs

## 4. Directory Taxonomy

| Directory | Purpose |
|-----------|---------|
| 00-OPERATIONS/ | Framework, methodology, scope |
| 01-DAILY-INTELLIGENCE/ | Daily briefs, coalition analysis, SITREPs |
| 02-CONSTITUENCY-INTELLIGENCE/ | Candidate dossiers, constituency profiles, campaign trails |
| 03-VERIFICATION/ | Fact-checks, verification outputs |
| 04-DATA-AND-SOURCES/ | Raw scrapes, processed entities, sentiment, SPR data |
| 05-TOOLS-AND-AUTOMATION/ | Scripts, templates, cronjob configs |
| 06-INFRASTRUCTURE/ | Infrastructure configs, Celery, deployment |
| 07-AUDIT/ | PIR registry, QA, auto-approve suggestion files |

## 5. Cronjob Architecture

| Cronjob | Name | Schedule | PIRs Covered | Deliver |
|---------|------|----------|--------------|---------|
| CJ-MLK-01 | Executive Leadership & Governance | Every 12h | PIR-01, 02, 06, 07, 08 | telegram |
| CJ-MLK-02 | Defence, Parliament & Federal Portfolios | Every 12h | PIR-03, 04, 11 | local |
| CJ-MLK-03 | Coalition Dynamics & Electoral Strategy | Every 12h | PIR-05, 09, 10 | telegram |
| CJ-MLK-04 | Grassroots & Secondary POI | Daily | PIR-12, 13, 14, 15 | local |
| CJ-MLK-05 | Daily Intelligence Brief & PIR Tracker | Daily 12:00 MYT | All 15 | origin |
| CJ-MLK-06 | Git Sync | Daily | N/A (script-only) | local |

## 6. Content Filter

Only collect articles DIRECTLY related to:
1. Melaka state politics, governance, or election
2. Named POIs from the roster above
3. Melaka DUN constituencies (Duyong, Merlimau, Tangga Batu, Jasin, Alor Gajah, Masjid Tanah, Hang Tuah Jaya, Bukit Katil)
4. Coalition dynamics SPECIFICALLY in Melaka context
5. Federal-state intersection topics (defence, PAC scrutiny) where Melaka POIs are actors

## 7. Auto-Approve Loop

Each LLM-driven cronjob (CJ-MLK-01 through CJ-MLK-05) implements the Self-Improving Collection Loop:
- End of cycle: generate TOP 3 PIR suggestions → write to `07-AUDIT/top3-mlk-suggestions-CJMLK0X.md`
- Start of next cycle: read that file and incorporate as AUTO-APPROVED additional search queries

## 8. Git Repository

- Remote: `https://github.com/ahmadfaurani/prn-melaka-poi.git` (private)
- Local: `/home/p62operator/.openclaw/workspace-mlk/`
- Sync: CJ-MLK-06 (script-only, daily, no_agent=True)
