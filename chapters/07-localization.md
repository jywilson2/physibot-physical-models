# Chapter 07 — Localization

> **License:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).  
> **Hardware:** simulation only.  
> **Lab code:** [`physibot_bringup`](../code/ros2_ws/src/physibot_bringup/); Nav2 adaptation notes in [`docs/adaptation-notes/nav2.md`](../docs/adaptation-notes/nav2.md).

## Learning goals

1. Distinguish local tracking, global localization, and the kidnapped-robot problem.
2. Explain particle-filter pose estimation on an occupancy map (AMCL-class methods).
3. Configure Nav2 localization for a Limo-class footprint using adapted tutorials.
4. Evaluate localization quality qualitatively in RViz and quantitatively with trajectory error when ground truth exists.

## 7.1 The localization problem

Given a **known map** \(m\) and streams of odometry and sensor data, estimate pose \(x_{t}\) in the map frame. ROS REP-105 splits the problem across frames:

- `odom` → `base_link`: smooth, drifts.
- `map` → `odom`: localization’s correction (can jump when the filter restarts).

**Local localization** tracks pose given a good initial guess. **Global localization** starts from high uncertainty (uniform or multi-hypothesis). **Kidnapped robot**: the robot is teleported; beliefs must recover multimodal hypotheses.

EKF tracking (Ch. 06) struggles with global localization because Gaussians are unimodal. Particle filters shine.

## 7.2 Particle filters for pose on maps

Represent belief by samples \(\{x_{t}^{[i]}, w_{t}^{[i]}\}_{i=1}^{N}\):

1. **Sample** from the motion model \(p(x_{t}\mid x_{t-1}, u_{t})\).
2. **Weight** by the measurement likelihood \(p(z_{t}\mid x_{t}, m)\) (likelihood field / beam model).
3. **Resample** so that high-weight particles survive.

AMCL (Adaptive Monte Carlo Localization) adjusts \(N\) and recovers from failures—Nav2’s classical localization workhorse. Read the conceptual overview in [Nav2 documentation](https://docs.nav2.org/) and the upstream AMCL literature rather than reimplementing resampling tricks in coursework unless assigned.

## 7.3 Nav2 localization bringup (adapt, don’t invent)

PhysiBot configures Nav2 localization for a differential-drive footprint matching the course robot. Prefer:

1. Official Nav2 localization tutorials for Humble.
2. Existing AgileX Limo / community Nav2 parameter sets, then tune footprint and topic remaps.
3. Course overlay launch files in `physibot_bringup` that include the map server + AMCL (or Nav2’s current recommended localizer).

YAML knobs you will actually touch:

| Parameter area | Why it matters |
|----------------|----------------|
| `robot_model_type` / footprint | Must match Limo geometry |
| Laser topic & frame | Must match bringup |
| `min_particles` / `max_particles` | CPU vs. robustness |
| Process noise (α params) | Motion model trust |
| Update thresholds | How often scans reshape weights |

Put tuned files under [`code/ros2_ws/src/physibot_bringup/config/`](../code/ros2_ws/src/physibot_bringup/config/) once adapted ([`docs/adaptation-notes/nav2.md`](../docs/adaptation-notes/nav2.md)).

## 7.4 Operating procedure in simulation

Typical flow once maps exist (maps come from Chapter 08; instructors may provide a starter map earlier):

```bash
# Prefer the Nav2-enabled image (Compose profile nav2 / ros2_nav2)
source /ws/install/setup.bash
ros2 launch physibot_bringup localization.launch.py
# Uses config/amcl_params.yaml + maps/demo_map.* by default
# In RViz: set initial pose (2D Pose Estimate)
# Drive with teleop; watch particle cloud collapse
```

Cross-link: [`labs/07-localization/`](../labs/07-localization/).

Debugging checklist:

1. Is `/scan` publishing? Correct `frame_id`?
2. Does the map appear? `map` → `odom` TF present?
3. Are particles spreading along corridors (symmetric ambiguity)?
4. Does setting a bad initial pose recover after a loop, or diverge?

## 7.5 Evaluating quality

| Method | Notes |
|--------|-------|
| Visual | Particle cloud tight; robot aligned to walls in RViz |
| ATE / RPE | If Gazebo ground truth available, compare to `/amcl_pose` |
| Repeatability | Relocalize from several initial guesses |

Absolute Trajectory Error (ATE) after time alignment is standard in SLAM literature; for class demos, a clear RViz narrative plus a few numeric RMSE numbers beats an overbuilt evaluation stack.

## 7.6 Lab 07 — Localize in a warehouse-style sim map

1. Obtain or build a map (instructor map or Chapter 08 output).
2. Launch localization bringup; set pose in RViz.
3. Traverse a loop that revisits a distinctive corner.
4. Kidnap: pause, jump the robot in Gazebo (or restart with wrong initial pose), recover.
5. Log `/amcl_pose` and, if available, ground truth; sketch error over time.

## 7.7 Exercises

1. Why can two particle clusters survive in a long symmetric hallway?
2. Explain how inflating odometry noise changes particle spread after a turn.
3. *(Grad)* Compare AMCL to a pose-graph localization approach conceptually; cite one modern lidar localization paper assigned by the instructor.

## 7.8 Further reading

- [Nav2 documentation](https://docs.nav2.org/)
- Dellaert et al. / Fox et al. — Monte Carlo localization lineage
- Thrun, Burgard, Fox — particle filter localization chapters
- [`docs/adaptation-notes/nav2.md`](../docs/adaptation-notes/nav2.md)


**Runnable lab writeup:** [`labs/07-localization/`](../labs/07-localization/).

## Pedagogical defaults (resolved)

- Launch name: `localization.launch.py`.
- Starter map: `physibot_bringup/maps/demo_map.yaml` (+ `.pgm`) so Ch. 07 is not blocked on finishing Ch. 08.
