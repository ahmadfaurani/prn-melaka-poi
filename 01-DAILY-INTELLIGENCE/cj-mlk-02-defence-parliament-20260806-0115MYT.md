# CJ-MLK-02 — Defence, Parliament & Federal Portfolios Collection Report

**Workstream:** PRN Melaka — Person of Interest (POI) Intelligence
**Cronjob:** CJ-MLK-02 (Defence, Parliament & Federal Portfolios)
**POIs of Interest:** Adly Zahari (Timbalan Menteri Pertahanan) · Mas Ermieyati Samsudin (Pengerusi PAC) · Adam Adli (AP Hang Tuah Jaya)
**PIRs Addressed:** PIR-POI-MLK-03 (CRITICAL) · PIR-POI-MLK-04 (CRITICAL) · PIR-POI-MLK-11 (HIGH)
**Collection Timestamp:** 2026-08-06 01:15 MYT (UTC+8)
**Cycle:** Third collection cycle (consumed 3/3 auto-approved suggestions from cycle 2's `07-AUDIT/top3-mlk-suggestions-CJMLK02.md`)
**Classification:** TLP:AMBER
**Collector:** CJ-MLK-02 Collection Agent (zai-org/GLM-5.2)

---

## 1. Collection Summary

This is the **third CJ-MLK-02 cycle**. The headline result: **PIR-03's Melaka-base agency gap is now FULLY RESOLVED.** Cycle 2 had proven the *structural* Melaka defence nexus (3rd Div + 10 Para Bde HQ) but flagged the absence of evidence that Adly personally engaged the Malacca-based formations. This cycle recovered the missing evidence directly from MINDEF's own website: on **8 April 2026**, Adly Zahari personally officiated the launch of the **Ikhtiar Autisme Angkatan Tentera Malaysia (IA-ATM)** programme at **PPDK Umi, Kem Terendak, Melaka** — his second site visit after Pangkalan TLDM Lumut (L1 mod.gov.my + L4 Utusan). The Melaka-base agency gap is closed.

This cycle also surfaced Adly's **full-spectrum 2026 defence agency**: (a) a National Defence Policy lecture at Maktab Ketahanan Nasional (17 Mar 2026); (b) DSA/NATSEC 2026 attendance with tri-service leadership and a bilateral meeting with Azerbaijan's Deputy Defence Industry Minister (19-23 Apr 2026); (c) MINDEF's signing of **RM3.54 billion** in 24 contracts/ICPs at DSA2026 (22 Apr 2026), with a 2-3 month procurement freeze earlier in 2026. Combined with cycle 2's capability-gaps statement and PERHEBAT plan, Adly is now documented across the policy-articulation, industry-implementation, procurement-diplomacy, and Melaka-base-engagement dimensions.

For PIR-11, Adam Adli's **concrete 2026 higher-education policy output** was captured: on **17 June 2026**, he announced three PTPTN reforms (targeted repayment by ability, income-contingent repayment, travel restrictions now income-based at RM6,000+ threshold instead of blanket) — directly answering the Dec 2025 Puad Zarkashi/netizen challenge to abolish PTPTN. This addresses the cycle-2 gap of "concrete higher-ed policy outputs beyond the AUKU memorandum reception."

For PIR-04, the PAC publications page (L1) was re-confirmed with all 6 reports and their official PDF URLs. However, the substantive content of the 5 non-LCS reports could **not** be extracted this cycle — a genuine technical blocker (PDFs exceed the extract tool's size limit, and parlimen.gov.my is unreachable via curl from this environment, HTTP 000). This sub-task carries to the next cycle.

**Auto-approved suggestions consumed (3/3):**
1. ⚠️ **PAC non-LCS report PDFs** — PARTIAL: 6 reports + PDF URLs re-confirmed (L1); 5 PDF contents BLOCKED (size limit + HTTP 000). URL pattern now confirmed for retry.
2. ✅ **Adly Melaka-base engagement + LCS response** — RESOLVED (Melaka-base gap): Adly at Kem Terendak Melaka (8 Apr 2026, L1+L4) + DSA2026 RM3.54B + Azerbaijan bilateral + National Defence Policy talk. Adly's *response to the PAC LCS directive* NOT surfaced (search token collision on "PAC"/"LCS").
3. ✅ **Adam Adli Hansard + higher-ed outputs + promotion signal** — PROGRESS: concrete PTPTN reform output captured (17 Jun 2026) + cabinet-reshuffle succession confirmed + MPP PKR membership. Hansard contributions NOT obtained (search blocked on "Adam" token). Explicit ministerial-promotion signal NOT found (but 6-deputy-promotion reshuffle pattern documented as structural context).

**10 new raw scrapes** saved; **12 new CVS claims (CVS-MLK-168 to 179)** logged (5 T1, 7 T2). CVS register now totals **179 claims**.

Raw scrapes saved to `04-DATA-AND-SOURCES/raw-scrapes/20260806/`. Scratch metadata at `04-DATA-AND-SOURCES/scratch/cj-mlk-02-cycle-20260806-0115-metadata.json`. CVS register updated (+12 claims).

---

## 2. Findings Table

| # | Source | Date | Summary | PIR | Tier | Confidence | Tag |
|---|--------|------|---------|-----|------|------------|-----|
| A1 | **mod.gov.my — MINDEF Official** | 8 Apr 2026 | **KEYSTONE: MELAKA-BASE AGENCY RESOLVED.** Adly Zahari personally officiated IA-ATM launch at **PPDK Umi, Kem Terendak, Melaka** — his 2nd site visit after Pangkalan TLDM Lumut. Welfare programme for autistic children (3-15 yrs) of defence personnel. Partners: JKM, NASOM, Lembaga Tabung Haji funding. Resolves cycle-2 gap. | PIR-03 | T1 | 10 | CRITICAL |
| A2 | **Utusan Malaysia** | 7 Apr 2026 | IA-ATM financial/programme detail: **RM528,000** total (RM2,200/participant), **12 Nasom modules**, **10 children per PPDK**. Senior military present: Panglima Armada Barat, Komander Pangkalan Lumut. Corroborates A1. | PIR-03 | T1 | 9 | CRITICAL |
| A3 | **BERNAMA** | 19 Apr 2026 | **DSA-NATSEC 2026 record turnout.** Adly attended with Minister Khaled Nordin + tri-service chiefs. 1,456 exhibitors/63 countries, 368 Malaysian companies, DIPN 30% local-component target, ICP documents RM1.4B. Strait of Malacca freedom-of-navigation referenced. | PIR-03 | T1 | 9 | HIGH |
| A4 | **BernamaBiz** | 22 Apr 2026 | **MINDEF signed RM3.54B** in 24 contracts/ICPs at DSA2026 (12 contracts + 4 LOIs RM1.01B + 8 ICPs RM1.40B). Adly + Khaled Nordin + **KSU Datuk Lokman Hakim Ali** (PAC LCS witness) present. Procurement frozen 2-3 months early 2026. | PIR-03 | T1 | 9 | CRITICAL |
| A5 | **Adly Zahari Official FB** | ~21 Apr 2026 | Adly held **bilateral defence meeting** with Azerbaijan Deputy Defence Industry Minister Mehman Bakhishov at DSA2026 — defence science/tech/industry cooperation. (L5 snippet; attendance L2-corroborated.) | PIR-03 | T2 | 5 | MEDIUM |
| A6 | **MINDEF Official FB** | 17 Mar 2026 | Adly delivered **"Eminent Speaker" talk**: "Malaysia's National Defence Policy: The Foundation of Its National Power in a Competitive Age" at Kursus Ketahanan Negara 7/2026, Maktab Ketahanan Nasional. (L5 snippet.) | PIR-03 | T2 | 6 | MEDIUM |
| B1 | **parlimen.gov.my — PAC Publications** | accessed 6 Aug 2026 | **L1 RE-CONFIRMS** 6 PAC 2026 reports + official PDF URLs (docs-NNN-NNN.pdf). DR.27/23/22/20/12/9. PDF contents BLOCKED this cycle (size limit + HTTP 000). | PIR-04 | T1 | 10 | HIGH |
| C1 | **MalaysiaPost** | 17 Jun 2026 | **Adam Adli concrete 2026 PTPTN policy:** 3 reforms — (1) targeted repayment by ability, (2) income-contingent repayment, (3) travel restrictions now income-based (**RM6,000+ threshold**) not blanket. Denies U-turn. Confirmed **MPP PKR**. | PIR-11 | T2 | 7 | HIGH |
| C2 | **The Rakyat Insight + MalaysiaGazette + mediatelus** | 16-17 Dec 2025 | **Puad Zarkashi (UMNO MKT) challenges** Adam Adli to abolish PTPTN; netizens echo. Confirms Adam Adli **replaced Datuk Mustapha Sakmud**. Activist-to-officeholder tension. 3 corroborating outlets. | PIR-11 | T2 | 8 | HIGH |
| C3 | **Harian Metro / BERNAMA** | 16 Dec 2025 | **Cabinet reshuffle detail:** 6 deputies → full ministers incl **Mustafa Sakmud** (Tim. Pendidikan Tinggi → Menteri JPM Sabah/Sarawak). Adam Adli filled vacated deputy slot (from Youth & Sports). 6-deputy-promotion pattern = ministerial-prospect structural context. | PIR-11 | T1 | 9 | HIGH |

---

## 3. PIR Resolution Status

| PIR ID | Status | New Evidence | Confidence |
|--------|--------|--------------|------------|
| **PIR-POI-MLK-03** (Adly Zahari — Defence Portfolio & Melaka Nexus) [CRITICAL] | **FULLY RESOLVED (Melaka-base gap closed + full-spectrum agency)** | **Melaka-base agency RESOLVED:** Adly personally officiated IA-ATM at PPDK Umi Kem Terendak Melaka (8 Apr 2026, L1 mod.gov.my + L4 Utusan) — first documented personal engagement at a Malacca military base. **Defence-industry agency NEW:** DSA/NATSEC 2026 attendance (19-23 Apr) with tri-service chiefs, DIPN 30% local-component, RM1.4B ICP; **RM3.54B in 24 contracts/ICPs signed** (22 Apr, L2 Bernamabiz) with KSU Lokman Hakim (PAC LCS witness) present; procurement frozen 2-3 months early 2026. **Defence diplomacy NEW:** bilateral with Azerbaijan Deputy Defence Industry Minister. **Policy thought-leadership NEW:** National Defence Policy lecture (17 Mar, Maktab Ketahanan Nasional). Carries from cycle 2: capability-gaps statement (Oct 2025), PERHEBAT plan (Feb 2026), tri-service aides, structural Melaka nexus. **Remaining sub-gap:** Adly's public response to PAC LCS directive (DR.22/2026) — not surfaced (search token collision). | **HIGH (all core dimensions answered)** |
| **PIR-POI-MLK-04** (Mas Ermieyati — PAC Scrutiny Targets) [CRITICAL] | **Substantially Resolved (agenda confirmed; PDF deepening blocked)** | **PAC 2026 agenda RE-CONFIRMED (L1):** 6 reports tabled under Mas Ermieyati with official PDF URLs (DR.27/23/22/20/12/9). Carries from cycle 2: full LCS report detail (DR.22/2026), BERSATU suspension verified, PAC chair confirmed despite suspension, cooking-oil border visit. **Blocker this cycle:** 5 non-LCS PDF contents could not be extracted (size limit + HTTP 000) — substantive findings of cooking-oil/vehicles/airports/health-insurance/FELCRA reports remain at headline level. PDF URLs now confirmed for retry. | **HIGH (agenda); MEDIUM (substantive findings pending)** |
| **PIR-POI-MLK-11** (Adam Adli — Parliamentary Trajectory & Ministerial Prospects) [HIGH] | **Substantially Resolved (concrete policy output + succession confirmed)** | **Concrete 2026 higher-ed policy output NEW:** PTPTN reform (17 Jun 2026, MalaysiaPost) — targeted repayment, income-contingent, RM6,000+ travel-restriction threshold; denies U-turn. Directly answers Dec 2025 Puad/netizen challenge. **Cabinet succession CONFIRMED:** Adam Adli replaced Mustafa Sakmud (promoted to Menteri JPM Sabah/Sarawak); 6-deputy-promotion pattern documented. **Party leadership NEW:** MPP PKR confirmed. Carries from cycle 2: L1 parliament profile, AUKU policy posture, UMANY demand, trajectory. **Remaining gaps:** specific 2026 Dewan Rakyat Hansard contributions (search blocked on "Adam" token); explicit ministerial-promotion signal not found (structural pattern documented, not direct signal). | **HIGH (policy + succession) / OPEN (Hansard + direct promotion signal)** |

---

## 4. Analytical Synthesis

### 4.1 PIR-03 Fully Resolved: Adly Zahari's Full-Spectrum 2026 Defence Agency

Cycle 1 established the *structural* Melaka defence nexus (3rd Div + 10 Para Bde HQ; MINDEF budget RM21.746B; DIPKN; tri-service aides). Cycle 2 captured Adly's *agentic* 2026 MINDEF initiatives (capability-gaps statement, PERHEBAT plan) and the *cross-POI* PAC↔MINDEF LCS scrutiny. This cycle closes the **last open dimension** — the *Melaka-base agency* — and adds three new agency dimensions:

1. **Melaka-base engagement (8 Apr 2026, L1):** Adly personally officiated the IA-ATM launch at **Kem Terendak, Melaka** — a Malacca military installation. The programme (RM528,000, Tabung Haji-funded, 12 Nasom modules, 10 autistic children of defence personnel per PPDK) is a welfare initiative, but the *venue* is the intelligence-relevant fact: Adly visited a Malacca military base in his deputy-minister capacity, with senior military present (Panglima Armada Barat). This is the Melaka-nexus agency signal PIR-03 required.

2. **Defence-industry procurement (DSA2026, 19-23 Apr, L2):** Adly attended DSA/NATSEC 2026 alongside Minister Khaled Nordin and the full tri-service leadership (Armed Forces Chief + TLDM Chief + TUDM Chief). MINDEF signed **RM3.54 billion** in 24 contracts/ICPs (12 contracts + 4 LOIs RM1.01B + 8 ICPs RM1.40B). The DIPN 30% local-component target (368 Malaysian companies) connects to Adly's Oct 2025 DIPKN-implementation statement. Critically, **KSU Datuk Lokman Hakim Ali** — named as a witness in the PAC LCS report (DR.22/2026) — was present at the RM3.54B signing. This is a direct institutional link between the PAC-scrutinised MINDEF leadership and the new procurement.

3. **Procurement freeze signal:** Khaled Nordin disclosed MINDEF **froze all procurement processes for 2-3 months early in 2026** due to "unavoidable circumstances." While the cause is unspecified, the timing (early 2026, before the PAC's 8 Jul 2026 LCS report tabling) raises a plausible link to the fiscal-discipline pressure the PAC was applying. This is a **T2 inference, not a verified causal link** — but it is a signal worth monitoring: MINDEF procurement discipline may be responsive to PAC scrutiny even before the formal report is tabled.

4. **Defence diplomacy + policy thought-leadership:** Adly held a bilateral meeting with Azerbaijan's Deputy Defence Industry Minister (defence science/tech/industry cooperation) and delivered a National Defence Policy lecture at Maktab Ketahanan Nasional (17 Mar 2026). These extend Adly's agency from domestic operations to international diplomacy and strategic-conceptual articulation.

**Assessment [T3]:** Adly Zahari's 2026 defence agency is now documented across all four dimensions — policy articulation (Maktab Ketahanan lecture), industry implementation (DSA2026/DIPKN), procurement diplomacy (RM3.54B + Azerbaijan bilateral), and Melaka-base engagement (Kem Terendak). PIR-03's core question is **fully answered**: Adly is driving capability modernisation, veterans' transformation, defence-industry localisation, and procurement diplomacy, with a documented personal link to the Melaka military base. The one remaining sub-gap (Adly's public response to the PAC LCS directive) is a monitoring item, not a core PIR-03 requirement.

### 4.2 The MINDEF Procurement Freeze ↔ PAC Scrutiny Nexus [ASSESSMENT — T3/T4]

The 2-3 month early-2026 MINDEF procurement freeze (Bernamabiz, 22 Apr 2026) and the PAC's 8 Jul 2026 LCS report (DR.22/2026, "no additional funds, cost under RM11.22B") are temporally adjacent. The PAC's proceeding on the LCS was 4 Feb 2026; the freeze was early 2026. [ASSESSMENT] It is plausible — but not verified — that the procurement freeze was partly a MINDEF response to the fiscal-discipline signal the PAC was preparing. The presence of KSU Lokman Hakim at both the PAC LCS proceeding (as witness) and the DSA2026 RM3.54B signing connects the two events institutionally. This is a **monitoring hypothesis (T4 projection)**, not a verified fact. The next cycle should seek the explicit cause of the "unavoidable circumstances" freeze.

### 4.3 Adam Adli's PTPTN Reform: From Abolition Demand to Targeted Reform (PIR-11)

Adam Adli's 17 June 2026 PTPTN announcement is a **concrete policy-output signal** that resolves the cycle-2 gap. Three reforms: (1) targeted repayment based on borrower ability, (2) income-contingent repayment element, (3) travel restrictions now income-assessed (RM6,000+ threshold) rather than blanket. Adam Adli explicitly denies a "U-turn" — framing this as *consistent* with his principles, *delivered* from within office.

This is the politically significant resolution of the Dec 2025 tension: Puad Zarkashi (UMNO MKT) and netizens challenged Adam Adli to *abolish* PTPTN (citing his Dataran Merdeka tent-protest activist past). Adam Adli's answer is *reform, not abolition* — a targeted, means-tested, compassionate approach that maintains fund sustainability. [ASSESSMENT — T3] This is the classic activist-to-officeholder transition: the radical demand (abolish) becomes the institutional reform (targeted repayment). It preserves Adam Adli's reformist credentials while demonstrating governability — a dual signal valuable for both his constituency and his ministerial-prospect trajectory.

The cabinet-reshuffle pattern (6 deputies → full ministers, Dec 2025) provides the **structural context** for Adam Adli's ministerial prospects: the same reshuffle that promoted his predecessor (Sakmud) to full minister created Adam Adli's current deputy slot. If the pattern repeats, Adam Adli is a candidate for full-minister promotion. His MPP PKR membership (central leadership council) is a parallel party-advancement signal. No *explicit* promotion signal surfaced this cycle, but the structural conditions are documented.

### 4.4 PIR-04: The PAC Deepening Blocker (Honest Reporting)

The PAC publications page (L1) was re-confirmed with all 6 reports and their official PDF URLs. However, the substantive content of the 5 non-LCS reports (cooking oil, govt vehicles, airports, health insurance, FELCRA) could not be extracted this cycle. Two independent blockers: (1) the web_extract tool returned "File exceeds size limit" for all 5 PDFs; (2) direct curl download from parlimen.gov.my returned HTTP 000 (server unreachable from this environment). The PDF URL pattern (docs-NNN-NNN.pdf) is now confirmed for retry via a different network or extractor in a future cycle. PIR-04's *agenda* is fully answered (L1); the *substantive findings* of 5 of 6 reports remain at headline level. The LCS report (DR.22/2026) was fully extracted in cycle 2.

---

## 5. Collection Limitations & Honest Reporting

- **PAC PDF extraction — genuine technical blocker:** All 5 non-LCS report PDFs (DR.27/23/20/12/9) failed extraction. web_extract returned "File exceeds size limit"; curl returned HTTP 000 (parlimen.gov.my unreachable). This is a real environment limitation, not a search failure. The PDF URLs are confirmed and will be retried. No fabricated content was introduced to compensate.
- **Search token collisions persist:** English-language search terms continue to collide: "Adam" → Biblical Adam / YouTube channels / AI CAD copilot; "PAC" → Political Action Committee / Pacman / PAC-Audio; "LCS" → League Championship Series (LoL). These dominated several query batches. **Malay institutional tokens and quoted POI names remain the productive strategy** — the Adly/Melaka breakthroughs this cycle all came from Malay-token queries (`Adly Zahari Pertahanan Melaka TLDM Pangkalan Tentera 2026`; `rombakan kabinet 2026 PKR`). The PTPTN results came from `Adam Adli Hang Tuah Jaya 2026 dasar`.
- **Facebook full extraction blocked:** Adly's DSA2026 posts (Azerbaijan bilateral) and MINDEF's National Defence Policy talk post returned extraction errors (Facebook antibot). Key facts were obtained from official-page search snippets (L5) and, where possible, corroborated by L2 BERNAMA (DSA2026 attendance) — but the bilateral-meeting detail (A5) and the lecture title (A6) remain single-L5-source and flagged accordingly.
- **Adly's PAC LCS response — not surfaced:** Multiple search attempts to find Adly's public response to the PAC's RM11.22B LCS directive failed (token collision). This sub-gap carries to the next cycle. It is a monitoring item, not a core PIR-03 requirement.
- **Adam Adli Hansard — not obtained:** The Parliament Hansard search was not reachable (token collision on "Adam"; parlimen.gov.my Hansard search not directly accessible). This PIR-11 sub-gap carries forward.
- **All high-impact claims are L1- or L2-sourced:** The Melaka-base keystone (A1) is L1 mod.gov.my corroborated by L4 Utusan. The RM3.54B procurement (A4) is L2 Bernamabiz. The cabinet reshuffle (C3) is L2 BERNAMA via Harian Metro. The PTPTN reform (C1) is L4 single-source (flagged T2, action: corroborate via Hansard/MOHE). No fabricated content. CVS Rule 6 compliance: AI-assigned tiers capped at T2 except where L1/L2 official sources provide direct corroboration (then T1). 5 of 12 new claims are T1 (L1/L2-sourced); 7 are T2.

---

## 6. Files Produced This Cycle

| Path | Type |
|------|------|
| `04-DATA-AND-SOURCES/raw-scrapes/20260806/PIR03-mod-gov-my-adly-kem-terendak-ia-atm-melaka-20260408-KEYSTONE.md` | Raw scrape (A1) — keystone: Melaka-base agency resolved |
| `04-DATA-AND-SOURCES/raw-scrapes/20260806/PIR03-utusan-adly-ikhtiar-autisme-melaka-20260407.md` | Raw scrape (A2) — IA-ATM financial/programme detail |
| `04-DATA-AND-SOURCES/raw-scrapes/20260806/PIR03-bernama-dsa-natsec-2026-adly-20260419.md` | Raw scrape (A3) — DSA2026 record turnout |
| `04-DATA-AND-SOURCES/raw-scrapes/20260806/PIR03-bernamabiz-mindef-rm3.54b-contracts-dsa2026-20260422.md` | Raw scrape (A4) — RM3.54B contracts |
| `04-DATA-AND-SOURCES/raw-scrapes/20260806/PIR03-adly-dsa2026-azerbaijan-bilateral-facebook-snippet.md` | Raw scrape (A5) — Azerbaijan bilateral (L5) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260806/PIR03-adly-national-defence-policy-talk-maktab-ketahanan-20260317.md` | Raw scrape (A6) — National Defence Policy lecture (L5) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260806/PIR04-pac-publications-2026-reports-confirmed-pdf-urls.md` | Raw scrape (B1) — PAC 6 reports + PDF URLs confirmed |
| `04-DATA-AND-SOURCES/raw-scrapes/20260806/PIR11-malaysiapost-adam-adli-ptptn-reform-20260617.md` | Raw scrape (C1) — Adam Adli PTPTN reform |
| `04-DATA-AND-SOURCES/raw-scrapes/20260806/PIR11-puad-netizen-adam-adli-ptptn-challenge-20251216.md` | Raw scrape (C2) — Puad/netizen PTPTN challenge |
| `04-DATA-AND-SOURCES/raw-scrapes/20260806/PIR11-hmetro-cabinet-reshuffle-dec2025-sakmud-promoted.md` | Raw scrape (C3) — cabinet reshuffle detail |
| `04-DATA-AND-SOURCES/scratch/cj-mlk-02-cycle-20260806-0115-metadata.json` | Scratch metadata |
| `04-DATA-AND-SOURCES/scratch/append-cvs-cjmlk02-cycle3.py` | CVS append script |
| `03-VERIFICATION/CVS-EVIDENCE-REGISTER.csv` | +12 claims (CVS-MLK-168 to 179); total 179 |
| `07-AUDIT/top3-mlk-suggestions-CJMLK02.md` | Auto-approved suggestions (overwritten for cycle 4) |
| `01-DAILY-INTELLIGENCE/cj-mlk-02-defence-parliament-20260806-0115MYT.md` | This report |

---

## 7. PIR Status Roll-Up (Cumulative Across 3 Cycles)

| PIR | Cycle 1 (00:27) | Cycle 2 (12:59) | Cycle 3 (01:15) | Overall |
|-----|-----------------|------------------|------------------|---------|
| PIR-03 (Adly — Defence & Melaka) | Structural nexus + fiscal frame | Agentic initiatives + cross-POI PAC scrutiny | **Melaka-base gap CLOSED** + RM3.54B procurement + defence diplomacy | **FULLY RESOLVED** |
| PIR-04 (Mas Ermieyati — PAC) | Chair status + agenda headline | Full LCS detail + suspension verified + cooking-oil visit | Agenda re-confirmed; PDF deepening blocked | **Substantially Resolved (agenda HIGH; findings MEDIUM)** |
| PIR-11 (Adam Adli — Parliament) | Status + trajectory | AUKU policy posture + succession | **Concrete PTPTN output** + reshuffle pattern + MPP PKR | **Substantially Resolved (Hansard + direct signal OPEN)** |

---

## TOP 3 PIR SUGGESTIONS FOR NEXT CYCLE (AUTO-APPROVED)

> These 3 suggestions have been written to `07-AUDIT/top3-mlk-suggestions-CJMLK02.md` for auto-incorporation into the next CJ-MLK-02 cycle.

### Suggestion 1: Retry PAC Non-LCS Report PDF Extraction via Alternate Route + Seek Adly's Public Response to the PAC LCS Directive
**Text:** The 5 non-LCS PAC report PDFs (DR.27/23/20/12/9) remain unextracted — the confirmed URLs (docs-323-400.pdf through docs-314-385.pdf) failed both web_extract (size limit) and curl (HTTP 000). The next cycle should: (a) retry extraction via alternate methods — a smaller-chunk PDF text extraction, a headless-browser fetch, or a different network path; (b) if extraction remains blocked, search for *news coverage* of each report's findings (NST/Bharian/Astro Awani typically report PAC report tablings) to obtain the substantive findings at L4 level; (c) the cooking-oil report (DR.27/2026, most recent, 16 Jul) is highest priority as it connects to the documented border working visit. Separately, Adly's public response to the PAC's RM11.22B LCS "no additional funds" directive (DR.22/2026) was not found this cycle due to search token collision — the next cycle should target this via Malay-specific queries (`Adly Zahari respons syor PAC LCS mindef 2026` / `Adly Zahari kapal peronda PAC bajet 2026`) and MINDEF news.
**Rationale:** PIR-04's substantive findings layer (agenda → findings) remains the open dimension. The PDF URL pattern is now confirmed (no guessing needed). The LCS-response angle is a fresh cross-POI monitoring item created by the cycle-2 keystone.
**Search Queries / Extractions:**
1. Retry: `web_extract` each PDF; or `curl -r 0-1000000` (range-limited) + `pdftotext`
2. `PAC DR.27 2026 minyak masak KPDN dapatan` / `PAC DR.23 2026 kenderaan kerajaan MOF` (news-coverage fallback)
3. `Adly Zahari respons syor PAC LCS mindef 2026` / `Adly Zahari kapal peronda PAC bajet 2026`
4. Direct extract: `https://www.mod.gov.my` news + `https://www.nst.com.my` for PAC LCS response

### Suggestion 2: Adam Adli's 2026 Dewan Rakyat Hansard Contributions + AUKU Memorandum Follow-Through + Direct Ministerial-Promotion Signal
**Text:** Adam Adli's concrete PTPTN reform output (17 Jun 2026) is captured, but PIR-11 still lacks his *specific 2026 parliamentary performance* (Dewan Rakyat questions answered, speeches) and the *follow-through on the AUKU memorandum* he received on 9 Feb 2026. The next cycle should: (a) extract the Parliament Hansard for Adam Adli's 2026 contributions — try the parlimen.gov.my oral-questions/Hansard search via direct URL navigation (the MP profile id=4176 may link to contributions) or search via `soalan jawab lisan parlimen 2026 pengajian tinggi timbalan menteri`; (b) seek any formal MOHE response to the AUKU abolition memorandum (the ministry said "no full abolition" — has Adam Adli's deputy posture produced any amendment or policy shift since Feb 2026?); (c) monitor for a direct ministerial-promotion signal — PKR National Congress is scheduled 15-16 Aug 2026 in Melaka (CVS-MLK-166), which is a high-probability window for leadership/promotion signals and is itself a Melaka-relevant event.
**Rationale:** PIR-11's parliamentary-performance and promotion-signal dimensions remain open. The PKR Congress (15-16 Aug, Melaka) is both a promotion-signal window and a Melaka-nexus event — doubly relevant to this workspace.
**Search Queries / Extractions:**
1. `parlimen.gov.my` Hansard/oral-questions for "Timbalan Menteri Pendidikan Tinggi" 2026 (navigate MP profile id=4176)
2. `Adam Adli AUKU memorandum respons 2026 pindaan` (AUKU follow-through)
3. `Kongres Nasional PKR 2026 Melaka Adam Adli` / `rombakan kabinet 2026 Ogos PKR menteri` (promotion signal + PKR Congress)
4. Direct extract: `https://www.mohe.gov.my` news for Adam Adli statements/programme launches

### Suggestion 3: Mas Ermieyati's Post-BERSATU-Suspension Political Trajectory + PAC's Post-LCS Forward Agenda
**Text:** Mas Ermieyati's BERSATU suspension (2 terms/6 years, March 2026) is verified, and her PAC chair status is confirmed (L1, despite suspension). But two forward-looking dimensions of PIR-04 are unmonitored: (a) her *political trajectory post-suspension* — does she remain with BERSATU/PN, defect (WAWASAN was flagged in CJ-MLK-03 as a possible destination), go independent, or align with another force? Her Ketua Srikandi BERSATU role was stripped; her next political move affects the PAC chair's political standing; (b) the PAC's *forward agenda* post-LCS — the 6 reports are tabled, but is the PAC opening new probes, scheduling follow-up proceedings, or issuing further directives to MINDEF (especially given the procurement freeze signal)? The next Dewan Rakyat sitting (special sitting 11 Aug 2026, CVS-MLK-084) may table new PAC business.
**Rationale:** PIR-04's *agenda* is answered; the *forward trajectory* (Mas Ermieyati's political future + PAC's next moves) is the live monitoring layer. Her post-suspension political move is time-sensitive and affects the cross-POI oversight architecture.
**Search Queries / Extractions:**
1. `Mas Ermieyati Samsudin 2026 Ogos politik` / `Mas Ermieyati WAWASAN OR PN OR bebas 2026` (political trajectory)
2. `PAC Parlimen 2026 Ogos prosiding baru` / `jawatankuasa kira wang sidang khas Ogos 2026` (forward agenda)
3. `Mas Ermieyati Srikandi BERSATU jawatan 2026` (stripped-role confirmation)
4. Monitor special Dewan Rakyat sitting 11 Aug 2026 for PAC business

---

*End of CJ-MLK-02 report — Cycle 2026-08-06 01:15 MYT*

---CVS BLOCK---
Claim: This CJ-MLK-02 cycle 3 report (2026-08-06 01:15 MYT) collected 10 new primary sources and logged 12 CVS claims (CVS-MLK-168 to 179), fully resolving PIR-03 (Melaka-base agency gap closed via Adly's Kem Terendak visit + RM3.54B DSA2026 procurement), substantially resolving PIR-11 (concrete Adam Adli PTPTN reform output + cabinet succession), and re-confirming PIR-04's agenda (with PDF deepening blocked).
Source: CJ-MLK-02 collection agent output (this report) — synthesised from L1 mod.gov.my + L2 BERNAMA/Bernamabiz + L4 news sources
Source Level: L1-L4 (mixed, per-claim in evidence register)
Tier: T3 (Analytical Interpretation — this synthesis is an analytical product)
Validation Status: Inferred (synthesis); per-claim validation in CVS-EVIDENCE-REGISTER.csv
Confidence Score: 8 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:0 — synthesis, not a single fact)
Action Required: Human review for analytical assessment elevation
---END CVS BLOCK---
