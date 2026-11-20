#!/usr/bin/env bash
# Stub exporter for PDF/DOCX — full pipeline is a later task.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
OUT="${ROOT}/textbook/exports"
mkdir -p "${OUT}"
echo "PhysiBot export stub — install pandoc/quarto and expand chapters before production builds." >&2
if command -v pandoc >/dev/null 2>&1; then
  pandoc \
    "${ROOT}/textbook/frontmatter/title.md" \
    "${ROOT}/chapters/"*.md \
    -o "${OUT}/physibot-stub.docx" \
    && echo "Wrote ${OUT}/physibot-stub.docx"
else
  echo "pandoc not found; skipping DOCX stub." >&2
  exit 0
fi
