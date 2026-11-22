# Lab P2-02 — Learned occupancy / neural mapping (sketch)

**Chapters:** Part 2 · 03  
**Hardware:** simulation  
**Status:** outline only — first-class lab outcome for Part 2

## Goal

Produce a **learned occupancy / neural map** artifact from sim trajectories
(and/or world-model latents from Lab P2-01). This map must be queryable by the
latent rollout planner (Lab P2-03).

## Prefer adapting

- Isaac Lab perception / occupancy-style examples when available for the pin
- Sim ground-truth occupancy from the course stub / Gazebo worlds as supervision
- Classical map frame conventions (`map` / `odom` / `base_link`) for overlays

## Student path (sketch)

1. Collect or replay a sim trajectory with known free/occupied labels.
2. Train or fit a teaching-scale map head (grid logits / BEV — default TBD).
3. Export map artifact + evaluation (precision/recall or IoU; safety-weighted).
4. Visualize overlay vs. classical occupancy for contrast (optional).

## Acceptance (sketch)

- [ ] Reproducible artifact + metric dump.
- [ ] Written note on false-free vs. false-occupied asymmetry.
- [ ] Explicitly **not** graded as “run slam_toolbox” (that remains classical Lab 08).

## Open

- Teaching default representation (BEV vs. grid vs. implicit) — professor review.
