# Adaptation: AgileX Limo Pro

## Intent

Use vendor and community ROS 2 packages for description, drivers, and bringup.
PhysiBot course packages (`physibot_bringup`, `physibot_description`, `physibot_sim`)
are thin wrappers / launch overlays — not a from-scratch robot stack.

## Upstream (pinned for this term)

| Resource | URL / ref |
|----------|-----------|
| ROS 2 packages | https://github.com/agilexrobotics/limo_ros2 — branch **`humble`** |
| **Frozen commit** | **`dcc5a8637f83236ed6778af86ad826e46a20cd92`** (tip of `humble` as of 2026-11-20; message: “add humble driver”) |
| Permalink | https://github.com/agilexrobotics/limo_ros2/tree/dcc5a8637f83236ed6778af86ad826e46a20cd92 |
| User docs | https://github.com/agilexrobotics/limo_ros2_doc |
| Pro docs (historic Foxy manual still useful for hardware) | https://github.com/agilexrobotics/limo_pro_doc |

```bash
git clone https://github.com/agilexrobotics/limo_ros2.git
cd limo_ros2 && git checkout dcc5a8637f83236ed6778af86ad826e46a20cd92
```

### Packages present at the frozen SHA

| Package | Role |
|---------|------|
| `limo_base` | Serial driver; `limo_base.launch.py`, `open_ydlidar_launch.py` |
| `limo_description` / `limo_car` | URDF / Gazebo / meshes |
| `limo_msgs` | Vendor messages |

Nav2 teaching configs stay in course `physibot_bringup` (see `nav2.md`). Related AgileX classroom Nav2 YAML lives outside this repo in [`agilex_open_class`](https://github.com/agilexrobotics/agilex_open_class) (`limo/limo_bringup/param/nav2.yaml` @ `8e799754af623c3cec954b74b186d63d6ce8fa62`) — use for **diff comments**, do not vendor the tree.

Re-verify URLs and re-freeze the SHA each term before CI / Orin images.

## Published footprint (course URDF / Nav2)

Sources (do not invent unsafe numbers):

- [AgileX Limo Pro user manual — tech specifications](https://github.com/agilexrobotics/limo_pro_doc/blob/master/Limo%20Pro%20user%20manual(EN).md)
- [LIMO ROS 2 Humble doc — tech specifications](https://github.com/agilexrobotics/limo_ros2_doc/blob/master/LIMO-ROS2-humble(EN).md)

| Spec | Value | Notes |
|------|-------|-------|
| Overall L×W×H | 322 × 220 × 251 mm | Published |
| Wheelbase | 200 mm | Published |
| Tread (track width) | 175 mm | Published |
| Mass | ~4.8 kg | Published dead load |
| Max speed | 1.0 m/s | Published no-load max |
| Ackermann min turn radius | 0.4 m | Published |
| Ground clearance | 24 mm | Published |
| Drive modes | differential, Ackermann, tracked, Mecanum | Published |
| On-robot compute (Pro) | NVIDIA Jetson Orin Nano | Published |
| LiDAR / depth | EAI T-mini Pro / Orbbec DaBai | Published |
| Wheel radius | **0.040 m teaching estimate** | **Not** in AgileX body table — measure tire before physical runs |

Course URDF: `code/ros2_ws/src/physibot_description/urdf/physibot_limo.urdf.xacro`
(visual body box height 180 mm is a simplified hull; overall published height remains 251 mm).

## Course overlay plan

1. Early chapters: simulated footprint + `cmd_vel` + course `physibot_sim` odom (no physical robot).
2. Mid chapters: Gazebo/Isaac assets adapted from `limo_ros2` description packages (meshes still under license review).
3. Ch. 12+: real drivers on Orin Nano at the frozen SHA; document network/DDS lab conventions.

## Open items

- [x] Pin concrete upstream repo URLs (branch `humble`)
- [x] Confirm Humble support for chosen Limo ROS 2 branch (`limo_ros2` default = humble)
- [x] Map drive modes to chapters (Ch. 03 diff-drive first; Ackermann/Mecanum later)
- [x] Freeze a commit SHA of `limo_ros2` for the term (`dcc5a8637f83236ed6778af86ad826e46a20cd92`)
- [ ] Vendor meshes under course license review (or keep geometric stubs)
