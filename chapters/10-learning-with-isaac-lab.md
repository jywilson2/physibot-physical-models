# Chapter 10 — Learning physical models with Isaac Lab

> **Status:** stub. **License:** CC BY-NC 4.0. **Hardware:** sim; DGX Spark optional for larger runs.

## Learning goals

- Place Isaac Lab in the PhysiBot stack (training + physics).
- Bridge Isaac Lab ↔ ROS 2 Humble using the official Lab `ros2` Docker profile.
- Train a small policy or dynamics residual (scope TBD) on a wheeled task.

## Outline

1. Isaac Lab mental model vs. Gazebo for this course.
2. Official Docker profiles: `base`, `ros2` (Humble), `kitless`.
3. Minimal wheeled / locomotion example adapted from Lab docs (not greenfield).
4. Export / checkpoint hygiene for later sim-to-real.
5. Lab: run a smoke training job locally or on a lab DGX Spark.

## Evidence / pins

- ROS 2 Humble via Isaac Lab `Dockerfile.ros2` — see `STATUS.md`.

## Adaptation notes

- `docs/adaptation-notes/isaac-lab.md`
