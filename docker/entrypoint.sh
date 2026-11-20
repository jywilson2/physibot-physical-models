#!/usr/bin/env bash
set -euo pipefail
source /opt/ros/${ROS_DISTRO:-humble}/setup.bash
if [[ -f /ws/install/setup.bash ]]; then
  # shellcheck disable=SC1091
  source /ws/install/setup.bash
fi
exec "$@"
