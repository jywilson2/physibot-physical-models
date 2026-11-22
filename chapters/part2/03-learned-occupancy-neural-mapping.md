# Part 2 · Chapter 03 — Learned occupancy & neural mapping

> **License:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).  
> **Hardware:** simulation.  
> **Lab sketch:** [`labs/part2/02-neural-mapping/`](../../labs/part2/02-neural-mapping/).  
> **Maps from classical:** **replaces** Ch. 08 mapping / SLAM as the primary map story for this track. Classical occupancy + slam_toolbox remain on the Nav2 track.

## Learning outcomes

1. Explain **learned occupancy** / neural mapping as a first-class navigation product (not a visualization side quest).
2. Contrast grid occupancy from laser SLAM with continuous or hybrid neural map representations.
3. Produce (or load) a course-format neural / learned-occupancy artifact usable by latent planning (P2-05).
4. State failure modes (hallucinated free space, topology errors) and how to evaluate them in sim.

## 3.1 Why maps still matter

World-model rollouts need somewhere to put “obstacle” and “goal.” Part 2 does **not** throw away maps; it changes how maps are **built and queried**. Learned occupancy may be:

- A decoder head \(m = h_\eta(z)\) over latents,
- A separate neural field / BEV network trained jointly or alternately,
- A hybrid: classical prior map + learned residual occupancy.

## 3.2 First-class lab outcome

Locked decision: neural / learned occupancy is a **graded lab deliverable**. Students should leave Lab 2 with a reproducible artifact (checkpoint + metadata + sim screenshot / metric dump), even if weights are teaching-scale.

## 3.3 Section skeleton (to expand)

| § | Working title | Notes |
|---|----------------|-------|
| 3.3 | Representations | Grid logits, BEV, implicit fields — pick one teaching default later |
| 3.4 | Supervision | Pseudo-labels from sim ground truth vs. self-supervised |
| 3.5 | Query API for planners | How P2-05 asks “is this latent trajectory in collision?” |
| 3.6 | Comparison table | vs. Ch. 08 slam_toolbox / occupancy grid |

## 3.4 Exercises (sketch)

1. Write a one-page comparison: classical `map` → `costmap_2d` vs. learned occupancy query in a rollout loop.
2. Design a sim metric that penalizes false-free cells more than false-occupied (safety asymmetry).

## Pedagogical defaults (sketch)

- Teaching default representation: **TBD** (open question in `STATUS.md`) — lean toward BEV / grid logits for ROS familiarity.
- Keep Humble + course TF conventions (`map` / `odom` / `base_link`) even when the map is neural.
