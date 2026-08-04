#!/bin/bash
# MLK Sentiment Analysis Pipeline Script (CJ-MLK-08)
# Scores sentiment in processed entity files → sentiment analysis output
# Run: daily 07:00 MYT by cronjob

set -euo pipefail

WORKSPACE="/home/p62operator/.openclaw/workspace-mlk"
TODAY=$(TZ=Asia/Kuala_Lumpur date '+%Y%m%d')
TIMESTAMP=$(TZ=Asia/Kuala_Lumpur date '+%Y-%m-%d %H:%M %Z')
PROC_DIR="${WORKSPACE}/04-DATA-AND-SOURCES/processed-entities/${TODAY}"
SENT_DIR="${WORKSPACE}/04-DATA-AND-SOURCES/sentiment-analysis/${TODAY}"
LOG_FILE="${WORKSPACE}/04-DATA-AND-SOURCES/raw-scrapes/logs/sentiment-analysis-${TODAY}.log"

mkdir -p "${SENT_DIR}" "$(dirname "${LOG_FILE}")"

echo "[${TIMESTAMP}] MLK Sentiment Analysis starting..." | tee "${LOG_FILE}"

# Check if processed entities exist
if [ ! -d "${PROC_DIR}" ] || [ -z "$(ls -A "${PROC_DIR}" 2>/dev/null)" ]; then
    echo "[${TIMESTAMP}] No processed entities found for ${TODAY}. Skipping." | tee -a "${LOG_FILE}"
    exit 0
fi

# Sentiment keyword sets (Malay + English)
POSITIVE_KEYWORDS="baik cemerlang gemilang terbaik berjaya maju sokong menyokong setuju bagus excellent success progress win victory triumph popular support baik hati jujur amanah"
NEGATIVE_KEYWORDS="buruk gagal rosak skandal rasuah korupsi kritik tolak bantah tidak setuju kecewa jatuh kalah pecat salah iring problem crisis controversial corrupt scandal fail decline"

# Process each entity file
TOTAL_FILES=0
TOTAL_POSITIVE=0
TOTAL_NEGATIVE=0
TOTAL_NEUTRAL=0

for ENTITY_FILE in "${PROC_DIR}"/*-entities.json; do
    [ -f "${ENTITY_FILE}" ] || continue
    
    BASENAME=$(basename "${ENTITY_FILE}" -entities.json)
    OUTPUT_FILE="${SENT_DIR}/${BASENAME}-sentiment.json"
    RAW_FILE="${WORKSPACE}/04-DATA-AND-SOURCES/raw-scrapes/${TODAY}/${BASENAME}.md"
    
    if [ ! -f "${RAW_FILE}" ]; then
        echo "[${TIMESTAMP}] Raw file not found for ${BASENAME}, skipping sentiment." | tee -a "${LOG_FILE}"
        continue
    fi
    
    echo "[${TIMESTAMP}] Scoring sentiment: ${BASENAME}" | tee -a "${LOG_FILE}"
    
    # Count positive/negative keywords
    POS_COUNT=0
    NEG_COUNT=0
    for kw in ${POSITIVE_KEYWORDS}; do
        c=$(grep -ci "${kw}" "${RAW_FILE}" 2>/dev/null || echo 0)
        POS_COUNT=$((POS_COUNT + c))
    done
    for kw in ${NEGATIVE_KEYWORDS}; do
        c=$(grep -ci "${kw}" "${RAW_FILE}" 2>/dev/null || echo 0)
        NEG_COUNT=$((NEG_COUNT + c))
    done
    
    # Determine overall sentiment
    if [ ${POS_COUNT} -gt $((NEG_COUNT * 2)) ]; then
        SENTIMENT="POSITIVE"
    elif [ ${NEG_COUNT} -gt $((POS_COUNT * 2)) ]; then
        SENTIMENT="NEGATIVE"
    else
        SENTIMENT="NEUTRAL"
    fi
    
    # Write sentiment JSON
    cat > "${OUTPUT_FILE}" << EOF
{
  "file": "${BASENAME}",
  "timestamp": "${TIMESTAMP}",
  "sentiment": "${SENTIMENT}",
  "positive_keywords": ${POS_COUNT},
  "negative_keywords": ${NEG_COUNT},
  "total_keywords": $((POS_COUNT + NEG_COUNT)),
  "sentiment_score": $(echo "scale=2; (${POS_COUNT} - ${NEG_COUNT}) / (${POS_COUNT} + ${NEG_COUNT} + 1)" | bc 2>/dev/null || echo 0)
}
EOF
    
    TOTAL_FILES=$((TOTAL_FILES + 1))
    TOTAL_POSITIVE=$((TOTAL_POSITIVE + POS_COUNT))
    TOTAL_NEGATIVE=$((TOTAL_NEGATIVE + NEG_COUNT))
    case ${SENTIMENT} in
        POSITIVE) TOTAL_NEUTRAL=$((TOTAL_NEUTRAL + 0)) ;;
        NEGATIVE) ;;
        NEUTRAL) TOTAL_NEUTRAL=$((TOTAL_NEUTRAL + 1)) ;;
    esac
done

# Generate daily sentiment summary
SUMMARY_FILE="${SENT_DIR}/_sentiment-summary-${TODAY}.md"
cat > "${SUMMARY_FILE}" << EOF
# Sentiment Analysis Summary — ${TODAY}

**Generated:** ${TIMESTAMP}
**Source:** CJ-MLK-08 Sentiment Analysis Pipeline
**Files Analyzed:** ${TOTAL_FILES}
**Total Positive Keywords:** ${TOTAL_POSITIVE}
**Total Negative Keywords:** ${TOTAL_NEGATIVE}

## Sentiment Distribution
- Positive-dominant files: $(grep -l '"POSITIVE"' "${SENT_DIR}"/*.json 2>/dev/null | wc -l)
- Negative-dominant files: $(grep -l '"NEGATIVE"' "${SENT_DIR}"/*.json 2>/dev/null | wc -l)
- Neutral files: $(grep -l '"NEUTRAL"' "${SENT_DIR}"/*.json 2>/dev/null | wc -l)

## PIR Relevance
- Negative sentiment spikes → flag for CRITICAL PIRs (01-05, 18, 27-30)
- Positive sentiment surges → monitor for coordinated campaigning (PIR-29)
- Neutral baseline → routine collection continues

## Delta Tracking
- Compare with previous day's sentiment scores
- Flag any POI with sentiment shift > 30% for review
EOF

echo "[${TIMESTAMP}] Sentiment analysis complete. ${TOTAL_FILES} files scored." | tee -a "${LOG_FILE}"
echo "[${TIMESTAMP}] Positive: ${TOTAL_POSITIVE} | Negative: ${TOTAL_NEGATIVE}" | tee -a "${LOG_FILE}"
echo "[${TIMESTAMP}] Output: ${SENT_DIR}" | tee -a "${LOG_FILE}"
