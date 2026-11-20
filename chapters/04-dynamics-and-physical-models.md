# Chapter 04 — Dynamics and AI physical models

> **Status:** stub. **License:** CC BY-NC 4.0. **Hardware:** simulation only.

## Learning goals

- Contrast kinematic vs. dynamic models for wheeled robots.
- Introduce “physical models” as structured priors for control and learning.
- Sketch where learned residual / neural dynamics fit next to classical models.

## Outline

1. Mass, friction, actuator limits — why kinematics fail at speed.
2. Simple planar dynamic models (parameterized; identify later).
3. Physical-model viewpoint: constraints, energy, and inductive bias.
4. Bridge to Isaac Lab: training with physics engines as the world model.
5. Lab stub: parameter sweep in sim; observe tracking error growth.

## Pointers

- Isaac Lab chapters later expand learning; keep this chapter conceptual + light code.
