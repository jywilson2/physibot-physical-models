# Part 2 · Chapter 05 — Planning via latent rollout

> **License:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).  
> **Hardware:** simulation (physical goals only after P2-06 gate).  
> **Lab sketch:** [`labs/part2/03-latent-rollout-planning/`](../../labs/part2/03-latent-rollout-planning/).  
> **Maps from classical:** **replaces** Ch. 09 Nav2 (global planner + DWB + BT) as this track’s navigator.

## Learning outcomes

1. Formulate goal-directed navigation as **search / optimization over imagined latent trajectories**.
2. Interface a rollout planner to ROS 2 (`cmd_vel` or short trajectory) on the course Limo footprint.
3. Use learned occupancy (P2-03) as a constraint or cost inside the rollout.
4. Debug open-loop imagination failures vs. classical costmap / controller failures.

## 5.1 Nav2 is the other track

This chapter is **not** “plug a network into Nav2’s controller.” Locked decision: replace the Nav2 navigation arc. Students may still *read* Ch. 09 for vocabulary (goals, footprints, recoveries), but the executable story here is:

```text
Goal (pose or latent target)
   ↓
Sample / optimize action sequence a_{t:t+H}
   ↓
Roll out ẑ with f_ψ (+ occupancy / reward heads)
   ↓
Execute first action(s) → cmd_vel; replan
```

## 5.2 Section skeleton (to expand)

| § | Working title | Notes |
|---|----------------|-------|
| 5.2 | Planners | CEM / MPPI-in-latent / shooting MPC — pick teaching default later |
| 5.3 | Costs | Goal distance, collision from neural map, control smoothness |
| 5.4 | Receding horizon | Replan rate vs. Orin compute budget (preview P2-07) |
| 5.5 | Safety layers | Hard clamps, footprint, e-stop — independent of the WM |

## 5.3 Exercises (sketch)

1. Compare DWB local tracking on a costmap to MPPI-style sampling in latent space (one page).
2. Given a hallucinated free corridor in the neural map, describe a detection + fallback policy.

## Pedagogical defaults (sketch)

- Teaching planner family: **TBD** (open in `STATUS.md`); lean toward receding-horizon sampling for continuity with Nav2 MPPI vocabulary.
- Output: `/cmd_vel` compatible with Part 1 sim packages.
