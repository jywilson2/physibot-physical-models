# Chapter 03 — Mobile robot kinematics

> **Status:** stub. **License:** CC BY-NC 4.0. **Hardware:** simulation only.

## Learning goals

- Derive unicycle / differential-drive kinematics and relate to Ackermann approximations.
- Map commanded velocities to wheel speeds for a Limo-class platform.
- Simulate simple open-loop trajectories in ROS 2 / Gazebo stubs.

## Outline

1. Configuration space for planar mobile robots.
2. Nonholonomic constraints (intuition + equations).
3. Forward and inverse velocity kinematics.
4. AgileX Limo Pro drive modes (adapt vendor docs; do not invent URDF from scratch).
5. Lab: publish `cmd_vel`, visualize TF and odometry in sim.

## Adaptation notes

- Prefer existing AgileX Limo ROS 2 description/bringup packages — see `docs/adaptation-notes/limo.md`.

## Student exercises

Follow **`labs/03-kinematics-teleop/`**. Summary:

- [ ] Plot open-loop circle vs. square path under unicycle model (`sim_diff_drive.launch.py`).
- [ ] Identify frames: `base_footprint` / `base_link`, `odom`, sensor frames.
