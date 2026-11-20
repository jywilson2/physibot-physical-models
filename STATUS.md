# PhysiBot — STATUS (professor review handoff)

**Phase:** PMT-5 review packaging (PDF recipe + sample, stronger tests, unified checklist).  
**Last updated:** 2026-11-20  
**Default branch:** `main`  
**This packaging PR branch:** `cursor/review-packaging-92ae` (does **not** replace open PRs #1 / #2)

## Open pull requests (coordinate here — do not fight merges)

| PR | Branch | Contents | Notes |
|----|--------|----------|-------|
| [#1](https://github.com/jywilson2/physibot-physical-models/pull/1) | `cursor/limo-pro-progressive-labs-c244` | Labs ladder, `physibot_*` packages, Docker/Nav2, kinematics smoke CI | CI green (layout + unit) |
| [#2](https://github.com/jywilson2/physibot-physical-models/pull/2) | `cursor/textbook-narrative-ecea` | Full Ch. 01–14 narrative, Pandoc export helper, professor edit notes | DOCX OK on agent; PDF was blocked then |
| **This PR** | `cursor/review-packaging-92ae` | Based on #1 + narrative chapters from #2; PDF sample + Docker TeX recipe; extra unit/integration tests; **this STATUS** | Prefer merge order: **#1 → #2 → packaging**, or merge packaging after resolving STATUS/README once |

Suggested merge order for humans: land labs (#1), then narrative (#2) accepting narrative `chapters/` + export tools, then packaging (or squash packaging after both).

---

## Review checklist

### Narrative (`chapters/`, `textbook/`)

- [x] Full-course prose drafted (Ch. 01–14 + outline) — from PR #2 sources on this branch
- [ ] Professor edit pass (see **What to edit — narrative** below)
- [ ] Figures / diagrams added where prose currently describes them
- [ ] Capstone dates / rubric weights finalized for the term

### Labs & code (`labs/`, `code/ros2_ws/`, `docker/`)

- [x] Progressive labs ladder (`labs/01` … `09` + Isaac/Orin stubs)
- [x] Packages: `physibot_description`, `physibot_sim`, `physibot_bringup`
- [ ] Freeze upstream `limo_ros2` SHA; swap stub laser / meshes after license review
- [ ] Docker Compose + `colcon` smoke on a runner that can pull `ros:humble`
- [ ] Align chapter launch names with real files (`sim_diff_drive`, `localization`, `mapping`, `nav2`)

### Hardware numbers (teaching stubs — verify on your Limo Pro)

| Quantity | Course stub | Where defined | Edit? |
|----------|-------------|---------------|-------|
| Body L×W | 0.322 × 0.220 m | `limo_body.xacro`, Nav2 header comment | Confirm vs your chassis |
| Height (URDF box) | 0.180 m body + mounts | `limo_body.xacro` | Align with published 251 mm overall if needed |
| Wheelbase | 0.200 m | `limo_body.xacro` | Measure |
| Tread (track width) | **0.175 m** | URDF, `kinematics.py`, odom defaults | Measure |
| Wheel radius | **0.040 m** | URDF, kinematics, odom | Measure / tire |
| \(v_{\max}\) | 1.0 m/s | odom node + Nav2 comments | Confirm controller limits |
| Frames | `base_footprint` → `base_link` → `laser_link` / `camera_link` / `imu_link` | URDF | Keep REP-105; rename only with narrative pass |

Unit test `tests/unit/test_hardware_constants.py` fails if URDF / sim defaults drift.

### PDF / DOCX export

| Artifact | Status | Path / command |
|----------|--------|----------------|
| **DOCX** | Verified (Pandoc) | `./docs/export-tools/export-stub.sh` → `textbook/exports/physibot.docx` (gitignored) |
| **PDF** | **Verified on packaging agent** (Pandoc + XeLaTeX + DejaVu) | Sample: [`textbook/exports/physibot.pdf`](textbook/exports/physibot.pdf) (~240 KB, ~42 pp, CC BY-NC 4.0) |
| Quarto | Preferred when installed; not required for sample | `quarto render textbook/physibot.qmd --to pdf --output-dir textbook/exports` |
| **Docker PDF** (no host TeX) | Recipe committed | `./docs/export-tools/export-pdf-docker.sh` → builds `docker/Dockerfile.textbook` |

Host packages: `pandoc`, `texlive-xetex`, `texlive-fonts-recommended`, `texlive-latex-extra`, `fonts-dejavu`.  
Export uses `markdown+tex_math_single_backslash` so `\(...\)` math survives XeLaTeX.

### Tests (student-runnable on host)

```bash
bash tests/smoke/test_repo_layout.sh
python3 -m pytest tests/unit tests/integration -q
```

| Suite | Covers |
|-------|--------|
| `tests/smoke/` | Layout, Humble pin, lab ladder, launch paths |
| `tests/unit/test_diff_drive_kinematics.py` | Unicycle + wheel Jacobian edge cases |
| `tests/unit/test_hardware_constants.py` | URDF ↔ sim ↔ Nav2 number consistency |
| `tests/integration/test_launch_and_packages.py` | Launch AST parse, package.xml, setup scripts |
| `tests/integration/test_export_sources.py` | Chapters ↔ Quarto ↔ export script wiring |

CI: `.github/workflows/smoke.yml` (layout + pytest unit/integration). Docker image job still optional.

---

## What to edit — narrative (professor)

Priority items also appear in chapter “Professor edit notes” footers:

1. **Docker host matrix** — Linux required vs WSL2 (Ch. 01).
2. **Frame / URDF names** — sync prose with `physibot_limo.urdf.xacro` (Ch. 02–03).
3. **Measured Limo Pro parameters** — replace stub tread / radius / footprint (Ch. 03, 09 + table above).
4. **Launch file names** — point students at real launches: `description`, `sim_diff_drive`, `localization`, `mapping`, `nav2` under `physibot_bringup` (Ch. 03, 07–09). Cross-link `labs/NN-*`.
5. **Gazebo vs Isaac Sim** for early dynamics/viz (Ch. 04).
6. **Topic graph + bags** — real sim topics; bags outside git (Ch. 05).
7. **Nav2 defaults** — DWB vs MPPI; `INSTALL_NAV2=1` image (Ch. 09).
8. **Isaac Lab pin** — release tag + wheeled example (Ch. 10 / `labs/10-isaac-lab`).
9. **Lab safety / networking** — e-stop, SSID, `ROS_DOMAIN_ID`, Orin image (Ch. 11–12).
10. **Spark booking** — accounts, shared FS, queues (Ch. 13).
11. **Capstone** — rubric weights, due dates, physical robot required? (Ch. 14).
12. **Figures** — TF tree, Nav2 BT, Bayes recursion, etc.

## What to edit — labs / code

1. Freeze `limo_ros2` **humble** SHA in `docs/adaptation-notes/limo.md`.
2. Replace stub laser with Gazebo/Isaac sensor once assets are licensed.
3. Diff `nav2_params.yaml` against AgileX Nav2 examples after SHA freeze.
4. Fill `labs/10-isaac-lab/` and `labs/12-orin-deploy/` when pins exist.
5. Keep secrets (hostnames, Wi-Fi, keys) out of git.

---

## ROS 2 / Isaac Lab decision

| Field | Value |
|-------|-------|
| **Pinned ROS 2 distro** | **Humble** |
| **Rationale** | Matches current NVIDIA Isaac Lab official ROS 2 Docker image; one distro for Compose + Lab `ros2` profile. |
| **Isaac Lab profile** | `ros2` (`Dockerfile.ros2`, `.env.ros2`) |
| **Caveat** | Re-verify each term — Lab ROS2 images have broken during Python upgrades before. |

### Evidence links

1. [Isaac Lab installation](https://docs.nvidia.com/isaaclab/isaac-lab/installation) — Humble in `Dockerfile.ros2`.
2. [Isaac Lab Docker guide](https://isaac-sim.github.io/IsaacLab/main/source/deployment/docker.html).
3. [Isaac Sim ROS 2 tutorials](https://docs.isaacsim.omniverse.nvidia.com/latest/ros2_tutorials/index.html) — Humble and Jazzy.
4. [Isaac Sim ROS 2 install](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/install_ros.html).

### Upstream pins

| Component | Pin |
|-----------|-----|
| AgileX `limo_ros2` | https://github.com/agilexrobotics/limo_ros2 branch **`humble`** (SHA TBD) |
| Nav2 / slam_toolbox | Humble apt (`INSTALL_NAV2=1` Compose profile) |

---

## Known gaps (not blocking professor narrative review)

- No Docker daemon on some cloud agents → student machines / CI must run Compose builds.
- Isaac Lab + Orin labs remain stubs/docs.
- Sample PDF has minor Unicode fallbacks for rare box-drawing glyphs in code fences (content intact).
- Full Quarto PDF theme / print CSS not customized yet (Pandoc book geometry is the verified path).

## How to regenerate exports

```bash
# Host (pandoc + TeX)
./docs/export-tools/export-stub.sh

# Docker (no host TeX)
./docs/export-tools/export-pdf-docker.sh

# Quarto
mkdir -p textbook/exports
quarto render textbook/physibot.qmd --to pdf --output-dir textbook/exports
quarto render textbook/physibot.qmd --to docx --output-dir textbook/exports
```

Details: [`docs/export-tools/README.md`](docs/export-tools/README.md).
