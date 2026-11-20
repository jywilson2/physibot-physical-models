# Chapter 05 — Sensing and observation models

> **License:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).  
> **Hardware:** simulation only.  
> **Lab code:** [`physibot_bringup`](../code/ros2_ws/src/physibot_bringup/); sensor plugins come from adapted Limo/Gazebo packages ([`docs/adaptation-notes/limo.md`](../docs/adaptation-notes/limo.md)).

## Learning goals

1. Describe a typical Limo Pro sensor suite (LiDAR, IMU, cameras) at the level needed for localization and navigation.
2. Write observation models that map state to expected measurements.
3. Treat noise, bias, calibration, and time synchronization as first-class engineering problems.
4. Inspect simulated sensor topics in ROS 2 and summarize empirical noise statistics.

## 5.1 Sensors as the other half of the physical model

Motion models predict how state evolves; **observation models** predict what sensors should see. Estimation (Ch. 06–07) multiplies these stories in probability. A beautiful process model with a wrong laser extrinsic will still diverge.

On AgileX Limo-class platforms you typically meet some mix of:

| Sensor | ROS-ish message | Role in PhysiBot |
|--------|-----------------|------------------|
| 2D LiDAR | `sensor_msgs/LaserScan` | Localization, mapping, Nav2 costmaps |
| IMU | `sensor_msgs/Imu` | Attitude rate, acceleration; fusion |
| Depth / RGB camera | `sensor_msgs/Image`, point clouds | Optional perception labs |
| Wheel encoders | often inside `/odom` | Dead reckoning |

Confirm the exact suite and topic names from current vendor docs when you pin packages—do not invent plugins ([adaptation notes](../docs/adaptation-notes/limo.md)).

## 5.2 Range-bearing and beam models

A landmark at world position \(m_{j}\) observed from pose \(x=(x,y,\theta)\) yields range-bearing

\[
z = h(x, m_{j}) + \nu =
\begin{bmatrix}
\sqrt{(m_{j,x}-x)^{2}+(m_{j,y}-y)^{2}} \\
\operatorname{atan2}(m_{j,y}-y, m_{j,x}-x) - \theta
\end{bmatrix}
+ \nu.
\]

For dense 2D LiDAR against an occupancy map, classic approaches use **beam** or **likelihood-field** models (Thrun, Burgard, Fox, *Probabilistic Robotics*). Intuition for likelihood fields: expected ranges that land in free space near occupied cells score better than ranges that pierce walls. AMCL-style particle filters (Ch. 07) implement variants of this idea.

## 5.3 Occupancy observations

Occupancy grid mapping treats each cell’s occupied probability as a binary Bayes filter updated by inverse sensor models. You will *run* this via adapted `slam_toolbox` (or vendor SLAM) in Chapter 08 rather than coding Bresenham by hand—but you should still know that a scan at a pose is a batch of Bernoulli evidence along rays.

## 5.4 IMU intuition (lightweight)

An IMU measures angular rate and specific force. For a planar teaching filter you might use yaw-rate as a direct measurement of \(\omega\), with bias \(b\):

\[
\omega_{\mathrm{meas}} = \omega + b + \eta, \qquad \dot b = \eta_{b}.
\]

Full 3D preintegration (Forster et al.) is graduate depth; the course point is: **biases walk**, so treat them as states or calibrate them out before trusting long open-loop integration.

## 5.5 Noise, bias, and calibration

| Effect | Symptom | Mitigation |
|--------|---------|------------|
| White noise | Jitter on short windows | Filtering; don’t over-trust single scans |
| Bias / scale | Steady drift | Augment state; calibrate |
| Extrinsic error | Consistent map mismatch | Measure TF; optimize extrinsics |
| Time skew | Motion distortion, bad fusion | Sync policies; hardware timestamps |

Calibration is a physical-model parameter estimate. Chapter 11 elevates it to a sim-to-real gate.

## 5.6 ROS 2 message models and time

Every message carries a `header.stamp` and usually a `frame_id`. TF lookups fail or extrapolate when stamps disagree. Habits:

1. Prefer sensor timestamps over “now” when transforming scans.
2. Use `use_sim_time:=true` in simulation so all nodes share `/clock`.
3. Record bags with enough topics to debug sync (`/scan`, `/imu`, `/odom`, `/tf`, `/tf_static`).

```bash
ros2 bag record -o sense_lab /scan /odom /tf /tf_static /clock
# add /imu/data when a real or Gazebo IMU is in the graph
```

### Course stub sim topics (today)

After `ros2 launch physibot_bringup sim_diff_drive.launch.py` (with `publish_laser:=true`):

| Topic | Source |
|-------|--------|
| `/cmd_vel` | teleop / your publisher |
| `/odom` | `physibot_sim` diff-drive odom node |
| `/scan` | `physibot_sim` stub laser (`laser_link`) |
| `/tf`, `/tf_static` | `robot_state_publisher` + odom |

Always confirm with `ros2 topic list`—vendor Gazebo bringup may rename IMU topics. **Bags stay out of git**; store homework bags on lab/course storage.

## 5.7 Lab 05 — Inspect simulated scans and IMU

1. Launch `ros2 launch physibot_bringup sim_diff_drive.launch.py`.
2. `ros2 topic list | grep -E 'scan|imu|odom'`.
3. `ros2 topic echo --once /scan`; note `angle_min`, `angle_increment`, `ranges` length, `header.frame_id` (`laser_link`).
4. Collect ~30 s of stationary data. Compute mean and variance of a mid-beam range (IMU yaw-rate when available).
5. Drive a slow rectangle; observe how scan “walls” move in RViz relative to `base_link`.

**Reuse plugins**—do not author a new Gazebo laser plugin for this course.

## 5.8 Exercises

1. Write \(h(x,m)\) for a single landmark and derive the Jacobian \(H = \partial h / \partial x\) (needed in Ch. 06 EKF).
2. Explain why a 1 cm laser extrinsic yaw error can ruin a narrow corridor localization.
3. *(Grad)* Summarize likelihood-field vs. beam models in one page with a citation to *Probabilistic Robotics*.

## 5.9 Further reading

- Thrun, Burgard, Fox — *Probabilistic Robotics* (measurement models).
- [sensor_msgs (Humble)](https://docs.ros2.org/humble/api/sensor_msgs/index-msg.html)
- Vendor Limo sensor documentation (pin each term)
- Forster et al., IMU preintegration — optional grad reading

## Pedagogical defaults (resolved)

- Stub topic graph documented above; vendor topics supersede when Gazebo assets land.
- Homework bags live in course storage, never in git.
