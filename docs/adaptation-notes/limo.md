# Adaptation: AgileX Limo Pro

## Intent

Use vendor and community ROS 2 packages for description, drivers, and bringup.
PhysiBot course packages (`physibot_bringup`, `physibot_description`) are thin
wrappers / launch overlays — not a from-scratch robot stack.

## Upstream pointers (verify URLs each term)

- AgileX Robotics documentation and Limo ROS 2 repositories (search current
  `limo_ros2` / AgileX GitHub orgs — pin specific SHAs in a later task).
- Jetson Orin Nano bringup guides from NVIDIA + AgileX for on-robot compute.
- Existing instructor demos (`spark_isaac_mycobot_*`) are **out of scope to
  reuse as this course repo**; borrow patterns only where pedagogically useful.

## Course overlay plan

1. Early chapters: simulated footprint + `cmd_vel` stub (no physical robot).
2. Mid chapters: Gazebo/Isaac assets adapted from Limo description packages.
3. Ch. 12+: real drivers on Orin Nano; document network/DDS lab conventions.

## Open items

- [ ] Pin concrete upstream repo URLs + licenses
- [ ] Confirm Humble support for chosen Limo ROS 2 branch
- [ ] Map drive modes (differential / Ackermann / omni if applicable) to chapters
