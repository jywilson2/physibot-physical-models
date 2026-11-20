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

with wheelbase \(L\). AgileX Limo platforms historically support multiple modes (differential, Ackermann, and sometimes omni depending on variant). **Do not invent the mode map**—read current AgileX Limo ROS 2 documentation and pin the branch used by this course in [`docs/adaptation-notes/limo.md`](../docs/adaptation-notes/limo.md).

For PhysiBot’s navigation chapters we standardize on a **differential-drive / unicycle** interface via `cmd_vel` unless the lab explicitly schedules Ackermann mode. That keeps Nav2 configurations comparable to the official [Nav2 Getting Started](https://docs.nav2.org/) differential examples.

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
| TF `odom` → `base_link` | Same story as `/odom`, as a transform |
| TF `base_link` → `laser_link` | Sensor extrinsics |

Course packages:

- [`physibot_description`](../code/ros2_ws/src/physibot_description/) — URDF/xacro (stub today; Limo-adapted later).
- [`physibot_bringup`](../code/ros2_ws/src/physibot_bringup/) — launch overlays.

Vendor description packages remain the source of truth for meshes, wheel parameters, and plugins; PhysiBot only overlays course launch files and teaching configs.

## 3.7 Lab 03 — Open-loop `cmd_vel` in simulation

### Course diff-drive sim (Lab 03)

1. Enter the container and build as in Chapter 01.
2. Launch the canonical sim bringup:

```bash
ros2 launch physibot_bringup sim_diff_drive.launch.py
```

3. In a second shell, manually publish twists (or use teleop):

```bash
source /ws/install/setup.bash
ros2 topic pub --once /cmd_vel geometry_msgs/msg/Twist \
  "{linear: {x: 0.2, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.3}}"
```

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

This starts description + `physibot_sim` odometry (and optional stub laser)—enough for TF / `/odom` / `/cmd_vel` without Gazebo. When vendor Gazebo assets are licensed in, keep the same launch **name** and swap internals (see adaptation notes). Visualize in RViz: TF, LaserScan, and Odometry.

### Offline unicycle plotting (required even with stub)

Implement Euler integration of the unicycle model in NumPy and plot:

1. Constant \(v>0\), \(\omega>0\) (circle).
2. A bang-bang square: forward segments and in-place spins (\(\omega\)-only).

Compare path length and final pose error if you add 5% scale bias on \(v\).

## 3.8 Exercises

1. Derive \(\phi_{L}, \phi_{R}\) from \(v, \omega\) for \(r=0.05\,\mathrm{m}\), \(b=0.2\,\mathrm{m}\). What happens when \(|\omega|\) is large enough to saturate one wheel?
2. Identify frames you expect on the Limo: `base_link`, `odom`, sensor frames—list them from vendor docs once pinned.
3. Show that pure \(\omega\) with \(v=0\) rotates in place for differential drive but is not a valid bicycle instantaneous motion with \(\delta=0\).
4. *(Grad)* Read a short section on nonholonomic motion planning (e.g. LaValle, *Planning Algorithms*, free online) and summarize why straight-line interpolation in \((x,y,\theta)\) is a bad open-loop plan.

## 3.9 Further reading

- Siciliano, Sciavicco, Villani, Oriolo — *Robotics: Modelling, Planning and Control* (mobile robot chapters).
- [REP 105](https://www.ros.org/reps/rep-0105.html)
- AgileX Limo ROS 2 repositories (pin URL/SHA in adaptation notes each term)
- [Gazebo / ros_gz documentation](https://gazebosim.org/docs) for sim bringup patterns


**Runnable lab writeup:** [`labs/03-kinematics-teleop/`](../labs/03-kinematics-teleop/).

## Professor edit notes

- Keep launch name `sim_diff_drive.launch.py`; swap stub meshes/sensors for licensed Limo Gazebo assets when ready.
- Insert measured Limo Pro \(b\), \(r\), and max \(v,\omega\) from the physical fleet.
