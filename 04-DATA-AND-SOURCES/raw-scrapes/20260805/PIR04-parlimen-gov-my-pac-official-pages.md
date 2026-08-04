# Raw Scrape — Official Malaysian Parliament PAC Pages (parlimen.gov.my)

**Source URLs:**
- https://parlimen.gov.my/jawatankuasa-dr.html?uweb=dr (Dewan Rakyat committees directory)
- https://parlimen.gov.my/pac (PAC official landing page)
- https://parlimen.gov.my/ahli-jawatankuasa.html (committee members — returned 404)
- https://parlimen.gov.my/publication-details.html?id=66 (PAC reports/publications — JS-rendered, empty)

**Title:** Portal Rasmi Parlimen Malaysia — Jawatankuasa Kira-kira Wang Negara (PAC)
**Date Retrieved:** 2026-08-05 00:27 MYT (UTC+8)
**PIR Tag:** PIR-POI-MLK-04 (Mas Ermieyati — PAC Scrutiny Targets) [CRITICAL]
**Priority:** CRITICAL
**Source Type:** Official government source (extracted via web_extract)

---

## Full Content (consolidated extraction)

### Dewan Rakyat Standing Committees (5)
| Committee (BM) | English | Link |
|---|---|---|
| Jawatankuasa Pemilih | Selection Committee | view=51 |
| **Jawatankuasa Kira-kira Wang Negara** | **Public Accounts Committee (PAC)** | parlimen.gov.my/pac |
| Jawatankuasa Peraturan Mesyuarat | Standing Orders Committee | view=55 |
| Jawatankuasa Dewan | House Committee | view=52 |
| Jawatankuasa Hak dan Kebebasan | Rights and Privileges Committee | view=54 |

### PAC Landing Page (parlimen.gov.my/pac) — Structure
The PAC official page presents three access portals:
1. **PROFIL** (Profile) → links to member list at parlimen.gov.my/ahli-jawatankuasa.html
2. **LAPORAN** (Reports) → links to publications at parlimen.gov.my/publication-details.html?id=66
3. **GALERI FOTO** (Photo Gallery) + **GALERI VIDEO** (Video Gallery)

### ★ PAC Photo Gallery — Most Recent Verifiable Activity Dates ★
| Date | Gallery link ID |
|---|---|
| **10 Disember 2024** (10 Dec 2024) | galeri-details.html?id=1915 |
| **5 Disember 2024** (5 Dec 2024) | galeri-details.html?id=1914 |
| **4 Disember 2024** (4 Dec 2024) | galeri-details.html?id=1913 |
| **28 November 2024** (28 Nov 2024) | galeri-details.html?id=1911 |

Video gallery notable entries:
- "KEHADIRAN SAKSI-SAKSI KE PROSIDING PAC PARLIMEN" (Attendance of witnesses at PAC Parliament proceedings)
- "Lawatan Delegasi Badan Akauntabilitas Publik Dewan Perwakilan Daerah Republik Indonesia" (Visit by Indonesian Regional Representative Council Public Accountability Body delegation)
- "PAC Siri 3", "PAC Siri 2"

### Member List Page (ahli-jawatankuasa.html) — STATUS
> **An error has occurred. The requested page cannot be found.**
The committee member list page returned a 404 error. Current PAC composition (chair, deputy, members) could NOT be obtained from the official parliament site this cycle. (Composition confirmed via Wikipedia instead: Chair = Mas Ermieyati since 4 Apr 2023; Deputy = Teresa Kok since 2024.)

### Reports Page (publication-details.html?id=66) — STATUS
The page structure contains a publication table (columns: Tajuk/Title, Tarikh Pembentangan/Presentation Date, Muat Turun/Download) plus an archive link (publication-details.html?arkib=yes&id=66). **However, the actual publication entries were NOT rendered** (require JavaScript to load dynamically, or category ID 66 currently has no active entries). No 2026 PAC report titles or scrutiny targets could be extracted.

### Page metadata
- Both pages last updated: 03/08/2026 (3 Aug 2026)
- Page generation time: ~0.024–0.026 seconds (v5)
- Languages: BM / EN toggle available

---

## Collector Notes (PIR-04 specific)
- The official PAC web presence confirms the institutional structure but does **NOT expose current (2026) scrutiny targets** through static scraping. The member list is 404; the reports list is JS-rendered.
- The **most recent verifiable PAC activity** from the official site is the **Dec 2024 meeting cadence** (4 meetings photographed between 28 Nov and 10 Dec 2024). There is a ~8-month gap with no photographed activity visible on the landing page — either PAC meetings in 2025–2026 are not yet gallery-published, or the gallery was not refreshed. This gap is itself a data point.
- The "Kehadiran saksi-saksi ke prosiding PAC" video confirms PAC holds witness-hearing proceedings (the core scrutiny mechanism).
- **Next-cycle action:** Attempt to (a) recover the member-list page via the correct URL (the sitemap or the BM/EN toggle may yield a working path), (b) access the PAC reports archive (publication-details.html?arkib=yes&id=66) for historical report titles, and (c) obtain 2025–2026 PAC report titles from Hansard or news sources.

*End of raw scrape — Parlimen Malaysia PAC official pages.*
