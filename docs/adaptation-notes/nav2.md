# Adaptation: Navigation2

## Intent

Teach localization, mapping handoff, and navigation using **Nav2** on a
Limo-class footprint. Prefer official Nav2 tutorials and existing Limo Nav2
configs over custom planners.

## Upstream pointers

- [Nav2 documentation](https://docs.nav2.org/)
- Nav2 Getting Started + configuration guides for Humble
- slam_toolbox (or vendor-recommended 2D SLAM) for Chapter 08 map building
- AgileX `limo_ros2` (`humble`) navigation / SLAM launch examples

## Course overlay plan

1. `physibot_bringup` launch files:
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
- [ ] Vendor or community Limo + Nav2 example SHA
- [ ] Optional CI job: `ros2 launch` dry-run inside Humble container
