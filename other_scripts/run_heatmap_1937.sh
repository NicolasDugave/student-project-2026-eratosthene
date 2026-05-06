#!/bin/bash
# run_heatmap_1937.sh
# Lance building_heatmap.py sur tous les fichiers *_decoupe.tif de 1937.

set -euo pipefail

FOLDER="../Cartes-reseau-transport/output-cartes/heatmap_bati/1937"
SCRIPT="other_scripts/building_heatmap.py"

# ── Paramètres heatmap (ajuster selon la carte) ──────────────────────────────
PRESET="red"
MIN_AREA=12
CLOSING_RADIUS=1
MAX_ECC=0.97
MEDIAN=5
SIGMA=50
MODE="count"
# -----------------------------------------------------------------------------

echo "=== Heatmap bâti 1937 ==="
echo "Dossier : $FOLDER"
echo ""

for INPUT in "$FOLDER"/*_decoupe.tif; do
    # Extraire le nom de base sans suffixe  ex. "1937_centre"
    BASENAME=$(basename "$INPUT" _decoupe.tif)
    OUTPUT="$FOLDER/${BASENAME}_heatmap.tif"

    echo "→ $BASENAME"
    python "$SCRIPT" \
        --input    "$INPUT" \
        --output   "$OUTPUT" \
        --preset   "$PRESET" \
        --min-area "$MIN_AREA" \
        --closing-radius "$CLOSING_RADIUS" \
        --max-eccentricity "$MAX_ECC" \
        --median-size "$MEDIAN" \
        --gaussian-sigma "$SIGMA" \
        --mode "$MODE"

    echo "   ✓ $(basename "$OUTPUT")"
    echo ""
done

echo "=== Terminé ==="
