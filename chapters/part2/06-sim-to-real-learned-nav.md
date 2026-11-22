# Part 2 · Chapter 06 — Sim-to-real for learned navigation

> **License:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).  
> **Hardware:** preparation for lab robot; physical motion gated like classical Ch. 11.  
> **Maps from classical:** adapts Ch. 11; shared gap taxonomy, new metrics for world models and neural maps.

## Learning outcomes

1. Reuse Part 1 sim-to-real gap sources (contact, actuators, sensing, timing, compute, extrinsics).
2. Add WM-specific gaps: latent distribution shift, map hallucination, rollout horizon collapse.
3. Define go / no-go criteria before on-robot fine-tuning (P2-07).
4. Plan logging so fine-tunes are attributable (bags + checkpoint IDs).

## 6.1 Same physics, different brittle points

Domain randomization and system ID from classical Ch. 11 still apply. Learned-nav adds:

| Gap | Symptom |
|-----|---------|
| Encoder shift | Latent jumps; planner oscillates |
| Dynamics bias | Rollouts optimistic on carpet / payload |
| Neural map errors | Paths through real obstacles |
| Compute latency | Horizon too short on Orin vs. Spark |

## 6.2 Section skeleton (to expand)

| § | Working title | Notes |
|---|----------------|-------|
| 6.2 | Calibration checklist | Extends classical Ch. 11 table |
| 6.3 | Domain randomization for WM | Which params to randomize first |
| 6.4 | Success metrics | Goal reach, collisions, intervention count |
| 6.5 | Go / no-go gate | Required before Lab 4 motors-enabled fine-tune |

## 6.3 Exercises (sketch)

1. Draft a one-page go / no-go checklist specific to latent rollout (not Nav2 BT).
2. Propose a fine-tune data budget (trajectories / minutes) without a hard GPU-time cap narrative.

## Pedagogical defaults (sketch)

- Sim-first remains mandatory.
- No hard GPU-time caps; still require **safety** and **queue** discipline.
