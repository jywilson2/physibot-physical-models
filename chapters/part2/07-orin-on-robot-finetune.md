# Part 2 · Chapter 07 — Orin Nano on-robot fine-tuning

> **License:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).  
> **Hardware:** **AgileX Limo Pro + NVIDIA Jetson Orin Nano** (after P2-06 gate).  
> **Lab sketch:** [`labs/part2/04-limo-on-robot-finetune/`](../../labs/part2/04-limo-on-robot-finetune/).  
> **Maps from classical:** adapts Ch. 12 — deploy **plus** on-robot fine-tuning; not Nav2-goal-only.

## Learning outcomes

1. Deploy the sim-validated world-model / planner stack onto the Orin Nano course image.
2. Run a supervised fine-tune loop (collect → update → evaluate) under lab safety rules.
3. Budget Orin CPU/GPU for drivers + inference + light training (Sparks remain heavy training).
4. Compare pre- vs post-fine-tune metrics on the same physical course.

## 7.1 Fine-tune is in-scope

Locked decision: **on-robot fine-tuning allowed**; no hard student GPU-time caps. That does **not** mean unsupervised overnight training on a busy hallway. Staff still set booking windows, e-stop ownership, and artifact paths ([`docs/adaptation-notes/limo.md`](../../docs/adaptation-notes/limo.md)).

## 7.2 Section skeleton (to expand)

| § | Working title | Notes |
|---|----------------|-------|
| 7.2 | Image + bringup | Reuse classical Orin pins; overlay learned-nav nodes |
| 7.3 | Inference vs. fine-tune modes | Freeze encoder? Update dynamics only? |
| 7.4 | Data capture | Bags, privilege, PII-free lab floors |
| 7.5 | Rollback | How to revert to last good checkpoint |

## 7.3 Exercises (sketch)

1. Write a fine-tune runbook with abort criteria (collision near-miss, thermal throttle, DDS loss).
2. Estimate Orin memory for a teaching-scale WM; list what moves to Spark if OOM.

## Pedagogical defaults (sketch)

- Progression: teleop → frozen inference → short fine-tune → supervised eval.
- Secrets / SSIDs stay on LMS, not git.
