#!/bin/bash
# MLK Entity Extraction Pipeline Script (CJ-MLK-07)
# Extracts named entities from raw scrapes → structured processed entities
# Run: daily 06:00 MYT by cronjob

set -euo pipefail

WORKSPACE="/home/p62operator/.openclaw/workspace-mlk"
TODAY=$(TZ=Asia/Kuala_Lumpur date '+%Y%m%d')
TIMESTAMP=$(TZ=Asia/Kuala_Lumpur date '+%Y-%m-%d %H:%M %Z')
RAW_DIR="${WORKSPACE}/04-DATA-AND-SOURCES/raw-scrapes/${TODAY}"
PROC_DIR="${WORKSPACE}/04-DATA-AND-SOURCES/processed-entities/${TODAY}"
LOG_FILE="${WORKSPACE}/04-DATA-AND-SOURCES/raw-scrapes/logs/entity-extraction-${TODAY}.log"

mkdir -p "${PROC_DIR}" "$(dirname "${LOG_FILE}")"

echo "[${TIMESTAMP}] MLK Entity Extraction starting..." | tee "${LOG_FILE}"

# Check if raw data exists
if [ ! -d "${RAW_DIR}" ] || [ -z "$(ls -A "${RAW_DIR}" 2>/dev/null)" ]; then
    echo "[${TIMESTAMP}] No raw scrapes found for ${TODAY}. Skipping." | tee -a "${LOG_FILE}"
    exit 0
fi

# POI name patterns for entity extraction
POI_NAMES=(
    "Ab Rauf Yusoh" "Muhamad Akmal Saleh" "Adly Zahari" "Mas Ermieyati Samsudin"
    "Adam Adli" "Zulkifli Ismail" "Mohd Noor Helmy" "Shamsul Iskandar"
    "Bakri Jamaluddin" "Sulaiman Md Ali" "Rais Yasin" "Rahmad Mariman"
    "Mohd Yadzil Yaakub" "Fairul Nizam Roslan" "Ngwe Hee Sem" "Kerk Chee Yee"
    "Muhammad Jailani Khamis" "Khaidhirah Abu Zahar" "Ibrahim Durum" "Hameed Mytheen"
)

# DUN constituency names
DUN_NAMES=(
    "Kuala Linggi" "Tanjung Bidara" "Ayer Limau" "Lendu" "Taboh Naning"
    "Rembia" "Gadek" "Machap Jaya" "Durian Tunggal" "Asahan"
    "Sungai Udang" "Pantai Kundor" "Paya Rumput" "Kelebang" "Pengkalan Batu"
    "Ayer Keroh" "Bukit Katil" "Ayer Molek" "Kesidang" "Kota Laksamana"
    "Duyong" "Bandar Hilir" "Telok Mas" "Bemban" "Rim" "Serkam" "Merlimau" "Sungai Rambai"
)

# Process each raw scrape file
ENTITY_COUNT=0
for RAW_FILE in "${RAW_DIR}"/*.md; do
    [ -f "${RAW_FILE}" ] || continue
    
    BASENAME=$(basename "${RAW_FILE}" .md)
    OUTPUT_FILE="${PROC_DIR}/${BASENAME}-entities.json"
    
    echo "[${TIMESTAMP}] Processing: ${BASENAME}" | tee -a "${LOG_FILE}"
    
    # Initialize JSON structure
    echo '{"file":"'${BASENAME}'","timestamp":"'${TIMESTAMP}'","entities":{' > "${OUTPUT_FILE}"
    
    FIRST_POI=true
    echo '"pois":[' >> "${OUTPUT_FILE}"
    for NAME in "${POI_NAMES[@]}"; do
        COUNT=$(grep -ci "${NAME}" "${RAW_FILE}" 2>/dev/null || echo 0)
        if [ "${COUNT}" -gt 0 ]; then
            [ "$FIRST_POI" = false ] && echo "," >> "${OUTPUT_FILE}"
            echo '{"name":"'${NAME}'","mentions":'${COUNT}'}' >> "${OUTPUT_FILE}"
            FIRST_POI=false
            ENTITY_COUNT=$((ENTITY_COUNT + 1))
        fi
    done
    echo '],' >> "${OUTPUT_FILE}"
    
    FIRST_DUN=true
    echo '"dun_seats":[' >> "${OUTPUT_FILE}"
    for NAME in "${DUN_NAMES[@]}"; do
        COUNT=$(grep -ci "${NAME}" "${RAW_FILE}" 2>/dev/null || echo 0)
        if [ "${COUNT}" -gt 0 ]; then
            [ "$FIRST_DUN" = false ] && echo "," >> "${OUTPUT_FILE}"
            echo '{"constituency":"'${NAME}'","mentions":'${COUNT}'}' >> "${OUTPUT_FILE}"
            FIRST_DUN=false
            ENTITY_COUNT=$((ENTITY_COUNT + 1))
        fi
    done
    echo ']}}' >> "${OUTPUT_FILE}"
done

# Generate summary
SUMMARY_FILE="${PROC_DIR}/_summary-${TODAY}.md"
cat > "${SUMMARY_FILE}" << EOF
# Entity Extraction Summary — ${TODAY}

**Generated:** ${TIMESTAMP}
**Source:** CJ-MLK-07 Entity Extraction Pipeline
**Files Processed:** $(ls "${RAW_DIR}"/*.md 2>/dev/null | wc -l)
**Total Entity Matches:** ${ENTITY_COUNT}

## POI Mentions by File
$(for f in "${PROC_DIR}"/*-entities.json; do [ -f "$f" ] && echo "- $(basename $f): $(grep -o '"mentions":[0-9]*' "$f" | awk -F: '{sum+=$2} END{print sum}') matches"; done)

## Next Steps
- Sentiment analysis (CJ-MLK-08) will score these entities
- Daily brief (CJ-MLK-05) will synthesize findings
- Weekly deep-dive (CJ-MLK-10) will analyze trends
EOF

echo "[${TIMESTAMP}] Entity extraction complete. ${ENTITY_COUNT} total matches across $(ls "${RAW_DIR}"/*.md 2>/dev/null | wc -l) files." | tee -a "${LOG_FILE}"
echo "[${TIMESTAMP}] Output: ${PROC_DIR}" | tee -a "${LOG_FILE}"
