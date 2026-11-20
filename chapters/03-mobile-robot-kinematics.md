# Chapter 03 — Mobile robot kinematics

> **License:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).  
> **Hardware:** simulation only.  
> **Lab code:** [`physibot_bringup`](../code/ros2_ws/src/physibot_bringup/), [`physibot_description`](../code/ros2_ws/src/physibot_description/), [`docs/adaptation-notes/limo.md`](../docs/adaptation-notes/limo.md).

## Learning goals

1. Write configuration and velocity kinematics for unicycle and differential-drive robots.
2. Explain nonholonomic constraints in plain language and equations.
3. Map `geometry_msgs/Twist` (`cmd_vel`) to wheel speeds for a Limo-class base.
4. Run open-loop motion in the course ROS 2 container and inspect TF / odometry topics once the sim bringup is adapted.

## 3.1 Configuration space for planar mobiles

A rigid robot in the plane has configuration

\[
q = (x, y, \theta) \in SE(2).
\]

Actuation rarely lets you command \(\dot q\) arbitrarily. Wheeled robots typically admit a **body twist** with forward speed \(v\) and yaw rate \(\omega\), related to world velocity by

\[
\begin{bmatrix} \dot x \\ \dot y \\ \dot\theta \end{bmatrix}
=
\begin{bmatrix}
\cos\theta & 0 \\
\sin\theta & 0 \\
0 & 1
\end{bmatrix}
\begin{bmatrix} v \\ \omega \end{bmatrix}.
\]

This is the **unicycle** (or “single-track”) model. It is the workhorse of indoor mobile robotics and the mental model behind most Nav2 controllers for differential-drive bases.

## 3.2 Nonholonomic constraints (intuition first)

A constraint is *holonomic* if it restricts configuration alone (e.g. “stay on this rail”). A rolling wheel that cannot slide sideways imposes a constraint on **velocity**:

\[
\dot x \sin\theta - \dot y \cos\theta = 0
\]

(no lateral velocity in the body frame). You cannot integrate that into a forbidden *region* of \((x,y,\theta)\)—parallel parking exists!—but instantaneous sideways slide is forbidden. That is the nonholonomic character of differential drive.

**Pedagogical point.** Path planning in \(SE(2)\) must respect these constraints (or approximate them). Nav2’s DWB/MPPI controllers reason in feasible controls, not in arbitrary \(\dot q\).

## 3.3 Differential-drive forward and inverse kinematics

Two wheels separated by track width \(b\), radius \(r\), left/right angular speeds \(\phi_{L}, \phi_{R}\):

\[
v = \frac{r}{2}(\phi_{R} + \phi_{L}), \qquad
\omega = \frac{r}{b}(\phi_{R} - \phi_{L}).
\]

Inverse (commanded \(v,\omega\) to wheel speeds):

\[
\phi_{R} = \frac{1}{r}\left(v + \frac{b}{2}\omega\right), \qquad
\phi_{L} = \frac{1}{r}\left(v - \frac{b}{2}\omega\right).
\]

Saturation at actuator limits turns a commanded circle into a clipped, smaller-radius curve—your first contact with “kinematics lie when dynamics bite” (Chapter 04).

## 3.4 Ackermann and Limo drive modes

Car-like (Ackermann) steering uses road-wheel angle \(\delta\) and axle speed, often approximated by a bicycle model:

\[
\dot x = v\cos\theta, \quad
\dot y = v\sin\theta, \quad
\dot\theta = \frac{v}{L}\tan\delta,
\]

with wheelbase \(L\). AgileX Limo Pro supports differential, Ackermann, tracked, and Mecanum modes ([Limo Pro user manual](https://github.com/agilexrobotics/limo_pro_doc/blob/master/Limo%20Pro%20user%20manual(EN).md)). PhysiBot pins upstream branch `humble` of [`limo_ros2`](https://github.com/agilexrobotics/limo_ros2) in [`docs/adaptation-notes/limo.md`](../docs/adaptation-notes/limo.md).

For navigation chapters we standardize on a **differential-drive / unicycle** interface via `cmd_vel` unless a lab explicitly schedules Ackermann mode. That keeps Nav2 configs comparable to the official [Nav2 Getting Started](https://docs.nav2.org/) differential examples.

### Published Limo Pro geometry (course defaults)

| Quantity | Value | Source |
|----------|-------|--------|
| Overall L×W×H | 322 × 220 × 251 mm | AgileX Limo Pro tech specs |
| Wheelbase | 200 mm | same |
| Tread (track width \(b\)) | 175 mm | same |
| No-load \(v_{\max}\) | 1.0 m/s | same |
| Wheel radius \(r\) | **0.040 m teaching estimate** | *not* in published body table — measure tire before physical runs |

Course URDF / kinematics use these numbers ([`limo_body.xacro`](../code/ros2_ws/src/physibot_description/urdf/limo_body.xacro), [`kinematics.py`](../code/ros2_ws/src/physibot_sim/physibot_sim/kinematics.py)). The visual body box height (180 mm) is a simplified collision hull; published **overall** height remains 251 mm including mounts.

## 3.5 Discrete integration and odometry

Given sampling period \(\Delta t\), a simple Euler step

\[
\begin{aligned}
x_{k+1} &= x_{k} + v_{k}\cos\theta_{k}\,\Delta t, \\
y_{k+1} &= y_{k} + v_{k}\sin\theta_{k}\,\Delta t, \\
\theta_{k+1} &= \theta_{k} + \omega_{k}\,\Delta t
\end{aligned}
\]

accumulates drift. Better integrators (second-order, Runge–Kutta) help numerically; they do **not** remove wheel slip or encoder bias. Odometry publishes a continuously evolving `odom` → `base_link` transform; localization later estimates `map` → `odom` to correct global pose (REP-105).

## 3.6 ROS 2 topics and frames you will live in

| Topic / frame | Role |
|---------------|------|
| `/cmd_vel` (`geometry_msgs/Twist`) | Commanded body twist |
| `/odom` (`nav_msgs/Odometry`) | Integrated pose + twist |
| TF `odom` → `base_footprint` → `base_link` | Odometry chain (REP-105) |
| TF `base_link` → `laser_link` | Sensor extrinsics |

See [`textbook/figures/tf-tree.svg`](../textbook/figures/tf-tree.svg).

Course packages:

- [`physibot_description`](../code/ros2_ws/src/physibot_description/) — Limo-class URDF/xacro teaching model.
- [`physibot_sim`](../code/ros2_ws/src/physibot_sim/) — planar odom + stub laser nodes.
- [`physibot_bringup`](../code/ros2_ws/src/physibot_bringup/) — launch overlays.

Vendor `limo_ros2` remains the source of truth for meshes and hardware drivers; PhysiBot overlays course launch files and teaching configs.

## 3.7 Lab 03 — Open-loop `cmd_vel` in simulation

1. Enter the container and build as in Chapter 01.
2. Launch the course diff-drive sim:

```bash
ros2 launch physibot_bringup sim_diff_drive.launch.py
```

3. In a second shell, publish twists (or use teleop if installed):

```bash
source /ws/install/setup.bash
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist \
  "{linear: {x: 0.2, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.3}}" -r 10
```

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

4. Inspect `/odom`, TF (`base_footprint`, `base_link`, `laser_link`), and optionally `/scan` from the stub laser.

This is **course stub sim** (no Gazebo required)—description + `physibot_sim` odometry (+ optional stub laser). When licensed vendor meshes land, keep the same launch **name** and swap internals. Cross-link: [`labs/03-kinematics-teleop/`](../labs/03-kinematics-teleop/).

### Offline unicycle plotting (required)

Implement Euler integration of the unicycle model in NumPy and plot:

1. Constant \(v>0\), \(\omega>0\) (circle).
2. A bang-bang square: forward segments and in-place spins (\(\omega\)-only).

Compare path length and final pose error if you add 5% scale bias on \(v\).

## 3.8 Exercises

1. Derive \(\phi_{L}, \phi_{R}\) from \(v, \omega\) for course defaults \(r=0.04\,\mathrm{m}\), \(b=0.175\,\mathrm{m}\). What happens when \(|\omega|\) is large enough to saturate one wheel?
2. List frames from the course URDF: `odom`, `base_footprint`, `base_link`, `laser_link`, `camera_link`, `imu_link`.
3. Show that pure \(\omega\) with \(v=0\) rotates in place for differential drive but is not a valid bicycle instantaneous motion with \(\delta=0\).
4. *(Grad)* Read a short section on nonholonomic motion planning (e.g. LaValle, *Planning Algorithms*, free online) and summarize why straight-line interpolation in \((x,y,\theta)\) is a bad open-loop plan.

## 3.9 Further reading

- Siciliano, Sciavicco, Villani, Oriolo — *Robotics: Modelling, Planning and Control* (mobile robot chapters).
- [REP 105](https://www.ros.org/reps/rep-0105.html)
- AgileX Limo ROS 2 repositories (pin URL/SHA in adaptation notes each term)
- [Gazebo / ros_gz documentation](https://gazebosim.org/docs) for sim bringup patterns


**Runnable lab writeup:** [`labs/03-kinematics-teleop/`](../labs/03-kinematics-teleop/).

## Pedagogical defaults (resolved)

- Launch: `sim_diff_drive.launch.py` (also `description.launch.py` / `sim_stub.launch.py` for smoke); swap stub meshes/sensors for licensed Limo Gazebo assets when ready.
- Geometry: published AgileX Limo Pro L×W×H / wheelbase / tread / \(v_{\max}\); wheel radius remains a labeled teaching estimate until tires are measured on the fleet.
