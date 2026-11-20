# Adaptation: NVIDIA Isaac Lab

## Intent

Use Isaac Lab for learning / physics-heavy labs. Bridge to ROS 2 via the
official Lab **`ros2` Docker profile**, which installs **ROS 2 Humble**.

## Evidence (course pin)

- [Isaac Lab installation](https://docs.nvidia.com/isaaclab/isaac-lab/installation) —
  *“Dockerfile.ros2 installs ROS 2 Humble”*; profile *“base image plus ROS 2 Humble”*.
- [Isaac Lab Docker guide](https://isaac-sim.github.io/IsaacLab/main/source/deployment/docker.html)

## Course overlay plan

1. Student day-to-day ROS work: `docker/compose.yaml` Humble image (this repo).
2. Isaac Lab labs: follow upstream `container.py` / Compose profiles; document
   how to attach the course workspace (`labs/10-isaac-lab/`).
3. DGX Spark (Ch. 13): same containers on lab hosts; no student-owned Spark assumed.
4. Adapt an existing wheeled / locomotion example — do not invent a full Lab task suite.

## Open items

- [ ] Pin Isaac Lab release tag compatible with lab drivers
- [ ] Note any ROS2 image known issues from Lab release notes each term
- [x] Decide Gazebo vs. Isaac Sim for Chapters 03–09: **course stub sim + Nav2 first**; Isaac Lab focus from Ch. 10
- [ ] Document exact mount of `code/ros2_ws` into Lab containers
