# Lab 09 — Navigation with Nav2

**Chapter:** 09 — Navigation with Nav2  
**Hardware:** simulation only (physical Limo later)  
**Image:** `ros2_nav2`

## Goals

1. Bring up Nav2 with course params sized for Limo Pro footprint.
2. Send a navigation goal and interpret costmaps / planner / controller.
3. Debug common failures (TF, costmap inflation, velocity limits).

## Run

```bash
docker compose -f docker/compose.yaml --profile nav2 run --rm ros2_nav2 bash
cd /ws && colcon build --symlink-install && source install/setup.bash
ros2 launch physibot_bringup nav2.launch.py
```

Send a goal (example):

```bash
ros2 action send_goal /navigate_to_pose nav2_msgs/action/NavigateToPose \
  "{pose: {header: {frame_id: map}, pose: {position: {x: 1.0, y: 0.5, z: 0.0}, orientation: {w: 1.0}}}}"
```

## Config location

`code/ros2_ws/src/physibot_bringup/config/nav2_params.yaml` — footprint, max velocity
(1.0 m/s), and costmap settings derived from Limo Pro dimensions. Tune rather than
rewrite; prefer upstream Nav2 + Limo examples when available.

## Exercises

- [ ] Raise inflation radius; observe wider clearance.
- [ ] Cap `max_vel_x` below 0.5 m/s; compare tracking.
- [ ] List TF frames required for a successful Nav2 bringup.
