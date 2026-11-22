#!/usr/bin/env bash
# Host-side smoke: required paths exist (no Docker required).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
required=(
  README.md
  STATUS.md
  LICENSE
  LICENSE-CODE
  chapters/00-outline.md
  chapters/14-capstone.md
  chapters/part2/00-outline.md
  chapters/part2/09-capstone-learned-navigation.md
  textbook/physibot.qmd
  textbook/physibot-part2.qmd
  docker/compose.yaml
  docker/Dockerfile.ros2
  labs/README.md
  labs/01-docker-hello/README.md
  labs/03-kinematics-teleop/README.md
  labs/04-odometry-models/README.md
  labs/07-localization/README.md
  labs/08-mapping/README.md
  labs/09-nav2/README.md
  labs/10-isaac-lab/README.md
  labs/12-orin-deploy/README.md
  labs/part2/README.md
  labs/part2/01-isaac-world-model/README.md
  labs/part2/02-neural-mapping/README.md
  labs/part2/03-latent-rollout-planning/README.md
  labs/part2/04-limo-on-robot-finetune/README.md
  docs/adaptation-notes/learned-navigation.md
  code/ros2_ws/src/physibot_bringup/package.xml
  code/ros2_ws/src/physibot_bringup/launch/description.launch.py
  code/ros2_ws/src/physibot_bringup/launch/sim_diff_drive.launch.py
  code/ros2_ws/src/physibot_bringup/launch/localization.launch.py
  code/ros2_ws/src/physibot_bringup/launch/mapping.launch.py
  code/ros2_ws/src/physibot_bringup/launch/nav2.launch.py
  code/ros2_ws/src/physibot_bringup/config/nav2_params.yaml
  code/ros2_ws/src/physibot_bringup/maps/demo_map.yaml
  code/ros2_ws/src/physibot_bringup/maps/demo_map.pgm
  code/ros2_ws/src/physibot_description/urdf/physibot_limo.urdf.xacro
  code/ros2_ws/src/physibot_description/urdf/physibot_stub.urdf.xacro
  code/ros2_ws/src/physibot_sim/package.xml
  code/ros2_ws/src/physibot_sim/physibot_sim/kinematics.py
  docs/adaptation-notes/isaac-lab.md
  docs/adaptation-notes/limo.md
  docs/adaptation-notes/nav2.md
  tests/unit/test_diff_drive_kinematics.py
  tests/unit/test_hardware_constants.py
  tests/integration/test_launch_and_packages.py
  tests/integration/test_export_sources.py
  docs/export-tools/export-stub.sh
  docs/export-tools/export-pdf-docker.sh
  docker/Dockerfile.textbook
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
# Compose exposes nav2 profile
grep -q 'profiles: \["nav2"\]' "${ROOT}/docker/compose.yaml" \
  || grep -q "nav2" "${ROOT}/docker/compose.yaml"
if [[ "${missing}" -ne 0 ]]; then
  exit 1
fi
echo "OK: layout + Humble pin + lab ladder checks passed (${ROOT})"
