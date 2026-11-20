# PhysiBot — Full course outline

Working brand: **PhysiBot** — AI physical models for mobile robotics.

Progression: math/kinematics refresh → physical models → estimation →
localization → mapping → navigation → Isaac Lab learning → sim-to-real →
Orin Nano deploy → DGX Spark training → capstone.

Physical AgileX Limo Pro appears only from mid/late course; early work is
Docker + simulation.

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
