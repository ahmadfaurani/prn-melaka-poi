# CVS Adapter — PRN Melaka 2026

**Classification:** TLP:AMBER  
**Created:** 2026-08-04  
**Master Framework:** `/home/p62operator/.openclaw/workspace/03-VERIFICATION/CVS-FRAMEWORK.md`

---

## Workstream: MLK
**Claim ID Format:** `CVS-MLK-NNN`

## Domain
Election Intelligence — PRN Melaka 2026

## Domain-Specific Rules

### SPR Official Data
All SPR/EC official data (candidate lists, results, election writ) is automatically **T1 — Verified Fact**. Confidence score minimum 8 (L1 source override). No cross-check required.

### Party Announcements
Official party statements from Sec-Gen or President are **T1** for the fact that the statement was made. The content of the statement is **T2** until independently verified.

### Social Media
- Verified accounts of named politicians: **T2** for statements made
- Party official accounts: **T2** for announcements
- Unverified accounts: **T6 (Rejected)** unless corroborated by L4 or above

### WhatsApp / Rumour
All WhatsApp forwards, anonymous tips, and unattributed claims are **T6 (Rejected)**. Logged in evidence register for trend tracking only. Never included in intelligence products.

### Analytical Assessments
Seat vulnerability assessments, swing projections, and electoral analysis → **T3 (Analytical Interpretation)**. Label as `[ASSESSMENT]`. Never present as fact.

## Domain Sources
- SPR (L1) — spr.gov.my
- Melaka State Government (L1) — melaka.gov.my
- Mainstream media (L4): Sinar Harian, The Star, NST, Astro Awani, Bernama, Utusan, Bharian, Kosmo!, mStar
- Independent media (L4): Malaysiakini, FMT, MalaysiaNow
- Party official social media (L4): verified accounts
- Unverified social media (L5): T6 unless corroborated

## Melaka-Specific Notes
- 28 DUN constituencies
- Historical three-cornered fights (PH vs BN vs PN) common since 2023
- State government composition as baseline for vulnerability assessment

---

**Classification:** TLP:AMBER
