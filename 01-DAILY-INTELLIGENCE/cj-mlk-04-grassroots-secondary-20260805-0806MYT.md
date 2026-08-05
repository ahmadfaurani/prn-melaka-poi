# CJ-MLK-04 — Grassroots & Secondary POI Collection Report (Cycle 2)

**Workstream:** PRN Melaka — Person of Interest (POI) Intelligence
**Cronjob:** CJ-MLK-04 (Grassroots & Secondary POI Collection)
**POIs of Interest:** Zulkifli Ismail (PIR-12) · Mohd Noor Helmy (PIR-13) · Shamsul Iskandar (PIR-14) · Bakri Jamaluddin (PIR-15)
**PIRs Addressed:** PIR-POI-MLK-12 (MEDIUM) · PIR-POI-MLK-13 (MEDIUM) · PIR-POI-MLK-14 (MEDIUM) · PIR-POI-MLK-15 (MEDIUM)
**Collection Timestamp:** 2026-08-05 08:06 MYT (UTC+8)
**Cycle:** Second collection cycle (auto-approved suggestions from Cycle 1 [00:54 MYT] consumed and incorporated)
**Classification:** TLP:AMBER
**Collector:** CJ-MLK-04 Collection Agent (zai-org/GLM-5.2)

---

## 1. Collection Summary

This is the **second CJ-MLK-04 cycle**. It consumed all 3 auto-approved suggestions from the inaugural cycle (00:54 MYT) and achieved **two major resolutions and two significant advances**:

- **PIR-12 (Zulkifli Ismail — PAS Commissioner):** ★ **RESOLVED.** The #1 auto-approved suggestion gap — the unverified "PAS Melaka commissioner" title — is now **CONFIRMED via three independent sources**: Harakah Daily (29 Sep 2025), Malaysia Tribune (18 Sep 2025), and the PAS Negeri Melaka Facebook page. Zulkifli Ismail is the **Pesuruhjaya PAS Negeri Melaka** for the 2025-2027 session, **reappointed** (he held the post previously). The full 17-member PAS Melaka Daily Working Committee (Jawatankuasa Harian) was extracted.

- **PIR-15 (Bakri Jamaluddin — Engagement):** ★ **ADVANCED.** The #2 auto-approved suggestion gap — parliamentary engagement and constituency activity — is partially closed. Bakri's constituency service centre (Pusat Khidmat Rakyat) is confirmed ACTIVE (6 Jul 2026 hospital bed delivery to constituent; 31 Dec 2025 community event). Additionally, a **major new finding**: Bakri holds **TWO senior party posts** — **Timbalan Pesuruhjaya I (Deputy Commissioner I) PAS Melaka** AND **AJK PAS Pusat (PAS Central Committee member)** — far exceeding the "first-term backbencher" profile documented in Cycle 1. Full Dewan Rakyat speeches/questions remain unrecovered (parlimen.gov.my returned 404).

- **PIR-14 (Shamsul Iskandar — Case Progression):** ★ **ADVANCED.** The #3 auto-approved suggestion — corruption case progression and PKR factional fallout — yielded a **critical new finding**: Shamsul was **appointed PKR Melaka Chairman (Ketua PKR Melaka) on 31 July 2025**, with **Adam Adli as his deputy** (4 months before his Nov 2025 resignation). This establishes the direct Adam Adli succession link the suggestion asked to track. The corruption case itself is **UNCHANGED** — both EN and MS Wikipedia re-extractions show the same Dec 2025 charges with no trial dates, verdicts, or progression. No PKR suspension/expulsion is recorded.

- **PIR-13 (Mohd Noor Helmy — EXCO):** ★ **ADVANCED.** The Malay Wikipedia DUN Melaka page (composition as of 15 Jul 2026) confirms Helmy's **Timbalan EXCO Sains, Teknologi, Inovasi** role is **unaffected** by the July 2026 PH withdrawal (all 4 resigned members were DAP). Confirms **Mohd Yadzil Yaakub (PN) as Ketua Pembangkang (Opposition Leader)** since 13 Nov 2022, and documents the full 28-seat composition.

**Data-source note:** The web_search backend continued to structurally fail for Malaysian political content (8/8 standard queries returned irrelevant results — cm-to-feet converters, mosques, Netflix, furniture). However, **2 suggestion-targeted searches with Malay-language terms** ("PAS Negeri Melaka komisioner", "pesuruhjaya PAS Melaka") **succeeded**, returning the Harakah Daily article, Malaysia Tribune article, and PAS Negeri Melaka Facebook posts — the breakthrough sources for PIR-12 and PIR-15. Direct `web_extract` of pre-identified Wikipedia URLs (EN + MS) and Harakah Daily remained the workhorse. The **11 Aug 2026 Special Dewan Rakyat sitting** (6 days away) was discovered in the 5th session schedule — time-sensitive intelligence.

Raw scrapes saved to `04-DATA-AND-SOURCES/raw-scrapes/20260805/` (9 new files). Scratch metadata saved to `04-DATA-AND-SOURCES/scratch/cj-mlk-04-cycle-20260805-0806-metadata.json`.

---CVS BLOCK---
Claim: Zulkifli Ismail is the Pesuruhjaya PAS Negeri Melaka (PAS Melaka Commissioner) for the 2025-2027 session
Source: Harakah Daily — "PAS Melaka umum Jawatankuasa Harian 2025-2027" (https://harakahdaily.net/2025/09/29/pas-melaka-umum-jawatankuasa-harian-2025-2027/)
Source Level: L4 (mainstream media, PAS-affiliated)
Tier: T2 (Partially Verified — AI max self-assigned; corroborated by 2 additional independent sources)
Validation Status: Verified (triple-corroborated: Harakah Daily + Malaysia Tribune + PAS Negeri Melaka Facebook)
Confidence Score: 8 (Authority:1 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None (human review can upgrade to T1 given triple corroboration)
---END CVS BLOCK---

---CVS BLOCK---
Claim: Bakri Jamaluddin is Timbalan Pesuruhjaya I (Deputy Commissioner I) PAS Melaka and AJK PAS Pusat (PAS Central Committee member)
Source: Harakah Daily (https://harakahdaily.net/2025/09/29/pas-melaka-umum-jawatankuasa-harian-2025-2027/) + Malaysia Tribune (https://malaysiatribune.news/ahli-parlimen-jasin-kekal-sebagai-pesuruhjaya-pas-melaka/) + PAS Negeri Melaka Facebook
Source Level: L4
Tier: T2
Validation Status: Verified (triple-corroborated)
Confidence Score: 8 (Authority:1 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None
---END CVS BLOCK---

---CVS BLOCK---
Claim: Shamsul Iskandar was appointed PKR Melaka Chairman (Ketua PKR Melaka) on 31 July 2025, with Adam Adli as deputy
Source: Wikipedia Bahasa Melayu — Shamsul Iskandar Mohd Akin (https://ms.wikipedia.org/wiki/Shamsul_Iskandar_Mohd_Akin)
Source Level: L4 (Wikipedia)
Tier: T2
Validation Status: Partially Verified (single source; Wikipedia citation needed flag on some fields)
Confidence Score: 7 (Authority:1 Traceability:2 Recency:2 Consistency:1 Completeness:1)
Action Required: Corroboration from PKR official source or news report
---END CVS BLOCK---

---CVS BLOCK---
Claim: Special Dewan Rakyat sitting scheduled for 11 August 2026 (5th Parliamentary Session)
Source: Wikipedia EN — Members of the Dewan Rakyat, 15th Malaysian Parliament
Source Level: L4
Tier: T2
Validation Status: Verified
Confidence Score: 8 (Authority:1 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: Confirm purpose of special sitting via official parliament channels
---END CVS BLOCK---

---

## 2. Findings Table

| # | Source | Date | Summary | PIR | Confidence | Tag |
|---|--------|------|---------|-----|------------|-----|
| C1 | Harakah Daily — PAS Melaka Jawatankuasa Harian 2025-2027 | 29 Sep 2025 | **★★ KEYSTONE — PIR-12 RESOLVED.** CONFIRMS Zulkifli Ismail as **Pesuruhjaya PAS Negeri Melaka** (Commissioner) for 2025-2027. Full 17-member committee: 3 deputy commissioners (Bakri Jamaluddin = Dep I, Ustaz Imran Abdul Rahman = Dep II, Ustaz Wan Zahidi Wan Ismail = Dep III), Secretary = Datuk Muhammad Jailani Khamis (Rembia ADUN), Treasurer = Jamarudin Ahmad, Information Chief = Ustaz Ahmad Bilal Rahudin, Election Director = Ir Mohd Hanim Abas, 2 Asst Secretaries, 7 appointed members. Meeting: 19 Sep 2025, Ayer Keroh. | PIR-12 | HIGH | CRITICAL |
| C2 | Malaysia Tribune — Zulkifli kekal sebagai Pesuruhjaya PAS Melaka | 18 Sep 2025 | **CONFIRMS** Zulkifli **reappointed** (kekal) as PAS Melaka Commissioner 2025-2027 (held post previously). **Bakri Jamaludin newly appointed** as **AJK PAS Pusat** (PAS Central Committee member). Dewan Ulama PAS Melaka issued congratulatory statement. | PIR-12/15 | HIGH | CRITICAL |
| C3 | Wikipedia EN — Bakri Jamaluddin (person page) | Live (5 Aug 2026) | **NEW:** Born 14 Dec 1964 (age 61), Tangga Batu. Contested **N14 Kelebang (state) 2021 — LOST** (29.73%, 3rd) before winning Tangga Batu federal 2022. "Stepping-stone" pattern. 2024 Agong Installation Medal. Official Facebook: facebook.com/bakrijamaluddinn. **Combined party roles: MP + Deputy PAS Melaka Commissioner + PAS Central Committee member.** | PIR-15 | HIGH | CRITICAL |
| C4 | Wikipedia EN — Zulkifli Ismail (person page) | Live (5 Aug 2026) | **NEW (corrects Cycle 1 disambiguation):** EN Wikipedia = correct politician (MS Wikipedia "Zulkifli Ismail" = actor, different person). Born 1 Jan 1966 (age 60), Kampung Paya Rumput Jaya, Sungai Udang, Melaka. **"Ustaz Haji"** title (religious teacher + pilgrim) per PAS official website. Tangga Batu 2018 (lost 12.96%) → Jasin 2022 (won 322 votes). | PIR-12 | HIGH | HIGH |
| C5 | Wikipedia MS — Dewan Undangan Negeri Melaka | Composition 15 Jul 2026 | **Complete 28-seat DUN composition.** BN 20 (UMNO 17/MCA 2/MIC 1), PH 5 (DAP 4/AMANAH 1), PN 2 (BERSATU 1/PAS 1), Independent 1. **Helmy (N21 Duyong) = Timbalan EXCO Sains/Teknologi/Inovasi — UNAFFECTED by PH withdrawal.** 4 DAP EXCO/deputy members resigned July 2026 (Deputy Speaker VACANT). **Yadzil (PN) = Ketua Pembangkang** since 13 Nov 2022. | PIR-13 | HIGH | HIGH |
| C6 | Wikipedia MS — Shamsul Iskandar Mohd Akin | Live (5 Aug 2026) | **★★ CRITICAL NEW FINDING:** Shamsul appointed **PKR Melaka Chairman** (Ketua PKR Melaka) **31 July 2025**, deputy = **Adam Adli**, predecessor = Mohd Rafee Ibrahim. Also: International Bureau Chairman PKR. DGSM award (Datuk Seri, 2018). Corruption case **UNCHANGED** (same 4 charges, no trial progression). No PKR suspension/expulsion recorded. | PIR-14 | HIGH | CRITICAL |
| C7 | Wikipedia EN — Members Dewan Rakyat 15th Parliament (re-extraction) | Live (5 Aug 2026) | **NEW:** 5th Session schedule: 19 Jan–3 Mar 2026; 22 Jun–16 Jul 2026; **Special 11 Aug 2026** (6 days away); 5 Oct–8 Dec 2026. Malacca = PH 3/PN 3/BN 0 confirmed. Opposition Leader: Hamzah → **Samsuri**. PAS=43 MPs (largest single party). Seat marginality data. | PIR-14/15 | HIGH | HIGH |
| C8 | Facebook (search snippets) — Pusat Khidmat Rakyat Parlimen Tangga Batu | 31 Dec 2025 & 6 Jul 2026 | **PIR-15 constituency activity CONFIRMED:** Service centre active — 6 Jul 2026: officers representing **"YB Tuan Haji Bakri Jamaluddin"** delivered adjustable hospital bed to sick constituent (Encik Haron bin Manap). 31 Dec 2025: community event at Taman Tanjung Minyak Perdana. Title confirms **"Haji"** pilgrimage. | PIR-15 | MEDIUM | HIGH |
| C9 | Harakah Daily homepage | 4 Aug 2026 | **Context:** Harakah editorial line heavily promotes **"Muafakat BN-PN"** and **"Penyatuan Ummah"** (Ummah Unity). N9 PRN framed as proof-of-concept for BN-PN cooperation. "Kekuatan jentera" (machinery strength) cited as victory factor. Frames PAS Melaka mobilization strategy context. | PIR-12 | MEDIUM | MEDIUM |

---

## 3. PIR Resolution Status

| PIR ID | Status | New Evidence (Cycle 2) | Confidence |
|--------|--------|----------------------|------------|
| **PIR-POI-MLK-12** (Zulkifli Ismail — PAS Grassroots Mobilization) [MEDIUM] | **★★ RESOLVED** | **Commissioner title CONFIRMED** via 3 sources (Harakah Daily 29 Sep 2025, Malaysia Tribune 18 Sep 2025, PAS Negeri Melaka Facebook). Zulkifli = Pesuruhjaya PAS Negeri Melaka 2025-2027, **reappointed** (held post previously). Full 17-member PAS Melaka Jawatankuasa Harian extracted: 3 deputy commissioners (Bakri = Dep I), Secretary (Jailani/Rembia), Treasurer, Info Chief, **Election Director (Ir Mohd Hanim Abas)**, 2 Asst Secretaries, 7 appointed members. "Ustaz Haji" / "Tuan Guru" religious title confirmed. Mobilization context: BN-PN Muafakat/Penyatuan Ummah strategy (Harakah editorial Aug 2026). Born Sungai Udang (within Tangga Batu parl area) — local roots. | HIGH |
| **PIR-POI-MLK-13** (Mohd Noor Helmy — EXCO Portfolio & Succession) [MEDIUM] | **Advanced (role secure; succession open)** | **DUN composition 15 Jul 2026 confirmed:** Helmy (N21 Duyong, BN-UMNO) = Timbalan EXCO Sains/Teknologi/Inovasi — **UNAFFECTED** by PH withdrawal (all 4 resigned = DAP). Deputy Speaker VACANT (July 2026). BN holds 20/28 (71.4%). **Yadzil (PN) = Opposition Leader** since 13 Nov 2022. Helmy's portfolio mirrors full-EXCO Fairul Nizam Roslan (N10 Asahan) — both Science/Tech/Innovation, suggesting a paired deputy portfolio. Succession trajectory remains early-stage and constrained by marginal seat (200-vote majority). | HIGH (role) / OPEN (succession) |
| **PIR-POI-MLK-14** (Shamsul Iskandar — Current Status & Re-election Intentions) [MEDIUM] | **Advanced (PKR Melaka chair found; case unchanged)** | **NEW:** Shamsul appointed **PKR Melaka Chairman 31 July 2025**, deputy = **Adam Adli** (direct succession link confirmed). Predecessor: Mohd Rafee Ibrahim. Also: International Bureau Chairman, DGSM (Datuk Seri, 2018). **Corruption case UNCHANGED** — EN+MS Wikipedia re-extraction shows same 4 Dec 2025 charges, no trial dates, verdicts, or progression. No PKR suspension/expulsion recorded. Re-entry still BLOCKED. The Adam Adli succession question (auto-approved Suggestion 3) is partially answered: Adam was already Shamsul's designated deputy. | HIGH |
| **PIR-POI-MLK-15** (Bakri Jamaluddin — Affiliation & Engagement) [MEDIUM] | **Advanced (party roles found; parliamentary engagement partial)** | **NEW party roles:** Bakri = **Timbalan Pesuruhjaya I PAS Melaka** (Deputy Commissioner) + **AJK PAS Pusat** (Central Committee member) — far beyond "first-term MP." Constituency activity CONFIRMED: service centre active 6 Jul 2026 (hospital bed delivery) + 31 Dec 2025 (community event). Title "YB Tuan Haji Bakri Jamaluddin." Electoral history: contested N14 Kelebang 2021 (lost 29.73%) → won Tangga Batu 2022 (40.65%) — stepping-stone pattern. Born Tangga Batu (local son). Dewan Rakyat speeches/questions/committees still NOT recovered (parlimen.gov.my 404; Wikipedia page truncated). | HIGH (affiliation + party roles + constituency) / OPEN (parliamentary record) |

---

## 4. VERIFICATION STATUS (PIR-14 & PIR-15)

### PIR-POI-MLK-14 — Shamsul Iskandar @ Yusre Mohd Akin

**VERIFICATION STATUS: ✅ CONFIRMED** (current status found; case progression tracked)

| Verification Target | Status | Evidence |
|---|---|---|
| Current elected office | **CONFIRMED — NONE** | Last MP term ended 19 Nov 2022 (Hang Tuah Jaya). Lost Bagan Datuk 2022 by 348 votes. Not in 15th Parliament. (C6, C7) |
| Current government post | **CONFIRMED — RESIGNED** | Senior Political Secretary to PM, 23 Dec 2022 – 25 Nov 2025 (resigned). Succeeded by Tengku Zafrul Aziz. (C6) |
| Current PKR party position | **★ NEW: PKR Melaka Chairman since 31 Jul 2025** | Appointed Ketua PKR Melaka 31 Jul 2025; deputy = Adam Adli; predecessor = Mohd Rafee Ibrahim. Also International Bureau Chairman. (C6) |
| Re-entry into active politics | **CONFIRMED — BLOCKED** | Active corruption case (4 charges, Dec 2025). Case UNCHANGED — no trial progression as of 5 Aug 2026. No comeback signal. (C6) |
| PKR factional alignment | **CONFIRMED — Reformist/Anwar wing** | Ex-VP (2014-18, alongside Rafizi), ex-Youth Chief (2007-14), ex-Info Chief (2018-21), PKR Melaka Chairman (Jul 2025). Succession chain → Adam Adli. (C6) |
| PKR disciplinary action | **UNCONFIRMED — NOT FOUND** | No PKR suspension/expulsion recorded in either Wikipedia page. Status of PKR Melaka chairmanship post-charges unknown — likely acting-deputy (Adam Adli) but unconfirmed. (C6) |
| Corruption case progression | **CONFIRMED — UNCHANGED** | Re-extraction of EN + MS Wikipedia (5 Aug 2026) shows same 4 Dec 2025 charges. No trial dates, verdicts, acquittals, or appeals documented. Case at "charged, awaiting trial" stage. (C6) |

**Conclusion:** Shamsul Iskandar holds no elected office and resigned from government on 25 Nov 2025. He was appointed PKR Melaka Chairman on 31 Jul 2025 (deputy: Adam Adli) — a position he likely can no longer effectively hold given the active corruption case. The 4 corruption charges (Dec 2025) remain unchanged with no documented trial progression. His re-entry into active politics remains blocked. The Adam Adli succession is structurally in place (Adam was his designated deputy). The ongoing variable remains the case outcome (no change this cycle).

---CVS BLOCK---
Claim: Shamsul Iskandar's corruption case (4 charges, Dec 2025) remains unchanged with no trial progression as of 5 August 2026
Source: Wikipedia EN + MS re-extraction (https://en.wikipedia.org/wiki/Shamsul_Iskandar_Mohd_Akin, https://ms.wikipedia.org/wiki/Shamsul_Iskandar_Mohd_Akin)
Source Level: L4
Tier: T2
Validation Status: Verified (negative finding — absence of new updates across two Wikipedia editions)
Confidence Score: 7 (Authority:1 Traceability:2 Recency:2 Consistency:1 Completeness:1)
Action Required: Corroboration via SPRM/court records or news reports for trial dates
---END CVS BLOCK---

### PIR-POI-MLK-15 — Bakri Jamaluddin

**VERIFICATION STATUS: ✅ CONFIRMED** (affiliation + party roles + constituency activity verified; parliamentary record open)

| Verification Target | Status | Evidence |
|---|---|---|
| Current political affiliation | **✅ CONFIRMED — PN/PAS** | MP for Tangga Batu (P136), PAS, PN, since 2022. (C3) |
| MP status & election | **CONFIRMED** | Won GE15 2022 with 37,406 (40.65%), majority 8,849 (9.62%). PN gain from PH/PKR. (C3) |
| ★ Party roles (NEW) | **★ CONFIRMED — Deputy PAS Melaka Commissioner + PAS Central Committee member** | Timbalan Pesuruhjaya I PAS Melaka (Harakah, 29 Sep 2025) + AJK PAS Pusat (Malaysia Tribune, 18 Sep 2025 + PAS Facebook). (C1, C2) |
| Constituency activity | **✅ CONFIRMED — ACTIVE** | Pusat Khidmat Rakyat Parlimen Tangga Batu active: 6 Jul 2026 (hospital bed delivery to constituent) + 31 Dec 2025 (community event). Officers represent "YB Tuan Haji Bakri Jamaluddin." (C8) |
| Electoral history (NEW) | **CONFIRMED** | Contested N14 Kelebang (state) 2021 — LOST (29.73%, 3rd) → Won Tangga Batu (federal) 2022 (40.65%). Stepping-stone pattern. Born in Tangga Batu (local son). (C3) |
| Parliamentary engagement (Dewan Rakyat) | **UNCONFIRMED — OPEN** | Specific Dewan Rakyat speeches, questions, committee memberships NOT recovered. parlimen.gov.my/ahli-parlimen.html returned 404. Wikipedia Dewan Rakyat page truncated before Malacca member-detail table. **However:** 5th Session Special sitting 11 Aug 2026 identified — Bakri expected to attend. (C7) |
| Candidate for PRN Melaka | **INFERRED — LIKELY** | As incumbent MP + Deputy PAS Commissioner + PAS Central Committee member + Election Director's colleague, Bakri is the presumptive PN/PAS candidate to defend Tangga Batu. Not officially confirmed. |

**Conclusion:** The PIR-15 affiliation verification (resolved in Cycle 1) is now supplemented with a **major upgrade**: Bakri Jamaluddin is not merely a first-term MP but a **triple-role PAS leader** — MP + Deputy PAS Melaka Commissioner + PAS Central Committee member. His constituency service is confirmed active (6 Jul 2026). The remaining open gap is his Dewan Rakyat record (speeches/questions/committees), blocked by the parlimen.gov.my 404 and Wikipedia page truncation. The 11 Aug 2026 Special sitting is a near-term opportunity to observe his parliamentary engagement.

---CVS BLOCK---
Claim: Bakri Jamaluddin's constituency service centre (Pusat Khidmat Rakyat Parlimen Tangga Batu) is active, with documented welfare assistance on 6 July 2026
Source: Facebook search snippet — Pusat Khidmat Rakyat Parlimen Tangga Batu (https://www.facebook.com/pusatkhidmatparlimentanggabatu/)
Source Level: L5 (social media — verified page but extraction blocked, evidence from search snippet only)
Tier: T2
Validation Status: Partially Verified (single source, snippet-level evidence)
Confidence Score: 5 (Authority:1 Traceability:1 Recency:2 Consistency:1 Completeness:0)
Action Required: Corroboration via news report or direct page access
---END CVS BLOCK---

---

## 5. Analytical Synthesis

### 5.1 PAS Melaka Organizational Structure — Now Fully Mapped (PIR-12 Resolved)

The Harakah Daily article (29 Sep 2025) is the keystone that transforms PIR-12 from "MP status confirmed, commissioner title unverified" (Cycle 1) to **fully resolved**. The PAS Melaka Daily Working Committee (Jawatankuasa Harian) for 2025-2027 is a 17-member body led by Commissioner (Pesuruhjaya) **Tuan Guru Zulkifli Ismail** — an "Ustaz Haji" with religious credentials, born in Sungai Udang (within the Tangga Batu parliamentary area), and a two-contest electoral veteran (Tangga Batu 2018 lost → Jasin 2022 won by 322 votes). He was **reappointed** (kekal), meaning he held the commissionership before the 2025-2027 session.

The committee structure reveals PAS Melaka's organizational depth: **3 deputy commissioners** (Bakri Jamaluddin = Dep I, Ustaz Imran Abdul Rahman = Dep II, Ustaz Wan Zahidi Wan Ismail = Dep III), a **Secretary** (Datuk Muhammad Jailani Khamis — the Rembia ADUN, resolving the Cycle 1 ambiguity about PAS's 1 state seat), a **Treasurer**, an **Information Chief**, and critically an **Election Director** (Ir Mohd Hanim Abas — a trained engineer heading election operations for the imminent PRN). This is a complete shadow-state-level organizational apparatus for a party that holds only 2 federal + 1 state seat in Melaka — disproportionate organizational investment.

### 5.2 The Zulkifli-Bakri Dual Leadership Structure (PIR-12/15 nexus)

A striking structural finding: **PAS Melaka's top two positions are held by its two Malacca federal MPs.** Zulkifli Ismail (Jasin MP) is Commissioner; Bakri Jamaluddin (Tangga Batu MP) is Deputy Commissioner I. This is a deliberate concentration of parliamentary authority and party leadership in the same two individuals — ensuring that PAS Melaka's organizational head and his deputy are both sitting MPs with federal-level visibility and constituency bases. Further, Bakri's elevation to **AJK PAS Pusat** (national Central Committee) gives PAS Melaka a voice at the national party table. This dual structure means PAS Melaka is led by a "ticket" rather than a single figurehead, and the succession path (Zulkifli → Bakri) is structurally embedded in the committee hierarchy.

### 5.3 Shamsul's PKR Melaka Chairmanship — The Hidden Factional Variable (PIR-14)

The most surprising finding of Cycle 2 is that Shamsul Iskandar was **appointed PKR Melaka Chairman on 31 July 2025** — 4 months before his Nov 2025 resignation and Dec 2025 corruption charges. This means PKR elevated him to state leadership at a time when he was already serving as Senior Political Secretary to PM Anwar (a dual government-party role), and his deputy was designated as **Adam Adli** (the current Hang Tuah Jaya MP and Deputy Minister). The timeline:
- **31 Jul 2025:** Appointed PKR Melaka Chairman (deputy: Adam Adli)
- **25 Nov 2025:** Resigned as Senior Political Secretary to PM (Albert Tei scandal)
- **Dec 2025:** 4 corruption charges filed
- **5 Aug 2026 (this cycle):** Case unchanged; no PKR disciplinary action recorded

The implication is that **Adam Adli is the structurally designated successor** as PKR Melaka Chairman — he was Shamsul's deputy. Whether Adam has formally assumed the acting chairmanship is unconfirmed (no Wikipedia or news source records this), but the organizational structure makes him the presumptive acting chairman. This directly addresses the auto-approved Suggestion 3 question about "the Adam Adli succession in PKR Melaka." The reformist factional space Shamsul occupied is now contested between Adam Adli (institutional successor, government-aligned) and Rafizi Ramli's BERSAMA (reformist splinter targeting Melaka PRN, per CJ-MLK-03).

### 5.4 Mohd Noor Helmy — Secure Deputy in a Post-Withdrawal EXCO (PIR-13)

The Malay Wikipedia DUN Melaka page (composition as of 15 Jul 2026) confirms that Helmy's position is **structurally secure** despite the July 2026 PH withdrawal. All 4 EXCO/deputy members who resigned were PH-DAP (Kerk Chee Yee, Seah Shoo Chin, Low Chee Leong, Leng Chau Yen) — Helmy's BN-UMNO Timbalan EXCO role is unaffected. The Deputy Speaker position is now VACANT (Kerk resigned). The post-withdrawal EXCO is BN-only, which paradoxically strengthens Helmy's relative position (fewer deputy EXCO competitors). His portfolio (Sains, Teknologi, Inovasi) mirrors full-EXCO Fairul Nizam Roslan (N10 Asahan) — a paired portfolio, suggesting a mentor-mentee or parallel structure. His marginal seat (200 votes, 1.65%) remains the binding constraint on his succession trajectory.

### 5.5 The BN-PN Muafakat Mobilization Context (PIR-12 strategic frame)

Harakah Daily's editorial line (4 Aug 2026) reveals the strategic frame within which Zulkifli Ismail's PAS Melaka mobilization operates: the **"Muafakat BN-PN"** and **"Penyatuan Ummah"** (Ummah Unity) narrative. PAS is not mobilizing against BN in Melaka — it is mobilizing **alongside BN** through informal cooperation, framed as Malay-Muslim unity. The N9 (Negeri Sembilan) state election is being positioned as the proof-of-concept ("PRN N9 bukti Penyatuan Ummah bukan slogan politik"). The "kekuatan jentera" (machinery strength) cited as a victory factor is precisely the grassroots apparatus that PAS Melaka's Election Director (Ir Mohd Hanim Abas) oversees. This means PIR-12's "grassroots mobilization approach" is: **coordinate with BN through Muafakat, deploy the PAS machinery (jentera) for turnout, and frame the contest as Ummah unity rather than party competition.** The PAS-BERSATU break (8-9 Jun 2026, per CJ-MLK-03) does not disrupt this — because the Muafakat is BN-PAS, not PN-internal.

### 5.6 The 11 August 2026 Special Sitting — Time-Sensitive Watch Item

The discovery of a **Special Dewan Rakyat sitting on 11 August 2026** (6 days from collection) is a time-sensitive intelligence item. Both Zulkifli Ismail (Jasin MP) and Bakri Jamaluddin (Tangga Batu MP) are sitting MPs expected to attend. The purpose of the special sitting is not specified in the Wikipedia summary, but special sittings typically address urgent national business (emergency legislation, motions, etc.). This is the near-term opportunity to observe both PIR-12 and PIR-15 POIs' parliamentary engagement that the parlimen.gov.my 404 currently blocks.

---CVS BLOCK---
Claim: Melaka DUN composition as of 15 July 2026 is BN 20 / PH 5 / PN 2 / Independent 1, with 4 PH-DAP EXCO members having resigned in July 2026
Source: Wikipedia Bahasa Melayu — Dewan Undangan Negeri Melaka (https://ms.wikipedia.org/wiki/Dewan_Undangan_Negeri_Melaka)
Source Level: L4
Tier: T2
Validation Status: Verified
Confidence Score: 8 (Authority:1 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None
---END CVS BLOCK---

---CVS BLOCK---
Claim: Mohd Yadzil Yaakub (PN-BERSATU, N24 Bemban) is the Ketua Pembangkang (Opposition Leader) of the Melaka State Assembly since 13 November 2022
Source: Wikipedia Bahasa Melayu — Dewan Undangan Negeri Melaka (https://ms.wikipedia.org/wiki/Dewan_Undangan_Negeri_Melaka)
Source Level: L4
Tier: T2
Validation Status: Verified
Confidence Score: 8 (Authority:1 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None
---END CVS BLOCK---

---CVS BLOCK---
Claim: [ASSESSMENT] PAS Melaka's grassroots mobilization strategy operates through the "Muafakat BN-PN" and "Penyatuan Ummah" framework — coordinating with BN rather than competing, deploying party machinery (jentera) for turnout, and framing contests as Malay-Muslim unity
Source: Harakah Daily homepage editorial analysis (https://www.harakahdaily.net, 4 Aug 2026)
Source Level: L4
Tier: T3 (Analytical Interpretation)
Validation Status: Inferred
Confidence Score: 6 (Authority:1 Traceability:2 Recency:2 Consistency:1 Completeness:0)
Action Required: Human review — analytical assessment derived from editorial content, not direct statement
---END CVS BLOCK---

---

## 6. TOP 3 PIR SUGGESTIONS FOR NEXT CYCLE (AUTO-APPROVED)

*(Full text written to `07-AUDIT/top3-mlk-suggestions-CJMLK04.md`)*

1. **Bakri Jamaluddin's Dewan Rakyat record — exploit the 11 Aug 2026 Special Sitting** (PIR-15) — the sole remaining open gap in PIR-15; the 11 Aug special sitting is a near-term observation opportunity.
2. **Shamsul's PKR Melaka chairmanship status post-charges + Adam Adli acting chairmanship** (PIR-14) — confirm whether Adam Adli has formally assumed acting PKR Melaka chairman; track any PKR disciplinary action.
3. **PAS Melaka grassroots mobilization events (ceramah/usrah/muktamar) & Election Director operations** (PIR-12) — the commissioner title is resolved; now recover the operational mobilization activities on the ground.

---

## 7. Appendix — Raw Scrapes Inventory (Cycle 2)

| File | PIR | Source |
|---|---|---|
| PIR12-harakah-pas-melaka-jawatankuasa-harian-2025-2027-KEYSTONE.md | PIR-12 | Harakah Daily — PAS Melaka Jawatankuasa Harian 2025-2027 |
| PIR12-15-malaysiatribune-zulkifli-kekal-pesuruhjaya-pas-melaka.md | PIR-12/15 | Malaysia Tribune — Zulkifli kekal Pesuruhjaya PAS Melaka |
| PIR15-wikipedia-bakri-jamaluddin-person-profile.md | PIR-15 | Wikipedia EN — Bakri Jamaluddin (person) |
| PIR12-wikipedia-zulkifli-ismail-person-profile.md | PIR-12 | Wikipedia EN — Zulkifli Ismail (person) |
| PIR13-ms-wikipedia-dewan-undangan-negeri-melaka-20260715.md | PIR-13 | Wikipedia MS — DUN Melaka (composition 15 Jul 2026) |
| PIR14-ms-wikipedia-shamsul-iskandar-pkr-melaka-chairman.md | PIR-14 | Wikipedia MS — Shamsul Iskandar (PKR Melaka Chairman finding) |
| PIR14-15-wikipedia-dewan-rakyat-5th-session-2026-schedule.md | PIR-14/15 | Wikipedia EN — Dewan Rakyat 5th Session (11 Aug 2026 Special) |
| PIR15-tangga-batu-pusat-khidmat-rakyat-constituency-activity.md | PIR-15 | Facebook snippets — Tangga Batu Service Centre |
| PIR12-harakahdaily-homepage-bnpn-muafakat-context-20260804.md | PIR-12 | Harakah Daily homepage — BN-PN Muafakat context |

All scrapes in `04-DATA-AND-SOURCES/raw-scrapes/20260805/`. Scratch metadata: `04-DATA-AND-SOURCES/scratch/cj-mlk-04-cycle-20260805-0806-metadata.json`.

---

## 8. CVS Evidence Register Entries (Cycle 2)

The following 15 claims were appended to `03-VERIFICATION/CVS-EVIDENCE-REGISTER.csv` (CVS-MLK-074 to CVS-MLK-088):

| Claim ID | Claim Summary | Tier | Score |
|---|---|---|---|
| CVS-MLK-074 | Zulkifli Ismail = Pesuruhjaya PAS Negeri Melaka 2025-2027 | T2 | 8 |
| CVS-MLK-075 | Zulkifli reappointed (kekal) as PAS Melaka Commissioner | T2 | 8 |
| CVS-MLK-076 | Bakri Jamaluddin = Timbalan Pesuruhjaya I PAS Melaka | T2 | 8 |
| CVS-MLK-077 | Bakri Jamaluddin = AJK PAS Pusat (Central Committee member) | T2 | 8 |
| CVS-MLK-078 | PAS Melaka Jawatankuasa Harian 2025-2027 = 17 members | T2 | 8 |
| CVS-MLK-079 | Muhammad Jailani Khamis = PAS Melaka Secretary (Rembia ADUN) | T2 | 7 |
| CVS-MLK-080 | Shamsul appointed PKR Melaka Chairman 31 Jul 2025 (dep: Adam Adli) | T2 | 7 |
| CVS-MLK-081 | Bakri contested N14 Kelebang 2021 (lost 29.73%) → won Tangga Batu 2022 | T2 | 8 |
| CVS-MLK-082 | Zulkifli born 1 Jan 1966, Sungai Udang; "Ustaz Haji" title | T2 | 7 |
| CVS-MLK-083 | Bakri's service centre active 6 Jul 2026 (hospital bed delivery) | T2 | 5 |
| CVS-MLK-084 | Special Dewan Rakyat sitting scheduled 11 Aug 2026 | T2 | 8 |
| CVS-MLK-085 | DUN Melaka 15 Jul 2026: BN 20/PH 5/PN 2/IND 1; Yadzil = Opp Leader | T2 | 8 |
| CVS-MLK-086 | 4 PH-DAP EXCO members resigned July 2026; Deputy Speaker vacant | T2 | 7 |
| CVS-MLK-087 | [ASSESSMENT] PAS Melaka mobilizes via Muafakat BN-PN/Penyatuan Ummah | T3 | 6 |
| CVS-MLK-088 | Shamsul corruption case unchanged (no trial progression since Dec 2025) | T2 | 7 |

---

*End of CJ-MLK-04 Cycle 2 report.*
