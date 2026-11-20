# Lab 12 — Orin Nano deploy (documentation-first)

**Chapter:** 12 — Orin Nano deploy  
**Hardware:** AgileX Limo Pro + **NVIDIA Jetson Orin Nano** (on-robot)  
**Backend (optional):** DGX Spark for any prior Isaac training (Lab 10) — not required on the robot  

This lab is **procedure + smoke checklist**. Course CI does **not** talk to a physical robot.

## Roles: Orin vs DGX Spark

| Machine | Role in this lab |
|---------|------------------|
| **Orin Nano** (on Limo Pro) | Drivers, sensors, Nav2 / localization at the edge |
| **DGX Spark** | Offline training / Isaac Lab only — do not run Spark as the robot computer |
| Student laptop | SSH / RViz / teleop client on the lab network |

## Upstream pin (drivers)

Freeze matches [`docs/adaptation-notes/limo.md`](../../docs/adaptation-notes/limo.md):

| Field | Value |
|-------|-------|
| Repo | https://github.com/agilexrobotics/limo_ros2 |
| Branch | **`humble`** |
| Commit | **`dcc5a8637f83236ed6778af86ad826e46a20cd92`** |
| Primary driver launch | `ros2 launch limo_base limo_base.launch.py` |

Docs: https://github.com/agilexrobotics/limo_ros2_doc  

At this SHA the humble tree provides `limo_base`, `limo_description` / `limo_car`, `limo_msgs` (README also mentions `limo_bringup`; verify packages after `colcon build`). Nav2 overlays for teaching live in **this** course repo (`physibot_bringup`), not vendored from that SHA.

## Goals

1. Confirm Humble + vendor drivers on Orin.
2. Bring up base + laser with known launch names from the pinned SHA.
3. Overlay course Nav2 / localization launches with `use_sim_time:=false` and driver remaps.
4. Practice lab network hygiene (`ROS_DOMAIN_ID`, no secrets in git).

## Expected hardware

- Limo Pro powered; e-stop reachable
- Orin Nano flashed per AgileX / NVIDIA JetPack guidance for the term
- LiDAR / depth as equipped (vendor launch may open YDLIDAR — see `limo_base/launch/open_ydlidar_launch.py` upstream)
- Lab Wi-Fi or Ethernet; laptop on same ROS domain

## Procedure

### 1. On Orin — workspace + pin

```bash
mkdir -p ~/physibot_ws/src && cd ~/physibot_ws/src
git clone https://github.com/agilexrobotics/limo_ros2.git
cd limo_ros2 && git checkout dcc5a8637f83236ed6778af86ad826e46a20cd92
cd ~/physibot_ws
# Also overlay course packages (copy or submodule) from physibot-physical-models/code/ros2_ws/src
colcon build --symlink-install
source install/setup.bash
echo "$ROS_DISTRO"   # expect: humble
```

### 2. Driver bringup (physical)

```bash
# Default serial device names are vendor-specific (e.g. ttylimo) — follow lab sheet, never commit site hostnames
ros2 launch limo_base limo_base.launch.py
```

Optional LiDAR (if installed and launch applies to your sensor):

```bash
ros2 launch limo_base open_ydlidar_launch.py
```

### 3. Course overlay — same graphs as Labs 07–09

On the robot (or a networked machine with the drivers already up), reuse course launches with **real time**:

```bash
source ~/physibot_ws/install/setup.bash
# Localization / Nav2 require maps + sensors; mapping builds a map while driving
ros2 launch physibot_bringup localization.launch.py use_sim_time:=false
# or
ros2 launch physibot_bringup mapping.launch.py use_sim_time:=false
# or
ros2 launch physibot_bringup nav2.launch.py use_sim_time:=false
```

You will need remaps so course `/scan` and `/odom` match vendor topics (pinned `limo_base` remaps wheel odom to `/wheel/odom` — align `nav2_params.yaml` / launch remaps in lab notes, not in git with robot-specific hacks unless generalized).

Canonical course launch names (sim or real overlay):

| Lab | Launch |
|-----|--------|
| Description | `physibot_bringup description.launch.py` |
| Diff-drive sim | `physibot_bringup sim_diff_drive.launch.py` |
| Localization | `physibot_bringup localization.launch.py` |
| Mapping | `physibot_bringup mapping.launch.py` |
| Nav2 | `physibot_bringup nav2.launch.py` |

### 4. Network checklist (no secrets in git)

- [ ] Agree `ROS_DOMAIN_ID` for the bench (document on the whiteboard / LMS, not in the repo)
- [ ] `ROS_LOCALHOST_ONLY=0` when multi-machine; firewall allows DDS as lab policy dictates
- [ ] Unique namespace if multiple Limos share a domain
- [ ] Never commit Wi-Fi SSIDs, passwords, private hostnames, or SSH keys

### 5. Instructor smoke (topic presence)

With drivers up, from Orin or laptop:

```bash
ros2 node list
ros2 topic list
ros2 topic hz /wheel/odom    # or whatever odom topic the pin publishes after remap
ros2 topic hz /scan          # if LiDAR launch is running
```

Pass criteria for a **bringup smoke** (not navigation quality): expected nodes alive, odom (and scan if required) streaming, TF tree includes `base_link` / `odom`.

## Safety

- Keep e-stop clear; start with low velocity limits in Nav2 (`velocity_smoother` / controller caps)
- First motion tests in a taped area with spotter
- Disable autonomy before changing batteries / networking

## Checkpoints

- [ ] Pinned `limo_ros2` SHA on Orin
- [ ] `limo_base.launch.py` runs; odom topic live
- [ ] Course launch names used (table above) — not obsolete `*_sim.launch.py` aliases
- [ ] Spark used only for offline work; Orin is the robot computer
- [ ] Domain ID / network notes kept out of git

## Pointers

- [`docs/adaptation-notes/limo.md`](../../docs/adaptation-notes/limo.md)
- [`docs/adaptation-notes/nav2.md`](../../docs/adaptation-notes/nav2.md)
- Labs 07–09 READMEs for Nav2 image / param locations
