# PhysiBot ROS 2 workspace

Distro: **Humble** (aligned with NVIDIA Isaac Lab `ros2` Docker profile).

```
src/
  physibot_description/   Limo-class URDF/xacro (course stub; adapt limo_ros2)
  physibot_sim/           Diff-drive odometry + stub laser (Python)
  physibot_bringup/       Progressive launches + Nav2/AMCL/SLAM configs
```

Build inside the course container:

```bash
cd /ws
colcon build --symlink-install
source install/setup.bash

# Lab 01
ros2 launch physibot_bringup description.launch.py

# Labs 03–04
ros2 launch physibot_bringup sim_diff_drive.launch.py

# Labs 07–09 (Nav2 image)
ros2 launch physibot_bringup localization.launch.py
ros2 launch physibot_bringup mapping.launch.py
ros2 launch physibot_bringup nav2.launch.py
```

Student lab writeups: `labs/`. Adaptation notes: `docs/adaptation-notes/`.
