#!/usr/bin/env bash
# PhysiBot textbook export helper — Pandoc fallback when Quarto is unavailable.
# Requires: pandoc. PDF also needs xelatex/lualatex/pdflatex (+ TeX Live fonts).
# Reproducible alternative: ./docs/export-tools/export-pdf-docker.sh
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

# Chapters use \(...\) / \[...\] math; enable those extensions explicitly.
PANDOC_FROM="markdown+tex_math_single_backslash+tex_math_dollars+raw_tex"
TITLE="PhysiBot: AI Physical Models for Mobile Robotics"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "pandoc not found. Install pandoc (and TeX for PDF), use Quarto, or Docker:" >&2
  echo "  ./docs/export-tools/export-pdf-docker.sh" >&2
  echo "  quarto render textbook/physibot.qmd --to docx --output-dir textbook/exports" >&2
  exit 1
fi

echo "Exporting DOCX via pandoc..."
pandoc \
  --from "${PANDOC_FROM}" \
  --toc \
  --metadata title="${TITLE}" \
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
  PDF_ARGS=(
    --from "${PANDOC_FROM}"
    --toc
    --pdf-engine="${PDF_ENGINE}"
    -V geometry:margin=1in
    --metadata title="${TITLE}"
  )
  # Prefer Unicode-capable fonts when present (box-drawing / Greek in chapters).
  # Avoid `fc-list | grep -q` under pipefail (SIGPIPE makes the test fail).
  if grep -qi "DejaVu Serif" < <(fc-list 2>/dev/null || true); then
    PDF_ARGS+=(-V mainfont="DejaVu Serif" -V monofont="DejaVu Sans Mono")
  fi
  if grep -qi "DejaVu Math TeX Gyre" < <(fc-list 2>/dev/null || true); then
    PDF_ARGS+=(-V mathfont="DejaVu Math TeX Gyre")
  fi
  pandoc "${PDF_ARGS[@]}" "${CHAPTERS[@]}" -o "${OUT}/physibot.pdf"
  echo "Wrote ${OUT}/physibot.pdf"
else
  echo "No LaTeX engine (xelatex/lualatex/pdflatex) found; skipping PDF." >&2
  echo "DOCX export succeeded. Install TeX Live, Quarto, or run:" >&2
  echo "  ./docs/export-tools/export-pdf-docker.sh" >&2
fi
