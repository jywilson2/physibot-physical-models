# Lab 03 — Kinematics & teleop (sim)

**Chapter:** 03 — Mobile robot kinematics  
**Hardware:** simulation only  
**Image:** `ros2` (base)

## Goals

1. Relate unicycle / differential-drive equations to `geometry_msgs/Twist`.
2. Drive a simulated Limo-class robot with `cmd_vel`.
3. Inspect `odom` → `base_link` TF and `/odom` messages.

## Run

```bash
docker compose -f docker/compose.yaml run --rm ros2 bash
cd /ws && colcon build --symlink-install && source install/setup.bash
ros2 launch physibot_bringup sim_diff_drive.launch.py
```

Teleop (second shell):

```bash
source /ws/install/setup.bash
# Option A: built-in demo publisher
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.2}, angular: {z: 0.3}}" -r 10

# Option B: if teleop_twist_keyboard is installed in the image
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

## Exercises

- [ ] Open-loop circle: constant `v` and `ω`; estimate radius `R = v / ω`.
- [ ] Square path: sequence of straight + pivot turns; note nonholonomic limits.
- [ ] Name frames: `odom`, `base_link`, `laser_link`, `camera_link`.

## Package map

| Piece | Package |
|-------|---------|
| URDF / xacro | `physibot_description` |
| Diff-drive odom integrator | `physibot_sim` (`diff_drive_odom`) |
| Launch | `physibot_bringup` (`sim_diff_drive.launch.py`) |
