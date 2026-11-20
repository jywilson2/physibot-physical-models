#!/usr/bin/env bash
# Build textbook PDF/DOCX inside a TeX+Pandoc container (no host TeX required).
# Uses docker/Dockerfile.textbook. Requires a working Docker daemon.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
IMAGE="${PHYSIBOT_TEXTBOOK_IMAGE:-physibot/textbook-export:local}"
FORMATS="${1:-pdf,docx}"

if ! command -v docker >/dev/null 2>&1; then
  echo "docker not found. Install Docker, or install pandoc+TeX and run:" >&2
  echo "  ./docs/export-tools/export-stub.sh" >&2
  exit 1
fi

echo "Building textbook export image (${IMAGE})..."
docker build -f "${ROOT}/docker/Dockerfile.textbook" -t "${IMAGE}" "${ROOT}"

mkdir -p "${ROOT}/textbook/exports"

IFS=',' read -ra WANT <<< "${FORMATS}"
for fmt in "${WANT[@]}"; do
  case "${fmt}" in
    pdf|docx) ;;
    *)
      echo "Unknown format: ${fmt} (use pdf, docx, or pdf,docx)" >&2
      exit 1
      ;;
  esac
done

echo "Rendering (${FORMATS})..."
docker run --rm \
  -v "${ROOT}:/book:rw" \
  -w /book \
  "${IMAGE}" \
  bash -lc "./docs/export-tools/export-stub.sh"

# export-stub always tries both; document requested formats for callers.
for fmt in "${WANT[@]}"; do
  art="${ROOT}/textbook/exports/physibot.${fmt}"
  if [[ -f "${art}" ]]; then
    echo "OK: ${art} ($(wc -c < "${art}") bytes)"
  else
    echo "MISSING expected artifact: ${art}" >&2
    exit 1
  fi
done
