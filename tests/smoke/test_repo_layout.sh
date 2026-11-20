#!/usr/bin/env bash
# Host-side smoke: required scaffold paths exist (no Docker required).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
required=(
  README.md
  STATUS.md
  LICENSE
  LICENSE-CODE
  chapters/00-outline.md
  chapters/14-capstone.md
  textbook/physibot.qmd
  docker/compose.yaml
  docker/Dockerfile.ros2
  code/ros2_ws/src/physibot_bringup/package.xml
  code/ros2_ws/src/physibot_description/urdf/physibot_stub.urdf.xacro
  docs/adaptation-notes/isaac-lab.md
)
missing=0
for rel in "${required[@]}"; do
  if [[ ! -e "${ROOT}/${rel}" ]]; then
    echo "MISSING: ${rel}" >&2
    missing=1
  fi
done
# Humble pin must be documented
grep -q "Humble" "${ROOT}/STATUS.md"
grep -q "Humble" "${ROOT}/README.md"
grep -q "ROS_DISTRO=humble" "${ROOT}/docker/Dockerfile.ros2"
if [[ "${missing}" -ne 0 ]]; then
  exit 1
fi
echo "OK: scaffold layout + Humble pin checks passed (${ROOT})"
