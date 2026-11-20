# Lab 08 — Mapping & SLAM

**Chapter:** 08 — Mapping and SLAM  
**Hardware:** simulation only  
**Image:** `ros2_nav2`

## Goals

1. Build an occupancy map with `slam_toolbox` (async) while driving the sim.
2. Save a map for Lab 07 / 09 reuse.
3. Connect observation models (Ch. 05) to occupancy updates.

## Run

```bash
docker compose -f docker/compose.yaml --profile nav2 run --rm ros2_nav2 bash
cd /ws && colcon build --symlink-install && source install/setup.bash
ros2 launch physibot_bringup mapping.launch.py
```

Drive with `/cmd_vel`. When ready:

```bash
ros2 run nav2_map_server map_saver_cli -f /ws/src/physibot_bringup/maps/student_map
```

## Caveat

The course sim publishes a **stub laser scan** suitable for smoke / teaching frames.
For realistic SLAM, adapt Gazebo or Isaac assets from upstream Limo packages
(`docs/adaptation-notes/limo.md`).

## Exercises

- [ ] Explain why odometry drift without loop closure corrupts the map.
- [ ] Export map YAML + PGM; load it in Lab 07.
