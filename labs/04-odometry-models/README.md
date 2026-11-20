# Lab 04 — Odometry & physical models

**Chapter:** 04 — Dynamics and physical models  
**Hardware:** simulation only  
**Image:** `ros2` (base)

## Goals

1. Treat the course odometry node as a **physical model** of planar motion.
2. Inject noise / slip parameters and observe drift.
3. Run pure-Python unit tests for the kinematics core (no Docker required for tests).

## Run sim with noise

```bash
docker compose -f docker/compose.yaml run --rm ros2 bash
cd /ws && colcon build --symlink-install && source install/setup.bash
ros2 launch physibot_bringup sim_diff_drive.launch.py \
  wheel_separation:=0.175 wheel_radius:=0.04 odom_noise_std:=0.01
```

## Unit tests (host or container)

```bash
# From repo root (Python 3; no ROS required)
python3 -m pytest tests/unit/test_diff_drive_kinematics.py -q
```

## Exercises

- [ ] Compare ideal vs. noisy odometry after a closed square path.
- [ ] Relate `wheel_separation` / `wheel_radius` to Limo Pro tread (175 mm) and wheel size.
- [ ] Sketch where a learned residual model (later Isaac Lab chapters) could correct drift.

## Pointers

- `code/ros2_ws/src/physibot_sim/physibot_sim/kinematics.py`
- Adaptation: vendor chassis model in `limo_ros2` when moving beyond the course stub.
