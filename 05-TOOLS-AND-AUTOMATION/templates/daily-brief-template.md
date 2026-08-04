# PRN Melaka POI — Intelligence Brief Template
## STANDARD FORMAT (all phases)

**Effective:** 2026-08-04  
**Applies to:** All Daily Intelligence Briefs for PRN Melaka POI Workstream  
**Cronjob:** CJ-MLK-05 — Daily Brief & PIR Tracker

---

## FILENAME CONVENTION

```
PRN-MLK-{PHASE}-YYYYMMDD.md
```

| Phase | Pattern | Example | Schedule |
|-------|---------|---------|----------|
| Pre-Campaign | `PRN-MLK-PRE-YYYYMMDD.md` | `PRN-MLK-PRE-20260804.md` | Daily 04:00 MYT |
| Campaign Period | `PRN-MLK-CAMPAIGN-YYYYMMDD.md` | `PRN-MLK-CAMPAIGN-20260824.md` | Daily 04:00 MYT |

---

## STANDARD HEADER BLOCK (mandatory)

```markdown
# PRN Melaka POI — Intelligence Brief
## {Phase} | Day {N} | TLP:AMBER

**Brief ID:** {FILENAME without .md}
**Generated:** YYYY-MM-DD HH:MM +08
**Classification:** TLP:AMBER — For official use only, distribution controlled
**Phase:** {Pre-Campaign | Campaign Period}
**POIs Tracked:** 20 (expanded roster)
**PIRs Active:** 30 (9 Critical, 12 High, 6 Medium)
**Distribution:** Head of Intelligence

---
```

---

## STANDARD SECTION STRUCTURE

### 1. EXECUTIVE SUMMARY (3-5 bullets)
- Top developments in last 24h
- PIR status changes (new evidence, resolved, escalated)
- Threats and opportunities flagged

### 2. PIR STATUS TRACKER
For each PIR, report:
- PIR ID and name
- Status: 🟢 Updated | 🟡 Stale | 🔴 No Data
- Last collection date
- Key finding (1 line)
- Priority change (if any)

Group by priority:
```
#### CRITICAL (9 PIRs)
- PIR-01 [🟢] Ab Rauf Governance — [finding]
- PIR-02 [🟢] Akmal Rhetoric — [finding]
- PIR-03 [🟡] Adly Defence Portfolio — [finding]
- PIR-04 [🟢] Mas Ermieyati PAC — [finding]
- PIR-05 [🟢] Coalition Seat Negotiation — [finding]
- PIR-18 [🔴] PN Opposition Strategy — [NO DATA]
- PIR-27 [🟢] Marginal Seat Defense — [finding]
- PIR-28 [🟡] Coalition Fracture Risk — [finding]
- PIR-30 [🟢] PRN Timing Readiness — [finding]

#### HIGH (12 PIRs)
- PIR-06 through PIR-26 (as applicable)

#### MEDIUM (6 PIRs)
- PIR-12 through PIR-24 (as applicable)
```

### 3. POI ACTIVITY LOG
Table of POI activities detected in last 24h:
- POI Name | Activity | Source | PIR Linkage | Sentiment

### 4. CONSTITUENCY INTELLIGENCE
- Marginal seat watch (N02, N15, N21, N24, N26)
- DUN-level developments
- Parliamentary seat updates

### 5. SENTIMENT SUMMARY
- Aggregate sentiment from CJ-MLK-08
- Notable sentiment shifts
- Social media ecosystem updates (PIR-29)

### 6. DATA QUALITY & GAPS
- Missing data fields
- Collection gaps
- Source reliability issues

### 7. TOP 3 SUGGESTIONS (for approval)
1. [Suggested action based on findings]
2. [Suggested action]
3. [Suggested action]

### 8. NEXT CYCLE PRIORITIES
- Which PIRs need escalation
- Which POIs need deeper collection
- Which constituencies need ground-level intel

---

## OUTPUT PATH
Save to: `01-DAILY-INTELLIGENCE/daily-briefs/PRN-MLK-PRE-YYYYMMDD.md`
