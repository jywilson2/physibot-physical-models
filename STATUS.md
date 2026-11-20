# PhysiBot — STATUS

**Phase:** PMT-4 progressive Limo Pro labs (sim-first Docker ladder).  
**Last updated:** 2026-11-20  
**Default branch (intended):** `main`

## Review checklist (current)

- [x] Course repo tree scaffolded (README, licenses, chapters, textbook, Docker, ROS 2 ws)
- [x] ROS 2 distro pin documented with NVIDIA evidence (**Humble**)
- [x] Local git `main` committed and pushed to GitHub
- [x] GitHub repo live: https://github.com/jywilson2/physibot-physical-models (public)
- [x] Progressive labs ladder under `labs/` (01, 03, 04, 07, 08, 09, 10 stub, 12 stub)
- [x] Course packages: `physibot_description`, `physibot_sim`, `physibot_bringup` (sim + Nav2 launches)
- [x] Host unit tests for diff-drive kinematics + layout smoke in CI
- [ ] Full textbook narrative written (chapters are stubs — narrative workers)
- [ ] PDF / DOCX export pipeline verified end-to-end
- [ ] Upstream `limo_ros2` meshes/drivers vendored or git-submodule at frozen SHA
- [ ] Docker Compose image build + `colcon` smoke green in CI (runner must pull `ros:humble`)
- [ ] Orin Nano deploy chapter runnable against lab hardware
- [ ] DGX Spark training workflow validated in lab
- [ ] Capstone brief + rubrics finalized
- [ ] Professor edit pass on narrative + code

## Code-side edit needs (professor / narrative coordination)

1. **Chapters ↔ labs** — chapter stubs still say “exercises (stubs)”; point students at `labs/NN-*` once narrative expands (do not rewrite chapters wholesale in code PRs).
2. **Gazebo / Isaac assets** — replace `physibot_sim` stub laser with adapted Limo Gazebo or Isaac sensors before claiming realistic SLAM.
3. **Nav2 params** — `nav2_params.yaml` is a teaching overlay; diff against AgileX Nav2 examples when SHA is frozen.
4. **Licensing of vendor meshes** — keep geometric stubs until mesh license review is done.
5. **Isaac Lab attach steps** — fill `labs/10-isaac-lab/` when Lab release tag is pinned.
6. **Orin runbook** — lab hostnames / `ROS_DOMAIN_ID` conventions belong in private lab docs, not git secrets.

## ROS 2 / Isaac Lab decision

| Field | Value |
|-------|-------|
| **Pinned ROS 2 distro** | **Humble** |
| **Rationale** | Most reliable match to current NVIDIA Isaac Lab official ROS 2 Docker image; keeps student Compose stack and Isaac Lab `ros2` profile on the same distro. |
| **Isaac Lab profile** | `ros2` (`Dockerfile.ros2`, `.env.ros2`) |
| **Isaac Sim note** | Isaac Sim documents Humble *and* Jazzy as recommended; course still pins Humble for Lab Docker alignment. |
| **Caveat** | Isaac Lab release notes have historically flagged intermittent ROS2 Docker image breakage during Python upgrades — re-verify before each term. |

### Evidence links

1. [Isaac Lab installation](https://docs.nvidia.com/isaaclab/isaac-lab/installation) — ROS 2 image section: *“Dockerfile.ros2 installs ROS 2 Humble from an apt package”*; profile table: *“The base image plus ROS 2 Humble”*.
2. [Isaac Lab Docker guide](https://isaac-sim.github.io/IsaacLab/main/source/deployment/docker.html) — ROS2 image extension installs Humble via apt; `ROS2_APT_PACKAGE` defaults to `ros-base`.
3. [Isaac Sim ROS 2 tutorials index](https://docs.isaacsim.omniverse.nvidia.com/latest/ros2_tutorials/index.html) — recommends ROS 2 Humble and Jazzy.
4. [Isaac Sim ROS 2 installation](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/install_ros.html) — platform/distro matrix (Humble on 22.04; Jazzy often paired with 24.04).

### Refresh procedure (each term)

1. Re-read Isaac Lab installation + Docker docs for the active release.
2. Confirm `Dockerfile.ros2` still installs Humble (or update pin + student images together).
3. Note any Isaac Lab ROS2 image known issues in release notes.
4. Update this section + README table in the same PR.

## Upstream adaptation pins

| Component | Pin |
|-----------|-----|
| AgileX `limo_ros2` | https://github.com/agilexrobotics/limo_ros2 branch **`humble`** (SHA TBD) |
| Nav2 | ROS 2 Humble apt (`ros-humble-navigation2`, `ros-humble-nav2-bringup`) |
| slam_toolbox | `ros-humble-slam-toolbox` in Nav2 Compose profile |

## How to run (code labs)

```bash
bash tests/smoke/test_repo_layout.sh
python3 -m pytest tests/unit/test_diff_drive_kinematics.py -q

docker compose -f docker/compose.yaml build ros2
docker compose -f docker/compose.yaml run --rm ros2 bash
# inside: colcon build --symlink-install && source install/setup.bash
#         ros2 launch physibot_bringup sim_diff_drive.launch.py

docker compose -f docker/compose.yaml --profile nav2 build ros2_nav2
```

## Remaining work

1. **Narrative** — expand `chapters/` stubs; wire Quarto/Pandoc for PDF+DOCX.
2. **Examples** — freeze `limo_ros2` SHA; swap stub laser for Gazebo/Isaac when ready.
3. **CI** — enable Docker smoke job when runners pull `ros:humble` reliably.
4. **Hardware labs** — Orin Nano + DGX Spark runbooks (secrets out of git).
