# PhysiBot labs — progressive Limo Pro ladder

Sim-first labs that grow with the textbook. Each lab has a README tied to a
chapter number. Run everything through Docker Compose (`docker/`).

| Lab | Chapter | Theme | What runs |
|-----|---------|-------|-----------|
| [`01-docker-hello`](01-docker-hello/) | 01 | Docker + description | `description.launch.py` |
| [`03-kinematics-teleop`](03-kinematics-teleop/) | 03 | Diff-drive + teleop | `sim_diff_drive.launch.py` |
| [`04-odometry-models`](04-odometry-models/) | 04 | Odometry / physical models | same sim + kinematics unit tests |
| [`07-localization`](07-localization/) | 07 | Localization (AMCL) | `localization.launch.py` (Nav2 image) |
| [`08-mapping`](08-mapping/) | 08 | Mapping / SLAM | `mapping.launch.py` (Nav2 image) |
| [`09-nav2`](09-nav2/) | 09 | Nav2 navigation | `nav2.launch.py` (Nav2 image) |
| [`10-isaac-lab`](10-isaac-lab/) | 10 | Isaac Lab | docs / stubs |
| [`12-orin-deploy`](12-orin-deploy/) | 12 | Orin Nano deploy | docs / stubs |

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

## Design rules

- Prefer adapting [agilexrobotics/limo_ros2](https://github.com/agilexrobotics/limo_ros2) (`humble` branch), Nav2 tutorials, and Isaac Lab over greenfield stacks.
- Early labs need **no GPU** and **no physical robot**.
- Course packages are thin overlays; see `docs/adaptation-notes/`.
