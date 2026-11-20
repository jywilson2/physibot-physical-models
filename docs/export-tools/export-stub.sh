#!/usr/bin/env bash
# PhysiBot textbook export helper — Pandoc fallback when Quarto is unavailable.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
OUT="${ROOT}/textbook/exports"
mkdir -p "${OUT}"

CHAPTERS=(
  "${ROOT}/textbook/frontmatter/title.md"
  "${ROOT}/chapters/00-outline.md"
  "${ROOT}/chapters/01-welcome-and-docker.md"
  "${ROOT}/chapters/02-linear-algebra-refresh.md"
  "${ROOT}/chapters/03-mobile-robot-kinematics.md"
  "${ROOT}/chapters/04-dynamics-and-physical-models.md"
  "${ROOT}/chapters/05-sensing-and-observation-models.md"
  "${ROOT}/chapters/06-estimation-fundamentals.md"
  "${ROOT}/chapters/07-localization.md"
  "${ROOT}/chapters/08-mapping-and-slam.md"
  "${ROOT}/chapters/09-navigation-with-nav2.md"
  "${ROOT}/chapters/10-learning-with-isaac-lab.md"
  "${ROOT}/chapters/11-sim-to-real.md"
  "${ROOT}/chapters/12-orin-nano-deploy.md"
  "${ROOT}/chapters/13-dgx-spark-training.md"
  "${ROOT}/chapters/14-capstone.md"
)

if ! command -v pandoc >/dev/null 2>&1; then
  echo "pandoc not found. Install pandoc (and TeX for PDF), or use Quarto:" >&2
  echo "  quarto render textbook/physibot.qmd --to docx --output-dir textbook/exports" >&2
  exit 1
fi

echo "Exporting DOCX via pandoc..."
pandoc \
  --from markdown \
  --toc \
  --metadata title="PhysiBot: AI Physical Models for Mobile Robotics" \
  "${CHAPTERS[@]}" \
  -o "${OUT}/physibot.docx"
echo "Wrote ${OUT}/physibot.docx"

PDF_ENGINE=""
for eng in xelatex lualatex pdflatex; do
  if command -v "${eng}" >/dev/null 2>&1; then
    PDF_ENGINE="${eng}"
    break
  fi
done

if [[ -n "${PDF_ENGINE}" ]]; then
  echo "Exporting PDF via pandoc (${PDF_ENGINE})..."
  pandoc \
    --from markdown \
    --toc \
    --pdf-engine="${PDF_ENGINE}" \
    --metadata title="PhysiBot: AI Physical Models for Mobile Robotics" \
    "${CHAPTERS[@]}" \
    -o "${OUT}/physibot.pdf"
  echo "Wrote ${OUT}/physibot.pdf"
else
  echo "No LaTeX engine (xelatex/lualatex/pdflatex) found; skipping PDF." >&2
  echo "DOCX export succeeded. Install TeX Live or Quarto for PDF." >&2
fi
