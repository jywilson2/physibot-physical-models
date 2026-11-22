# PhysiBot Part 2 — Learned navigation (alternate track)

> **License:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) (see `chapters/LICENSE`).  
> **Status:** **Sketch** for professor review — narrative spine and lab sequence only; no production training pipelines yet.  
> **Branch:** `learned_navigation` (addition to the textbook; classical Part 1 + Nav2 path remains on `main`).

## What this Part 2 is

An **alternate navigation arc** that replaces the classical **AMCL → SLAM / occupancy → Nav2** sequence with a **latent world-model** stack: train a dynamics model in Isaac Lab, build **learned occupancy / neural maps**, plan by **rolling out in latent space**, then **fine-tune on the AgileX Limo Pro** (Orin Nano / DGX Spark backends). Sim-first still applies; GPU time is **not** hard-capped for students.

This Part 2 is intended to **sit as an addition** beside the existing textbook. It does **not** delete or globally rewrite Chapters 07–09 on `main`. Cohorts may run the classical Nav2 track, this learned-nav track, or both as staff assign.

## Shared foundation (unchanged)

Students still complete **Part 1 classical physical models** before branching:

| Ch | Theme | Role for Part 2 |
|----|-------|-----------------|
| 01 | Welcome + Docker | Same containers / Humble pin |
| 02 | Linear algebra refresh | Frames, transforms for latent ↔ body |
| 03 | Mobile robot kinematics | Diff-drive / unicycle priors |
| 04 | Dynamics + AI physical models | \(f_\theta + g_\phi\) vocabulary for world models |
| 05 | Sensing + observation models | Sensors that feed encoders |
| 06 | Estimation fundamentals | Bayes / filters as contrast to latent belief |

ROS 2 **Humble** and Isaac Lab **`v3.0.0`** pins match Part 1 (`STATUS.md`).

## What this track replaces vs keeps

| Classical (Part 1 mid-course) | Learned-nav Part 2 | Notes |
|-------------------------------|--------------------|-------|
| Ch. 07 AMCL / particle localization | **P2-04** Latent state & localization | Latent belief / encoder pose; AMCL optional contrast only |
| Ch. 08 Occupancy mapping / SLAM | **P2-03** Learned occupancy / neural mapping | **First-class lab outcome** |
| Ch. 09 Nav2 (planner + DWB + BT) | **P2-05** Planning via latent rollout | World-model MPC / CEM-style search — **not** a Nav2 residual add-on |
| Ch. 10 Isaac Lab intro (late) | **P2-01–P2-02** World models + Isaac Lab training | Isaac Lab moves **earlier** as the primary training home |
| Ch. 11 Sim-to-real | **P2-06** Sim-to-real for learned nav | Same gap taxonomy; metrics for policies / rollouts |
| Ch. 12 Orin deploy (Nav2 on robot) | **P2-07** On-robot fine-tuning | Deploy **and** fine-tune; no GPU-time hard caps |
| Ch. 13 DGX Spark training | **P2-08** World-model scale on Sparks | Same shared-instrument rules; larger WM runs |
| Ch. 14 Capstone (Nav2 options) | **P2-09** Learned-nav capstone | Capstone options rewritten for WM stack |

**Stays shared:** Docker workflow, URDF / frames, kinematics and dynamics language, Humble + Lab pins, Limo Pro hardware story, Spark booking principles, safety / `ROS_DOMAIN_ID` / e-stop.

## Part 2 chapter list (sketch)

| # | File | Title | Hardware |
|---|------|-------|----------|
| P2-01 | `01-latent-world-models.md` | Latent world models for navigation | Sim |
| P2-02 | `02-isaac-lab-world-model-training.md` | Isaac Lab world-model training | Sim / Spark |
| P2-03 | `03-learned-occupancy-neural-mapping.md` | Learned occupancy & neural mapping | Sim |
| P2-04 | `04-latent-state-and-localization.md` | Latent state & localization | Sim |
| P2-05 | `05-planning-via-latent-rollout.md` | Planning via latent rollout | Sim |
| P2-06 | `06-sim-to-real-learned-nav.md` | Sim-to-real for learned navigation | Sim → lab |
| P2-07 | `07-orin-on-robot-finetune.md` | Orin Nano on-robot fine-tuning | **Limo + Orin** |
| P2-08 | `08-dgx-spark-world-model-scale.md` | DGX Spark world-model scale | **Lab Sparks** |
| P2-09 | `09-capstone-learned-navigation.md` | Capstone: learned navigation | Lab as assigned |

## Lab sequence (sketch)

Prefer adapting existing Isaac Lab / ROS 2 Humble / Limo examples over greenfield stacks. Full training code is a **later** pass.

| Lab | Directory | Ties to | Outcome |
|-----|-----------|---------|---------|
| 1 | [`labs/part2/01-isaac-world-model/`](../../labs/part2/01-isaac-world-model/) | P2-01–02 | Train / run a stub world-model loop in Isaac Lab |
| 2 | [`labs/part2/02-neural-mapping/`](../../labs/part2/02-neural-mapping/) | P2-03 | Produce a learned occupancy / neural map artifact |
| 3 | [`labs/part2/03-latent-rollout-planning/`](../../labs/part2/03-latent-rollout-planning/) | P2-04–05 | Plan goals by latent rollout → `cmd_vel` |
| 4 | [`labs/part2/04-limo-on-robot-finetune/`](../../labs/part2/04-limo-on-robot-finetune/) | P2-06–07 | On-robot fine-tune (sim gate first) |

## How to read with Part 1

1. Complete Chapters **01–06** (shared).
2. **Either** continue classical **07–14** (Nav2 track on `main`), **or** enter this Part 2 outline, **or** survey both if staff assign a comparison project.
3. Export sketch: [`textbook/physibot-part2.qmd`](../../textbook/physibot-part2.qmd) (separate from the classical Quarto book).

## Non-goals of this sketch pass

- Shipping trained policy weights or a full student GPU cluster playbook.
- Removing Nav2 packages / labs from the classical tree.
- Claiming a single upstream “official” world-model API — pins and example names stay open for professor review (see `STATUS.md`).
