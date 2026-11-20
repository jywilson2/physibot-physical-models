# PhysiBot — STATUS (professor review handoff)

**Phase:** PMT-6 labs/code STATUS polish (SHA freeze, Isaac/Orin docs labs, Nav2 comment diff).  
**Last updated:** 2026-11-20  
**Default branch:** `main`  

**Landed:** PR #1 (progressive labs), PR #2 (full textbook narrative), PR #3 (review packaging). Labs checklist items below closed in the labs STATUS PR (PMT-6).

---

## Review checklist

### Narrative (`chapters/`, `textbook/`)

- [x] Full-course prose drafted (Ch. 01–14 + outline) — from PR #2 sources on this branch
- [ ] Professor edit pass (see **What to edit — narrative** below)
- [ ] Figures / diagrams added where prose currently describes them
- [ ] Capstone dates / rubric weights finalized for the term

### Labs & code (`labs/`, `code/ros2_ws/`, `docker/`)

- [x] Progressive labs ladder (`labs/01` … `09` + Isaac/Orin documentation-first labs)
- [x] Packages: `physibot_description`, `physibot_sim`, `physibot_bringup`
- [x] Freeze upstream `limo_ros2` humble SHA (`dcc5a8637f83236ed6778af86ad826e46a20cd92`) in `docs/adaptation-notes/limo.md`
- [ ] Swap stub laser / meshes after license review (still open)
- [x] Docker Compose smoke **documented** (host CI green without Docker; optional job commented in `.github/workflows/smoke.yml` — enable when runners can pull `ros:humble`)
- [x] Align chapter + lab launch names with real files (`description`, `sim_diff_drive`, `localization`, `mapping`, `nav2`)
- [x] `nav2_params.yaml` comments diffed vs Nav2 Humble + AgileX open_class (no vendored trees)
- [x] `labs/10-isaac-lab/` and `labs/12-orin-deploy/` documentation-first procedures (Spark vs Orin roles)

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

CI: `.github/workflows/smoke.yml` (layout + pytest unit/integration) — **required green path**.  

**Docker Compose smoke** (needs Docker daemon + `ros:humble` pull; not available on all cloud agents):

```bash
docker compose -f docker/compose.yaml build ros2
docker compose -f docker/compose.yaml --profile smoke run --rm smoke
```

Optional `ros2-image` job remains commented in the workflow until runners reliably pull Humble.

---

## What to edit — narrative (professor)

Priority items also appear in chapter “Professor edit notes” footers:

1. **Docker host matrix** — Linux required vs WSL2 (Ch. 01).
2. **Frame / URDF names** — sync prose with `physibot_limo.urdf.xacro` (Ch. 02–03).
3. **Measured Limo Pro parameters** — replace stub tread / radius / footprint (Ch. 03, 09 + table above).
4. **Launch file names** — canonical names are set (`description`, `sim_diff_drive`, `localization`, `mapping`, `nav2`); narrative polish can still deepen cross-links to `labs/NN-*`.
5. **Gazebo vs Isaac Sim** for early dynamics/viz (Ch. 04).
6. **Topic graph + bags** — real sim topics; bags outside git (Ch. 05).
7. **Nav2 defaults** — course uses RPP; optional DWB/MPPI teaching note (`INSTALL_NAV2=1` image) (Ch. 09).
8. **Isaac Lab pin** — course pin `v2.3.2` in Lab 10 / adaptation notes; confirm wheeled example ID per term (Ch. 10).
9. **Lab safety / networking** — e-stop, SSID, `ROS_DOMAIN_ID`, Orin image (Ch. 11–12); Lab 12 has a docs checklist.
10. **Spark booking** — accounts, shared FS, queues (Ch. 13).
11. **Capstone** — rubric weights, due dates, physical robot required? (Ch. 14).
12. **Figures** — TF tree, Nav2 BT, Bayes recursion, etc.

## What to edit — labs / code

1. ~~Freeze `limo_ros2` **humble** SHA in `docs/adaptation-notes/limo.md`.~~ Done: `dcc5a8637f83236ed6778af86ad826e46a20cd92`.
2. Replace stub laser with Gazebo/Isaac sensor once assets are licensed.
3. ~~Diff `nav2_params.yaml` against AgileX Nav2 examples after SHA freeze.~~ Done (comments + `nav2.md` table; no vendored trees).
4. ~~Fill `labs/10-isaac-lab/` and `labs/12-orin-deploy/` when pins exist.~~ Done (documentation-first; Isaac not in CI).
5. Keep secrets (hostnames, Wi-Fi, keys) out of git.
6. Enable optional Compose smoke CI job when runners can pull `ros:humble`.

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
| AgileX `limo_ros2` | https://github.com/agilexrobotics/limo_ros2 branch **`humble`** @ **`dcc5a8637f83236ed6778af86ad826e46a20cd92`** |
| AgileX Nav2 example (diff only) | `agilex_open_class` `limo/limo_bringup/param/nav2.yaml` @ `8e799754af623c3cec954b74b186d63d6ce8fa62` |
| Isaac Lab | tag **`v2.3.2`** (`37ddf626871758333d6ed89cf64ad702aef127d0`) — Lab 10 |
| Nav2 / slam_toolbox | Humble apt (`INSTALL_NAV2=1` Compose profile) |

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
