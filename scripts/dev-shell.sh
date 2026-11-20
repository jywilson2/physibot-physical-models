#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "${ROOT}"
docker compose -f docker/compose.yaml build ros2
docker compose -f docker/compose.yaml run --rm ros2 bash
