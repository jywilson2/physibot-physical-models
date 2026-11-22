# Part 2 · Chapter 04 — Latent state & localization

> **License:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).  
> **Hardware:** simulation.  
> **Lab sketch:** shared setup with [`labs/part2/03-latent-rollout-planning/`](../../labs/part2/03-latent-rollout-planning/).  
> **Maps from classical:** **replaces** Ch. 07 AMCL as the primary localizer for this track. Particle filters stay as contrast / optional reading.

## Learning outcomes

1. Distinguish latent state \(z_t\) from SE(2) pose \(x_t\) and explain when you need both.
2. Describe encoder-based localization / belief updates without AMCL as the runtime dependency.
3. Evaluate pose / goal-reaching error in sim with the same honesty standards as Ch. 07.
4. Keep REP-105 frame discipline even when the estimator is learned.

## 4.1 Belief without particles (as the default)

Classical Ch. 07 centers AMCL on a known occupancy map. Part 2’s default is: the world model’s latent (and optional pose head) **is** the belief for planning. Particles may still appear as a teaching contrast or as a bootstrap for map-frame alignment—not as the stack you ship for this track’s Nav2 replacement.

## 4.2 Section skeleton (to expand)

| § | Working title | Notes |
|---|----------------|-------|
| 4.2 | Pose heads vs. pure latent | When to decode \(x_t \in SE(2)\) for ROS tools |
| 4.3 | Kidnapped robot analogue | Reset / re-encode strategies |
| 4.4 | Observability | What lidar/camera must provide for \(e_\phi\) |
| 4.5 | Metrics | ATE / RPE / success under occlusion |

## 4.3 Exercises (sketch)

1. Map AMCL’s motion + measurement update onto encoder + dynamics steps.
2. Propose a recovery behavior when latent reconstruction error spikes (without calling Nav2 recoveries).

## Pedagogical defaults (sketch)

- Runtime stack for this track: **learned belief**, not AMCL.
- Students who completed classical Lab 07 may reuse maps only as **evaluation** overlays.
