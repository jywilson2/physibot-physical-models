# Part 2 · Chapter 08 — DGX Spark world-model scale

> **License:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).  
> **Hardware:** lab **NVIDIA DGX Sparks** (shared; students do not own them).  
> **Maps from classical:** adapts Ch. 13 for larger world-model / neural-map jobs; same queue etiquette.

## Learning outcomes

1. Explain Sparks as shared instruments for WM pretrain / heavy fine-tune—not personal GPUs.
2. Submit or run a containerized Isaac Lab world-model job on a Spark using the term pin.
3. Sync checkpoints into the course artifact layout for Orin deploy / fine-tune (P2-07).
4. Compare laptop vs. Spark turnaround for the same teaching config.

## 8.1 No hard GPU-time caps — still shared hardware

Course policy for this track: **no hard student GPU-time caps** as a pedagogical limit. Lab operations still require booking, cleanup, and fair use. Document LMS queue URLs outside git (classical Ch. 13 pattern).

## 8.2 Section skeleton (to expand)

| § | Working title | Notes |
|---|----------------|-------|
| 8.2 | What belongs on Spark | Pretrain WM, large neural maps, long horizon eval |
| 8.3 | What stays on Orin | Inference, light fine-tune, teleop bags |
| 8.4 | Artifact contract | Checkpoint naming shared with P2-02 / P2-07 |
| 8.5 | Failure drills | Spot killed mid-epoch; resume from last ckpt |

## 8.3 Exercises (sketch)

1. Draw a dataflow: Spark train → artifact store → Orin pull → fine-tune → metrics back.
2. Propose a “teaching vs. stretch” config pair for one booking slot.

## Pedagogical defaults (sketch)

- Same Isaac Lab **`v3.0.0`** pin as P2-02 unless staff announce otherwise.
- Prefer adapting Lab’s Docker / `container.py` path over custom cluster scripts.
