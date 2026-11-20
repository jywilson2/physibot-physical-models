# Lab 07 — Localization (AMCL)

**Chapter:** 07 — Localization  
**Hardware:** simulation only  
**Image:** `ros2_nav2` (Nav2 profile)

## Goals

1. Localize on a known occupancy map with Nav2 AMCL.
2. Understand particle-filter pose on a Limo-class footprint.
3. Practice map → `odom` → `base_link` frame relationships.

## Build Nav2 image

```bash
docker compose -f docker/compose.yaml --profile nav2 build ros2_nav2
docker compose -f docker/compose.yaml --profile nav2 run --rm ros2_nav2 bash
```

## Run

```bash
cd /ws && colcon build --symlink-install && source install/setup.bash
ros2 launch physibot_bringup localization.launch.py
```

This starts:

- Diff-drive sim (odom + TF)
- Map server with the course demo map
- AMCL with Limo-sized footprint parameters

Drive with `/cmd_vel` and watch `/amcl_pose` (or RViz on a desktop host).

## Exercises

- [ ] Set an initial pose; verify particles converge.
- [ ] Kidnap the robot (teleport via large `cmd_vel` burst + noise) and recover.
- [ ] Note remaining work: swap demo map for a Gazebo/Isaac warehouse map.

## Adaptation

Prefer Nav2 tutorials + AgileX Limo Nav2 examples — `docs/adaptation-notes/nav2.md`.
