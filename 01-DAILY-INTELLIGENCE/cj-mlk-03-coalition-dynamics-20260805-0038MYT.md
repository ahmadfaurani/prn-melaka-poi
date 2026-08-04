# CJ-MLK-03 — Coalition Dynamics & Electoral Strategy Collection Report

**Workstream:** PRN Melaka — Person of Interest (POI) Intelligence
**Cronjob:** CJ-MLK-03 (Coalition Dynamics & Electoral Strategy)
**POIs of Interest:** Cross-cutting — all 9 POIs (Ab Rauf, Akmal, Adly, Mas Ermieyati, Adam Adli + others)
**PIRs Addressed:** PIR-POI-MLK-05 (CRITICAL — Coalition Seat Negotiation & Electoral Strategy) · PIR-POI-MLK-09 (HIGH — Mas Ermieyati / PN-Bersatu Electoral Strategy) · PIR-POI-MLK-10 (HIGH — Adly Zahari / PH-Amanah Coalition Positioning)
**Collection Timestamp:** 2026-08-05 00:38 MYT (UTC+8)
**Cycle:** First collection cycle (no prior `07-AUDIT/top3-mlk-suggestions-CJMLK03.md` existed; sibling cycles CJ-MLK-01/02 context consumed)
**Classification:** TLP:AMBER
**Collector:** CJ-MLK-03 Collection Agent (zai-org/GLM-5.2)

---

## 1. Collection Summary

This is the inaugural CJ-MLK-03 cycle. **10 web_search queries** were executed; as documented across the parallel CJ-MLK-01 and CJ-MLK-02 cycles, the configured search backend **structurally fails** to index Malaysian political content — this cycle's queries returned Ubuntu download pages, casino spam, porn, and travel/tourism results. Zero relevant Malaysian news was surfaced via search. (The one useful search result — the Perikatan Nasional Wikipedia disambiguation — was used as a seed URL.)

**Productive intelligence came ENTIRELY from direct `web_extract` of pre-identified high-value URLs** — primarily Wikipedia (EN + BM) election/coalition/leader pages — supplemented by context from the sibling cycles. **12 primary sources** were extracted and saved as raw scrapes. The single most important source — the **2026 Malacca state election Wikipedia page** — directly addresses the core PIR-05 requirement (the next PRN) and was not previously captured by any cycle.

**Key thematic finding:** The Melaka PRN is **1-3 months away** (due on/before Nov 2026, possibly Sep; CM disclosed a 120-day window on 17 May 2026). The Melaka state BN-PH coalition government **collapsed in July 2026** (PH withdrew over a BN+PN constitutional amendment creating 7 unelected seats, passed 23-5, defying PM Anwar). Nationally, an **informal BN-PAS pact** — analysts call it "similar to former Muafakat Nasional alliance" — has delivered BN landslide wins in Johor (11 Jul, 48/56) and Negeri Sembilan (1 Aug, 25/36), while **BERSATU was wiped out in three consecutive state elections** (Sabah Nov 2025, Johor Jul 2026, NS Aug 2026) and **PAS cut ties with BERSATU (8-9 June 2026)**. This is the de facto reactivation of the UMNO-PAS (Muafakat) alignment that Dr Akmal Saleh has advocated — achieved *informally* despite UMNO President Zahid's rejection of the *formal* revival. A new entrant, **BERSAMA (Rafizi Ramli's party)**, is targeting the Melaka PRN. The next state election will be a **four-way contest**: BN(+PAS informal) vs PH(DAP-led, weakened) vs BERSATU(moribund, isolated in PN) vs BERSAMA(new reformist, vote-splitter risk).

Raw scrapes saved to `04-DATA-AND-SOURCES/raw-scrapes/20260805/`. Scratch metadata saved to `04-DATA-AND-SOURCES/scratch/cj-mlk-03-cycle-20260805-0038-metadata.json`. Auto-approved suggestions written to `07-AUDIT/top3-mlk-suggestions-CJMLK03.md`.

---

## 2. Findings Table

| # | Source | Date | Summary | PIR | Confidence | Tag |
|---|--------|------|---------|-----|------------|-----|
| A1 | Wikipedia EN — 2026 Malacca state election | live (PRN due ≤Nov 2026) | **★ KEYSTONE.** Next PRN: 28 seats, majority 15. Current assembly: **BN 20 (UMNO 17, MCA 2, MIC 1), PH 5 (DAP 4, AMANAH 1), PN 3 (BERSATU 1, PAS 1, WAWASAN 1)**. **PH withdrew from state govt 14-16 Jul 2026** over a 7-unelected-seats constitutional amendment passed 23-5 (BN+PN vs PH), defying Anwar. CM disclosed 120-day window (17 May). Bersama targeting this election (15 Jul). All 28 incumbents (N01-N24 captured). | PIR-05/10/09 | HIGH | CRITICAL |
| A2 | Wikipedia EN — 2026 Negeri Sembilan state election | 1 Aug 2026 | **KEYSTONE.** BN+PN informal pact won **25/36 (two-thirds)**; BN 18 (UMNO 16, MCA 2), PN 7 (PAS 4, WAWASAN 3), **BERSATU solo 0**; PH 11 (DAP 9, PKR 2, AMANAH 0). Tok Mat (Mohamad Hasan) led BN. PAS cut ties with BERSATU 9 Jun 2026. Bersama withdrew "to focus on Malacca election." | PIR-05/09/10 | HIGH | CRITICAL |
| A3 | Wikipedia EN — 2026 Johor state election | 11 Jul 2026 | **BN 48/56 landslide (supermajority)**, best since 2008; PN 0 (wiped out); PH 8 (DAP 6, AMANAH 1, PKR 1). PAS lost all Johor assembly seats since 2004. **Informal BN-PAS pact: Tuan Ibrahim (PAS) urged vote BN; Hadi said "don't vote PH"; "similar to former Muafakat Nasional."** BERSAMA debut 0 (rejected coalition talks). Non-Malay shift away from PH/DAP. | PIR-05/10 | HIGH | CRITICAL |
| A4 | Wikipedia EN — Perikatan Nasional (PN) | live | PN = 2nd largest coalition, 68/222 MPs (Malacca: 3 MPs). **Chairman: Samsuri (PAS)** since 22 Feb 2026. **★ PAS broke political cooperation with BERSATU 8 Jun 2026** (both remain in PN). WAWASAN (Hamzah) formed 13 Jun 2026, 6 MPs. PAS dominates all PN leadership posts (chairman, sec-gen Takiyuddin, elections director Sanusi, youth chief). | PIR-05/09 | HIGH | CRITICAL |
| A5 | Wikipedia EN — Muafakat Nasional (MN) | live | UMNO-PAS pact (2019), **dissolved as coalition 15 Dec 2022 → NGO**. Five-point charter signed by Hadi (PAS) + Zahid (UMNO). BERSATU historically excluded (contested UMNO in 2020 Sabah). **Malacca MN chairman = Muhammad Jailani Khamis** (now PN-PAS ADUN Rembia). Akmal's "revive MN" proposal = reactivate this NGO-era cooperation. | PIR-05 | HIGH | CRITICAL |
| A6 | Wikipedia EN — 2021 Malacca state election | 20 Nov 2021 | **Baseline:** BN 21 (two-thirds), PH 5 (DAP 4, AMANAH 1, PKR 0), PN 2 (BERSATU 2). BN+PN (govt partners) competed against each other. Mas Ermieyati lost Tanjung Bidara to Ab Rauf (was PN's CM candidate). BN won Masjid Tanah (54.65%) & Alor Gajah (45.29%) federally. | PIR-05/09 | HIGH | CRITICAL |
| A7 | Wikipedia EN — BERSATU | live | 19 MPs (1 Malacca — Mas Ermieyati/Masjid Tanah). **Wiped out in Sabah (Nov 2025), Johor (2026), NS (2026)**; lost 4 consecutive by-elections. "Malay vote split between UMNO and PAS, BERSATU unable to establish clear identity." Women's Chief = Nolee Ashilin (≠ Mas Ermieyati's Srikandi chief post). Previously partnered Malacca state govt (ended). | PIR-09 | HIGH | HIGH |
| A8 | Wikipedia EN — Ahmad Samsuri Mokhtar | live | PN Chairman (PAS, since 22 Feb 2026); MB Terengganu; MP Kemaman. **★ 18th Opposition Leader: 16 May–13 Jun 2026 = 28 days, shortest ever** (never attended parliament). Removal announced live by Hadi. Tenure ended days before PAS-BERSATU break (8-9 Jun). Resolves CJ-MLK-02 "Hamzah→Samsuri→Hamzah" query. | PIR-09/05 | HIGH | HIGH |
| A9 | Wikipedia BM — Perikatan Nasional | live | Corroborates EN: Samsuri (PAS) chairman, Takiyuddin (PAS) sec-gen, Sanusi (PAS) elections director. **Ketua Pembangkang = Hamzah Zainudin (WAWASAN)** — confirms Hamzah holds Opposition Leader (parliament) while Samsuri holds PN chairmanship (party). Current slogan "BERSATU, BERGERAK, SE-MALAYSIA" (since 21 Mar 2025). | PIR-05/09 | HIGH | HIGH |
| A10 | Wikipedia EN — 2025 Sabah state election | 29 Nov 2025 | Hung assembly; GRS 29, WARISAN 25, BN 6, **PH 1 (-5)**, PN 1. PH collapse precedent; DAP lost all contested seats (cited as Johor precedent). BN weak in East Malaysia but resurgent in Peninsula. GRS-PH electoral pact = example of cross-coalition seat negotiation. | PIR-05/10 | HIGH | HIGH (context) |
| A11 | Wikipedia EN — Rafizi Ramli | live | Former Economy Minister + PKR deputy president; **lost to Nurul Izzah 2025 (9,803 vs 3,866)**; founded BERSAMA 2026; debut Johor 0 seats; **targeting Melaka PRN (15 Jul statement)**; rejected coalition talks → vote-splitter risk. | PIR-05 | HIGH | HIGH |
| C1 | Malay Mail — Melaka tag (404) + sidebar | 4 Aug 2026 | Melaka tag 404. Sidebar confirms: **DAP putting gov role to vote** (CEC); **Anthony Loke resigned NS DAP chief** after defeat (22-yr tenure), stays sec-gen. Unity-govt strain signals. | PIR-05/10 | MEDIUM | HIGH (context) |

---

## 3. PIR Resolution Status

| PIR ID | Status | New Evidence | Confidence |
|--------|--------|--------------|------------|
| **PIR-POI-MLK-05** (Cross-POI — Coalition Seat Negotiation & Electoral Strategy) [CRITICAL] | **Substantially RESOLVED (structure/dynamics); Open (specific seat allocations)** | **MASSIVELY advanced.** (1) **PRN timing**: due ≤Nov 2026, possibly Sep; 120-day window disclosed 17 May 2026. (2) **Current assembly**: BN 20 / PH 5 / PN 3 (split BERSATU 1, PAS 1, WAWASAN 1). (3) **Melaka BN-PH state coalition collapsed** (PH withdrew 14-16 Jul 2026 over 7-unelected-seats amendment, 23-5, defying Anwar). (4) **Informal BN-PAS pact** (de facto Muafakat reactivation) won Johor 48/56 + NS 25/36; PAS publicly directs votes to BN. (5) **PAS-BERSATU break** (8-9 Jun 2026). (6) **BERSAMA (Rafizi)** targeting Melaka, rejected coalition talks. (7) 2021 baseline (BN 21/PH 5/PN 2). (8) All 28 incumbents (partial). **Gap**: specific seat allocations/candidate lists for the imminent PRN not yet published (election 1-3 months away). | HIGH (structure) / OPEN (allocations) |
| **PIR-POI-MLK-09** (Mas Ermieyati — PN/Bersatu Electoral Strategy) [HIGH] | **Partial → Advanced (strategy context); Open (her personal status)** | **Strongly advanced.** BERSATU in **electoral freefall** (wiped out Sabah Nov 2025, Johor Jul 2026, NS Aug 2026; lost 4 by-elections). **PAS cut ties with BERSATU** (8-9 Jun 2026) — PAS chose UMNO over BERSATU. **PN electoral machine is PAS-run** (chairman Samsuri, elections director Sanusi, sec-gen Takiyuddin — all PAS). BERSATU holds only **1 of PN's 3 Melaka state seats** (Sungai Udang); PN Melaka chief = Radzi Jidin (BERSATU), "not contested." Mas Ermieyati = BERSATU's sole Malacca MP (Masjid Tanah); lost Tanjung Bidara to Ab Rauf 2021. **PN's viable path in Melaka = PAS-backed, BERSATU-marginalised.** **Gap**: Mas Ermieyati's personal 2026 status (the unverified BERSATU-membership-suspension signal from CJ-MLK-02 was NOT corroborated by the BERSATU page this cycle); her specific candidacy plans for Masjid Tanah/state seat. | HIGH (party context) / OPEN (personal status) |
| **PIR-POI-MLK-10** (Adly Zahari — PH/Amanah Coalition Positioning) [HIGH] | **Partial → Advanced (positioning documented); Open (electoral trajectory)** | **Advanced.** Adly = **PH state chief since Aug 2017**, sole AMANAH MLA (Bukit Katil, N17). **He led PH's withdrawal from the Melaka state government (16 Jul 2026), defying PM Anwar's plea** — a concrete, dated assertion of state-PH autonomy, but it leaves PH (5 seats, DAP-heavy) isolated against the 23-strong BN+PN bloc. AMANAH electorally marginal (0 in NS 2026, 1 in Melaka 2021); PH's only reliable Melaka engine is DAP (4 urban seats). **PH/DAP national strain** (DAP putting gov role to vote; Loke resigned NS chair). Adly's coalition positioning is in a weakened, DAP-dependent PH now in state opposition. **Gap**: Adly's specific PRN candidacy/campaign; AMANAH's seat-negotiation stance with DAP/PKR/BERSAMA. | HIGH (positioning) / OPEN (campaign) |

---

## 4. Analytical Synthesis

### 4.1 The Melaka PRN is Imminent and the Coalition Map has been Rewritten (PIR-05)

The single most important deliverable of this cycle is establishing that the **Melaka state election is 1-3 months away** (due ≤Nov 2026, possibly Sep; 120-day window disclosed 17 May 2026) AND that the coalition configuration has fundamentally changed since 2021:

- **The Melaka BN-PH state government coalition has collapsed.** In July 2026, PH withdrew from the BN-led state administration it had joined in 2023 (to mirror the federal unity government). The trigger was a BN+PN constitutional amendment (14 Jul) creating **7 unelected assembly seats**, passed 23-5 (all 21 BN + 2 PN vs all 5 PH). DAP withdrew immediately; Adly Zahari (PH state chief) initially stayed then rejoined the PH withdrawal on 16 July, **overriding PM Anwar Ibrahim's plea to defer** (Star, 16 Jul 2026). The next PRN will therefore be contested with **PH in opposition**, not in coalition with BN.

- **The 7-unelected-seats amendment is a coalition-engineering tool.** With 23 elected BN+PN votes + 7 appointable seats, the BN+PN bloc can command up to 30 of 35 (expanded) seats regardless of the elected result — a structural lock-in that marginalises PH (5 elected) and entrenches the BN+PN working relationship. This is the most consequential governance/coalition development in Melaka this year.

- **PN's Melaka presence is now split across all three substantive components.** The 2021 result (PN 2, both BERSATU) has become PN 3: BERSATU 1 (Sungai Udang), PAS 1 (Rembia — Muhammad Jailani Khamis), WAWASAN 1 (likely Bemban). This state-level split mirrors the federal PAS-BERSATU realignment and means BERSATU's Melaka legislative footprint has *shrunk* from 2 to 1 even as PN grew.

### 4.2 The De Facto Muafakat Nasional Reactivation (PIR-05 / cross-ref PIR-02)

CJ-MLK-01 established the **Akmal-Zahid split**: Akmal proposed UMNO exit the unity government and revive Muafakat Nasional (UMNO-PAS) cooperation; Zahid rejected both. This cycle establishes that the **UMNO-PAS cooperation has been reactivated *informally*** regardless of Zahid's formal rejection:

- **Johor (11 Jul 2026):** BN 48/56 landslide; PN wiped out; but **PAS Deputy President Tuan Ibrahim publicly urged supporters to vote BN in non-PN seats**, and PAS President Hadi Awang said "don't vote PH." Analysts explicitly describe this as "potentially leading to informal pact similar to former Muafakat Nasional alliance."
- **Negeri Sembilan (1 Aug 2026):** BN+PN informal pact won 25/36 (two-thirds); the winning PN seats were **PAS 4 + WAWASAN 3 — BERSATU (contesting solo) won 0.** The MB-designate was sworn in 2 Aug 2026.
- **Muafakat Nasional is an NGO** (since 15 Dec 2022); its Malacca chairman, **Muhammad Jailani Khamis, is now a PN-PAS ADUN (Rembia)** — a single individual straddling the MN NGO structure and a sitting PN-PAS seat. This is a person-level UMNO-PAS realignment nexus.

The electoral arithmetic is now clear: the viable Malay-Muslim opposition/right bloc is **UMNO + PAS (+ WAWASAN)**, with BERSATU excluded. This is, in substance, Akmal's Muafakat vision — achieved *de facto* at state level even as Zahid blocks it *formally* at federal level. The next Melaka PRN will almost certainly replicate the Johor/NS template: BN dominant, PAS tactically backing BN in Malay seats, BERSATU marginalised.

### 4.3 BERSATU's Electoral Freefall and Mas Ermieyati's Precarious Position (PIR-09)

The BERSATU page and the three state-election results establish a consistent, damning pattern:

- **BERSATU wiped out in Sabah (Nov 2025), Johor (Jul 2026), NS (Aug 2026)** — three consecutive state elections with zero seats.
- **Lost 4 consecutive by-elections** (Pulai, Kuala Kubu Baharu, Nenggiri, Mahkota).
- "The Malay vote remained mostly split between UMNO and PAS, with Bersatu unable to establish a clear identity."
- **PAS cut political cooperation with BERSATU (8-9 June 2026)** — PAS chose UMNO over BERSATU after BERSATU assemblymen withdrew support for UMNO in the NS crisis.

For **Mas Ermieyati Samsudin** (Ketua Srikandi BERSATU, MP Masjid Tanah, PAC Chair): she sits atop a party in existential electoral decline. BERSATU holds **1 of PN's 3 Melaka state seats** and **1 of Malacca's 6 MP seats** (hers). The PN electoral machine is **PAS-run** (chairman Samsuri, elections director Sanusi — both PAS MBs). Her Masjid Tanah federal seat — won in the BN-favourable 2021 baseline (BN took Masjid Tanah parliamentary with 54.65%) — is now electorally imperilled: BERSATU cannot win on its own, PAS has severed cooperation, and the winning Melaka formula is BN(+PAS). Her viable paths are narrowing to: (a) contest under a PAS-directed PN ticket as a BERSATU figurehead (electorally weak), or (b) defection/accommodation. The **unverified BERSATU-membership-suspension signal** (EN-Wikipedia, CJ-MLK-02) was **NOT corroborated** by the BERSATU page this cycle — it remains an open, high-priority verification target.

### 4.4 Adly Zahari's Autonomy Assertion and PH's Structural Weakness (PIR-10)

Adly Zahari's leadership test this cycle is sharply defined: he **led PH's withdrawal from the Melaka state government on 16 July 2026, defying PM Anwar's plea** — a concrete, dated assertion of state-PH autonomy. But this assertion of principle leaves PH electorally exposed:

- PH holds **5 state seats: 4 DAP (urban) + 1 AMANAH (Adly's Bukit Katil)**. AMANAH's Melaka legislative presence is *entirely* Adly's single seat.
- AMANAH won **0 seats in NS (2026)** and 1 in Melaka (2021) — the party is electorally marginal nationwide at state level.
- **PH/DAP national support is collapsing**: non-Malay voters shifted to MCA/MIC in Johor (DAP -4) and Sabah (DAP lost all); the Johor analysis attributes this to "slow pace of national reforms under PH-led federal government." If this trend reaches Melaka, even DAP's 4 urban seats (Ayer Keroh, Kesidang, Kota Laksamana, Bandar Hilir) are at risk.
- **DAP is questioning its own government role** (CEC putting participation to a vote, 4 Aug 2026) and Anthony Loke resigned as NS DAP chief — the PH coalition is under internal strain at the very moment Adly needs a united front.

Adly's coalition positioning is therefore in a **weakened, DAP-dependent PH now in state opposition**, leading a party (AMANAH) with a near-zero state electoral base, against a 23-strong BN+PN bloc backed by an informal UMNO-PAS pact. His autonomy assertion is morally notable but electorally precarious.

### 4.5 BERSAMA — The Fourth Force and the Vote-Splitter Risk (PIR-05)

A new entrant reshapes the Melaka arithmetic. **BERSAMA (Malaysian United Party)**, founded by **Rafizi Ramli** (former Economy Minister, PKR deputy president who lost to Nurul Izzah Anwar in 2025), is **explicitly targeting the Melaka PRN** (Rafizi statement, 15 Jul 2026; Bersama withdrew from NS "to focus on the Malacca election"). Critically, **BERSAMA rejected coalition talks** (per the Johor page). This creates a **four-way contest**:

1. **BN** (+ informal PAS backing) — incumbent, 20 seats, front-runner
2. **PH** (DAP-led, weakened) — 5 seats, now in opposition
3. **BERSATU** (in PN shell, isolated, moribund) — 1 state seat
4. **BERSAMA** (new reformist, Rafizi-led) — 0 seats but resourced, vote-splitter

If BERSAMA contests PH-leaning urban/reformist seats without a pact, it risks **splitting the anti-BN vote** — the very "seat negotiations among opposition parties expected to be critical" flagged for Melaka. Rafizi's break from PKR (and PKR's near-zero Melaka state base, which Adam Adli is rebuilding per CJ-MLK-02) means BERSAMA may also directly compete with PKR in Malay-mixed seats.

### 4.6 The Federal-State Posture Split, Intensified (cross PIR-05 / PIR-02)

CJ-MLK-01 documented a federal/state posture split (Akmal attacks DAP federally but cooperates with a Melaka DAP deputy-exco at state level). This cycle shows that split has *intensified and inverted*:

- **Federally**: BN (Zahid) remains in the unity government with PH (Zahid reaffirmed 30 Apr 2026 during the NS crisis). DAP is now questioning whether to stay (CEC vote, 4 Aug 2026).
- **At Melaka state level**: the BN-PH coalition has **collapsed** (PH withdrew Jul 2026); the next PRN is BN(+PAS) vs PH.
- **At Johor/NS state level**: BN wins *against* PH, with PAS backing.

So BN cooperates with PH federally (under strain) but competes against PH at state level (Johor, NS, now Melaka). This federal/state divergence is the defining structural feature of the coming Melaka PRN and bears directly on Ab Rauf's autonomy (PIR-06, cross-cut) — he runs a state BN that has just shed its PH partner while his federal president (Zahid) remains in cabinet with PH.

### 4.7 The 9 POIs in the Coalition Frame

- **Ab Rauf Yusoh** (PIR-01/06): Incumbent CM (Tanjung Bidara), front-runner; engineered the 7-unequent-seats amendment with PN; shed PH partner. His autonomy vs federal Zahid is now sharper (state BN diverges from federal BN's PH partnership).
- **Dr Akmal Saleh** (PIR-02/07/08): His Muafakat-revival advocacy is vindicated *de facto* by the Johor/NS informal BN-PAS pacts — even as Zahid blocked it *formally*.
- **Adly Zahari** (PIR-10): Led PH's state-govt withdrawal; sole AMANAH MLA; weakened PH.
- **Mas Ermieyati Samsudin** (PIR-09): BERSATU in freefall; party isolated in PAS-run PN; Masjid Tanah seat imperilled.
- **Adam Adli** (PIR-11): Acting PKR Melaka chair rebuilding a near-zero state base; now faces BERSAMA (Rafizi) competition for the reformist-Malay space.
- **Tok Mat / Mohamad Hasan**: Led the NS BN campaign (cross-ref CJ-MLK-01 Suggestion 3) — the federal UMNO elections strategist.
- **Muhyiddin Yassin / Hamzah Zainudin / Samsuri / Sanusi**: PN leadership churn; PAS now runs PN; BERSATU isolated.

---

## 5. Collection Limitations & Honest Reporting

- **Search backend — structural failure (confirmed across THREE cycles):** 10 web_search queries this cycle returned Ubuntu, casino, porn, and travel/tourism results — zero relevant Malaysian political content. Token collisions: "Melaka"→tourism; "PN"→Prurigo Nodularis/Pinterest; "Adly"→Thai casino spam; "Muafakat"/"DUN"→Ubuntu. This is a **confirmed structural limitation** flagged by CJ-MLK-01 and CJ-MLK-02 and re-confirmed here. **Productive intelligence this cycle came ENTIRELY from direct `web_extract` of pre-identified Wikipedia URLs**, not from search. The Director should be aware that *all three Melaka cronjobs* are operating without a functioning news search backend.
- **Wikipedia as primary source:** Because news search is non-functional, this cycle's evidence base is **reference/structural** (Wikipedia coalition/election/leader pages) plus **context** (sibling cycles' news scrapes + Malay Mail sidebar), not **current-event news articles**. The Wikipedia 2026 Malacca/NS/Johor state-election pages are, however, well-maintained and contain dated, specific political events (the Jul 2026 PH withdrawal, the 7-unequent-seats amendment, dated leader changes) — making them high-value despite being encyclopedia pages.
- **Malay Mail Melaka tag = 404:** Unlike a general "Malaysia" feed, Malay Mail does not maintain a Melaka tag. Future Melaka-specific news collection must use the general feed + search (which is non-functional) or direct outlet extraction.
- **Truncation:** The 2026 Malacca state election page extraction truncated at N24 (Bemban); N25-N28 incumbents and any "Analysis/Aftermath" section were not captured. The WAWASAN state seat is inferred (likely Bemban) but not confirmed from the truncated text.
- **Unverified signal NOT corroborated:** The Mas Ermieyati "BERSATU membership suspended since 2026" note (EN-Wikipedia, CJ-MLK-02) was **NOT corroborated** by the BERSATU Wikipedia page this cycle (which details BERSATU's electoral decline but does not mention her suspension). It remains **UNVERIFIED** and is the #1 next-cycle priority.
- **No fabricated content:** All content is from real `web_extract` retrieval. Inferences (e.g., WAWASAN = Bemban) are explicitly labelled as inferences.

---

## 6. Files Produced This Cycle

| Path | Type |
|------|------|
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/PIR05-10-09-wikipedia-2026-malacca-state-election-keystone.md` | Raw scrape (A1 — KEYSTONE) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/PIR05-09-10-wikipedia-2026-ns-state-election-keystone.md` | Raw scrape (A2 — KEYSTONE) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/PIR05-wikipedia-2026-johor-state-election-bnpas-pact.md` | Raw scrape (A3) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/PIR05-09-wikipedia-perikatan-nasional-pn-structure.md` | Raw scrape (A4) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/PIR05-wikipedia-muafakat-nasional-mn-ngo.md` | Raw scrape (A5) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/PIR05-wikipedia-2021-malacca-state-election-baseline.md` | Raw scrape (A6) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/PIR09-wikipedia-bersatu-electoral-freefall.md` | Raw scrape (A7) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/PIR09-wikipedia-samsuri-pn-chairman.md` | Raw scrape (A8) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/PIR05-09-wikipedia-perikatan-nasional-ms.md` | Raw scrape (A9) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/PIR05-10-wikipedia-2025-sabah-state-election-context.md` | Raw scrape (A10) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/PIR05-wikipedia-rafizi-bersama-malacca-focus.md` | Raw scrape (A11) |
| `04-DATA-AND-SOURCES/raw-scrapes/20260805/CONTEXT-malaymail-melaka-tag-20260804.md` | Raw scrape (C1) |
| `04-DATA-AND-SOURCES/scratch/cj-mlk-03-cycle-20260805-0038-metadata.json` | Scratch metadata |
| `07-AUDIT/top3-mlk-suggestions-CJMLK03.md` | Auto-approved suggestions (next cycle) |
| `01-DAILY-INTELLIGENCE/cj-mlk-03-coalition-dynamics-20260805-0038MYT.md` | This report |

---

## TOP 3 PIR SUGGESTIONS FOR NEXT CYCLE (AUTO-APPROVED)

> These 3 suggestions have been written to `07-AUDIT/top3-mlk-suggestions-CJMLK03.md` for auto-incorporation into the next CJ-MLK-03 cycle.

### Suggestion 1: Melaka PRN Candidate Lists & Seat Allocations (the 1-3 month window)
**Text:** With the Melaka PRN now confirmed as imminent (due ≤Nov 2026, possibly Sep; 120-day window disclosed 17 May 2026), the next cycle MUST capture the actual candidate lists and seat allocations as they are announced: BN's incumbent-retention decisions (CJ-MLK-01 sidebar signalled "BN retain most incumbents"), PN's seat split among BERSATU/PAS/WAWASAN (and whether Mas Ermieyati contests Masjid Tanah or a state seat), PH/DAP/AMANAH/PKR seat-sharing (and whether Adly Zahari defends Bukit Katil), and BERSAMA's (Rafizi) contested seats. Also recover the N25-N28 incumbents truncated this cycle and confirm the WAWASAN state seat.
**Rationale:** PIR-05 is RESOLVED on coalition *structure/dynamics* but OPEN on the specific *seat allocations* — which is the core deliverable as the election is 1-3 months away. The 7-unequent-seats amendment (passed 23-5) also needs monitoring for who BN+PN appoints. This is the highest-value gap.
**Search Queries:**
1. `Melaka PRN calon 2026 BN PH PN senarai kawasan` (then extract any Malay-news URL surfaced)
2. `Pilihan raya negeri Melaka 2026 calon dicalonkan kerusi` (Bernama/Utusan/Sinar Harian candidate pages)
3. Direct extract: Election Commission (spr.gov.my) Melaka candidate list + `2026 Malacca state election` Wikipedia re-extraction (recover N25-N28 + candidate section)

### Suggestion 2: VERIFY Mas Ermieyati's 2026 BERSATU Status & Her PRN Candidacy Plan (PIR-09 keystone)
**Text:** The "BERSATU membership suspended since 2026" signal (EN-Wikipedia, CJ-MLK-02) was NOT corroborated by the BERSATU page this cycle — it remains UNVERIFIED and is now urgent given (a) the PAS-BERSATU break (8-9 Jun 2026), (b) BERSATU's electoral freefall, and (c) the imminent Melaka PRN. The next cycle must determine: (a) whether/when BERSATU suspended her membership and why; (b) whether she contests Masjid Tanah (federal) or a state seat in the PRN; (c) whether PN fields a PAS or BERSATU candidate in her Masjid Tanah-area state seats (Tanjung Bidara, held by Ab Rauf). Recovery must use Malay news terms + direct extraction; the web_search backend cannot retrieve her name.
**Rationale:** PIR-09 is advanced on *party context* (BERSATU freefall, PAS-run PN) but OPEN on her *personal status* — which is the foundation of her electoral strategy. A suspended BERSATU leader contesting under a PAS-directed PN, or defecting, would be the defining PIR-09 event of the cycle. Highest-impact unverified signal across both CJ-MLK-02 and CJ-MLK-03.
**Search Queries:**
1. `Mas Ermieyati Samsudin gantung keahlian BERSATU 2026 sebab` (extract any Malay-news URL)
2. `Mas Ermieyati calon PRN Melaka 2026 Masjid Tanah Tanjung Bidara PN PAS`
3. Direct extract: re-check `ms.wikipedia.org/wiki/Mas_Ermieyati_Samsudin` + BERSATU/PN official statements + Malay Mail/Bernama BERSATU tag pages

### Suggestion 3: BERSAMA (Rafizi) Melaka Strategy & the Opposition Seat-Negotiation Dynamics
**Text:** BERSAMA (Rafizi Ramli's new party) is explicitly targeting the Melaka PRN (15 Jul 2026 statement) and has *rejected coalition talks* — creating a four-way contest and a vote-splitter risk. The next cycle must capture: (a) which Melaka seats BERSAMA targets (likely urban/reformist seats overlapping DAP/PKR); (b) whether BERSAMA, PH, and PKR (Adam Adli's acting chair) enter any seat negotiation or remain split; (c) Rafizi's specific Melaka messaging and candidate slate; (d) the impact on PKR's near-zero Melaka state base. Also monitor whether the PH/DAP "government role to vote" (4 Aug 2026) resolves and how it affects PH's Melaka state posture.
**Rationale:** PIR-05 flags "seat negotiations among opposition parties expected to be critical" — BERSAMA is the new variable that determines whether the anti-BN vote unifies or splits. Adam Adli's PKR Melaka chairmanship (CJ-MLK-02) is directly threatened by a BERSAMA challenge to PKR's reformist-Malay space. This is the highest-value *new-development* gap (BERSAMA is a 2026 entrant not in the original POI set but materially shaping the coalition frame).
**Search Queries:**
1. `BERSAMA Rafizi Ramli Melaka calon PRN 2026 kerusi strategi`
2. `Rafizi Ramli Bersama PH DAP PKR perbincangan kerusi Melaka 2026`
3. Direct extract: rafiziramli.com + BERSAMA official site/social + Malay Mail/NST/Bernama "Bersama"/"Rafizi" tag pages + re-extract `2026 Malacca state election` Wikipedia for BERSAMA candidate section

---

*End of CJ-MLK-03 report — Cycle 2026-08-05 00:38 MYT*
