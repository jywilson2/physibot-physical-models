# Part 2 · Chapter 02 — Isaac Lab world-model training

> **License:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).  
> **Hardware:** simulation; GPU recommended. DGX Spark optional for larger runs (P2-08).  
> **Lab sketch:** [`labs/part2/01-isaac-world-model/`](../../labs/part2/01-isaac-world-model/).  
> **Maps from classical:** expands / relocates Ch. 10 Isaac Lab content; Ch. 10 prose on `main` stays for the Nav2 track.

## Learning outcomes

1. Run Isaac Lab via the official **`ros2`** Docker profile (**Humble**) pinned for the term (`v3.0.0` unless `STATUS.md` updates).
2. Adapt an existing Lab wheeled / locomotion or imagination-style example into a **world-model training** loop (no greenfield task suite).
3. Log checkpoints, rollouts, and metrics into the course artifact layout (not git blobs).
4. Explain sim-first gates before any on-robot fine-tune.

## 2.1 Isaac Lab as the Part 2 training home

In the classical track, Isaac Lab appears late (Ch. 10) after Nav2 literacy. In this alternate Part 2, Lab is the **primary** place students train \(e_\phi, f_\psi,\) and map heads. Everyday ROS still uses [`docker/compose.yaml`](../../docker/compose.yaml); Lab uses upstream containers ([`docs/adaptation-notes/isaac-lab.md`](../../docs/adaptation-notes/isaac-lab.md)).

## 2.2 Adapt, don’t invent

Prefer:

1. Current Isaac Lab locomotion / wheeled tutorials for the pinned tag.
2. Course overlay mounts of `code/ros2_ws` as documented in Lab 10 / Part 2 Lab 1.
3. Small teaching configs first; scale on Sparks (P2-08) without inventing a new cluster OS.

Exact upstream example names remain an **open STATUS question** (tutorials rename across Lab versions).

## 2.3 Section skeleton (to expand)

| § | Working title | Notes |
|---|----------------|-------|
| 2.3 | Env + observation design | Proprioception, camera/lidar encodings for Limo-class |
| 2.4 | Training loop sketch | Dataset / online rollouts, losses for dynamics + reconstruction / occupancy |
| 2.5 | Checkpoint hygiene | Same artifact rules as classical Ch. 13 |
| 2.6 | ROS 2 bridge | When to emit latent goals vs. raw `cmd_vel` |

## 2.4 Exercises (sketch)

1. Diff a classical Lab 10 “policy” README against Part 2 Lab 1: what changes when the target is a world model?
2. Propose a minimum viable metric set (prediction error, rollout horizon usefulness, collision proxy).

## Pedagogical defaults (sketch)

- Pin: Isaac Lab **`v3.0.0`** + Humble `ros2` profile until re-verified.
- No hard student GPU-time caps; queue etiquette still applies on Sparks.
