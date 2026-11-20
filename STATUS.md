# PhysiBot — STATUS (professor review handoff)

**Phase:** PMT-6 STATUS polish — narrative + labs checklists resolved (union after PR #4 + #5).  
**Last updated:** 2026-11-20  
**Default branch:** `main`  

**Landed:** PR #1 (progressive labs), PR #2 (full textbook narrative), PR #3 (review packaging), PR #4 (labs STATUS), PR #5 (narrative STATUS).  
**Export refresh:** Regenerated `textbook/exports/physibot.pdf` (~295 KB, 46 pp, figures embedded) from `main` after PR #4/#5 via `./docs/export-tools/export-stub.sh` (DOCX regenerated locally; gitignored).

---

## Review checklist

### Narrative (`chapters/`, `textbook/`)

- [x] Full-course prose drafted (Ch. 01–14 + outline) — from PR #2 sources on this branch
- [x] Pedagogical defaults resolved (Docker/WSL2, frames, launches, Gazebo vs Isaac, Nav2 DWB, safety, Spark queue, capstone) — see **Narrative defaults** below
- [x] Figures / diagrams added (`textbook/figures/`: TF tree, Bayes recursion, Nav2 BT sketch)
- [x] Capstone rubric weights + **sample calendar** (placeholder term dates clearly marked in Ch. 14)

### Labs & code (`labs/`, `code/ros2_ws/`, `docker/`)

- [x] Progressive labs ladder (`labs/01` … `09` + Isaac/Orin documentation-first labs)
- [x] Packages: `physibot_description`, `physibot_sim`, `physibot_bringup`
- [x] Freeze upstream `limo_ros2` humble SHA (`dcc5a8637f83236ed6778af86ad826e46a20cd92`) in `docs/adaptation-notes/limo.md`
- [ ] Swap stub laser / meshes after license review (still open)
- [x] Docker Compose smoke **documented** (host CI green without Docker; optional job commented in `.github/workflows/smoke.yml` — enable when runners can pull `ros:humble`)
- [x] Align chapter + lab launch names with real files (`description`, `sim_diff_drive`, `localization`, `mapping`, `nav2`)
- [x] `nav2_params.yaml` comments diffed vs Nav2 Humble + AgileX open_class (no vendored trees); teaching controller **DWB**
- [x] `labs/10-isaac-lab/` and `labs/12-orin-deploy/` documentation-first procedures (Spark vs Orin roles)

### Hardware numbers (published AgileX Limo Pro + labeled estimates)

Sources: [Limo Pro user manual tech specs](https://github.com/agilexrobotics/limo_pro_doc/blob/master/Limo%20Pro%20user%20manual(EN).md), [LIMO ROS2 Humble doc](https://github.com/agilexrobotics/limo_ros2_doc/blob/master/LIMO-ROS2-humble(EN).md).

| Quantity | Course value | Where defined | Status |
|----------|--------------|---------------|--------|
| Body L×W | **0.322 × 0.220 m** | `limo_body.xacro`, Nav2 comments | Published overall footprint |
| Overall height | **0.251 m** | docs / `overall_height` xacro property | Published; URDF visual box stays 0.180 m hull |
| Wheelbase | **0.200 m** | `limo_body.xacro` | Published |
| Tread (track width) | **0.175 m** | URDF, `kinematics.py`, odom | Published |
| Wheel radius | **0.040 m** | URDF, kinematics, odom | **Teaching estimate only** — not in AgileX body table; measure tire |
| \(v_{\max}\) | **1.0 m/s** | odom + Nav2 comments | Published no-load max |
| Frames | `base_footprint` → `base_link` → `laser_link` / `camera_link` / `imu_link` | URDF + Ch. 02–03 | Locked to course URDF |

Unit test `tests/unit/test_hardware_constants.py` fails if URDF / sim defaults drift.

### PDF / DOCX export

| Artifact | Status | Path / command |
|----------|--------|----------------|
| **DOCX** | Verified (Pandoc) | `./docs/export-tools/export-stub.sh` → `textbook/exports/physibot.docx` (gitignored) |
| **PDF** | **Verified** (Pandoc + XeLaTeX + DejaVu; post–PR #4/#5 refresh) | Sample: [`textbook/exports/physibot.pdf`](textbook/exports/physibot.pdf) (~295 KB, 46 pp, CC BY-NC 4.0) |
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

CI: `.github/workflows/smoke.yml` (layout + pytest unit/integration) — **required green path**.  

**Docker Compose smoke** (needs Docker daemon + `ros:humble` pull; not available on all cloud agents):

```bash
docker compose -f docker/compose.yaml build ros2
docker compose -f docker/compose.yaml --profile smoke run --rm smoke
```

Optional `ros2-image` job remains commented in the workflow until runners reliably pull Humble.

---

## Narrative defaults (resolved without waiting on professor)

Chapter footers now say **Pedagogical defaults (resolved)** instead of open edit notes.

| # | Topic | Resolution |
|---|-------|------------|
| 1 | Docker host matrix | Linux required; WSL2 supported with caveats (Ch. 01 §1.6) |
| 2 | Frame / URDF names | Locked to `physibot_limo` / `limo_body` (`base_footprint`…) |
| 3 | Limo Pro parameters | Published L×W×H / wheelbase / tread / \(v_{\max}\); wheel radius labeled estimate |
| 4 | Launch names | `description`, `sim_diff_drive`, `localization`, `mapping`, `nav2` (+ `sim_stub`) |
| 5 | Gazebo vs Isaac | Stub sim (+ Gazebo when licensed) for Ch. 03–09; Isaac Lab from Ch. 10 |
| 6 | Topics + bags | Stub topic graph in Ch. 05; bags outside git |
| 7 | Nav2 defaults | **DWB** teaching default; MPPI optional; Compose profile `nav2` |
| 8 | Isaac Lab pin | **`v3.0.0`** + Humble `ros2` profile (Ch. 10 / adaptation notes) |
| 9 | Safety / networking | E-stop + `ROS_DOMAIN_ID` principles in Ch. 11–12; secrets on LMS |
| 10 | Spark booking | Generic lab-queue guidance (Ch. 13); URLs on LMS |
| 11 | Capstone | Default rubric weights; physical optional; **sample calendar** marked |
| 12 | Figures | `textbook/figures/{tf-tree,bayes-recursion,nav2-bt-sketch}.svg` |

**Still open (true blockers / lab-local):** fleet tire measurement for wheel radius; LMS secrets (SSID, domain IDs, Spark booking URL); exact wheeled Isaac Lab tutorial name if upstream renames it.

## What to edit — labs / code

1. ~~Freeze `limo_ros2` **humble** SHA in `docs/adaptation-notes/limo.md`.~~ Done: `dcc5a8637f83236ed6778af86ad826e46a20cd92`.
2. Replace stub laser with Gazebo/Isaac sensor once assets are licensed.
3. ~~Diff `nav2_params.yaml` against AgileX Nav2 examples after SHA freeze.~~ Done (comments + `nav2.md` table; teaching controller **DWB**; no vendored trees).
4. ~~Fill `labs/10-isaac-lab/` and `labs/12-orin-deploy/` when pins exist.~~ Done (documentation-first; Isaac not in CI).
5. Keep secrets (hostnames, Wi-Fi, keys) out of git.
6. Enable optional Compose smoke CI job when runners can pull `ros:humble`.

---

## ROS 2 / Isaac Lab decision

| Field | Value |
|-------|-------|
| **Pinned ROS 2 distro** | **Humble** |
| **Isaac Lab release** | **`v3.0.0`** (GA) |
| **Rationale** | Lab `ros2` Docker profile installs Humble; one distro for Compose + Lab. |
| **Isaac Lab profile** | `ros2` (`Dockerfile.ros2`, `.env.ros2`) |
| **Caveat** | Re-verify each term — Lab ROS2 images have broken during Python upgrades before. |

### Evidence links

1. [Isaac Lab `v3.0.0` installation](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/isaaclab/installation.html) — `ros2` profile = base + Humble.
2. [Isaac Lab `v3.0.0` GitHub release](https://github.com/isaac-sim/IsaacLab/releases/tag/v3.0.0).
3. [NVIDIA Isaac Lab installation hub](https://docs.nvidia.com/isaaclab/isaac-lab/installation).
4. [Isaac Sim ROS 2 tutorials](https://docs.isaacsim.omniverse.nvidia.com/latest/ros2_tutorials/index.html) — Humble and Jazzy.

### Upstream pins

| Component | Pin |
|-----------|-----|
| NVIDIA Isaac Lab | Git tag **`v3.0.0`** |
| AgileX `limo_ros2` | https://github.com/agilexrobotics/limo_ros2 branch **`humble`** @ **`dcc5a8637f83236ed6778af86ad826e46a20cd92`** |
| AgileX Nav2 example (diff only) | `agilex_open_class` `limo/limo_bringup/param/nav2.yaml` @ `8e799754af623c3cec954b74b186d63d6ce8fa62` |
| Nav2 / slam_toolbox | Humble apt (`INSTALL_NAV2=1` Compose profile); controller **DWB** |

---

## Known gaps (not blocking professor narrative review)

- No Docker daemon on some cloud agents → document Compose smoke locally; host pytest/layout CI is the required path.
- Isaac Lab + Orin labs are documentation-first (not full Isaac/Orin CI).
- Stub laser / vendor meshes still pending license review.
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
