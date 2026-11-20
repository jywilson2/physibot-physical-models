# Chapter 01 — Welcome to PhysiBot & the Docker workflow

> **License:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) (see `chapters/LICENSE`).  
> **Hardware:** none — simulation and containers only.  
> **Lab code:** [`docker/compose.yaml`](../docker/compose.yaml), [`code/ros2_ws/`](../code/ros2_ws/), [`scripts/dev-shell.sh`](../scripts/dev-shell.sh).

## Learning goals

By the end of this chapter you should be able to:

1. State what **PhysiBot** is, who it is for, and how physical models organize the course.
2. Explain the hardware roadmap: simulation first, then AgileX Limo Pro with Jetson Orin Nano, with DGX Sparks as lab backends.
3. Build and enter the course ROS 2 Humble Docker environment and run the workspace smoke build.
4. Name the major software layers (ROS 2, Nav2, Isaac Lab) and where each appears in later chapters.

## 1.1 What PhysiBot is

**PhysiBot** is a full-course treatment of *AI physical models for mobile robotics*. The brand is the course identity: we teach how structured models of motion, sensing, and uncertainty—classical and learned—support localization and navigation on a small wheeled robot.

The course is written for a **mixed undergraduate / graduate** audience. We assume you have seen linear algebra once; Chapter 02 refreshes what you need without pretending you still remember every determinant trick. Probability and estimation are developed as the narrative needs them.

Two design choices shape everything that follows:

1. **Simulation and Docker first.** You can complete early chapters without touching a physical robot. The same containers later host Nav2 and (via NVIDIA’s images) Isaac Lab workloads.
2. **Adapt, don’t invent.** AgileX Limo ROS 2 packages, [Navigation2](https://docs.nav2.org/), and [NVIDIA Isaac Lab](https://isaac-sim.github.io/IsaacLab/) already solve hard integration problems. PhysiBot wraps and teaches those stacks; it does not rebuild them from scratch. Adaptation notes live in [`docs/adaptation-notes/`](../docs/adaptation-notes/).

## 1.2 The physical-models thread

A *physical model* in this course is any structured description that constrains how the robot can move, what sensors should report, or how uncertainty evolves. Examples you will meet:

| Model class | Typical use | First appears |
|-------------|-------------|---------------|
| Planar kinematics (unicycle, differential drive) | Open-loop motion, odometry | Ch. 03 |
| Simple dynamics (mass, friction, actuator limits) | Tracking error, identification | Ch. 04 |
| Observation models (range, bearing, IMU) | Measurement likelihoods | Ch. 05 |
| Probabilistic filters (KF / EKF / UKF / particles) | State estimation | Ch. 06–07 |
| Occupancy / pose-graph maps | Mapping and SLAM | Ch. 08 |
| Nav2 costmaps and controllers | Goal-directed navigation | Ch. 09 |
| Learned residuals / policies in Isaac Lab | Data-driven physical models | Ch. 10–13 |

Classical models are not the enemy of learning. They are **inductive bias**: they tell the learner what cannot happen (wheels don’t slide sideways without cost; range measurements are positive; poses live on manifolds). Later chapters treat neural residuals as corrections to these priors, not as replacements for them.

## 1.3 Hardware roadmap (when the robot appears)

| Phase | Chapters | What you need |
|-------|----------|---------------|
| Containers + kinematics/estimation | 01–06 | Laptop/desktop + Docker |
| Localization, mapping, Nav2 in sim | 07–09 | Same; GPU optional for viz |
| Isaac Lab learning | 10 | GPU recommended; DGX Spark optional |
| Sim-to-real preparation | 11 | Still readable without robot |
| Physical Limo Pro + Orin Nano | **12** | Lab robot time |
| Heavy training on DGX Sparks | **13** | Instructor/lab backends |
| Capstone | 14 | Sim required; physical optional per cohort |

The course robot is the **AgileX Limo Pro**. On-robot compute is an **NVIDIA Jetson Orin Nano**. Two **NVIDIA DGX Sparks** serve as instructor/lab backend machines for Isaac Lab training—you are not assumed to own a Spark. See [`docs/adaptation-notes/limo.md`](../docs/adaptation-notes/limo.md).

## 1.4 Software stack overview

```text
┌─────────────────────────────────────────────────────────┐
│  Isaac Lab (Ch. 10, 13) — physics + learning            │
│  Official Lab `ros2` Docker profile → ROS 2 Humble      │
├─────────────────────────────────────────────────────────┤
│  Nav2 + slam_toolbox-class tools (Ch. 07–09, 12)        │
├─────────────────────────────────────────────────────────┤
│  Course ROS 2 workspace: physibot_* packages            │
│  docker/compose.yaml  →  physibot/ros2-humble:local     │
├─────────────────────────────────────────────────────────┤
│  Host: Docker Engine + Compose v2                       │
└─────────────────────────────────────────────────────────┘
```

**ROS 2 Humble** is the pinned student distro because NVIDIA Isaac Lab’s official ROS 2 Docker image installs Humble (`Dockerfile.ros2` / `ros2` profile). Evidence and the termly refresh checklist are in [`STATUS.md`](../STATUS.md). Isaac Sim also documents Humble and Jazzy as recommended; we stay on Humble so student Compose, Nav2 examples, and Lab stay aligned.

Primary references for the stack:

- [ROS 2 Humble documentation](https://docs.ros.org/en/humble/)
- [Nav2 documentation](https://docs.nav2.org/)
- [Isaac Lab installation](https://docs.nvidia.com/isaaclab/isaac-lab/installation)
- [Isaac Lab Docker guide](https://isaac-sim.github.io/IsaacLab/main/source/deployment/docker.html)

## 1.5 Repository map

| Path | Role |
|------|------|
| `chapters/` | Textbook narrative (this tree) |
| `textbook/` | Quarto book config and PDF/DOCX exports |
| `code/ros2_ws/` | Student ROS 2 workspace |
| `docker/` | Everyday Humble student image |
| `docs/adaptation-notes/` | How we wrap Limo / Nav2 / Isaac Lab |
| `tests/smoke/` | Layout and CI smoke checks |
| `scripts/dev-shell.sh` | Convenience wrapper into Compose |

Licensing: narrative is **CC BY-NC 4.0**; code and Docker are **Apache-2.0**. See the repo [`README.md`](../README.md).

## 1.6 Lab 01 — First Docker shell

**Prerequisites:** Docker Engine and Docker Compose v2 on Linux (or an equivalent setup that can build the course image). GPU is *not* required for this lab.

### Step A — Build the student image

From the repository root:

```bash
docker compose -f docker/compose.yaml build
```

This builds `physibot/ros2-humble:local` from [`docker/Dockerfile.ros2`](../docker/Dockerfile.ros2). The default build does **not** install the full Nav2 metapackage (`INSTALL_NAV2=0`) so the everyday image stays lean; later chapters document enabling Nav2 layers.

### Step B — Enter an interactive shell

```bash
docker compose -f docker/compose.yaml run --rm ros2 bash
# or: ./scripts/dev-shell.sh
```

Inside the container:

```bash
echo $ROS_DISTRO          # expect: humble
cd /ws
colcon build --symlink-install
source install/setup.bash
ros2 pkg list | grep physibot
```

You should see at least `physibot_bringup` and `physibot_description`.

### Step C — Launch the simulation stub

```bash
ros2 launch physibot_bringup sim_stub.launch.py
```

In a second shell attached to the same Compose network (or another `compose run`):

```bash
source /ws/install/setup.bash
ros2 node list
ros2 topic list
```

The stub currently publishes a minimal `robot_description` via `robot_state_publisher` ([`sim_stub.launch.py`](../code/ros2_ws/src/physibot_bringup/launch/sim_stub.launch.py)). It is intentionally thin: later chapters replace it with adapted Limo description and Gazebo/Isaac bringup. Read the launch log—it points at the stub URDF path under `physibot_description`.

### Optional smoke profile

```bash
docker compose -f docker/compose.yaml --profile smoke run --rm smoke
```

This builds the workspace non-interactively and greps for `physibot` packages—the same idea as CI.

## 1.7 How to study this course

- **Read with a terminal open.** Every early chapter ends in a container exercise.
- **Keep a lab notebook** (Markdown is fine): commands that worked, parameter values, plots of error.
- **Prefer upstream docs for APIs.** Course chapters teach *why* and *how we wire things*; Nav2 and Isaac Lab change faster than a textbook—follow their current pages for flags and YAML keys.
- **Safety culture starts in sim.** Treat `cmd_vel` as dangerous even in Gazebo; later physical chapters formalize e-stop and supervised runs.

## 1.8 Exercises

1. Build and enter the `ros2` service. Screenshot or paste `echo $ROS_DISTRO`.
2. After `colcon build`, list packages matching `physibot`.
3. Run `sim_stub.launch.py` and identify which node provides TF / robot state.
4. Skim [`docs/adaptation-notes/README.md`](../docs/adaptation-notes/README.md) and write three sentences: what we adapt from Limo, Nav2, and Isaac Lab respectively.
5. *(Grad stretch)* Compare Humble vs. Jazzy on the Isaac Sim ROS 2 page linked in `STATUS.md`. Argue in half a page why this course still pins Humble.

## 1.9 Further reading

- Course overview: [`README.md`](../README.md), outline: [`00-outline.md`](00-outline.md)
- [Docker Compose overview](https://docs.docker.com/compose/)
- [colcon documentation](https://colcon.readthedocs.io/)
- Thrun, Burgard, and Fox, *Probabilistic Robotics* — conceptual spine for Ch. 06–08 (we cite chapter-level ideas as we go)
- Siciliano and Khatib (eds.), *Springer Handbook of Robotics* — optional depth on mobile bases

## Professor edit notes

- Confirm lab Docker host OS matrix (Linux required vs. Windows/WSL2 supported).
- Replace stub launch screenshots with cohort-specific terminal captures when available.
- Decide whether Nav2 should be default-on in the student image by mid-term.
