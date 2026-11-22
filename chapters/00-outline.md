# PhysiBot — Full course outline

Working brand: **PhysiBot** — AI physical models for mobile robotics.

Progression: math/kinematics refresh → physical models → estimation →
localization → mapping → navigation → Isaac Lab learning → sim-to-real →
Orin Nano deploy → DGX Spark training → capstone.

Physical AgileX Limo Pro appears only from mid/late course; early work is
Docker + simulation. Narrative chapters `01`–`14` are full prose.
Course launches: `description`, `sim_diff_drive`, `localization`, `mapping`,
`nav2` (plus `sim_stub` for smoke). Isaac Lab pin: **`v3.0.0`**.

| Ch | File | Theme | Hardware |
|----|------|-------|----------|
| 01 | `01-welcome-and-docker.md` | Course goals, brand, Docker workflow | None (sim/Docker) |
| 02 | `02-linear-algebra-refresh.md` | Vectors, frames, transforms | None |
| 03 | `03-mobile-robot-kinematics.md` | Differential / Ackermann kinematics | Sim |
| 04 | `04-dynamics-and-physical-models.md` | Dynamics + AI physical models | Sim |
| 05 | `05-sensing-and-observation-models.md` | Sensors, observation models | Sim |
| 06 | `06-estimation-fundamentals.md` | Bayes, KF / EKF / UKF | Sim |
| 07 | `07-localization.md` | Pose estimation, AMCL-class methods | Sim |
| 08 | `08-mapping-and-slam.md` | Occupancy maps, SLAM concepts | Sim |
| 09 | `09-navigation-with-nav2.md` | Nav2 stack (adapt existing) | Sim |
| 10 | `10-learning-with-isaac-lab.md` | Isaac Lab + physical model learning | Sim / DGX optional |
| 11 | `11-sim-to-real.md` | Domain gap, calibration, validation | Sim → lab |
| 12 | `12-orin-nano-deploy.md` | Deploy on Jetson Orin Nano | **Limo Pro + Orin** |
| 13 | `13-dgx-spark-training.md` | DGX Spark training workflows | **Lab DGX Sparks** |
| 14 | `14-capstone.md` | Integrated project | Lab as assigned |

ROS 2 distro for all student containers: **Humble** (Isaac Lab–aligned). See `STATUS.md`.

## Alternate Part 2 — learned navigation (addition)

On branch `learned_navigation`, an **alternate Part 2** explores latent world-model
navigation that **replaces** the Nav2 / AMCL / SLAM arc for that track only. It is
an **addition** to this textbook, not a global deletion of Chapters 07–09.

- Outline + stubs: [`part2/00-outline.md`](part2/00-outline.md)
- Labs sketch: [`../labs/part2/`](../labs/part2/)
- Quarto: [`../textbook/physibot-part2.qmd`](../textbook/physibot-part2.qmd)
- Review status / open questions: [`../STATUS.md`](../STATUS.md)

Shared foundation remains Chapters **01–06**. Classical **07–14** stay the Nav2 track.

## How to read

- Each chapter ends with labs/exercises that cross-link `docker/`, `code/ros2_ws/`, and `docs/adaptation-notes/`.
- Runnable labs (sim-first): `labs/` — start at `labs/README.md`.
- Prefer upstream Nav2 / Isaac Lab / AgileX docs for flags that churn; chapters teach structure and pedagogy.
- Textbook exports: see `textbook/README.md`.
