# TOP 3 PIR SUGGESTIONS FOR NEXT CYCLE (AUTO-APPROVED) — CJ-MLK-02

**Cronjob:** CJ-MLK-02 (Defence, Parliament & Federal Portfolios)
**Cycle:** 2026-08-06 01:15 MYT (third cycle)
**Author:** CJ-MLK-02 Collection Agent
**Status:** AUTO-APPROVED by Director protocol — to be incorporated as additional search queries/extractions in the next CJ-MLK-02 cycle.

**Cycle 3 outcome:**
1. ✅ Suggestion 1 (PAC non-LCS PDFs) — PARTIAL: 6 reports + PDF URLs re-confirmed (L1); 5 PDF contents BLOCKED (size limit + HTTP 000).
2. ✅ Suggestion 2 (Adly Melaka-base + LCS response) — RESOLVED (Melaka-base): Adly at Kem Terendak Melaka (8 Apr 2026, L1+L4) + DSA2026 RM3.54B + Azerbaijan bilateral + National Defence Policy talk. Adly LCS/PAC response NOT surfaced (token collision).
3. ✅ Suggestion 3 (Adam Adli Hansard + policy + promotion) — PROGRESS: concrete PTPTN reform output (17 Jun 2026) + cabinet-reshuffle succession + MPP PKR. Hansard NOT obtained (token collision). Direct promotion signal NOT found.

**Keystone finding this cycle:** PIR-03 FULLY RESOLVED — Adly personally officiated IA-ATM at Kem Terendak Melaka (8 Apr 2026, L1 mod.gov.my), closing the cycle-2 Melaka-base agency gap. Combined with RM3.54B DSA2026 contracts (KSU Lokman Hakim = PAC LCS witness present), procurement freeze, Azerbaijan bilateral, and National Defence Policy lecture, Adly's defence agency is now full-spectrum.

**Cross-POI institutional link deepened:** KSU Datuk Lokman Hakim Ali — named as witness in PAC LCS report (DR.22/2026) — was present at the DSA2026 RM3.54B contract signing. The PAC-scrutinised MINDEF leadership is the same leadership signing new procurement.

---

## Suggestion 1: Retry PAC Non-LCS Report PDF Extraction via Alternate Route + Seek Adly's Public Response to the PAC LCS Directive

**Text:** The 5 non-LCS PAC report PDFs (DR.27/23/20/12/9) remain unextracted — the confirmed URLs (docs-323-400.pdf through docs-314-385.pdf) failed both web_extract (size limit) and curl (HTTP 000). The next cycle should: (a) retry extraction via alternate methods — a smaller-chunk PDF text extraction (curl with byte-range `-r 0-1000000`), a headless-browser fetch, or a different network path; (b) if extraction remains blocked, search for *news coverage* of each report's findings (NST/Bharian/Astro Awani typically report PAC report tablings) to obtain the substantive findings at L4 level; (c) the cooking-oil report (DR.27/2026, most recent, 16 Jul) is highest priority as it connects to the documented border working visit. Separately, Adly's public response to the PAC's RM11.22B LCS "no additional funds" directive (DR.22/2026) was not found this cycle due to search token collision — the next cycle should target this via Malay-specific queries and MINDEF news.

**Rationale:** PIR-04's substantive findings layer (agenda → findings) remains the open dimension. The PDF URL pattern is now confirmed (no guessing needed). The LCS-response angle is a fresh cross-POI monitoring item created by the cycle-2 keystone and reinforced by this cycle's procurement-freeze signal.

**Search Queries / Direct Extractions:**
1. Retry: `web_extract` each PDF; or `curl -r 0-1000000` (range-limited) + `pdftotext -f 1 -l 20` (first 20 pages)
2. `PAC DR.27 2026 minyak masak KPDN dapatan` / `PAC DR.23 2026 kenderaan kerajaan MOF` (news-coverage fallback)
3. `PAC DR.20 2026 lapangan terbang MAHB` / `PAC DR.12 2026 insurans kesihatan BNM` / `PAC DR.9 2026 FELCRA sawit`
4. `Adly Zahari respons syor PAC LCS mindef 2026` / `Adly Zahari kapal peronda PAC bajet 2026` (Adly LCS response)
5. Direct extract: `https://www.mod.gov.my` news + `https://www.nst.com.my` for PAC LCS response coverage

---

## Suggestion 2: Adam Adli's 2026 Dewan Rakyat Hansard Contributions + AUKU Memorandum Follow-Through + Direct Ministerial-Promotion Signal (PKR Congress 15-16 Aug Melaka)

**Text:** Adam Adli's concrete PTPTN reform output (17 Jun 2026) is captured, but PIR-11 still lacks his *specific 2026 parliamentary performance* (Dewan Rakyat questions answered, speeches) and the *follow-through on the AUKU memorandum* he received on 9 Feb 2026. The next cycle should: (a) extract the Parliament Hansard for Adam Adli's 2026 contributions — try the parlimen.gov.my oral-questions/Hansard search via direct URL navigation (MP profile id=4176 may link to contributions) or search via `soalan jawab lisan parlimen 2026 pengajian tinggi timbalan menteri`; (b) seek any formal MOHE response to the AUKU abolition memorandum (the ministry said "no full abolition" — has Adam Adli's deputy posture produced any amendment or policy shift since Feb 2026?); (c) monitor for a direct ministerial-promotion signal — PKR National Congress is scheduled 15-16 Aug 2026 in Melaka (CVS-MLK-166), which is a high-probability window for leadership/promotion signals and is itself a Melaka-relevant event.

**Rationale:** PIR-11's parliamentary-performance and promotion-signal dimensions remain open. The PKR Congress (15-16 Aug, Melaka) is both a promotion-signal window and a Melaka-nexus event — doubly relevant to this workspace. It is also time-sensitive (9-10 days from this collection).

**Search Queries / Direct Extractions:**
1. `parlimen.gov.my` Hansard/oral-questions for "Timbalan Menteri Pendidikan Tinggi" 2026 (navigate MP profile id=4176)
2. `Adam Adli AUKU memorandum respons 2026 pindaan` / `KPT AUKU pindaan 2026 Adam Adli` (AUKU follow-through)
3. `Kongres Nasional PKR 2026 Melaka Adam Adli` / `rombakan kabinet 2026 Ogos PKR menteri` (promotion signal + PKR Congress)
4. Direct extract: `https://www.mohe.gov.my` news for Adam Adli statements/programme launches
5. Monitor PKR Congress 15-16 Aug 2026 Melaka outcomes

---

## Suggestion 3: Mas Ermieyati's Post-BERSATU-Suspension Political Trajectory + PAC's Forward Agenda (Post-LCS + Special Sitting 11 Aug)

**Text:** Mas Ermieyati's BERSATU suspension (2 terms/6 years, March 2026) is verified, and her PAC chair status is confirmed (L1, despite suspension). But two forward-looking dimensions of PIR-04 are unmonitored: (a) her *political trajectory post-suspension* — does she remain with BERSATU/PN, defect (WAWASAN was flagged in CJ-MLK-03 as a possible destination), go independent, or align with another force? Her Ketua Srikandi BERSATU role was stripped; her next political move affects the PAC chair's political standing and the cross-POI oversight architecture; (b) the PAC's *forward agenda* post-LCS — the 6 reports are tabled, but is the PAC opening new probes, scheduling follow-up proceedings, or issuing further directives to MINDEF (especially given the procurement-freeze signal)? The special Dewan Rakyat sitting (11 Aug 2026, CVS-MLK-084) may table new PAC business.

**Rationale:** PIR-04's *agenda* is answered; the *forward trajectory* (Mas Ermieyati's political future + PAC's next moves) is the live monitoring layer. Her post-suspension political move is time-sensitive and affects the cross-POI oversight architecture (PAC chair scrutinising MINDEF). The 11 Aug special sitting is 5 days from collection.

**Search Queries / Direct Extractions:**
1. `Mas Ermieyati Samsudin 2026 Ogos politik` / `Mas Ermieyati WAWASAN OR PN OR bebas 2026` (political trajectory)
2. `PAC Parlimen 2026 Ogos prosiding baru` / `jawatankuasa kira wang sidang khas Ogos 2026` (forward agenda)
3. `Mas Ermieyati Srikandi BERSATU jawatan 2026` (stripped-role confirmation)
4. Monitor special Dewan Rakyat sitting 11 Aug 2026 for PAC business
5. `PAC MINDEF LCS pemantauan 2026 Ogos` (follow-up LCS monitoring)

---

*End of auto-approved suggestions for CJ-MLK-02 cycle 4 — to be consumed by next CJ-MLK-02 cycle.*
