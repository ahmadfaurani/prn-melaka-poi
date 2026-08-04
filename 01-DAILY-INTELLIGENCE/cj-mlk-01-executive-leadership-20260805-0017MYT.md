# CJ-MLK-01 — Executive Leadership & Governance Collection Report

**Workstream:** PRN Melaka — Person of Interest (POI) Intelligence
**Cronjob:** CJ-MLK-01 (Executive Leadership & Governance)
**POIs of Interest:** Ab Rauf Yusoh (Ketua Menteri Melaka) · Dr Muhamad Akmal Saleh (Ketua Pemuda UMNO Malaysia)
**PIRs Addressed:** PIR-POI-MLK-01 (CRITICAL) · PIR-POI-MLK-02 (CRITICAL) · PIR-POI-MLK-06 (HIGH) · PIR-POI-MLK-07 (HIGH) · PIR-POI-MLK-08 (HIGH)
**Collection Timestamp:** 2026-08-05 00:17 MYT (UTC+8)
**Cycle:** First collection cycle (no prior `07-AUDIT/top3-mlk-suggestions-CJMLK01.md` existed)
**Classification:** TLP:AMBER
**Collector:** CJ-MLK-01 Collection Agent (zai-org/GLM-5.2)

---

## 1. Collection Summary

This is the inaugural CJ-MLK-01 cycle. 19 search queries were executed across the configured backend; the backend poorly indexes Malaysian news outlets (queries containing the token "AB" matched AllianceBernstein/Rockwell; "Akmal" matched a Russian singer; `site:` operators returned empty; Kosmo.com.my blocks scraping via anti-bot). Productive results came from the first-batch generic queries plus direct `web_extract` of discovered URLs. **6 primary articles** were collected with full content; **4 additional secondary references** were captured from the primary articles' sidebars (cited with attribution, marked unverified — Kosmo anti-bot prevented direct scrape).

Raw scrapes saved to `04-DATA-AND-SOURCES/raw-scrapes/20260805/`. Scratch metadata saved to `04-DATA-AND-SOURCES/scratch/cj-mlk-01-cycle-20260805-0017-metadata.json`.

**Key thematic finding:** A clear **Akmal–Zahid policy split** is the engine driving Akmal's national rhetoric. Akmal proposed (a) UMNO exit the federal unity government and (b) revive Muafakat Nasional cooperation with PAS; President Zahid rejected both. Akmal then executed a *selective resignation* (Melaka EXCO, 19 Jan 2026) while retaining the national Youth chief platform — a pressure tactic that decouples his anti-DAP rhetoric from state-coalition constraint. Meanwhile, Ab Rauf Yusoh's governance is being projected (via UMNO Online / BN Comms) as proof of UMNO's *delivery capability* — a federal-alignment narrative rather than divergence.

---

## 2. Findings Table

| # | Source | Date | Summary | PIR | Confidence | Tag |
|---|--------|------|---------|-----|------------|-----|
| A1 | BN Comms (bncomms.my) | 2026-04-21 | Ab Rauf chairs MAIM + MCorp board meetings (Bil.1/2026). Governance agenda = people-centric "Melaka Sayang Rakyat" (MeSRa); pillars: religious affairs, education, state finance. 3 budget agendas: economic development, human capital/welfare, governance & integrity. | PIR-01 | HIGH | CRITICAL |
| A2 | MYKMU.NET (UMNO Online) | 2026-04-21 | Same event as A1. Frames Kampung Digital initiative as proof of UMNO governing competence = **federal-alignment narrative** (state policy projected as UMNO delivery, not divergence). | PIR-01 | HIGH | CRITICAL |
| A3 | The Star | 2026-07-26 | **Freshest Akmal rhetoric** (ceramah Linggi/Port Dickson, NS). Draws 3R red lines (religion/race/rulers); dares govt to arrest him; confirms UMNO Youth excluded Pakatan from 2023 assembly. Exporting rhetoric to NS state-polls battleground. | PIR-02 | HIGH | CRITICAL |
| A4 | Kosmo Digital | 2026-02-05 | Akmal resigned Melaka EXCO on 19 Jan 2026 (letter routed via Ab Rauf to Governor). Selective resignation = pressure on Zahid while keeping Youth chief. Sidebar reveals very recent (Aug 2-4 2026) Melaka admin reshuffle. | PIR-02 / PIR-08 | HIGH | CRITICAL |
| A5 | New Straits Times | 2026-02-12 | Keluar Sekejap podcast (with Khairy). Multiracial inoculation: "mother-in-law is Chinese"; "DAP has chauvinist DNA, 10-20 yrs to change". Cites working relationship with Melaka DAP deputy exco = **federal/state posture split**. Boycott triggers: flag, Allah socks, UEC, Kampung Baru. | PIR-02 | HIGH | CRITICAL |
| A6 | Malay Mail | 2026-01-09 | **KEYSTONE PIR-08.** Akmal proposed UMNO leave federal govt + revive Muafakat Nasional with PAS; Zahid rejected both. Asyraf Wajdi = mediating "elder brother" who placed Akmal in Youth chief role. Akmal-Zahid split = engine of national rhetoric. | PIR-08 / PIR-02 | HIGH | HIGH→CRITICAL cross-cut |
| S1 | The Star sidebar (via A3) | ~2026-07-25 | "Melaka Barisan likely to retain most incumbents for state polls" — suggests Ab Rauf controls incumbent list. *(unverified secondary ref)* | PIR-06 | MEDIUM | HIGH |
| S2 | Kosmo sidebar (via A4) | 2026-08-04 | "3 Exco BN dijangka kekal dalam pentadbiran baharu" — fresh Melaka admin reshuffle underway; Akmal's vacated EXCO slot being redistributed. *(unverified; Kosmo anti-bot)* | PIR-01 / PIR-06 | MEDIUM | HIGH |
| S3 | Kosmo sidebar (via A4) | 2026-08-02 | "Giliran Melaka pula pertahan kemenangan BN – Ab. Rauf" — Ab Rauf framing Melaka as next BN defense; PRN/electoral context. *(unverified)* | PIR-01 / PIR-06 | MEDIUM | HIGH |
| S4 | Kosmo sidebar (via A4) | 2026-08-02 | "Ramalan saya hampir tepat, BN-PN mampu kuasai Melaka" — coalition/PRN capability signal. *(unverified)* | PIR-05 (cross) | LOW | — |

---

## 3. PIR Resolution Status

| PIR ID | Status | New Evidence | Confidence |
|--------|--------|--------------|------------|
| **PIR-POI-MLK-01** (Ab Rauf — Governance Agenda & Federal Alignment) [CRITICAL] | **Partial** | Governance agenda well-documented: MeSRa flagship; MAIM + MCorp board chairmanship (religious + development-corp control); 3 budget agendas (economy, human capital, governance/integrity); Kampung Digital as UMNO-delivery narrative. **Federal-alignment angle** = state policy projected as proof of UMNO competence (MYKMU framing) — alignment, not divergence. Gap: candidate-selection & 2026 roadmap detail still thin. | HIGH |
| **PIR-POI-MLK-02** (Dr Akmal — Rhetoric Trajectory & National Impact) [CRITICAL] | **Partial → Resolved (rhetoric); Open (impact)** | Rhetoric trajectory strongly documented Jan→Jul 2026: 3R red lines, arrest-dare, DAP-"chauvinist-DNA" doctrine (10-20yr change horizon), "defend-not-attack" framing, named boycott triggers (flag, Allah socks/KK Mart, UEC, Kampung Baru), multiracial inoculation ("mother-in-law is Chinese"), export to NS state polls. UMNO Youth confirmed as internal opposition to unity govt (excluded Pakatan from 2023 assembly). **Gap:** *measurable* electoral/commercial impact not yet quantified — flagged as top suggestion. | HIGH |
| **PIR-POI-MLK-06** (Ab Rauf — Federal-State Power Dynamics) [HIGH] | **Open** | Only indirect proxies: Akmal's EXCO resignation routed *through* Ab Rauf (gatekeeper role); sidebar refs to "Melaka BN retain incumbents" & "Ab Rauf pertahan kemenangan BN". **No direct Ab Rauf–Zahid or Ab Rauf–Tok Mat interaction documented.** Most under-resolved PIR — flagged as top suggestion. | MEDIUM |
| **PIR-POI-MLK-07** (Dr Akmal — Youth Mobilization & Ground Impact in Melaka) [HIGH] | **Open** | Weakest PIR. Indirect only: Akmal = ADUN Merlimau; cited working relationship with a Melaka DAP deputy-exco; mobilization exported beyond Melaka (NS ceramah, Kinabatangan by-election). **No direct Merlimau grassroots/Youth-campaign-on-the-ground data collected.** | LOW |
| **PIR-POI-MLK-08** (Dr Akmal — Succession Positioning & Party Dynamics) [HIGH] | **Partial → Resolved** | **Keystone established:** Akmal–Zahid split (Akmal proposed UMNO leave federal govt + revive Muafakat Nasional with PAS; Zahid rejected both). Asyraf Wajdi Dusuki = mediating "elder brother" who elevated Akmal to Youth chief (key relationship node). Selective-resignation tactic (EXCO out, Youth chief kept) = pressure without losing national platform. Succession-as-internal-opposition doctrine: Akmal positions as standard-bearer of the anti-unity-government UMNO faction. | HIGH |

---

## 4. Analytical Synthesis

### 4.1 The Akmal–Zahid Axis (cross-PIR-02 / PIR-08)

The single most important intelligence thread this cycle is the documented **policy split** between Dr Akmal and UMNO President Zahid Hamidi (Malay Mail, 9 Jan 2026). Akmal tabled two proposals at the party political bureau: (1) UMNO exits the federal unity government; (2) revive Muafakat Nasional (UMNO-PAS Malay-Muslim consolidation). Zahid rejected both. Akmal's subsequent threat to "step aside" and his actual resignation of the Melaka EXCO (19 Jan 2026, via Ab Rauf to the Governor) constitute a **selective-resignation pressure tactic**: he surrendered state executive power (and the coalition-government constraint that came with it) while preserving the national Youth chief platform from which he attacks DAP and the unity arrangement.

This split is the **causal engine** of Akmal's national rhetoric (PIR-02). His 3R red lines, the KK Mart/"Allah socks" boycott, the "DAP chauvinist DNA" doctrine, and the "challenge the government to arrest me" escalation are all instruments of an internal UMNO faction fight exported to the public arena. Asyraf Wajdi Dusuki (sec-gen, self-described "elder brother" who placed Akmal in the Youth role) is the mediating node between Akmal and Zahid — a relationship to monitor for succession signals.

### 4.2 Ab Rauf's Governance Posture (PIR-01)

Ab Rauf Yusoh's governance is articulated through the **"Melaka Sayang Rakyat" (MeSRa)** brand, prioritising welfare over pure physical development, with three stated budget agendas (economic development, human capital/welfare, governance & integrity). His simultaneous chairmanship of MAIM (Islamic Religious Council) and MCorp (state development corporation) boards signals consolidation of both the Malay-Muslim religious base apparatus and the state's development corporate vehicle.

Crucially, UMNO-aligned media (MYKMU/UMNO Online) frames the Kampung Digital initiative as **proof of UMNO's governing competence** — i.e., Ab Rauf's state policy is being projected as UMNO *delivery*, an alignment narrative rather than divergence from federal UMNO. The federal-alignment question (PIR-01) is therefore partially answered: at the *narrative* level, Ab Rauf is aligned with federal UMNO's self-presentation. Direct evidence of policy divergence (or its absence) requires further collection.

### 4.3 The Federal/State Posture Split (cross-PIR-02 / PIR-07)

A notable finding: Akmal explicitly cited a **working relationship with a Melaka DAP deputy-exco** (NST, 12 Feb 2026) — direct evidence that at the *state* level, Akmal cooperates with DAP (within the BN-PH Melaka coalition) even while attacking DAP *nationally*. This federal/state posture split is a structural feature of his positioning and bears on PIR-07 (Melaka ground): his Merlimau constituency operation exists within a BN-PH coalition state government he rhetorically opposes at the federal level.

### 4.4 Fresh Signals (Aug 2-4, 2026) — Melaka Administration Reshuffle

The most time-sensitive unverified signals come from Kosmo sidebars (anti-bot prevented full scrape): a **fresh Melaka state administration reshuffle** appears underway, with "3 Exco BN expected to remain in the new administration" (4 Aug) and Ab Rauf framing Melaka as "next to defend BN's victory" (2 Aug), against the backdrop of BN being the "biggest winner" in the Negri Sembilan state polls (2 Aug). This suggests (a) Akmal's vacated EXCO slot is being redistributed, and (b) Melaka PRN/electoral positioning is activating. These are the highest-priority targets for the next cycle.

---

## 5. Collection Limitations & Honest Reporting

- **Search backend weakness:** The configured web_search backend returned large volumes of irrelevant results for Malaysian-political queries (token collisions on "AB", "Akmal", "Rauf", "Ketua"). `site:` operators returned empty. Productive yield came from generic first-batch queries + direct `web_extract` of discovered article URLs. This is a **structural collection limitation** that should be flagged to the Director.
- **Kosmo.com.my anti-bot:** Direct scraping of Kosmo's very recent (Aug 2-4, 2026) articles failed with `document_antibot`. The 4 secondary references (S1–S4) are cited from the sidebars of *successfully* scraped primary articles (The Star, Kosmo Feb 5), with attribution and dates. They are marked **unverified** and should be re-attempted next cycle via Google cache / archive.org / alternative Malay-language search.
- **PIR-07 remains weak:** No direct Merlimau grassroots / Youth-campaign-on-the-ground data was obtainable this cycle (backend does not surface constituency-level Malay-language reporting). Flagged in suggestions.
- **No fabricated content:** All article content is from real `web_extract` retrieval. Secondary sidebar references are explicitly labelled unverified. No synthetic data was introduced.

---

## 6. Files Produced This Cycle

| Path | Type |
|------|------|
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/PIR01-bncomms-abrauf-governance-maim-mcorp-20260421.md` | Raw scrape (A1) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/PIR01-mykmu-abrauf-kampung-digital-governance-20260421.md` | Raw scrape (A2) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/PIR02-star-akmal-fight-dap-not-chinese-20260726.md` | Raw scrape (A3) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/PIR02-08-kosmo-akmal-resigns-exco-20260205.md` | Raw scrape (A4) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/PIR02-nst-akmal-not-anti-chinese-keluar-sekejap-20260212.md` | Raw scrape (A5) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/PIR08-malaymail-akmal-zahid-muafakat-nasional-20260109.md` | Raw scrape (A6) |
| `04-DATA-AND-SOURCES/scratch/cj-mlk-01-cycle-20260805-0017-metadata.json` | Scratch metadata |
| `07-AUDIT/top3-mlk-suggestions-CJMLK01.md` | Auto-approved suggestions (next cycle) |
| `01-DAILY-INTELLIGENCE/cj-mlk-01-executive-leadership-20260805-0017MYT.md` | This report |

---

## TOP 3 PIR SUGGESTIONS FOR NEXT CYCLE (AUTO-APPROVED)

> These 3 suggestions have been written to `07-AUDIT/top3-mlk-suggestions-CJMLK01.md` for auto-incorporation into the next CJ-MLK-01 cycle.

### Suggestion 1: Melaka State Administration Reshuffle & EXCO Reallocation (Aug 2026)
**Text:** Investigate the fresh Melaka state administration reshuffle signalled by very recent (Aug 2-4, 2026) reports — "3 Exco BN dijangka kekal dalam pentadbiran baharu" (Kosmo, 4 Ogos 2026) and "Ab. Rauf pertahan kemenangan BN" (Kosmo, 2 Ogos 2026). Determine which EXCO portfolios were reallocated after Akmal's Jan resignation, whether Ab Rauf consolidated portfolios, and what this signals for his autonomy vs federal direction.
**Rationale:** Freshest signals (1-3 days old); directly address PIR-01 (governance agenda) and PIR-06 (portfolio-selection autonomy). Kosmo sidebar refs could not be directly scraped (anti-bot) — next cycle must recover full text via Google cache / archive.org / Malay-language search. A reshuffle is a concrete governance-decision data point currently missing.
**Search Queries:**
1. `Ab Rauf Yusoh EXCO Melaka baharu 2026 timbalan exco pelantikan`
2. `Melaka pentadbiran baharu Ogos 2026 exco kekal jawatan`
3. `site:kosmo.com.my OR site:hmetro.com.my "Exco" Melaka 2026 baharu Ab Rauf`

### Suggestion 2: Akmal's KK Mart Boycott Campaign — Measurable Electoral & Commercial Impact
**Text:** Collect evidence on the measurable impact of Dr Akmal's KK Mart boycott campaign (triggered by the 'Allah' socks incident) on (a) KK Mart commercial performance, (b) Malay-Muslim consumer sentiment, and (c) BN's multiracial electoral positioning. The NST article named the socks issue as a core Akmal "defense" trigger, but no impact metrics have been collected.
**Rationale:** PIR-02 explicitly requires *measurable impact* on BN/UMNO's national electoral positioning and multiracial appeal. Current cycle captured the *rhetoric* and *doctrine* (3R red lines, DAP-chauvinist-DNA, "defend not attack") but NOT the *impact*. The KK Mart boycott is the flagship campaign and the most tractable to measure (commercial data + sentiment). Highest-value gap to close for the Critical PIR-02.
**Search Queries:**
1. `KK Mart boycott Akmal Saleh impact sales Muslim 2026`
2. `Akmal UMNO Youth KK Mart kaus kaki Allah boikot kesan`
3. `Akmal Saleh boycott campaign multiracial BN electoral DAP Chinese reaction 2026`

### Suggestion 3: Ab Rauf Yusoh — Direct Relationship with Zahid Hamidi & Tok Mat (Federal-State Autonomy)
**Text:** Obtain direct evidence on Ab Rauf Yusoh's relationship with federal UMNO leadership — President Ahmad Zahid Hamidi and DPM/"Tok Mat" Mohamad Hasan — and the degree of autonomy he exercises in state-level candidate and political decisions. Current cycle found only indirect proxies (Akmal's resignation routed through Ab Rauf; sidebar "Melaka BN retain incumbents"). No direct Ab Rauf–Zahid or Ab Rauf–Tok Mat interaction has been documented.
**Rationale:** PIR-06 (HIGH) is the most under-resolved PIR after this cycle (status: Open, confidence: MEDIUM). Ab Rauf's autonomy in candidate selection is the core requirement and is currently inferred, not evidenced. The "Melaka BN likely to retain most incumbents" (Star, ~25 Jul 2026) signal suggests Ab Rauf controls the incumbent list — but whether that reflects federal deference or Ab Rauf's independent power is unknown. Essential before the next state polls.
**Search Queries:**
1. `Ab Rauf Yusoh Zahid Hamidi Mesyuarat Tertinggi UMNO calon Melaka`
2. `Ab Rauf Yusoh Tok Mat Hasan Melaka BN perhubungan negeri 2026`
3. `"Ab Rauf" Melaka calon PRN 2026 kekal penyandang UMNO perhubungan`

---

*End of CJ-MLK-01 report — Cycle 2026-08-05 00:17 MYT*
