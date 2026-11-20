# PhysiBot — STATUS

**Phase:** PMT-3 textbook narrative drafted (full-course prose in `chapters/01`–`14`).  
**Last updated:** 2026-11-20  
**Default branch:** `main` (narrative landed via PR branch `cursor/textbook-narrative-ecea` unless fast-forwarded)

## Review checklist (current)

- [x] Course repo tree scaffolded (README, licenses, chapters, textbook, Docker, ROS 2 ws)
- [x] ROS 2 distro pin documented with NVIDIA evidence (**Humble**)
- [x] GitHub repo live: https://github.com/jywilson2/physibot-physical-models
- [x] **Full textbook narrative written** (`chapters/01`–`14` + outline; professor edit notes at each chapter end)
- [x] DOCX export verified via Pandoc (`./docs/export-tools/export-stub.sh` → `textbook/exports/physibot.docx`; gitignored)
- [ ] PDF export verified (needs Quarto **or** Pandoc + TeX Live — TeX not present on cloud agent image)
- [ ] Limo / Nav2 / Isaac example adaptations filled in (placeholders / stub launches remain)
- [ ] Student smoke tests green in CI on a real runner
- [ ] Orin Nano deploy chapter runnable against lab hardware
- [ ] DGX Spark training workflow validated in lab
- [ ] Capstone brief + rubrics finalized (draft rubric in Ch. 14)
- [ ] Professor edit pass on narrative + code

## Chapter list (narrative)

| Ch | Title | Depth |
|----|-------|-------|
| 00 | Outline | Course map |
| 01 | Welcome & Docker | Full |
| 02 | Linear algebra refresh | Full |
| 03 | Mobile robot kinematics | Full |
| 04 | Dynamics & AI physical models | Full |
| 05 | Sensing & observation models | Full |
| 06 | Estimation fundamentals | Full |
| 07 | Localization | Full |
| 08 | Mapping & SLAM | Full |
| 09 | Navigation with Nav2 | Full |
| 10 | Learning with Isaac Lab | Full |
| 11 | Sim-to-real | Full |
| 12 | Orin Nano deploy | Full |
| 13 | DGX Spark training | Full |
| 14 | Capstone | Full |

## Export status (PDF / DOCX)

**Commands** (repo root):

```bash
# Preferred — Quarto
mkdir -p textbook/exports
quarto render textbook/physibot.qmd --to pdf --output-dir textbook/exports
quarto render textbook/physibot.qmd --to docx --output-dir textbook/exports

# Fallback — Pandoc
./docs/export-tools/export-stub.sh
# → textbook/exports/physibot.docx
# → textbook/exports/physibot.pdf  (if xelatex/lualatex/pdflatex present)
```

**Agent environment (2026-11-20):**

| Artifact | Status |
|----------|--------|
| DOCX | **OK** — installed `pandoc` 3.1.3; `./docs/export-tools/export-stub.sh` wrote `textbook/exports/physibot.docx` (~60 KB). Path is gitignored (`textbook/exports/*`). |
| PDF | **Blocked** — no `quarto`, and no `xelatex`/`lualatex`/`pdflatex`. Install TeX Live or Quarto on a workstation/CI runner, then re-run export commands. |
| Quarto | Not installed on agent; `textbook/physibot.qmd` includes remain the preferred path when Quarto is available. |

Do not commit multi-megabyte export binaries unless course policy explicitly wants them in git; prefer LMS/releases.

## What needs professor editing (narrative)

Priority items called out in chapter “Professor edit notes” footers:

1. **Docker host matrix** — Linux required vs. WSL2 support (Ch. 01).
2. **Frame / URDF names** — align all text with final adapted Limo description (Ch. 02–03).
3. **Measured Limo Pro parameters** — track width, wheel radius, max \(v,\omega\), footprint polygon (Ch. 03, 09).
4. **Launch file names** — replace `*_when adapted` placeholders (`sim_limo`, `slam_sim`, `localization_sim`, `nav2_sim`) once packages land (Ch. 03, 07–09).
5. **Gazebo vs. Isaac Sim** for Ch. 03–09 dynamics/viz sandbox (Ch. 04 adaptation note).
6. **Topic graph + bags** — paste real sim topic names; host sample bags outside git (Ch. 05).
7. **Nav2 defaults** — DWB vs. MPPI; `INSTALL_NAV2` in student image (Ch. 09).
8. **Isaac Lab pin** — release tag + exact upstream wheeled example for Ch. 10.
9. **Lab safety / networking** — e-stop form, SSID, `ROS_DOMAIN_ID` map, Orin image strategy (Ch. 11–12).
10. **Spark booking** — accounts, shared FS paths, queue scripts (Ch. 13).
11. **Capstone** — rubric weights, due dates, whether physical robot is required (Ch. 14).
12. **Figures** — add diagrams (TF tree, Nav2 BT, Bayes recursion) where prose currently describes them.

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

## Remaining work (post-narrative)

1. **Export verify** — install Quarto or Pandoc+TeX; produce `textbook/exports/physibot.{pdf,docx}`.
2. **Examples** — adapt AgileX Limo ROS 2, Nav2, and Isaac Lab demos per `docs/adaptation-notes/`.
3. **CI** — flesh out smoke workflow beyond layout stubs; optional export job.
4. **Hardware labs** — Orin Nano + DGX Spark runbooks with lab-specific hostnames/secrets out of git.
5. **Professor edit pass** — address the numbered narrative list above.

## Out of scope for this narrative pass

- Production-ready robot stacks written from scratch
- Assuming students own DGX Sparks
- Committing multi-GB Isaac checkpoints
