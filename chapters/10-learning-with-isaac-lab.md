# Chapter 10 — Learning physical models with Isaac Lab

> **License:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).  
> **Hardware:** simulation; GPU strongly recommended. DGX Spark optional for larger runs (Chapter 13).  
> **Lab code:** NVIDIA Isaac Lab containers; bridge notes in [`docs/adaptation-notes/isaac-lab.md`](../docs/adaptation-notes/isaac-lab.md). Everyday ROS still uses [`docker/compose.yaml`](../docker/compose.yaml).

## Learning goals

1. Place Isaac Lab in the PhysiBot stack as the physics + learning environment.
2. Use the official Lab Docker profiles—especially `ros2` (Humble)—without forking Lab’s install path.
3. Adapt a minimal wheeled / locomotion example from Lab docs (not a greenfield task suite).
4. Practice checkpoint hygiene for later sim-to-real and Spark workflows.

## 10.1 Gazebo vs. Isaac Lab in this course

| Tool | PhysiBot role |
|------|----------------|
| Gazebo / ros_gz + Nav2 | Integration labs: TF, maps, costmaps, student ROS packages |
| **Isaac Lab** | Parallelized physics, RL / imitation, residual learning, domain randomization |

Both are simulators; they optimize for different pedagogies. Chapters 03–09 emphasize ROS 2 literacy. Chapters 10 and 13 emphasize **learning with physical models at scale**.

## 10.2 Mental model: environments, tasks, and physics

Isaac Lab (built on Isaac Sim / PhysX) exposes:

- **Articulations / rigid bodies** with physically parameterized links.
- **Sensors** (cameras, contacts, etc.) for observation.
- **Tasks / MDPs** wrapping observations, actions, rewards.
- **Training loops** (e.g. RSL-RL and related workflows—follow current Lab docs).

A *learned physical model* here might be a policy \(\pi(a\mid o)\) that respects dynamics implicitly, or an explicit residual dynamics module trained on rollouts. Revisit Chapter 04’s \(f_{\theta}+g_{\phi}\) split.

## 10.3 Official Docker profiles and the Humble pin

Follow NVIDIA’s documentation—not a third-party blog—for installs:

- [Isaac Lab installation](https://docs.nvidia.com/isaaclab/isaac-lab/installation)
- [Isaac Lab Docker guide](https://isaac-sim.github.io/IsaacLab/main/source/deployment/docker.html)

Profiles of interest:

| Profile | Role |
|---------|------|
| `base` | Core Lab image |
| **`ros2`** | Base + **ROS 2 Humble** (`Dockerfile.ros2`) |
| `kitless` | Headless / alternate workflows per docs |

Course pin: **Humble**, matching student Compose ([`STATUS.md`](../STATUS.md)). Re-verify each term—Lab release notes have historically warned about intermittent ROS2 image issues during Python upgrades.

## 10.4 Adaptation plan (do not invent a stack)

Per [`docs/adaptation-notes/isaac-lab.md`](../docs/adaptation-notes/isaac-lab.md):

1. Students keep day-to-day ROS in `physibot/ros2-humble:local`.
2. Isaac Lab labs use upstream `container.py` / Compose profiles.
3. Attach or mount the course workspace only as documented for the term.
4. Adapt an **existing** wheeled or locomotion example from Lab’s tutorials; change rewards/observations lightly for teaching.

Capstone option B (Ch. 14) may deploy a residual or policy back into ROS sim—keep export formats simple (TorchScript / ONNX as Lab supports; pin one).

## 10.5 Checkpoint and artifact hygiene

- **Never** commit multi-gigabyte checkpoints to git.
- Store runs under lab shared storage or student object storage with a manifest YAML: seed, Lab commit SHA, config path, metrics.
- Log `git` SHAs of PhysiBot + Isaac Lab tags used for the run.
- Prefer smaller teaching configs for laptops; scale the same config on Sparks in Chapter 13.

## 10.6 Lab 10 — Smoke training job

### On a GPU workstation (or cloud GPU)

1. Follow current Isaac Lab Docker quickstart until a tutorial env trains for a few iterations.
2. Record wall-clock time for \(N\) iterations and final reward/return.
3. Save checkpoint + config sidecar **outside** the PhysiBot git tree.
4. Write half a page: what physical parameters were randomized (if any), and what structure remained classical.

### Without a local GPU

Use a lab DGX Spark account (Chapter 13 procedures) or instructor-provided logs to complete the written portion; still walk through the Docker profile documentation so you can operate a Spark later.

### Optional ROS 2 bridge smoke

If the term enables Lab’s `ros2` profile with a demo publisher/subscriber, show `ros2 topic list` from a Humble shell talking to the Lab container on a shared DDS domain. Document `ROS_DOMAIN_ID` carefully.

## 10.7 Exercises

1. Explain why domain randomization is a physical-model tool, not merely “more data.”
2. List three quantities you would freeze (not randomize) when the target is a specific Limo Pro.
3. *(Grad)* Propose a residual dynamics learning objective compatible with your Chapter 04 model; cite one paper.

## 10.8 Further reading

- Isaac Lab docs (installation, tutorials, Docker)
- [Isaac Sim ROS 2 tutorials](https://docs.isaacsim.omniverse.nvidia.com/latest/ros2_tutorials/index.html)
- Course [`STATUS.md`](../STATUS.md) evidence table for Humble

## Professor edit notes

- Pin Isaac Lab release tag for the term before week 10.
- Select the exact upstream example (wheeled task name) students clone.
- Clarify GPU lab booking vs. Spark booking.
