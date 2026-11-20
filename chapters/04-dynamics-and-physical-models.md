# Chapter 04 — Dynamics and AI physical models

> **License:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).  
> **Hardware:** simulation only.  
> **Lab code:** course container; Isaac Lab appears in depth in Chapter 10 ([`docs/adaptation-notes/isaac-lab.md`](../docs/adaptation-notes/isaac-lab.md)).

## Learning goals

1. Contrast kinematic and dynamic models for wheeled robots and know when kinematics fail.
2. Write a simple planar dynamic model with mass, drag, and actuator limits as structured parameters.
3. Explain “physical models” as inductive bias for control and learning.
4. Sketch how learned residual dynamics sit next to classical models—and how Isaac Lab supplies physics as a world model.

## 4.1 When kinematics are not enough

Chapter 03’s unicycle model assumes you get the \(v\) and \(\omega\) you ask for. Reality disagrees when:

- Acceleration limits and motor torque saturate.
- Friction and rolling resistance dissipate energy.
- Payload mass changes the transient response.
- High speed + sharp yaw commands excite slip.

Nav2 controllers that ignore dynamics still *work* at modest indoor speeds on a Limo-class robot—but tracking error, costmap collisions at corners, and sim-to-real gaps all grow when the plant is under-modeled. Physical models give you language for those failures.

## 4.2 A minimal planar dynamic model

Let body-forward speed \(v\) and yaw rate \(\omega\) be states, with first-order-ish actuator lags:

\[
\begin{aligned}
m \dot v &= -c_{v} v + F_{\mathrm{cmd}} + F_{\mathrm{dist}}, \\
J \dot\omega &= -c_{\omega} \omega + \tau_{\mathrm{cmd}} + \tau_{\mathrm{dist}}.
\end{aligned}
\]

Map commanded twist \((v^{\star}, \omega^{\star})\) through saturated low-level controllers into \(F_{\mathrm{cmd}}, \tau_{\mathrm{cmd}}\). Parameters \(\{m, J, c_{v}, c_{\omega}\}\) are **physical knobs**: identify them from step responses in simulation first, then on hardware (Ch. 11–12).

Even this cartoon model teaches useful habits:

1. **Name parameters** you might estimate.
2. **Separate** nominal physics from disturbances.
3. **Saturate** commands explicitly—optimization-based controllers need limits.

## 4.3 Energy, constraints, and inductive bias

A *physical-model viewpoint* asks: what structure must any plausible model obey?

- Nonholonomic / friction cones constrain admissible contact forces.
- Energy dissipation: undamped perpetual motion is a modeling bug.
- Symmetry: a left–right symmetric chassis should not invent a preferred turning direction without cause.

Learning systems that ignore these structures need more data and fail more strangely. PhysiBot’s thesis is that **AI physical models** combine classical structure with data-driven residuals:

\[
\dot s = f_{\theta}(s, u) + g_{\phi}(s, u),
\]

where \(f_{\theta}\) is a parameterized physics prior and \(g_{\phi}\) is a learned correction (neural net, Gaussian process, etc.). Chapter 10 instantiates related ideas inside Isaac Lab; here we only need the conceptual split.

## 4.4 From models to controllers and estimators

| Consumer | How it uses a physical model |
|----------|------------------------------|
| Feedforward tracking | Invert approximate dynamics to shape \(u\) |
| EKF prediction | \(x_{k+1} = f(x_{k}, u_{k}) + w_{k}\) |
| MPPI / MPC (Nav2 plugins) | Roll out \(f\) over a horizon |
| Residual learning | Train \(g_{\phi}\) on prediction error |

A wrong model with honest noise covariances often beats a “perfect” black box you cannot tune. Keep both stories available.

## 4.5 Bridge to Isaac Lab (preview)

[NVIDIA Isaac Lab](https://isaac-sim.github.io/IsaacLab/) provides GPU-accelerated physics and learning environments. For PhysiBot:

- Everyday ROS 2 work stays on [`docker/compose.yaml`](../docker/compose.yaml) (Humble).
- Training workloads use Lab’s official containers; the `ros2` profile installs **ROS 2 Humble**—same pin as the student stack ([evidence in `STATUS.md`](../STATUS.md)).
- We adapt an existing wheeled/locomotion example rather than authoring a full task suite ([`docs/adaptation-notes/isaac-lab.md`](../docs/adaptation-notes/isaac-lab.md)).

Think of Isaac Lab as a **high-throughput physical model** you can differentiate through and randomize—ideal for residual policies—while Gazebo/ros_gz remains the comfortable home for Nav2 integration labs.

## 4.6 Lab 04 — Parameter sweep and tracking error

### Part A — Simulated plant in NumPy

Implement the first-order speed model \(\dot v = (-v + v^{\star})/\tau\) with time constant \(\tau\) and saturation \(|v^{\star}|\le v_{\max}\). Drive a unicycle with a square-wave speed command and plot \(v(t)\) vs \(v^{\star}(t)\) for \(\tau \in \{0.05, 0.2, 0.5\}\) s.

### Part B — Open-loop path sensitivity

Using Chapter 03’s integrator, compare paths when commanded \((v,\omega)\) is applied instantly vs. filtered by the lag model. Measure final pose error after 10 s.

### Part C — Course container observation (when sim robot exists)

Teleop a slow circle and a fast circle; record `/odom` and commanded `/cmd_vel`. Qualitatively note lag and radius error. Store bags for Chapter 06 noise analysis.

```bash
ros2 bag record -o limo_dyn_sweep /cmd_vel /odom
```

## 4.7 Exercises

1. Explain in one paragraph why a pure kinematic MPC can still collide at a fast corner entry.
2. List three parameters you would identify on the physical Limo Pro before trusting a learned residual.
3. *(Grad)* Read a short survey paragraph on residual dynamics / physics-informed networks (instructor may assign a current paper). Map its notation onto \(f_{\theta}+g_{\phi}\).

## 4.8 Further reading

- Spong, Hutchinson, Vidyasagar — *Robot Modeling and Control* (dynamics foundations).
- Haarnoja et al. and related RL-for-locomotion literature — motivation for learned controllers (details in Ch. 10).
- Isaac Lab docs: [installation](https://docs.nvidia.com/isaaclab/isaac-lab/installation), [Docker](https://isaac-sim.github.io/IsaacLab/main/source/deployment/docker.html)


**Runnable lab writeup:** [`labs/04-odometry-models/`](../labs/04-odometry-models/).

## Professor edit notes

- Insert measured step-response plots from the lab Limo fleet when available.
- Decide Gazebo vs. Isaac Sim as the primary dynamics sandbox for Ch. 04 labs.
