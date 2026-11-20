# PhysiBot ROS 2 workspace

Distro: **Humble** (aligned with NVIDIA Isaac Lab `ros2` Docker profile).

```
src/
  physibot_bringup/       Launch overlays (sim stub)
  physibot_description/   Stub URDF/xacro (adapt Limo upstream)
```

Build inside the course container:

```bash
cd /ws
colcon build --symlink-install
source install/setup.bash
ros2 launch physibot_bringup sim_stub.launch.py
```

See `docs/adaptation-notes/` before growing this tree into a full robot stack.
