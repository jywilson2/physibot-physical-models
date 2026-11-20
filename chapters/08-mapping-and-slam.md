# Chapter 08 — Mapping and SLAM

> **Status:** stub. **License:** CC BY-NC 4.0. **Hardware:** simulation only.

## Learning goals

- Build occupancy grid maps from laser data.
- Explain SLAM as joint localization and mapping.
- Run an existing 2D SLAM stack in the course container (adapt, don’t reinvent).

## Outline

1. Occupancy grid mapping.
2. Pose-graph / filter SLAM intuition.
3. Course choice: adapt slam_toolbox / vendor Limo demos.
4. Lab: map a sim world; save map for Nav2.

## Lab

- Runnable writeup: `labs/08-mapping/`
- Launch: `ros2 launch physibot_bringup mapping.launch.py` (Nav2 Compose profile)

## Adaptation notes

- `docs/adaptation-notes/nav2.md`, `docs/adaptation-notes/limo.md`
