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
labs/              Progressive runnable labs (tied to chapter numbers)
textbook/          Quarto book + exports (sample PDF under exports/)
docs/              Adaptation notes, PDF/DOCX export helpers
code/ros2_ws/      ROS 2 workspace (description, sim, bringup)
docker/            Student ROS 2 image + textbook TeX export image
tests/             Host smoke + unit + integration tests
scripts/           Local helper scripts
```

## Progressive labs

See [`labs/README.md`](labs/README.md) for the full ladder (description → teleop/odom → localization → mapping → Nav2 → Isaac/Orin stubs).

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
ros2 launch physibot_bringup description.launch.py
# later: sim_diff_drive.launch.py
```

Nav2 labs (07–09):

```bash
docker compose -f docker/compose.yaml --profile nav2 build ros2_nav2
docker compose -f docker/compose.yaml --profile nav2 run --rm ros2_nav2 bash
```

Host tests (no Docker / no ROS):

```bash
bash tests/smoke/test_repo_layout.sh
python3 -m pytest tests/unit tests/integration -q
```

Textbook PDF / DOCX:

```bash
./docs/export-tools/export-stub.sh          # host pandoc + TeX
./docs/export-tools/export-pdf-docker.sh    # no host TeX (needs Docker)
# Sample PDF: textbook/exports/physibot.pdf
```

Physical Limo Pro + Orin Nano workflows appear only in later chapters — early work stays in simulation.

## Hardware story

1. **Early chapters** — Docker + course stub sim / Isaac Lab; no robot required.
2. **Middle chapters** — localization, mapping, Nav2 on simulated Limo-class platforms (adapt existing OSS examples).
3. **Later chapters** — deploy to Orin Nano on the physical Limo Pro; train / heavy Isaac Lab workloads on DGX Sparks.

DGX Sparks are instructor/lab backends — students are not assumed to own them.

## Licensing

| Material | License |
|----------|---------|
| Textbook / narrative (`chapters/`, `textbook/`) | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) — see notice in those trees |
| Code (`code/`, `docker/`, `labs/` READMEs as course ops, scripts, CI) | [Apache License 2.0](LICENSE) — see [`LICENSE-CODE`](LICENSE-CODE) |

## Textbook

Chapter sources: [`chapters/`](chapters/). Build PDF/DOCX from [`textbook/`](textbook/) (Quarto preferred; Pandoc / Docker TeX — see [`docs/export-tools/README.md`](docs/export-tools/README.md)).

## Status & review

Full-course narrative + progressive labs are on `main`. Professor review checklist, hardware numbers, and PDF/DOCX status: [`STATUS.md`](STATUS.md).

## Brand

Working course brand: **PhysiBot** — AI physical models in mobile robotics (not a university seal).
