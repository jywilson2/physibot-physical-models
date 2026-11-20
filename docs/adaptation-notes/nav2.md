# Adaptation: Navigation2

## Intent

Teach localization, mapping handoff, and navigation using **Nav2** on a
Limo-class footprint. Prefer official Nav2 tutorials and existing Limo Nav2
configs over custom planners.

## Upstream pointers

- [Nav2 documentation](https://docs.nav2.org/)
- Nav2 Getting Started + configuration guides for Humble
- slam_toolbox (or vendor-recommended 2D SLAM) for Chapter 08 map building
- AgileX `limo_ros2` (`humble` @ `dcc5a8637f83236ed6778af86ad826e46a20cd92`) — **drivers only** at this pin (no Nav2 YAML in-tree)
- AgileX classroom Nav2 example (diff comments only, not vendored):
  [`agilex_open_class` `limo/limo_bringup/param/nav2.yaml`](https://github.com/agilexrobotics/agilex_open_class/blob/8e799754af623c3cec954b74b186d63d6ce8fa62/limo/limo_bringup/param/nav2.yaml)
  @ `8e799754af623c3cec954b74b186d63d6ce8fa62`
- Official Humble defaults: `navigation2` / `nav2_bringup/params/nav2_params.yaml` (`humble` branch)

## Diff summary (course overlay)

| Topic | Nav2 Humble TB3 | AgileX open_class | PhysiBot course |
|-------|-----------------|-------------------|-----------------|
| Local planner | DWB | DWB | Regulated Pure Pursuit (swap to DWB optional) |
| Base frame | `base_link` | `base_link` | `base_footprint` (course URDF) |
| Footprint | radius 0.22 | polygon ~0.30×0.20 | radius **0.20** |
| `max_vel` / smoother | ~0.26 m/s | ~0.26 m/s DWB | smoother **1.0** m/s (Limo Pro) |
| Goal xy tol | 0.25 | 0.15 | 0.15 |

Comments in `code/ros2_ws/src/physibot_bringup/config/nav2_params.yaml` record these choices.

## Course overlay plan

1. `physibot_bringup` launch files (canonical names — use these in chapters/labs):
   - `description.launch.py`
   - `sim_diff_drive.launch.py`
   - `localization.launch.py` (AMCL + map_server)
   - `mapping.launch.py` (slam_toolbox)
   - `nav2.launch.py` (includes `nav2_bringup`)
2. YAML configs in `code/ros2_ws/src/physibot_bringup/config/`:
   - Footprint radius ~0.20 m (from 322×220 mm body)
   - `max_velocity` linear 1.0 m/s (published Limo Pro limit)
3. Docker Compose profile `nav2` builds image with `INSTALL_NAV2=1`.
4. Physical robot (Ch. 12) reuses the same Nav2 graph with driver remaps.

## Open items

- [x] Costmap footprint numbers from published Limo Pro dimensions
- [x] CI host smoke that asserts lab/config files exist (no GPU)
- [x] Document AgileX + Nav2 Humble reference SHAs for param diffs (no vendor tree)
- [ ] Optional CI job: `ros2 launch` dry-run inside Humble container (see STATUS / smoke workflow)
