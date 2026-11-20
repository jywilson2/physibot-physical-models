# PhysiBot — STATUS

**Phase:** PMT-2 scaffold only (structure + outline + Docker skeleton).  
**Last updated:** 2026-11-20  
**Default branch (intended):** `main`

## Review checklist (current)

- [x] Course repo tree scaffolded (README, licenses, chapters, textbook, Docker, ROS 2 ws)
- [x] ROS 2 distro pin documented with NVIDIA evidence (**Humble**)
- [x] Local git `main` committed and pushed to GitHub
- [x] GitHub repo live: https://github.com/jywilson2/physibot-physical-models (public)
- [x] `origin` remote configured to that URL
- [x] First push of `main` complete — https://github.com/jywilson2/physibot-physical-models (`ea91e694f36be2a1e42efcc0aa61f163488938f9`)
- [ ] Full textbook narrative written (chapters are stubs)
- [ ] PDF / DOCX export pipeline verified end-to-end
- [ ] Limo / Nav2 / Isaac example adaptations filled in (placeholders only)
- [ ] Student smoke tests green in CI on a real runner
- [ ] Orin Nano deploy chapter runnable against lab hardware
- [ ] DGX Spark training workflow validated in lab
- [ ] Capstone brief + rubrics finalized
- [ ] Professor edit pass on narrative + code

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

## Remaining work (post-scaffold)

1. **Narrative** — expand `chapters/` stubs into full textbook prose; wire Quarto/Pandoc for PDF+DOCX.
3. **Examples** — adapt AgileX Limo ROS 2, Nav2, and Isaac Lab demos per `docs/adaptation-notes/`.
4. **CI** — flesh out smoke workflow beyond stubs once images publish.
5. **Hardware labs** — Orin Nano + DGX Spark runbooks with lab-specific hostnames/secrets out of git.

## Out of scope for PMT-2

- Full chapter prose and figures
- Production-ready robot stacks written from scratch
- Assuming students own DGX Sparks
