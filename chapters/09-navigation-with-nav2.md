# Chapter 09 — Navigation with Nav2

> **Status:** stub. **License:** CC BY-NC 4.0. **Hardware:** simulation only (physical later).

## Learning goals

- Configure Nav2 for a differential-drive footprint matching Limo-class geometry.
- Send goals and interpret costmaps / planners / controllers.
- Debug common Nav2 failure modes in sim.

## Outline

1. Nav2 architecture overview.
2. Costmaps, planners, controllers — configuration map to Limo.
3. Behavior trees at a high level.
4. Lab: navigate a mapped sim environment end-to-end.

## Lab

- Runnable writeup: `labs/09-nav2/`
- Launch: `ros2 launch physibot_bringup nav2.launch.py` (Nav2 Compose profile)

## Adaptation notes

- Prefer official Nav2 tutorials + AgileX Limo Nav2 examples; see `docs/adaptation-notes/nav2.md`.
