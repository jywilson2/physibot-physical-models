# Part 2 · Chapter 01 — Latent world models for navigation

> **License:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).  
> **Hardware:** simulation / reading only.  
> **Sketch:** conceptual spine — full worked examples land in later passes.  
> **Maps from classical:** bridges after Ch. 06; **replaces** the assumption that navigation = Nav2 costmaps + BT (Ch. 09).

## Learning outcomes

By the end of this chapter you should be able to:

1. Define a **latent world model** as encoder + dynamics + decoder (or reward/value head) used for navigation.
2. Contrast **rollout-based planning** with classical global planners on occupancy costmaps.
3. Place learned occupancy / neural maps as inputs or side products of the world model (preview of P2-03).
4. State why PhysiBot Part 2 treats Nav2 as the *other* track, not a residual wrapper around a neural policy.

## 1.1 From physical models to latent dynamics

Part 1 gave you explicit models: unicycle kinematics, simple dynamics \(f_\theta\), observation likelihoods, and Bayesian filters. A **world model** keeps that idea—predict what happens next—but moves the state into a **latent** \(z_t\):

\[
z_t = e_\phi(o_{\le t}), \qquad
\hat{z}_{t+1} = f_\psi(z_t, a_t), \qquad
\hat{o}_{t+1} \approx d_\theta(\hat{z}_{t+1}).
\]

Navigation then becomes: choose actions whose **imagined** rollouts reach a goal (or maximize return) while respecting constraints encoded in \(z\) or an auxiliary map head.

## 1.2 Why not pure imitation of `cmd_vel`?

Locked course architecture: **latent world model with rollout for planning**, not sensor→twist imitation as the primary story. Imitation can bootstrap, but the pedagogical spine is:

- Learn \(f_\psi\) (and related heads) that support multi-step imagination.
- Plan by searching or optimizing action sequences in latent space.
- Fine-tune on-robot when the gap shows up (P2-07).

## 1.3 Section skeleton (to expand)

| § | Working title | Notes for full draft |
|---|----------------|----------------------|
| 1.3 | Taxonomy | RSSM-style, Dreamer-class, JEPA-like, occupancy-centric hybrids — teach *roles*, not one paper |
| 1.4 | Interfaces to ROS 2 | Observations in; `cmd_vel` / trajectory out; TF still matters |
| 1.5 | Safety envelope | Rollouts do not remove e-stop, speed limits, or footprint checks |
| 1.6 | Reading list | Pointers to upstream Isaac Lab / WM tutorials (staff-pinned each term) |

## 1.4 Exercises (sketch)

1. Given a Part 1 EKF block diagram, redraw it with \(z_t\) and a rollout planner instead of AMCL + Nav2 controller.
2. List three failure modes unique to open-loop latent rollouts vs. DWB on a costmap.

## Pedagogical defaults (sketch)

- Architecture: **latent WM + rollout planning** (locked).
- Classical Nav2 chapters remain available on the other track; do not delete them from student mental models—**contrast** them.
