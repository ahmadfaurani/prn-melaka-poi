# CJ-MLK-02 — Defence, Parliament & Federal Portfolios Collection Report

**Workstream:** PRN Melaka — Person of Interest (POI) Intelligence
**Cronjob:** CJ-MLK-02 (Defence, Parliament & Federal Portfolios)
**POIs of Interest:** Adly Zahari (Timbalan Menteri Pertahanan) · Mas Ermieyati Samsudin (Pengerusi PAC) · Adam Adli (AP Hang Tuah Jaya)
**PIRs Addressed:** PIR-POI-MLK-03 (CRITICAL) · PIR-POI-MLK-04 (CRITICAL) · PIR-POI-MLK-11 (HIGH)
**Collection Timestamp:** 2026-08-05 00:27 MYT (UTC+8)
**Cycle:** First collection cycle (no prior `07-AUDIT/top3-mlk-suggestions-CJMLK02.md` existed; none consumed)
**Classification:** TLP:AMBER
**Collector:** CJ-MLK-02 Collection Agent (zai-org/GLM-5.2)

---

## 1. Collection Summary

This is the inaugural CJ-MLK-02 cycle. **28 search queries** were executed across the configured backend. As with the parallel CJ-MLK-01 cycle, the backend **structurally fails** to index Malaysian political content for these POIs — ~20 queries returned zero relevant Malaysian results, with severe token collisions: `"Mas"` → Microsoft Activation Scripts / Monetary Authority of Singapore; `"Adam"` → Biblical Adam; `"Public"` → public.com / Cambridge dictionary; `"Deputy"` → deputy.com scheduling software; `"Hang"` → Merriam-Webster / Hang Seng Bank; `"MINDEF"` → Singapore MINDEF; `"Terendak"` → Room to Read. Only two distinctive Malay institutional tokens (`TLDM`, `Jawatankuasa Kira Wang Negara`) surfaced useful results (navy.mil.my, parlimen.gov.my).

Productive yield came **entirely from direct `web_extract` of Wikipedia (EN + BM) and official Malaysian government pages** — not from search. **9 primary sources** were extracted and saved as raw scrapes: 4 PIR-03 (Adly/defence), 2 PIR-04 (Mas Ermieyati/PAC), 2 PIR-11 (Adam Adli/cabinet), and 1 cross-cutting context (Malay Mail news index, 4 Aug 2026). **No 2026 news article directly naming any of the 3 POIs was obtainable this cycle** — the search backend did not surface Malaysian news for any POI name. The current-context news index (Malay Mail, 4 Aug 2026) did not name the POIs in its top stories but supplied critical political-environment intelligence.

Raw scrapes saved to `04-DATA-AND-SOURCES/raw-scrapes/20260805/`. Scratch metadata saved to `04-DATA-AND-SOURCES/scratch/cj-mlk-02-cycle-20260805-0027-metadata.json`. Auto-approved suggestions written to `07-AUDIT/top3-mlk-suggestions-CJMLK02.md`.

**Key thematic findings:**
1. A **structural Melaka defence nexus is now proven** (PIR-03): the Malaysian Army's **3rd Division and 10th Parachute Brigade are headquartered in Malacca** — a divisional HQ + an elite airborne rapid-reaction formation sit in Adly Zahari's home state. The nexus is **Army/land-airborne, NOT naval** (TLDM HQ is Lumut, Perak).
2. A **high-priority unverified 2026 signal** on Mas Ermieyati (PIR-04): English Wikipedia states her **BERSATU membership has been suspended since 2026**; Malay Wikipedia does not corroborate; no news confirmation obtainable.
3. Adam Adli's **ministerial trajectory is documented and ascending** (PIR-11): Dec 2025 move to Deputy Minister of Higher Education + Acting PKR Melaka chairman, now serving under a BN-UMNO minister.

---

## 2. Findings Table

| # | Source | Date | Summary | PIR | Confidence | Tag |
|---|--------|------|---------|-----|------------|-----|
| A1 | Wikipedia (EN+BM) — Adly Zahari | live | Deputy Minister of Defence since 10 Dec 2022 (under Khaled Nordin since Dec 2023). MP Alor Gajah (maj. 890). MLA Bukit Katil (sole AMANAH MLA in Melaka). AMANAH VP. **PH Chairman for BOTH Malacca AND Kelantan.** PH Treasurer. Former 11th Melaka CM (2018–2020). Speculated for Domestic Trade minister (2023) — Armizan appointed instead (non-advancement). | PIR-03 | HIGH | CRITICAL |
| A2 | Wikipedia — Ministry of Defence (Malaysia) | live | Confirms Adly as incumbent Deputy Defence Minister under Minister Khaled Nordin (BN-UMNO). **2026 budget MYR 21.746B.** DIPKN (National Defence & Security Industry Policy, Mar 2023). Procurement + Defence Industry divisions under deputy purview. Defence White Paper (2020) framework. | PIR-03 | HIGH | CRITICAL |
| A3 | Wikipedia — Malaysian Army | live | **KEYSTONE MELAKA NEXUS:** 3rd Division + 10th Parachute Brigade HQ in **Malacca**. Chief of Army Gen. Azhan Md Othman (since 1 Jan 2026). Western Field Army HQ covers 2nd/3rd/4th Divisions (Peninsula). 10 Para = elite airborne rapid-reaction. | PIR-03 | HIGH | CRITICAL |
| A4 | Wikipedia — Royal Malaysian Navy (TLDM) | live | TLDM HQ = Lumut, Perak (NOT Melaka). ~18,000 personnel. Fleet modernisation: 5 subs + 5 frigates + 3 corvettes under construction (major procurement). SLOC: Straits of Malacca + Singapore. Chief of Navy Adm. Zulhelmy (since Aug 2024). Corrective: Melaka nexus is Army, not naval. | PIR-03 | HIGH | CRITICAL |
| A5 | Wikipedia (EN+BM) — Mas Ermieyati Samsudin | live | PAC Chairperson since 4 Apr 2023 (2nd female PAC chair; dep. Teresa Kok since 2024). MP Masjid Tanah (since 2013). Ketua Srikandi BERSATU (since Oct 2024). **★ EN-WP note: "BERSATU membership suspended since 2026" — UNVERIFIED, BM-WP does not mention.** Lost Tanjung Bidara (Melaka state) to Ab Rauf 2021 (was PN's CM candidate). Salary RM41,681.65/mo. China-PR insinuation controversy (Star, Dec 2023). | PIR-04 | HIGH (role) / UNVERIFIED (suspension) | CRITICAL |
| A6 | parlimen.gov.my — PAC official pages | live (updated 3 Aug 2026) | PAC is 1 of 5 Dewan Rakyat standing committees. Member-list page returned **404**; reports page **JS-rendered/empty**. Most recent verifiable PAC activity = **Dec 2024 photo gallery** (meetings 28 Nov, 4/5/10 Dec 2024). ~8-month gallery gap. Witness-hearing proceedings ("kehadiran saksi-saksi") confirmed. | PIR-04 | MEDIUM | CRITICAL |
| A7 | Wikipedia (EN+BM) — Adam Adli | live | **Deputy Minister of Higher Education since 16/17 Dec 2025** (under Minister Zambry, BN-UMNO). MP Hang Tuah Jaya (maj. 8,638). **Acting PKR Melaka chairman (memangku) since Dec 2025.** PKR Communications Director. Was Deputy Youth & Sports (2022–2025, succeeded by Mordi Bimol/DAP); former AMK Chief (2022–2025). Student-activist sedition case acquitted 2018. | PIR-11 | HIGH | HIGH |
| A8 | Wikipedia — Anwar Ibrahim cabinet | live | Confirms Dec 2023 reshuffle (Khaled Nordin: Higher Ed→Defence; Zambry: Foreign→Higher Ed) setting both Adly's & Adam Adli's ministerial superiors. Dec 2025 reshuffle moved Adam Adli to Higher Ed deputy. **Opposition Leader changed 2026** (Hamzah→Samsuri→Hamzah). Cross-coalition deputy pairings (PH deputy under BN minister) for both Adly & Adam Adli. | PIR-03/11 | HIGH | HIGH (context) |
| C1 | Malay Mail — Malaysia news index | 4 Aug 2026 | **CONTEXT (no direct POI mentions).** NS state election → DAP/PH defeat → Anthony Loke resigned NS DAP chairman; DAP putting government role to vote. Active MACC/RCI Tabung Haji corruption probes (RM300k "renovation bribes"; RM8M rubber-sapling; Tony Pua). Dewan Negara adjourned (12 Bills). NS election opinion piece (Praba Ganesan, 30 Jul). | PIR-04/11 (context) | MEDIUM-HIGH | HIGH (context) |

---

## 3. PIR Resolution Status

| PIR ID | Status | New Evidence | Confidence |
|--------|--------|--------------|------------|
| **PIR-POI-MLK-03** (Adly Zahari — Defence Portfolio & Melaka Nexus) [CRITICAL] | **Partial** | **Defence portfolio** confirmed: Deputy Minister of Defence since Dec 2022 under Khaled Nordin (BN-UMNO); MINDEF 2026 budget MYR 21.746B; DIPKN + Procurement + Defence Industry divisions in his purview. **Melaka nexus PROVEN & characterised:** 3rd Army Division + 10th Parachute Brigade HQ in Malacca (land/airborne, not naval); TLDM HQ is Lumut (Perak); Straits of Malacca SLOC is a TLDM operational area. Adly's political base (Alor Gajah/Bukit Katil) overlaps the army concentration. Documented 2023 non-advancement (Armizan got Domestic Trade over him). **Gap:** No 2026-specific *initiatives Adly is personally driving*, no Melaka-specific procurement/industry-investment decisions, no Adly statements on the Malacca bases. | HIGH (structure) / OPEN (agency) |
| **PIR-POI-MLK-04** (Mas Ermieyati — PAC Scrutiny Targets) [CRITICAL] | **Partial (role); Open (agenda) + Unverified signal** | **Role confirmed:** PAC Chairperson since 4 Apr 2023 (>3 yrs); deputy Teresa Kok (since 2024); 2nd female PAC chair. **High-priority unverified signal:** EN-WP states BERSATU membership suspended since 2026 (BM-WP silent; no news confirmation). **PAC activity:** official site shows Dec 2024 meeting cadence then ~8-month gallery gap; member-list 404; reports JS-empty. **Scrutiny targets:** NOT obtained — no 2026 PAC agenda, no named entities under active investigation. Environmental proxy: active MACC/RCI Tabung Haji corruption probes (4 Aug 2026) are the class of matter PAC scrutinises, but no parallel PAC inquiry confirmed. **Gap:** current 2026 PAC agenda + scrutiny targets + BERSATU-suspension verification. | HIGH (role) / UNVERIFIED (suspension) / OPEN (agenda) |
| **PIR-POI-MLK-11** (Adam Adli — Parliamentary Trajectory & Ministerial Prospects) [HIGH] | **Partial (trajectory); Open (performance/positions)** | **Trajectory documented & ascending:** student activist → PKR (2021) → AMK Chief + MP Hang Tuah Jaya (2022, maj. 8,638) → Deputy Min. Youth & Sports (2022–2025) → **Deputy Min. Higher Education (16/17 Dec 2025) + Acting PKR Melaka chair**. Now serves under BN-UMNO minister Zambry (cross-coalition pairing). Accumulated Melaka party authority (PKR MPN acting chair). **Prospects:** trajectory consistent with grooming for full minister; no 2026 evidence of imminent promotion. **Gap:** No 2026 Dewan Rakyat performance data (questions/speeches), no current Higher-Ed policy positions, no promotion signal — search backend failed entirely on "Adam Adli". | HIGH (trajectory) / OPEN (current performance) |

---

## 4. Analytical Synthesis

### 4.1 The Melaka Defence Nexus — Proven, and It's Army, Not Navy (PIR-03)

The PIR's framing assumed a "TLDM/Melaka defence industry" link. The evidence corrects this: **TLDM's headquarters is at Lumut, Perak, not Malacca.** The actual structural Melaka defence nexus is **land and airborne** — the Malaysian Army's **3rd Division** (a Western Field Army division covering the Peninsula) and the **10th Parachute Brigade** (the army's elite airborne rapid-reaction formation) are both headquartered in Malacca. This is not a minor installation: a divisional HQ plus a strategic airborne brigade in a single state is a substantial military concentration.

The geographic overlap with Adly Zahari's political base is exact — he is MP for Alor Gajah and MLA for Bukit Katil, both in Malacca. As Deputy Minister of Defence, Adly is the federal political overseer of the very ministry whose premier Peninsula land/airborne formations are headquartered in his home state. This creates a **direct minister-to-local-base structural nexus** that is the strongest PIR-03 finding of the cycle. What remains open is the *agentic* dimension: whether Adly has personally engaged with these formations (visits, statements, basing/procurement decisions) in 2026 — this is the #2 priority for next cycle.

The fiscal/policy frame is also now established: MINDEF's 2026 budget is MYR 21.746 billion, and the DIPKN (National Defence & Security Industry Policy, March 2023) plus the Defence Industry and Procurement divisions sit within Adly's deputy purview. The TLDM fleet modernisation (5 subs + 5 frigates + 3 corvettes under construction) is a large-scale procurement programme his ministry oversees — procurement interests are live, though not Melaka-specific.

### 4.2 The BERSATU-Suspension Signal & PAC Institutional Risk (PIR-04)

The single most time-sensitive signal this cycle is the English Wikipedia note that **Mas Ermieyati's BERSATU membership has been suspended since 2026** — a claim absent from the Malay Wikipedia and unconfirmed by any news source (the search backend could not retrieve Malaysian news for her name). If verified, this has two consequences: (a) it alters her standing within the PN opposition bloc at a moment when opposition leadership is itself churning (Hamzah → Samsuri → Hamzah in 2026); (b) it raises a question about the PAC chairmanship, which is conventionally held by an opposition MP appointed by the Speaker. A BERSATU suspension does not automatically remove a parliamentary appointment, but it complicates the "opposition MP chairs PAC" convention and would be a notable institutional anomaly. **This is flagged UNVERIFIED and is the #1 next-cycle priority.**

The PAC's *current 2026 agenda and scrutiny targets* remain the core open gap of PIR-04. The official parlimen.gov.my PAC pages were partly inaccessible (member list 404; reports JS-rendered/empty); the most recent verifiable activity is a Dec 2024 meeting cadence followed by an ~8-month gallery gap. The political environment, however, is oversight-rich: the 4 Aug 2026 Malay Mail index documents active MACC/RCI corruption probes into Tabung Haji (a "design firm director" over RM300k "renovation bribes"; a former estate manager over an RM8M rubber-sapling supply probe under MACC Act s.18; Tony Pua denying a stake in a tech firm awarded a Tabung Haji project). These are precisely the class of government-spending/integrity matters the PAC scrutinises — but whether Mas Ermieyati's PAC has opened a parallel inquiry is unknown and is a concrete, tractable target for the next cycle.

### 4.3 Adam Adli's Ascending Trajectory & the PH/DAP Strain Window (PIR-11)

Adam Adli's ministerial trajectory is the clearest documented arc of the three POIs: student activist → PKR (2021) → AMK Chief + MP Hang Tuah Jaya (2022) → Deputy Minister Youth & Sports (2022–2025) → **Deputy Minister Higher Education (Dec 2025)**, simultaneously becoming **Acting PKR Melaka chairman**. The Dec 2025 move is a portfolio upgrade to a larger, policy-heavy ministry (Higher Education under Minister Zambry, BN-UMNO) — a cross-coalition deputy pairing that structurally mirrors Adly Zahari's (PH deputy under BN minister). He has now accumulated Melaka party authority (PKR MPN acting chair) on top of his federal seat, making him PKR's senior Melaka figure.

The PIR asks about "prospects for ministerial appointment within the PH federal government" — note he is **already a Deputy Minister**; the live question is promotion to **full Minister**. His trajectory is consistent with grooming, but two 2026 environmental factors shape the prospect: (a) the **Negeri Sembilan state election defeat** (DAP/PH lost) triggered Anthony Loke's resignation as NS DAP chairman and DAP "putting government role to vote" — a strain within the PH coalition that could reshuffle PKR's ministerial slots and either open or close space for Adam Adli's promotion; (b) the opposition-leadership churn (Hamzah→Samsuri→Hamzah) changes the competitive frame. No 2026 Dewan Rakyat performance data (questions/speeches/committee work) or current Higher-Ed policy positions were captured — this is the principal PIR-11 gap and the #3 next-cycle priority.

### 4.4 A Structural Pattern: PH Deputies Under BN Ministers

A cross-cutting finding worth flagging: both Adly Zahari (Deputy Defence under BN-UMNO's Khaled Nordin) and Adam Adli (Deputy Higher Education under BN-UMNO's Zambry) serve as **PH deputies beneath BN ministers** — a structural feature of Anwar's "unity government" power-sharing. This pairing can constrain a deputy's visibility and policy autonomy (the senior minister sets direction) and may shape advancement timelines. Adly's documented 2023 non-advancement (speculated for Domestic Trade minister after Salahuddin's death, but GRS's Armizan appointed instead) is a data point on how cross-coalition deputies can be passed over for full-minister promotions that go to other coalition partners. Adam Adli's promotion path should be read against this precedent.

---

## 5. Collection Limitations & Honest Reporting

- **Search backend — structural failure (confirmed across two cycles):** ~20 web_search queries returned ZERO relevant Malaysian results for these POIs. Token collisions are severe and predictable: `Mas`→Microsoft Activation Scripts/Monetary Authority of Singapore; `Adam`→Biblical Adam; `Public`→public.com/Cambridge; `Deputy`→deputy.com; `Hang`→Merriam-Webster/Hang Seng; `MINDEF`→Singapore MINDEF; `Terendak`→Room to Read. Only distinctive Malay institutional tokens (`TLDM`, `Jawatankuasa Kira Wang Negara`) surfaced useful domains (navy.mil.my, parlimen.gov.my). This is a **structural limitation** that should be flagged to the Director — CJ-MLK-01 documented the identical failure. **Productive intelligence this cycle came ENTIRELY from direct `web_extract` of pre-identified Wikipedia and government URLs, not from search.**
- **No 2026 POI-named news articles obtained:** The freshest current news source (Malay Mail index, 4 Aug 2026) did not name any of the 3 POIs. No dated 2026 news article directly featuring Adly, Mas Ermieyati, or Adam Adli was captured. The intelligence base is therefore *reference/structural* (Wikipedia + official pages) plus *environmental context* (Malay Mail), not *current-event*.
- **PAC official pages partly inaccessible:** The committee member-list returned 404; the reports list is JavaScript-rendered (empty on static extract). Current PAC composition was confirmed via Wikipedia instead; 2026 scrutiny targets could NOT be obtained. The most recent verifiable PAC activity is a Dec 2024 photo-gallery cadence.
- **Unverified signal clearly labelled:** The Mas Ermieyati "BERSATU membership suspended since 2026" note is flagged UNVERIFIED throughout (it appears only in English Wikipedia, not Malay, with no news corroboration). No fabricated confirmation was introduced.
- **No fabricated content:** All article content is from real `web_extract` retrieval of Wikipedia and official Malaysian government pages. The one fresh signal (BERSATU suspension) is explicitly labelled unverified with its corroboration gap stated.

---

## 6. Files Produced This Cycle

| Path | Type |
|------|------|
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/PIR03-wikipedia-adly-zahari-profile.md` | Raw scrape (A1) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/PIR03-wikipedia-mindef-malaysia-adly-deputy.md` | Raw scrape (A2) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/PIR03-wikipedia-malaysian-army-melaka-nexus.md` | Raw scrape (A3) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/PIR03-wikipedia-royal-malaysian-navy-tldm.md` | Raw scrape (A4) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/PIR04-wikipedia-mas-ermieyati-pac-profile.md` | Raw scrape (A5) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/PIR04-parlimen-gov-my-pac-official-pages.md` | Raw scrape (A6) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/PIR11-wikipedia-adam-adli-profile.md` | Raw scrape (A7) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/PIR11-wikipedia-anwar-cabinet-reshuffle-context.md` | Raw scrape (A8) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/CONTEXT-malaymail-malaysia-news-index-20260804.md` | Raw scrape (C1) |
| `04-DATA-AND-SOURCES/scratch/cj-mlk-02-cycle-20260805-0027-metadata.json` | Scratch metadata |
| `07-AUDIT/top3-mlk-suggestions-CJMLK02.md` | Auto-approved suggestions (next cycle) |
| `01-DAILY-INTELLIGENCE/cj-mlk-02-defence-parliament-20260805-0027MYT.md` | This report |

---

## TOP 3 PIR SUGGESTIONS FOR NEXT CYCLE (AUTO-APPROVED)

> These 3 suggestions have been written to `07-AUDIT/top3-mlk-suggestions-CJMLK02.md` for auto-incorporation into the next CJ-MLK-02 cycle.

### Suggestion 1: VERIFY Mas Ermieyati's BERSATU Membership Suspension (2026) & PAC Chair Status
**Text:** Confirm whether/when BERSATU suspended Mas Ermieyati's membership, the stated reason, and whether it affects her PAC chairmanship (a parliamentary appointment, not a party one — so suspension may not remove her, but complicates the "opposition MP chairs PAC" convention). Determine her factional position amid 2026 opposition-leadership churn (Hamzah→Samsuri→Hamzah).
**Rationale:** Freshest (2026), highest-impact, currently UNVERIFIED signal. A suspended-chair PAC is a major institutional anomaly. Recovery must use Malay-language news terms + direct site extraction (web_search failed on her name).
**Search Queries:**
1. `Mas Ermieyati Samsudin gantung keahlian BERSATU 2026 sebab`
2. `Pengerusi PAC Mas Ermieyati status 2026 BERSATU PN`
3. Direct extract: ms.wikipedia re-check + BERSATU/PN official statements + Malay Mail/Bernama BERSATU tag pages

### Suggestion 2: Adly Zahari's 2026 MINDEF Initiatives & the Melaka 3rd-Division/10-Para Nexus
**Text:** Target Adly's 2026 MINDEF statements/programme launches (Defence White Paper implementation, DIPKN industry development, veteran/national-service files); any Adly visit to or statement about the Malacca-based 3rd Div/10 Para Bde (his constituency hosts them); Melaka-specific defence-industry investment or TLDM Straits-of-Malacca patrol activity.
**Rationale:** PIR-03 (CRITICAL) requires *what Adly is driving* + the *Melaka nexus*. Structural nexus now proven; *agentic* nexus (Adly's personal engagement) is the open gap. Use distinctive Malay institutional tokens + direct extraction of mod.gov.my / army.mil.my / navy.mil.my news.
**Search Queries:**
1. `Adly Zahari lawatan 3 Divisi 10 Para Kem Malacca 2026`
2. `Kementah DIPKN industri pertahanan 2026 Timbalan Menteri Pertahanan`
3. Direct extract: mod.gov.my + army.mil.my news + Bernama defence/MINDEF category

### Suggestion 3: Adam Adli's 2026 Parliamentary Performance & Post-Dec-2025 Higher-Education Policy Positions
**Text:** Obtain Adam Adli's 2026 Dewan Rakyat contributions (questions/speeches/committee work) via Parliament Hansard/MP profile pages; his policy positions as Deputy Higher Education minister (university funding, student affairs, PTPTN, autonomy); any promotion-to-full-minister signal, especially given post-NS-election PH/DAP strain (DAP putting government role to vote) which may reshuffle PKR ministerial slots.
**Rationale:** PIR-11 (HIGH) only PARTIALLY resolved — trajectory documented; current performance/positions absent. Dec 2025 reshuffle + Aug 2026 PH/DAP strain is the window where ministerial-prospect signals surface. web_search failed entirely on "Adam Adli"; use parliamentary record directly + Malay tokens.
**Search Queries:**
1. `Adam Adli Hang Tuah Jaya soalan Dewan Rakyat 2026`
2. `Timbalan Menteri Pendidikan Tinggi Adam Adli dasar universiti 2026`
3. Direct extract: parlimen.gov.my MP profile (P137) + mohe.gov.my news + Malay Mail/NST/Bernama Higher Education category

---

*End of CJ-MLK-02 report — Cycle 2026-08-05 00:27 MYT*
