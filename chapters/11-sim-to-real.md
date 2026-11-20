# Chapter 11 — Sim-to-real transfer

> **License:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).  
> **Hardware:** preparation for lab robot; physical operation begins in Chapter 12.  
> **Lab code:** checklists here; deploy scripts land with Ch. 12 ([`docs/adaptation-notes/limo.md`](../docs/adaptation-notes/limo.md)).

## Learning goals

1. Name primary sources of sim-to-real gap for wheeled indoor robots.
2. Plan calibration, latency, and safety checks before physical runs.
3. Define success metrics that transfer from simulation to the AgileX Limo Pro.
4. Complete a go / no-go checklist used as the gate into Chapter 12.

## 11.1 The gap is a modeling problem

Sim-to-real failure is usually not mystical—it is mismatched **physical models**:

| Gap source | Example on Limo-class robots |
|------------|------------------------------|
| Contact / friction | Carpet vs. Gazebo friction coeffs |
| Actuator dynamics | Torque limits, deadband, latency |
| Sensing | LiDAR reflectivity, IMU bias, missing glass |
| Timing | Sim stepped vs. real DDS jitter |
| Compute | Laptop GPU vs. Orin Nano CPU budget |
| Extrinsics | URDF guess ≠ measured laser mount |

Chapter 04 gave parameters; Chapter 05 gave observation models; Nav2 assumed both. This chapter forces an honest inventory before anyone enables motors on a physical base.

## 11.2 Two complementary tools

**System identification.** Estimate \(m, c_v,\) wheel radius scale, latency from step responses and bagged trajectories on the *real* robot (or a high-fidelity sim that you trust). Feed identified parameters back into controllers and residual learners.

**Domain randomization.** In Isaac Lab (Ch. 10), randomize friction, mass, sensor noise so policies are less brittle. Randomization without a safety envelope still fails on hardware—treat it as complementary, not magical.

## 11.3 Latency and compute

Measure:

1. Time from `/cmd_vel` publish to observed wheel response (or IMU surge).
2. Laser → AMCL → controller loop rates on the Orin Nano target.
3. Whether Nav2 configurations that worked on a desktop still meet control rates on-robot.

If the Orin Nano cannot sustain your sim CPU rate, simplify observation pipelines before blaming the algorithm.

## 11.4 Safety envelope for first physical tests

Non-negotiables (adapt to local lab rules):

1. Supervised operation with a clear e-stop owner.
2. Soft velocity caps far below mechanical limits.
3. Open space free of cables that wind into wheels.
4. No unsupervised “just one Nav2 goal” overnight runs.
5. Logging enabled before motion.

Sim practice: rehearse the same recovery behaviors and teleop takeover you will use on hardware.

## 11.5 Metrics that transfer

Pick metrics you can compute on both sides:

| Metric | Sim | Real |
|--------|-----|------|
| Goal success rate | Easy | Easy with supervision |
| Path tracking RMSE vs. reference | vs. Gazebo truth | vs. surveyed path / mocap if available |
| Localization variance / NIS | Yes | Yes (no truth required) |
| Mean time between manual interventions | Proxy | Critical |

Avoid metrics that only exist in sim (perfect ATE) as your sole gate.

## 11.6 Lab 11 — Pre-deploy checklist (desk exercise + sim)

Complete and submit:

1. **Parameter inventory** — list URDF extrinsics, Nav2 velocity limits, and filter covariances you will re-validate on hardware.
2. **Bag comparison plan** — which topics to record on first physical teleop (mirror Ch. 05).
3. **Kill switch drill** — who holds e-stop; verbal protocol.
4. **Success definition** — e.g. “two supervised Nav2 goals in the lab arena with ≤1 intervention.”
5. **No-go criteria** — e.g. TF tree incomplete, laser rate < X Hz, brake/e-stop untested.

Optional sim stress: add noise to `/scan` ranges and latency to `/cmd_vel` using a relay node; note when AMCL/Nav2 break.

## 11.7 Exercises

1. Rank the top three gap sources for *your* lab environment and justify.
2. Why can domain randomization hide a wrong laser extrinsic until the policy faces a narrow door?
3. *(Grad)* Read a sim-to-real survey section assigned by the instructor; map each cited method onto identification vs. randomization vs. adaptation.

## 11.8 Further reading

- Tobin et al., domain randomization (classic reference)
- Zhao, Queralta, Westerlund — sim-to-real surveys in robotics (pick a current review)
- Vendor Limo + Orin bringup safety notes
- Course Chapters 04, 05, 10 as prerequisites

## Professor edit notes

- Insert lab-specific e-stop and arena rules.
- Provide the official go/no-go form students must print for Ch. 12.
