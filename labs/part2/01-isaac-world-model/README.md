# Lab P2-01 — Isaac Lab world-model training (sketch)

**Chapters:** Part 2 · 01–02  
**Hardware:** simulation (GPU recommended; Spark optional)  
**License (ops text):** Apache-2.0 course ops; narrative CC BY-NC 4.0  
**Status:** outline only — no full training code in this pass

## Goal

Stand up Isaac Lab (pinned tag in `STATUS.md`, **`v3.0.0`** baseline) with the
official **`ros2`** / Humble profile and adapt an existing wheeled / locomotion
example into a **minimal world-model training** loop (encoder + dynamics ±
decoder). Deliver a teaching-scale checkpoint and logged prediction metrics.

## Prefer adapting

- NVIDIA Isaac Lab Docker / `container.py` workflows ([adaptation notes](../../../docs/adaptation-notes/isaac-lab.md))
- Existing Lab locomotion / imagination-related tutorials for the pinned tag
- Course mount pattern from classical [`labs/10-isaac-lab/`](../../10-isaac-lab/)

## Student path (sketch)

1. Verify pin + pull Lab image / clone tag per adaptation notes.
2. Run a smoke env (cart / wheeled) from upstream docs.
3. Enable a stub WM loss (reconstruction / next-latent) — **implementation TBD**.
4. Export checkpoint + metrics JSON to the course artifact layout (not git).

## Acceptance (sketch)

- [ ] Documented commands reproduce a short train step on Lab hardware or Spark.
- [ ] Artifact IDs recorded in the lab handin template (LMS).
- [ ] No Nav2 runtime required.

## Open

- Exact upstream example name for the term (see `STATUS.md` Part 2 questions).
