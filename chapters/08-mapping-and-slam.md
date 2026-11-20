# Chapter 08 — Mapping and SLAM

> **License:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).  
> **Hardware:** simulation only.  
> **Lab code:** [`physibot_bringup`](../code/ros2_ws/src/physibot_bringup/); see [`docs/adaptation-notes/nav2.md`](../docs/adaptation-notes/nav2.md) and [`docs/adaptation-notes/limo.md`](../docs/adaptation-notes/limo.md).

## Learning goals

1. Explain occupancy grid mapping as recursive evidence fusion along laser rays.
2. State SLAM as the joint estimation of pose and map; contrast filter vs. pose-graph intuitions.
3. Run an existing 2D SLAM stack (e.g. slam_toolbox) in the course container—adapted, not reinvented.
4. Save a map usable by Nav2 localization and navigation.

## 8.1 From localization to SLAM

Chapter 07 assumed a known map. **SLAM** (Simultaneous Localization and Mapping) estimates map \(m\) and trajectory \(x_{1:t}\) together. For indoor differential-drive robots with 2D LiDAR, the industry pattern is:

1. Build a map with a 2D SLAM package while teleoperating carefully.
2. Save `map.pgm` + `map.yaml`.
3. Freeze the map and run AMCL + Nav2 for day-to-day autonomy.

PhysiBot follows that pattern. Research frontiers (NeRF maps, learned SLAM) are optional graduate digressions—not the lab path.

## 8.2 Occupancy grid mapping

Discretize the plane into cells \(m_{i} \in \{\mathrm{free}, \mathrm{occupied}\}\) (in practice: log-odds probabilities). Each scan at a known pose updates cells along rays with an inverse sensor model. If pose were perfect, mapping would be “just” painting. Pose error smears walls—hence joint SLAM.

**Resolution tradeoff.** Finer grids look sharp but cost CPU/memory and punish tiny calibration errors. Start with the resolution used in Nav2 tutorials for TurtleBot-scale robots, then match Limo footprint practice.

## 8.3 Filter SLAM vs. pose-graph SLAM (intuition)

| Style | Idea | Feel |
|-------|------|------|
| EKF / FastSLAM lineage | Augment state with landmarks or particles over maps | Online, historically influential |
| Pose-graph / optimization | Nodes = poses; edges = odometry & loop closures; optimize | Dominant in modern 2D lidar tools |

[slam_toolbox](https://github.com/SteveMacenski/slam_toolbox) (commonly paired with Nav2) embodies the pose-graph style for 2D laser mapping with lifelong options. Prefer it or a vendor-recommended Limo SLAM demo over writing your own graph optimizer.

## 8.4 Course choice and adaptation

Documented intent ([`docs/adaptation-notes/nav2.md`](../docs/adaptation-notes/nav2.md)):

1. Adapt slam_toolbox (or vendor Limo SLAM) launch into `physibot_bringup`.
2. Keep map save/load paths documented for students.
3. Reuse the same map in Chapters 07 and 09.

Do not commit huge binary maps to git if they are regenerable; small classroom maps are fine. Large site maps live in lab storage.

## 8.5 Practical mapping hygiene

1. **Drive slow.** Motion distortion and poor odometry ruin first maps.
2. **Close loops deliberately.** Revisit distinctive geometry.
3. **Avoid glass palaces.** Transparent walls defeat 2D lidar—note for physical labs.
4. **Check laser ↔ base TF** before blaming the optimizer.
5. **Save early, save often.** `map_saver` equivalents after a clean loop.

## 8.6 Lab 08 — Map a sim world

```bash
source /ws/install/setup.bash
ros2 launch physibot_bringup mapping.launch.py
# Teleop a full loop of the teaching world
ros2 run nav2_map_server map_saver_cli -f /ws/maps/classroom_world
```

(Exact package names follow Nav2 Humble docs—verify if CLIs change.)

Deliverables:

1. `classroom_world.pgm` + `.yaml`
2. Screenshot of the finished map in RViz
3. One paragraph: where the map smeared and what you changed (speed, loop, params)

Then restart Chapter 07 localization using **your** map.

## 8.7 Exercises

1. Why does a bad `laser` → `base_link` yaw make walls look doubled after a loop closure?
2. Explain loop closure in one paragraph without equations.
3. *(Grad)* Read slam_toolbox’s design overview / paper references; summarize lifelong mapping vs. one-shot mapping.

## 8.8 Further reading

- Thrun, Burgard, Fox — occupancy mapping & SLAM chapters
- [slam_toolbox](https://github.com/SteveMacenski/slam_toolbox)
- [Nav2 map server docs](https://docs.nav2.org/)
- Cadena et al., “Past, Present, and Future of Simultaneous Localization and Mapping” — survey for grads


**Runnable lab writeup:** [`labs/08-mapping/`](../labs/08-mapping/).

## Professor edit notes

- Pin slam_toolbox version compatible with Humble image.
- Provide a “known good” map for students who fail the mapping lab so Nav2 week is not blocked.
