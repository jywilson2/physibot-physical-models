# Lab P2-03 — Planning via latent rollout (sketch)

**Chapters:** Part 2 · 04–05  
**Hardware:** simulation  
**Status:** outline only — replaces Nav2 as this track’s navigator

## Goal

Given a world-model checkpoint (Lab P2-01) and neural / learned occupancy
(Lab P2-02), plan to a pose goal by **rolling out in latent space** and emit
`/cmd_vel` (or a short trajectory) to the course diff-drive sim.

## Prefer adapting

- Course sim bringup: `sim_diff_drive.launch.py` / description stack (no Nav2 profile required)
- Sampling / MPC patterns familiar from Nav2 MPPI docs — **as algorithm vocabulary only**
- Isaac Lab evaluation loops for imagined rollouts

## Student path (sketch)

1. Load frozen WM + map head.
2. Implement receding-horizon action sampling / CEM-style search (stub OK this pass).
3. Score rollouts with goal cost + occupancy collision proxy.
4. Close the loop in sim; log success rate and interventions (keyboard e-stop).

## Acceptance (sketch)

- [ ] Goal reach demo in sim without `nav2.launch.py`.
- [ ] Failure analysis when the neural map is wrong.
- [ ] Footprint / speed clamps documented.

## Open

- Teaching planner default (CEM vs. MPPI-in-latent vs. other) — see `STATUS.md`.
