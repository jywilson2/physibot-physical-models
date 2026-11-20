# Chapter 12 — Deploy on Jetson Orin Nano (Limo Pro)

> **License:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).  
> **Hardware:** **AgileX Limo Pro + NVIDIA Jetson Orin Nano** — first chapter that *requires* the physical robot for the graded lab.  
> **Lab code:** vendor Limo + Orin images; course overlays in [`physibot_bringup`](../code/ros2_ws/src/physibot_bringup/); [`docs/adaptation-notes/limo.md`](../docs/adaptation-notes/limo.md).

## Learning goals

1. Verify the Orin Nano course image and network/DDS conventions used in the lab.
2. Deploy the ROS 2 Humble stack practiced in simulation onto the robot computer.
3. Run a supervised progression: teleop → localization → short Nav2 goal.
4. Capture logs for post-run analysis and compare to sim baselines from Chapter 11.

## 12.1 Compute story: laptop sim vs. on-robot Orin

| Role | Machine |
|------|---------|
| Develop, debug Nav2 YAML, map in Gazebo | Student workstation + Docker |
| Heavy Isaac Lab training | Lab DGX Sparks (Ch. 13) |
| **On-robot autonomy** | **Jetson Orin Nano on Limo Pro** |

The Orin Nano is not a mini-DGX. Budget CPU/GPU for drivers, lidar, AMCL, and controllers. Strip unused perception pipelines. Prefer the same Humble distro as simulation to minimize “works in Docker, fails on robot” surprises.

## 12.2 Image and bringup (vendor first)

**Do not invent board support.** Follow AgileX + NVIDIA Jetson documentation for flashing/verifying the Orin Nano image used on the fleet. Course staff pin:

- OS / JetPack version
- ROS 2 Humble install method on device (native vs. container-on-Orin)
- Driver packages for base, lidar, IMU

Record the pins in lab runbooks (may stay out of public git if they include internal mirrors). PhysiBot packages overlay launch files and parameters only.

## 12.3 Network, DDS, and `ROS_DOMAIN_ID`

Lab conventions (fill with local values during professor edit):

| Setting | Purpose |
|---------|---------|
| Wi-Fi / Ethernet SSID | Robot ↔ operator laptop |
| `ROS_DOMAIN_ID` | Isolate class robots on shared Wi-Fi |
| RMW (`rmw_fastrtps_cpp` default in Compose) | Match laptop tools |
| Firewall / multicast | DDS discovery |

Before autonomy:

```bash
# On Orin (example)
echo $ROS_DOMAIN_ID
ros2 topic list
# From operator laptop on same domain
ros2 topic hz /scan
```

If discovery fails, fix network before debugging Nav2.

## 12.4 Real drivers vs. Gazebo plugins

Simulation substituted plugins for hardware. On the robot:

1. Base driver publishes `/odom` and consumes `/cmd_vel`.
2. Lidar driver publishes `/scan` with real `frame_id`s.
3. Static TF from the calibrated URDF must match metal.

Diff your sim launch vs. real launch: same Nav2 graph, different `bringup` include. That is the point of thin course overlays.

## 12.5 Supervised lab procedure

**Gate:** completed Chapter 11 checklist signed by TA/instructor.

### Stage A — Teleop

1. E-stop owner identified.
2. Soft velocity limits enabled.
3. Teleop along a taped rectangle; verify odometry direction signs.
4. Record bag: `/cmd_vel`, `/odom`, `/scan`, `/tf`, `/tf_static`.

### Stage B — Localization

1. Load the lab map (pre-built for the arena).
2. Set initial pose; verify particle convergence.
3. Walk a loop; note any corridor ambiguity.

### Stage C — Short Nav2 goal

1. Single goal in open space, ≤ 3 m.
2. Operator ready to preempt / e-stop.
3. On success, second goal requiring one turn.
4. Stop. Do not improvise obstacle courses on day one.

## 12.6 Logging and post-run analysis

Immediately after the run:

1. Save bags + Nav2 configs + `ros2 doctor` output.
2. Plot commanded vs. measured speed; estimate latency.
3. Compare localization jitter to sim bags.
4. File a short “incident” note even if nothing failed (what almost went wrong).

## 12.7 Lab 12 deliverables

1. Signed safety checklist (Ch. 11).
2. Bag from Stages A–C (or instructor-approved subset).
3. One-page report: TF tree sketch, domain ID, two plots, go/no-go reflection for a second session.

## 12.8 Exercises

1. List three nodes you would disable on Orin to reclaim CPU if AMCL starves.
2. Why might `use_sim_time` accidentally left `true` brick a physical bringup?
3. *(Grad)* Propose an online bias estimator for yaw rate using the Stage A bag.

## 12.9 Further reading

- NVIDIA Jetson Orin Nano product / JetPack docs
- AgileX Limo Pro user + ROS 2 docs (pin each term)
- [Nav2 on hardware troubleshooting](https://docs.nav2.org/)
- [`docs/adaptation-notes/limo.md`](../docs/adaptation-notes/limo.md)


**Runnable lab writeup:** [`labs/12-orin-deploy/`](../labs/12-orin-deploy/).

## Professor edit notes

- Publish lab SSID, domain ID assignments, and map files via course LMS.
- Decide native Humble vs. container-on-Orin for the fleet.
- Schedule robot slots; one robot per group minimum when possible.
