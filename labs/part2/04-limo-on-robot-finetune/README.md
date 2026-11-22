# Lab P2-04 — Limo on-robot fine-tuning (sketch)

**Chapters:** Part 2 · 06–07 (Spark scale in P2-08 as needed)  
**Hardware:** sim gate first; then **AgileX Limo Pro + Orin Nano**  
**Status:** outline only — fine-tune allowed; no hard GPU-time caps

## Goal

Deploy a sim-validated world-model / planner stack to the Orin Nano and run a
**supervised on-robot fine-tune** under lab safety rules. Heavy pretrain may
use DGX Sparks; Orin focuses on inference + light updates.

## Prefer adapting

- Classical [`labs/12-orin-deploy/`](../../12-orin-deploy/) image / networking checklists
- AgileX `limo_ros2` humble pin ([adaptation notes](../../../docs/adaptation-notes/limo.md))
- Course artifact sync from Spark jobs (Part 2 Ch. 08)

## Student path (sketch)

1. Pass P2-06 go / no-go checklist (sim metrics + e-stop drill).
2. Bring up sensors + teleop on Orin; verify TF / DDS / `ROS_DOMAIN_ID`.
3. Run frozen inference to a short goal; log interventions.
4. Collect fine-tune data; update allowed modules; re-evaluate same course.
5. Rollback plan tested once.

## Acceptance (sketch)

- [ ] Before/after metrics table.
- [ ] Safety abort demonstrated (or dry-run documented if hardware unavailable).
- [ ] No claim of unlimited hallway autonomy — fine-tune is supervised.

## Open

- Which modules are fine-tuned by default (dynamics only vs. full WM).
- Exact JetPack / image pins for the term (may stay LMS-local).
