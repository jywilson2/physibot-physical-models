# Adaptation: Navigation2

## Intent

Teach localization, mapping handoff, and navigation using **Nav2** on a
Limo-class footprint. Prefer official Nav2 tutorials and existing Limo Nav2
configs over custom planners.

## Upstream pointers

- [Nav2 documentation](https://docs.nav2.org/)
- Nav2 Getting Started + configuration guides for Humble
- slam_toolbox (or vendor-recommended 2D SLAM) for Chapter 08 map building

## Course overlay plan

1. Provide `physibot_bringup` launch files that include Nav2 with parameters
   tuned for the course sim robot (footprint, inflations, velocities).
2. Keep YAML configs in `code/ros2_ws/src/physibot_bringup/config/` once adapted.
3. Physical robot (Ch. 12) reuses the same Nav2 graph with driver remaps.

## Open items

- [ ] Vendor or community Limo + Nav2 example SHA
- [ ] Costmap footprint numbers from real Limo Pro dimensions
- [ ] CI smoke that only asserts launch file XML/Python loads (no GPU)
