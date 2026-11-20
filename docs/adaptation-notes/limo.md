# Adaptation: AgileX Limo Pro

## Intent

Use vendor and community ROS 2 packages for description, drivers, and bringup.
PhysiBot course packages (`physibot_bringup`, `physibot_description`, `physibot_sim`)
are thin wrappers / launch overlays — not a from-scratch robot stack.

## Upstream (pinned for this term)

| Resource | URL / ref |
|----------|-----------|
| ROS 2 packages | https://github.com/agilexrobotics/limo_ros2 — default branch **`humble`** |
| User docs | https://github.com/agilexrobotics/limo_ros2_doc |
| Pro docs (historic Foxy manual still useful for hardware) | https://github.com/agilexrobotics/limo_pro_doc |

Re-verify URLs and default branch each term before freezing a SHA in CI.

## Published footprint (course URDF / Nav2)

| Spec | Value |
|------|-------|
| Body (L×W×H) | 322 × 220 × 251 mm |
| Wheelbase | 200 mm |
| Tread (track width) | 175 mm |
| Mass | ~4.8 kg |
| Max speed | 1.0 m/s |
| Ackermann min turn radius | 0.4 m |
| Drive modes | differential, Ackermann, tracked, Mecanum |
| On-robot compute (Pro) | NVIDIA Jetson Orin Nano |
| LiDAR / depth | EAI T-mini Pro / Orbbec DaBai |

Course stub URDF: `code/ros2_ws/src/physibot_description/urdf/physibot_limo.urdf.xacro`.

## Course overlay plan

1. Early chapters: simulated footprint + `cmd_vel` + course `physibot_sim` odom (no physical robot).
2. Mid chapters: Gazebo/Isaac assets adapted from `limo_ros2` description packages.
3. Ch. 12+: real drivers on Orin Nano; document network/DDS lab conventions.

## Open items

- [x] Pin concrete upstream repo URLs (branch `humble`)
- [x] Confirm Humble support for chosen Limo ROS 2 branch (`limo_ros2` default = humble)
- [x] Map drive modes to chapters (Ch. 03 diff-drive first; Ackermann/Mecanum later)
- [ ] Freeze a commit SHA of `limo_ros2` for the term
- [ ] Vendor meshes under course license review (or keep geometric stubs)
