# CJ-MLK-04 — Grassroots & Secondary POI Collection Report

**Workstream:** PRN Melaka — Person of Interest (POI) Intelligence
**Cronjob:** CJ-MLK-04 (Grassroots & Secondary POI Collection)
**POIs of Interest:** Zulkifli Ismail (PIR-12) · Mohd Noor Helmy (PIR-13) · Shamsul Iskandar (PIR-14) · Bakri Jamaluddin (PIR-15)
**PIRs Addressed:** PIR-POI-MLK-12 (MEDIUM) · PIR-POI-MLK-13 (MEDIUM) · PIR-POI-MLK-14 (MEDIUM) · PIR-POI-MLK-15 (MEDIUM)
**Collection Timestamp:** 2026-08-05 00:54 MYT (UTC+8)
**Cycle:** First collection cycle (no prior `07-AUDIT/top3-mlk-suggestions-CJMLK04.md` existed; sibling cycles CJ-MLK-01/02/03 context consumed)
**Classification:** TLP:AMBER
**Collector:** CJ-MLK-04 Collection Agent (zai-org/GLM-5.2)

---

## 1. Collection Summary

This is the inaugural CJ-MLK-04 cycle. **8 web_search queries** (the PIR-specified set) were executed; consistent with the parallel CJ-MLK-01/02/03 cycles, the configured search backend **structurally fails** to index Malaysian political content — all 8 queries returned irrelevant results (Vietnamese banking pages, Italian furniture shops, Bali tourism, Malaysian property listings, Netflix shows, name-disambiguation pages). Only **one** search result was useful: query 4 surfaced the Wikipedia "Members of the Dewan Rakyat, 15th Malaysian Parliament" page, which corroborates the Malacca federal-seat split (PH 3 / PN 3 / BN 0).

**Productive intelligence came ENTIRELY from direct `web_extract` of pre-identified high-value Wikipedia URLs** — constituency pages, person biographies, the Malacca State Executive Council page, and the PAS national page. **9 primary sources** were extracted and saved as raw scrapes. The single most important source — **Shamsul Iskandar's Wikipedia person page** — directly resolves PIR-14's core question (current status / re-entry intentions) by documenting his November 2025 resignation, MACC arrest, and four December 2025 corruption charges.

**Key thematic finding:** All four Medium-tier PIRs were advanced this cycle, two to resolution. **PIR-15 (Bakri Jamaluddin)** affiliation is **CONFIRMED** (PN/PAS, Tangga Batu MP). **PIR-14 (Shamsul Iskandar)** current status is **CONFIRMED** (not an MP, resigned from government, facing active corruption charges — political re-entry BLOCKED). **PIR-12 (Zulkifli Ismail)** MP status is confirmed but the "PAS Melaka commissioner" title remains unverified. **PIR-13 (Mohd Noor Helmy)** Deputy-EXCO role and marginal seat are documented. A striking cross-PIR finding: **Tangga Batu is a recurring battleground** — Shamsul (PIR-14) contested it 2004 (lost), Zulkifli (PIR-12) contested it 2018 (lost), and Bakri (PIR-15) won it 2022. All three POIs' electoral histories intersect in one seat.

Raw scrapes saved to `04-DATA-AND-SOURCES/raw-scrapes/20260805/`. Scratch metadata saved to `04-DATA-AND-SOURCES/scratch/cj-mlk-04-cycle-20260805-0054-metadata.json`. Auto-approved suggestions written to `07-AUDIT/top3-mlk-suggestions-CJMLK04.md`.

---

## 2. Findings Table

| # | Source | Date | Summary | PIR | Confidence | Tag |
|---|--------|------|---------|-----|------------|-----|
| B1 | Wikipedia EN — Jasin (federal constituency) | MP since 2022 (extracted 5 Aug 2026) | **★ Zulkifli Ismail MP CONFIRMED.** Jasin P139, PN/PAS, since 2022. Won GE15 27,893 (35.95%) vs BN 27,571 (35.53%) vs PH 21,674 (27.93%) — **majority 322 votes (0.42%)**, extremely marginal. PN GAIN from BN (BN held 1974-2022, incl. ex-DPM Ghafar Baba). Seat 74.3% Malay. State seats within: 4 BN (UMNO) + 1 PN (WAWASAN/Bemban). | PIR-12 | HIGH | CRITICAL |
| B2 | Wikipedia EN — Tangga Batu (federal constituency) | MP since 2022 | **★ Bakri Jamaluddin affiliation CONFIRMED.** Tangga Batu P136, PN/PAS, since 2022. Won GE15 37,406 (40.65%) vs PH/PKR Rusnah 28,557 (31.03%) vs BN/MCA Lim Ban Hong 25,095 (27.27%) — majority 8,849 (9.62%). PN GAIN from PKR. Seat 71.9% Malay, 22.3% Chinese; pop 198,033 (largest Malacca federal seat). State seats within: 3 BN + 1 PN (BERSATU). **History:** Shamsul Iskandar (PKR) contested 2004 (lost, 20.64%); Zulkifli Ismail (PAS) contested 2018 (lost, 12.96%); Bakri (PN/PAS) WON 2022. | PIR-15 (cross PIR-12/14) | HIGH | CRITICAL |
| B3 | Wikipedia EN — Shamsul Iskandar Mohd Akin (person) | live (updated through Dec 2025) | **★ KEYSTONE — PIR-14 RESOLVED.** Born 29 Dec 1974 (age 51), Malacca. PKR. MP Bukit Katil 2013-18 (defeated CM Mohd Ali Rustam), MP Hang Tuah Jaya 2018-22. Deputy Min Primary Industries 2018-20. **Senior Political Secretary to PM Anwar 23 Dec 2022 – 25 Nov 2025 (RESIGNED).** GE15 2022: challenged Zahid for Bagan Datuk — LOST by 348 votes. **★ Nov 2025 corruption scandal:** businessman Albert Tei bribery video (via middleman Sofia Rini); arrested by SPRM, remanded 6 days; **Dec 2025: 4 corruption charges** (Sabah mineral license: RM 100k cash Nov 2023, RM 40k cash Jan 2024, furniture/electrical items Feb-Mar 2024). PKR faction: reformist/Anwar wing (ex-VP alongside Rafizi Ramli, ex-Youth chief). | PIR-14 | HIGH | CRITICAL |
| B4 | Wikipedia EN — Malacca State Executive Council | EXCO formed 31 Mar 2023 (⚠ STALE — pre-July-2026) | **★ Mohd Noor Helmy = Deputy (Timbalan) EXCO.** Portfolio: Science, Technology, Innovation, Digital Communications (mirrors full EXCO Fairul Nizam Roslan/Asahan). BN/UMNO, ADUN Duyong (N21). Deputy since 6 Apr 2023. JUNIOR role (one of 10 deputies; not a full EXCO member). ⚠ Page reflects pre-July-2026 BN+PH coalition; PH withdrew 14-16 Jul 2026 (per CJ-MLK-03) — page NOT updated. Akmal's full-EXCO term end = 19 Jan 2026 (resigned); Youth/Sports/NGOs deputy slot VACANT. | PIR-13 | HIGH | CRITICAL |
| B5 | Wikipedia EN — Duyong (state constituency, N21) | MLA since 2021 | **Mohd Noor Helmy ADUN Duyong.** Won 2021 state election 4,684 (38.55%) vs PH/DAP Damian Yeo 4,484 (36.90%) vs PN 2,874 (23.65%) — **majority 200 votes (1.65%)**, MARGINAL. BN gain from PH (DAP). **First UMNO holder** of a former-MCA seat (Gan family held 1995-2013). Seat 61.4% Malay / 33.3% Chinese. Listed as marginal (<45%) in 2021 analysis — one of BN's 5 most marginal seats (cross-ref PIR-27). | PIR-13 | HIGH | HIGH |
| B6 | Wikipedia EN — Bukit Katil (defunct) + Hang Tuah Jaya (successor) | Bukit Katil defunct 2018; Hang Tuah Jaya live | Shamsul was LAST MP of Bukit Katil (2013-18, defeated CM Ali Rustam); FIRST MP of Hang Tuah Jaya (2018-22). Bukit Katil abolished/redelineated → Hang Tuah Jaya 2018. In 2022 Shamsul did NOT defend it (gambled on Bagan Datuk, lost). **Adam Adli Abd Halim (PH/PKR) inherited & held** Hang Tuah Jaya 2022 (39,418 / 41.72%, maj 8,638). Direct succession: Shamsul → Adam Adli (PIR-11). No vacancy for Shamsul to return. | PIR-14 (cross PIR-11) | HIGH | HIGH |
| B7 | Wikipedia EN — Members of Dewan Rakyat, 15th Parliament | term since 19 Dec 2022 | **Malacca 6 federal seats = PH 3 / PN 3 / BN 0.** PN's 3: Masjid Tanah (Mas Ermieyati/BERSATU), Tangga Batu (Bakri/PAS), Jasin (Zulkifli/PAS). **PAS holds 2 of PN's 3 Malacca federal seats.** Shamsul NOT among current 222 MPs (lost Bagan Datuk). BN's federal wipeout in Malacca = structural backdrop (BN power is state-only). ⚠ Page truncated before full Malacca member-detail table. | PIR-12/14/15 | HIGH | HIGH |
| B8 | Wikipedia EN — Malaysian Islamic Party (PAS) | live | PAS = 43/222 MPs (largest single party), 146/611 ADUNs, 1.005M members. Wings: Ulamak, Muslimat, Pemuda, DHPP. Harakah newspaper. **PAS Malacca footprint is SMALL:** 2 federal MPs (Zulkifli, Bakri) + 1 state ADUN (Jailani/Rembia) — peripheral to PAS's core belt (Kelantan/Terengganu/Kedah/Perlis). **State commissioners NOT named** on national page — Zulkifli's "commissioner" title remains unverified. | PIR-12 | HIGH | MEDIUM |
| B9 | Wikipedia EN — 2021 Malacca state election | 20 Nov 2021 | Baseline: BN 21 (two-thirds), PH 5, PN 2. **PAS won 0 state seats (6.96%)**; PKR won 0 (lost all). BN led Tangga Batu (39.62%) & Jasin (45.40%) parliamentary areas in 2021 → PN won both federal seats in 2022 (Green Wave). Duyong explicitly marginal (38.55%). Shamsul contested Paya Rumput (state) 2021 — LOST (36.03%). | PIR-12/13/15 | HIGH | MEDIUM (context) |

---

## 3. PIR Resolution Status

| PIR ID | Status | New Evidence | Confidence |
|--------|--------|--------------|------------|
| **PIR-POI-MLK-12** (Zulkifli Ismail — PAS Grassroots Mobilization) [MEDIUM] | **Partial → Advanced (MP status confirmed); Open (commissioner title & mobilisation specifics)** | **MP status CONFIRMED:** Zulkifli Ismail = Jasin MP (PN/PAS) since 2022, won by 322 votes (0.42%), PN gain from BN. He contested Tangga Batu 2018 under PAS (lost, 12.96%) — PAS loyalist, two attempts before entering parliament. PAS Malacca footprint documented: 2 federal MPs + 1 state ADUN; PAS won 0 state seats in 2021 but 2 federal in 2022 (PN-assisted Green Wave). PAS holds 2 of PN's 3 Malacca federal seats; BERSATU marginalised (PAS cut ties 8-9 Jun 2026). **OPEN:** the "PAS Melaka commissioner" (Yang Dipertua PAS Negeri Melaka) title is NOT corroborated by Wikipedia (ms.wikipedia Zulkifli Ismail = an actor, different person); specific grassroots mobilisation events/strategy not recovered. | HIGH (MP) / OPEN (commissioner) |
| **PIR-POI-MLK-13** (Mohd Noor Helmy — EXCO Portfolio & Succession) [MEDIUM] | **Advanced (role & seat documented); Open (succession trajectory)** | **Role CONFIRMED:** Mohd Noor Helmy = **Deputy (Timbalan) EXCO**, portfolio Science/Tech/Innovation/Digital Communications (mirrors full EXCO Fairul Nizam Roslan). BN/UMNO, ADUN Duyong (N21) since 2021. **Junior** executive role (deputy, not full EXCO; one of 10 deputies). **Seat = MARGINAL:** won 2021 by 200 votes (1.65%); first UMNO holder of former-MCA seat (Gan family held 1995-2013). 61.4% Malay / 33.3% Chinese — three-cornered marginal (BN 38.55% / PH 36.90% / PN 23.65%). ⚠ EXCO page is STALE (pre-July-2026 BN+PH coalition; PH withdrew 14-16 Jul 2026 per CJ-MLK-03). **Succession:** early-stage, constrained by marginal seat — his retention depends on surviving the imminent PRN (≤Nov 2026). | HIGH (role/seat) / OPEN (succession) |
| **PIR-POI-MLK-14** (Shamsul Iskandar — Current Status & Re-election Intentions) [MEDIUM] | **★ SUBSTANTIALLY RESOLVED** | **Current status CONFIRMED via Wikipedia person page:** (1) NOT an MP since 19 Nov 2022 (lost Bagan Datuk to Zahid by 348 votes; old seat Hang Tuah Jaya won by Adam Adli). (2) Resigned as Senior Political Secretary to PM Anwar on **25 Nov 2025**. (3) **4 corruption charges (Dec 2025)** — Sabah mineral-exploration license: RM 100k cash (Nov 2023), RM 40k cash (Jan 2024), furniture/electrical items (Feb-Mar 2024); co-accused businessman Albert Tei; triggered by Tei's bribery video (via middleman Sofia Rini); arrested by SPRM, remanded 6 days. **Re-entry into active politics BLOCKED** while charges active; no comeback signal. **PKR faction:** reformist/Anwar wing (ex-VP alongside Rafizi Ramli, ex-Youth chief); now outside PKR mainstream. PIR-14's "re-entry intentions" question answered: **no current intention/capacity**. | HIGH |
| **PIR-POI-MLK-15** (Bakri Jamaluddin — Affiliation Confirmation & Engagement) [MEDIUM] | **★ Affiliation RESOLVED; Engagement OPEN** | **Affiliation CONFIRMED:** Bakri Jamaluddin = Tangga Batu MP (PN/PAS) since 2022; won GE15 40.65% (majority 8,849 / 9.62%), PN gain from PKR. The PIR registry note ("affiliation unconfirmed — user flagged uncertainty") is CLOSED. Malay-majority seat (71.9%); state seats beneath: 3 BN + 1 PN(BERSATU). **OPEN:** parliamentary engagement (Dewan Rakyat speeches/questions/committees/attendance) and constituency activity in Tangga Batu NOT captured — Dewan Rakyat page truncated before Malacca detail; parlimen.gov.my not attempted. | HIGH (affiliation) / OPEN (engagement) |

---

## 4. VERIFICATION STATUS (PIR-14 & PIR-15)

### PIR-POI-MLK-14 — Shamsul Iskandar @ Yusre Mohd Akin

**VERIFICATION STATUS: ✅ CONFIRMED** (current political status found and documented)

| Verification Target | Status | Evidence |
|---|---|---|
| Current elected office | **CONFIRMED — NONE** | Last MP term ended 19 Nov 2022 (Hang Tuah Jaya). Lost Bagan Datuk 2022 by 348 votes. Not in 15th Parliament (B7). |
| Current government post | **CONFIRMED — RESIGNED** | Senior Political Secretary to PM Anwar, 23 Dec 2022 – **25 Nov 2025 (resigned)** (B3). |
| Re-entry into active politics | **CONFIRMED — BLOCKED** | Active corruption case (4 charges, Dec 2025). No comeback signal. Re-entry implausible while charges active (B3). |
| PKR factional alignment | **CONFIRMED — Reformist/Anwar wing** | Ex-PKR VP (2014-18, alongside Rafizi Ramli); ex-PKR Youth Chief (2007-14); appointed by Anwar as Senior Political Secretary (B3). |

**Conclusion:** Shamsul Iskandar is a former MP (Bukit Katil 2013-18, Hang Tuah Jaya 2018-22) and former Deputy Minister (2018-20) who, since losing Bagan Datuk in GE15 2022, served as Anwar's Senior Political Secretary until resigning on 25 Nov 2025 amid a corruption scandal. He faces four corruption charges (Dec 2025) linked to a Sabah mineral-exploration license. He holds no elected office and no government post. His re-entry into active politics is blocked by the active criminal case. His old seat (Hang Tuah Jaya) is held by Adam Adli (PKR). PKR factional alignment: reformist/Anwar wing, now marginalised.

### PIR-POI-MLK-15 — Bakri Jamaluddin

**VERIFICATION STATUS: ✅ CONFIRMED** (affiliation verified)

| Verification Target | Status | Evidence |
|---|---|---|
| Current political affiliation | **✅ CONFIRMED — PN/PAS** | Bakri Jamaluddin is the current MP for Tangga Batu (P136), party PAS, coalition PN, since 2022 (B2, B7). |
| MP status & election | **CONFIRMED** | Won GE15 2022 with 37,406 (40.65%), majority 8,849 (9.62%), PN gain from PH/PKR (B2). |
| Parliamentary engagement | **UNCONFIRMED — OPEN** | Specific Dewan Rakyat activity (speeches, questions, committees) not recovered. Dewan Rakyat page truncated before Malacca detail (B7). parlimen.gov.my not attempted this cycle. |
| Constituency activity (Tangga Batu) | **UNCONFIRMED — OPEN** | No constituency-program data captured. Seat composition documented: 4 state seats (3 BN + 1 PN/BERSATU) (B2). |

**Conclusion:** The PIR-15 user-flagged uncertainty ("affiliation unconfirmed") is **RESOLVED — Bakri Jamaluddin is PN/PAS**, confirmed via Wikipedia's authoritative electoral data for Tangga Batu. He is a sitting MP (since 2022). His parliamentary engagement and constituency activity remain open gaps for the next cycle (see Suggestions).

---

## 5. Analytical Synthesis

### 5.1 Two of Four PIRs Resolved; Two Advanced (PIR-12/13/14/15)

This cycle closes two verification gates and advances the other two:
- **PIR-14 (Shamsul) — RESOLVED.** The Wikipedia person page is a complete current-status dossier: no elected office, resigned from government, four corruption charges. The "re-entry intentions" question is definitively answered (no current capacity). This is the highest-value resolution of the cycle.
- **PIR-15 (Bakri) — Affiliation RESOLVED; engagement open.** The user-flagged "uncertain affiliation" is closed: PN/PAS confirmed. The parliamentary-engagement half remains open (Dewan Rakyat page truncation; parlimen.gov.my not attempted).
- **PIR-12 (Zulkifli) — MP status confirmed; commissioner title open.** Zulkifli's Jasin MP/PN-PAS status is confirmed (322-vote marginal win), but the "PAS Melaka commissioner" title attributed to him in the PIR registry is NOT corroborated by Wikipedia — this is the largest remaining open item.
- **PIR-13 (Mohd Noor Helmy) — role & seat documented; succession open.** His Deputy-EXCO (Science/Tech/Digital) role and marginal Duyong seat are confirmed; his UMNO-succession trajectory is early-stage and constrained by the marginal seat.

### 5.2 Tangga Batu — The Cross-POI Battleground (PIR-12/14/15 nexus)

A striking structural finding: **Tangga Batu (P136) is the seat where three of the four CJ-MLK-04 POIs' electoral histories intersect.** Shamsul Iskandar (PKR) contested it in 2004 and lost (20.64%); Zulkifli Ismail (PAS) contested it in 2018 and lost (12.96%); Bakri Jamaluddin (PN/PAS) won it in 2022 (40.65%). Tangga Batu functions as a "stepping-stone" seat: two POIs used failed Tangga Batu bids as precursors to winning seats elsewhere (Shamsul → Bukit Katil 2013; Zulkifli → Jasin 2022), while the third (Bakri) ultimately captured it. The seat's history (Idris Haron/BN 2004-13 → Abu Bakar/BN 2013-18 → Rusnah/PKR 2018-22 → Bakri/PAS 2022-present) shows it has oscillated across all three coalitions — a true three-way bellwether. With the PRN ≤3 months away, Tangga Batu is a PN-defence seat (9.62% margin) in a Malay-majority (71.9%) electorate where the informal BN-PAS dynamic will determine whether Bakri holds or BN reclaims it.

### 5.3 PAS's Malacca Footprint: PN-Assisted Growth, Not Organisational Mass (PIR-12)

PAS's Malacca presence is small but disproportionately PN-defining. PAS holds **2 of PN's 3 Malacca federal seats** (Zulkifli/Jasin, Bakri/Tangga Batu) and 1 of PN's 3 state seats (Jailani/Rembia) — yet PAS won **0 state seats in 2021** (6.96% vote). The jump from 0 state seats (2021) to 2 federal seats (2022) is the local "Green Wave" — achieved through the PN umbrella and the national PAS surge, not through standalone PAS organisational mass in Malacca. PAS's core belt remains Kelantan/Terengganu/Kedah/Perlis; Malacca is peripheral. This frames PIR-12's mobilisation question: Zulkifli's role (if he is indeed commissioner) operates within a PN-assisted growth model, where the informal BN-PAS (Muafakat) dynamic (cross-ref CJ-MLK-03) and the PAS-BERSATU break (8-9 Jun 2026) shape the ground more than PAS's own 1M+ membership machinery. The PAS Melaka commissioner title remains the key unverified premise.

### 5.4 Mohd Noor Helmy — Marginal-Seat Deputy in a Reshuffled EXCO (PIR-13)

Mohd Noor Helmy is a **first-term, marginal-seat Deputy EXCO** — the most junior tier of the state executive. His portfolio (Science/Tech/Digital Communications) mirrors full-EXCO Fairul Nizam Roslan; deputies do not chair committees independently. His defining constraint is electorla: Duyong (N21) was won by 200 votes (1.65%) in 2021, making it one of BN's 5 most marginal seats (cross-ref PIR-27). He is also the **first UMNO holder of a former-MCA seat** (the Gan family/MCA held 1995-2013) — a Malay-seat consolidation within BN that may carry MCA-UMNO seat-allocation friction into the PRN. His UMNO-succession positioning is therefore early-stage and structurally fragile: he is a rising junior, but his retention of office depends on surviving a three-cornered marginal contest (BN 38.55% / PH 36.90% / PN 23.65%) in the imminent election. ⚠ The EXCO page is stale (pre-July-2026 BN+PH coalition; PH withdrew 14-16 Jul 2026) — the current post-withdrawal EXCO composition is not captured, though Helmy's own BN/UMNO deputy position is unaffected.

### 5.5 Shamsul Iskandar — From Reformist Rising Star to Corruption-Case Defendant (PIR-14)

Shamsul's trajectory is a sharp rise-and-fall arc now terminally interrupted. A PKR reformist core figure (Youth Chief 2007-14 succeeding Ezam, VP 2014-18 alongside Rafizi Ramli and Nurul Izzah), he achieved a signature win in 2013 by defeating then-CM Mohd Ali Rustam in Bukit Katil. He rose to Deputy Minister (2018-20) and then to Senior Political Secretary to PM Anwar (2022-25). The 2022 Bagan Datuk gamble (challenging Zahid, losing by 348 votes) cost him his parliamentary seat; the November 2025 corruption scandal (Albert Tei bribery video) cost him his government post; the December 2025 four charges now cost him his political viability. His reformist factional space is being contested by Rafizi Ramli's BERSAMA (targeting the Melaka PRN) and by Adam Adli (who inherited Shamsul's Hang Tuah Jaya seat and leads PKR Melaka). PIR-14 is resolved on current status; the ongoing variable is the corruption-case outcome (a conviction ends his career; an acquittal could theoretically reopen a reformist comeback in a weakened PKR Melaka).

### 5.6 Cross-Cycle Corroboration & the Data-Source Constraint

This cycle corroborates and is corroborated by the sibling cycles. The Malacca federal split (PH 3 / PN 3 / BN 0) and the PAS dominance of PN's Malacca federal footprint (B7) align with CJ-MLK-03's coalition analysis. Akmal's EXCO resignation (19 Jan 2026, B4) aligns with CJ-MLK-01. The PAS-BERSATU break (8-9 Jun 2026) and the PH state-government withdrawal (14-16 Jul 2026) are consumed from CJ-MLK-03. **The persistent data-source constraint** — the web_search backend's structural inability to retrieve Malaysian political content (confirmed across all four cycles) — means Wikipedia constituency/person pages remain the workhorse, but they cannot reach Malay-language grassroots sources (harakahdaily, Sinar Harian, PAS official sites) needed to confirm Zulkifli's commissioner title or Bakri's parliamentary engagement. These remain the top-priority gaps for the next cycle (see Suggestions).

---

## 6. TOP 3 PIR SUGGESTIONS FOR NEXT CYCLE (AUTO-APPROVED)

*(Full text in `07-AUDIT/top3-mlk-suggestions-CJMLK04.md`)*

1. **Verify Zulkifli Ismail's "PAS Melaka Commissioner" title & PAS Melaka grassroots structure** (PIR-12) — the largest open item; requires Malay-language source extraction (harakahdaily, PAS Melaka, Sinar Harian).
2. **Bakri Jamaluddin's parliamentary engagement & Tangga Batu constituency programs** (PIR-15) — affiliation confirmed, engagement open; requires parlimen.gov.my + Malay news extraction.
3. **Track the Shamsul Iskandar corruption case progression & PKR factional fallout** (PIR-14) — case is the decisive variable; track trial status/verdict and PKR/Anwar statements on his status.

---

## 7. Appendix — Raw Scrapes Inventory

| File | PIR | Source |
|---|---|---|
| PIR12-wikipedia-jasin-federal-constituency-zulkifli.md | PIR-12 | Wikipedia EN — Jasin (federal constituency) |
| PIR15-wikipedia-tangga-batu-federal-constituency-bakri.md | PIR-15 | Wikipedia EN — Tangga Batu (federal constituency) |
| PIR14-wikipedia-shamsul-iskandar-person-profile-keystone.md | PIR-14 | Wikipedia EN — Shamsul Iskandar Mohd Akin (KEYSTONE) |
| PIR13-wikipedia-malacca-state-executive-council.md | PIR-13 | Wikipedia EN — Malacca State Executive Council |
| PIR13-wikipedia-duyong-state-constituency-helmy.md | PIR-13 | Wikipedia EN — Duyong (state constituency) |
| PIR14-wikipedia-bukit-katil-hang-tuah-jaya-shamsul-seats.md | PIR-14 | Wikipedia EN — Bukit Katil + Hang Tuah Jaya |
| PIR12-14-15-wikipedia-dewan-rakyat-15th-parliament-mp-verification.md | PIR-12/14/15 | Wikipedia EN — Members of Dewan Rakyat, 15th Parliament |
| PIR12-wikipedia-pas-malaysian-islamic-party.md | PIR-12 | Wikipedia EN — Malaysian Islamic Party (PAS) |
| PIR12-13-15-wikipedia-2021-malacca-state-election-context.md | PIR-12/13/15 | Wikipedia EN — 2021 Malacca state election |

All scrapes in `04-DATA-AND-SOURCES/raw-scrapes/20260805/`. Scratch metadata: `04-DATA-AND-SOURCES/scratch/cj-mlk-04-cycle-20260805-0054-metadata.json`.

---

*End of CJ-MLK-04 report.*
