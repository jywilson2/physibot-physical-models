# Lab 01 — Docker hello + robot description

**Chapter:** 01 — Welcome & Docker  
**Hardware:** none  
**Image:** `ros2` (base)

## Goals

1. Build and enter the PhysiBot ROS 2 Humble container.
2. Confirm `ROS_DISTRO=humble`.
3. Publish the Limo-class URDF via `robot_state_publisher`.

## Run

```bash
# Host
docker compose -f docker/compose.yaml build ros2
docker compose -f docker/compose.yaml run --rm ros2 bash

# Container
cd /ws
colcon build --symlink-install
source install/setup.bash
echo "$ROS_DISTRO"   # expect: humble
ros2 launch physibot_bringup description.launch.py
```

In a second container shell (same Compose project):

```bash
docker compose -f docker/compose.yaml run --rm ros2 bash
source /ws/install/setup.bash
ros2 topic list
ros2 node list
```

## Checkpoints

- [ ] `echo $ROS_DISTRO` → `humble`
- [ ] `/robot_description` parameter present on `robot_state_publisher`
- [ ] TF tree includes `base_link` (and wheel / sensor frames from the course URDF)

## Notes

Dimensions in `physibot_description` match published Limo Pro footprint
(322 × 220 × 251 mm, wheelbase 200 mm, tread 175 mm). Full vendor meshes and
drivers come from upstream `limo_ros2` later — see `docs/adaptation-notes/limo.md`.
