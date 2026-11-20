# PhysiBot

**PhysiBot** teaches AI physical models for mobile robotics — a full-course textbook plus a Docker-first example project built around the AgileX Limo Pro (simulation first, physical robot later).

## Course at a glance

| Item | Choice |
|------|--------|
| Audience | Mixed undergraduate / graduate |
| Pedagogy | Simulation + Docker first; physical Limo Pro in later chapters |
| Robot | AgileX Limo Pro |
| On-robot compute | NVIDIA Jetson Orin Nano |
| Backend compute | Two NVIDIA DGX Sparks (instructor / lab) |
| Middleware | **ROS 2 Humble** (pinned for Isaac Lab compatibility) |
| Learning / sim | NVIDIA Isaac Lab (ROS 2 bridge via official `ros2` Docker profile) |
| Textbook exports | PDF and DOCX (from Markdown / Quarto sources) |

## Why ROS 2 Humble?

Current NVIDIA Isaac Lab documents its official ROS 2 Docker image as installing **ROS 2 Humble** (`Dockerfile.ros2` / `ros2` Compose profile). Isaac Sim also lists Humble as a tested/recommended distro alongside Jazzy; for this course we pin **Humble** so student containers, Nav2 examples, and Isaac Lab’s supported ROS image stay aligned.

Evidence (verify when refreshing pins):

- [Isaac Lab installation — ROS 2 image](https://docs.nvidia.com/isaaclab/isaac-lab/installation) — *“Dockerfile.ros2 installs ROS 2 Humble”*; *“base image plus ROS 2 Humble”*
- [Isaac Lab Docker guide](https://isaac-sim.github.io/IsaacLab/main/source/deployment/docker.html) — ROS2 image extension installs Humble
- [Isaac Sim ROS 2 overview](https://docs.isaacsim.omniverse.nvidia.com/latest/ros2_tutorials/index.html) — recommends Humble and Jazzy

Decision details and refresh checklist live in [`STATUS.md`](STATUS.md).

## Repository layout

```
chapters/          Full-course textbook narrative (Ch. 01–14)
textbook/          Quarto book + export config (PDF/DOCX)
docs/              Adaptation notes, build helpers
code/ros2_ws/      ROS 2 workspace skeleton (student containers)
docker/            Dockerfiles + Compose for student workflow
tests/smoke/       Minimal smoke / CI stubs
scripts/           Local helper scripts
```

## Quick start (students)

Prerequisites: Docker Engine + Docker Compose v2.

```bash
# From repo root
docker compose -f docker/compose.yaml build
docker compose -f docker/compose.yaml run --rm ros2 bash
```

Inside the container (Humble workspace):

```bash
cd /ws && colcon build --symlink-install
source install/setup.bash
ros2 launch physibot_bringup sim_stub.launch.py
```

Physical Limo Pro + Orin Nano workflows appear only in later chapters — early work stays in simulation.

## Hardware story

1. **Early chapters** — Docker + Gazebo / Isaac Lab simulation; no robot required.
2. **Middle chapters** — localization, mapping, Nav2 on simulated Limo-class platforms (adapt existing OSS examples).
3. **Later chapters** — deploy to Orin Nano on the physical Limo Pro; train / heavy Isaac Lab workloads on DGX Sparks.

DGX Sparks are instructor/lab backends — students are not assumed to own them.

## Licensing

| Material | License |
|----------|---------|
| Textbook / narrative (`chapters/`, `textbook/`) | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) — see notice in those trees |
| Code (`code/`, `docker/`, scripts, CI) | [Apache License 2.0](LICENSE) — see [`LICENSE-CODE`](LICENSE-CODE) |

## Textbook

Chapter sources: [`chapters/`](chapters/). Build PDF/DOCX from [`textbook/`](textbook/) (Quarto preferred; Pandoc fallback — see [`textbook/README.md`](textbook/README.md)).

## Status & review

Full-course narrative drafted in `chapters/` (PMT-3). Example adaptations and verified PDF/DOCX exports remain open — see [`STATUS.md`](STATUS.md) for the review checklist and professor edit list.

## Brand

Working course brand: **PhysiBot** — AI physical models in mobile robotics (not a university seal).
