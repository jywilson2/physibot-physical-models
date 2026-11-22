# PhysiBot labs — progressive Limo Pro ladder

Sim-first labs that grow with the textbook. Each lab has a README tied to a
chapter number. Run everyday ROS work through Docker Compose (`docker/`).

| Lab | Chapter | Theme | What runs |
|-----|---------|-------|-----------|
| [`01-docker-hello`](01-docker-hello/) | 01 | Docker + description | `description.launch.py` |
| [`03-kinematics-teleop`](03-kinematics-teleop/) | 03 | Diff-drive + teleop | `sim_diff_drive.launch.py` |
| [`04-odometry-models`](04-odometry-models/) | 04 | Odometry / physical models | same sim + kinematics unit tests |
| [`07-localization`](07-localization/) | 07 | Localization (AMCL) | `localization.launch.py` (Nav2 image) |
| [`08-mapping`](08-mapping/) | 08 | Mapping / SLAM | `mapping.launch.py` (Nav2 image) |
| [`09-nav2`](09-nav2/) | 09 | Nav2 navigation | `nav2.launch.py` (Nav2 image) |
| [`10-isaac-lab`](10-isaac-lab/) | 10 | Isaac Lab | docs-first procedure (DGX Spark; pin `v3.0.0`) |
| [`12-orin-deploy`](12-orin-deploy/) | 12 | Orin Nano deploy | docs-first procedure (physical Limo + Orin) |

### Alternate Part 2 labs (learned navigation — sketch)

Latent world-model track that replaces Nav2/AMCL/SLAM for that track only.
See [`part2/README.md`](part2/README.md) and [`../chapters/part2/00-outline.md`](../chapters/part2/00-outline.md).

| Lab | Chapters | Theme |
|-----|----------|-------|
| [`part2/01-isaac-world-model`](part2/01-isaac-world-model/) | P2-01–02 | Isaac Lab world-model training |
| [`part2/02-neural-mapping`](part2/02-neural-mapping/) | P2-03 | Learned occupancy / neural mapping |
| [`part2/03-latent-rollout-planning`](part2/03-latent-rollout-planning/) | P2-04–05 | Planning via latent rollout |
| [`part2/04-limo-on-robot-finetune`](part2/04-limo-on-robot-finetune/) | P2-06–07 | Limo on-robot fine-tuning |

## Canonical launch names (`physibot_bringup`)

Use these names in chapters and lab sheets (do **not** invent `*_sim.launch.py` aliases):

| Launch | Package |
|--------|---------|
| `description.launch.py` | `physibot_bringup` |
| `sim_diff_drive.launch.py` | `physibot_bringup` |
| `localization.launch.py` | `physibot_bringup` |
| `mapping.launch.py` | `physibot_bringup` |
| `nav2.launch.py` | `physibot_bringup` |

Supporting packages: `physibot_description` (URDF), `physibot_sim` (odom / stub laser).

`sim_stub.launch.py` remains as a thin alias that includes `sim_diff_drive` for older notes — prefer `sim_diff_drive` / `description` in new prose.

## Quick path

```bash
# From repo root — everyday student image (no Nav2 metapackage)
docker compose -f docker/compose.yaml build ros2
docker compose -f docker/compose.yaml run --rm ros2 bash

# Inside container
cd /ws && colcon build --symlink-install && source install/setup.bash
ros2 launch physibot_bringup description.launch.py
```

For Chapters 07–09, build the Nav2 profile (larger image):

```bash
docker compose -f docker/compose.yaml --profile nav2 build ros2_nav2
docker compose -f docker/compose.yaml --profile nav2 run --rm ros2_nav2 bash
```

Optional Compose smoke (requires Docker daemon + ability to pull `ros:humble`):

```bash
docker compose -f docker/compose.yaml build ros2
docker compose -f docker/compose.yaml --profile smoke run --rm smoke
```

Host-only checks (no Docker; what CI runs today):

```bash
bash tests/smoke/test_repo_layout.sh
python3 -m pytest tests/unit tests/integration -q
```

## Design rules

- Prefer adapting [agilexrobotics/limo_ros2](https://github.com/agilexrobotics/limo_ros2) (`humble` @ `dcc5a8637f83236ed6778af86ad826e46a20cd92`), Nav2 tutorials, and Isaac Lab over greenfield stacks.
- Early labs need **no GPU** and **no physical robot**.
- Course packages are thin overlays; see `docs/adaptation-notes/`.
- DGX Spark = training / Isaac; Orin Nano = on-robot deploy (Labs 10 vs 12).
