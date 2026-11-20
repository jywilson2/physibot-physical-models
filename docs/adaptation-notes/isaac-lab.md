# Adaptation: NVIDIA Isaac Lab

## Intent

Use Isaac Lab for learning / physics-heavy labs. Bridge to ROS 2 via the
official Lab **`ros2` Docker profile**, which installs **ROS 2 Humble**.

## Evidence (course pin)

- [Isaac Lab installation](https://docs.nvidia.com/isaaclab/isaac-lab/installation) —
  *“Dockerfile.ros2 installs ROS 2 Humble”*; profile *“base image plus ROS 2 Humble”*.
- [Isaac Lab Docker guide](https://isaac-sim.github.io/IsaacLab/main/source/deployment/docker.html)

## Term pin

| Field | Value |
|-------|-------|
| Tag | **`v2.3.2`** |
| Commit | `37ddf626871758333d6ed89cf64ad702aef127d0` |
| Permalink | https://github.com/isaac-sim/IsaacLab/tree/v2.3.2 |
| ROS 2 | Humble via Lab `ros2` profile |

Re-verify each term (newer tags such as `v3.0.0` may land). Student procedure: [`labs/10-isaac-lab/README.md`](../../labs/10-isaac-lab/README.md).

## Course overlay plan

1. Student day-to-day ROS work: `docker/compose.yaml` Humble image (this repo).
2. Isaac Lab labs: follow upstream `container.py` / Compose profiles; mount
   `code/ros2_ws` read-only as documented in Lab 10.
3. DGX Spark (Ch. 13): training / heavy sim; **Orin Nano** is deploy-only (Lab 12).
4. Adapt an existing wheeled / locomotion example — do not invent a full Lab task suite.

## Open items

- [x] Pin Isaac Lab release tag compatible with course Humble story (`v2.3.2`)
- [ ] Note any ROS2 image known issues from Lab release notes each term
- [x] Decide Gazebo vs. Isaac Sim for Chapters 03–09: **course stub sim + Nav2 first**; Isaac Lab focus from Ch. 10
- [x] Document mount of `code/ros2_ws` into Lab containers (Lab 10 README)
