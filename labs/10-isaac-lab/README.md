# Lab 10 — Isaac Lab (documentation-first)

**Chapter:** 10 — Learning with Isaac Lab  
**Hardware:** DGX Spark (preferred) or any workstation with a supported NVIDIA GPU  
**Not required:** physical Limo, everyday student `docker/compose.yaml` image  

This lab is **runnable as a documented procedure** on lab GPUs. Full Isaac Lab is **not** in course CI — host layout/unit tests still cover repo wiring.

## Roles: DGX Spark vs Orin Nano

| Role | Machine | What you do here |
|------|---------|------------------|
| Training / heavy sim | **DGX Spark** (instructor lab) | Pull Isaac Lab Docker, run wheeled examples, export checkpoints |
| Everyday ROS labs | Laptop / lab PC | Continue using `docker/compose.yaml` (Humble) — Labs 01–09 |
| On-robot inference | **Jetson Orin Nano** (Lab 12) | Deploy policies / Nav2; do **not** train Isaac Lab on Orin |

Sparks are shared backend compute (Ch. 13). Students are not assumed to own one.

## Course pin (re-verify each term)

| Field | Value |
|-------|-------|
| Isaac Lab tag | **`v3.0.0`** |
| Commit | `37ddf626871758333d6ed89cf64ad702aef127d0` |
| ROS 2 via Lab | Humble (`ros2` Docker profile / `Dockerfile.ros2`) |
| Course ROS image | `docker/compose.yaml` — separate from Isaac containers |

Newer tags (e.g. `v3.0.0`) may exist; stick to the pin above unless the instructor updates `STATUS.md` and this README.

Upstream:

- [Isaac Lab installation](https://docs.nvidia.com/isaaclab/isaac-lab/installation)
- [Isaac Lab Docker guide](https://isaac-sim.github.io/IsaacLab/main/source/deployment/docker.html)
- Course notes: [`docs/adaptation-notes/isaac-lab.md`](../../docs/adaptation-notes/isaac-lab.md)

## Goals

1. Boot Isaac Lab with the official **`ros2`** profile (Humble).
2. Mount this course repo’s `code/ros2_ws` read-only for TF / topic familiarity.
3. Run **one** upstream wheeled / locomotion example (adapt, don’t invent a full task suite).
4. Record which topics / frames you would later bridge to PhysiBot Nav2 (Labs 07–09).

## Prerequisites (lab host)

- NVIDIA GPU + drivers suitable for Isaac Sim / Lab (see NVIDIA docs for the pinned tag)
- Docker with NVIDIA Container Toolkit
- Disk space for Isaac images (tens of GB — use Spark shared storage when available)
- Git clone of this course repo

## Procedure

### 1. Clone Isaac Lab at the course pin

```bash
# On DGX Spark (or approved GPU host) — paths are examples; follow local lab conventions
git clone https://github.com/isaac-sim/IsaacLab.git
cd IsaacLab
git checkout v3.0.0
```

### 2. Build / start the `ros2` profile

Follow the upstream Docker guide for your pin. Typical pattern:

```bash
# From Isaac Lab repo — exact flags follow upstream docs for v3.0.0
./docker/container.py start ros2
./docker/container.py enter ros2
```

Confirm inside the container:

```bash
echo "$ROS_DISTRO"   # expect: humble
```

### 3. Attach the course workspace (read-only mount)

On the **host**, when starting or recreating the Lab container, bind-mount the course workspace
(adjust host path to your clone):

```text
<code-ros2-ws-host>  →  /course/ros2_ws   (read-only)
```

Example sketch (do **not** vendor Isaac Compose into this repo; keep mounts local):

```bash
# Illustrative — merge with whatever container.py / compose Isaac documents for the pin
docker run --rm -it \
  -v "$HOME/physibot-physical-models/code/ros2_ws:/course/ros2_ws:ro" \
  ... isaac-lab-ros2-image ...
```

Inside the Lab container you can `source` a separately built course overlay **only if** Humble packages match; otherwise keep course packages for reference and run Isaac examples alone.

### 4. Run one upstream wheeled example

Prefer an official locomotion / wheeled demo from the pinned Isaac Lab tree (names change by release). Pattern:

```bash
# Inside Isaac Lab ros2 container — replace with the demo path documented for v3.0.0
# Example shape only:
python scripts/reinforcement_learning/rsl_rl/train.py --task=<WheeledOrLocomotionTask> --headless
```

Stop after a short smoke train or play run. Goal is **pipeline literacy**, not overnight training on a laptop.

### 5. Bridge notes (for later chapters)

Write down (notebook / lab sheet — not secrets):

- Observation / action spaces of the example
- How you would map `cmd_vel` ↔ policy actions for Limo-class diff-drive
- Frames you must keep REP-105-compatible (`odom`, `base_link` / `base_footprint`)

## Checkpoints

- [ ] `ROS_DISTRO=humble` inside the Lab `ros2` container
- [ ] Course pin `v3.0.0` checked out (or instructor-updated pin)
- [ ] One upstream example ran (train smoke or play)
- [ ] Notes on Spark vs Orin roles (train on Spark; deploy on Orin in Lab 12)
- [ ] No Wi-Fi passwords / hostnames committed to git

## What CI covers

| Check | Where |
|-------|-------|
| This README + adaptation notes exist | `tests/smoke/test_repo_layout.sh` |
| Course Humble Compose (no Isaac) | optional Docker job — see `STATUS.md` / `.github/workflows/smoke.yml` |
| Full Isaac Lab image pull | **not** in CI |

## Open items (instructor)

- [ ] Confirm GPU driver matrix on lab Sparks each term
- [ ] Optionally bump pin from `v3.0.0` → newer after smoke on Sparks
- [ ] Choose the exact upstream task ID printed in the term handout
