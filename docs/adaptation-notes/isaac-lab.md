# Adaptation: NVIDIA Isaac Lab

## Intent

Use Isaac Lab for learning / physics-heavy labs. Bridge to ROS 2 via the
official Lab **`ros2` Docker profile**, which installs **ROS 2 Humble**.

## Course pin (term baseline)

| Field | Value |
|-------|-------|
| **Release tag** | **`v3.0.0`** (GA) |
| GitHub | https://github.com/isaac-sim/IsaacLab/releases/tag/v3.0.0 |
| Docs | https://isaac-sim.github.io/IsaacLab/v3.0.0/source/isaaclab/installation.html |
| Clone | `git clone --branch v3.0.0 --depth 1 https://github.com/isaac-sim/IsaacLab.git` |
| ROS 2 profile | `ros2` → `Dockerfile.ros2` installs **Humble** |

## Evidence

- [Isaac Lab installation (v3.0.0)](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/isaaclab/installation.html) —
  *“`ros2` … The `base` image plus ROS 2 Humble”*.
- [Isaac Lab Docker / cloud features](https://isaac-sim.github.io/IsaacLab/v3.0.0-EA/source/features/docker_cloud.html) (profile table; re-check versioned docs each term).
- [NVIDIA Isaac Lab installation hub](https://docs.nvidia.com/isaaclab/isaac-lab/installation)

Student procedure: [`labs/10-isaac-lab/README.md`](../../labs/10-isaac-lab/README.md).

## Course overlay plan

1. Student day-to-day ROS work: `docker/compose.yaml` Humble image (this repo).
2. Isaac Lab labs: follow upstream `container.py` / Compose profiles; mount
   `code/ros2_ws` read-only as documented in Lab 10.
3. DGX Spark (Ch. 13): same **`v3.0.0`** tag for training / heavy sim; **Orin Nano** is deploy-only (Lab 12); no student-owned Spark assumed.
4. Adapt an existing wheeled / locomotion example — do not invent a full Lab task suite.

## Open items

- [x] Pin Isaac Lab release tag compatible with lab drivers → **`v3.0.0`**
- [ ] Note any ROS2 image known issues from Lab release notes each term
- [x] Decide Gazebo vs. Isaac Sim for Chapters 03–09: **course stub sim + Nav2 first**; Isaac Lab focus from Ch. 10
- [x] Document mount of `code/ros2_ws` into Lab containers (Lab 10 README)
