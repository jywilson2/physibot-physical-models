# Bringup configs

| File | Lab | Notes |
|------|-----|-------|
| `amcl_params.yaml` | 07 | AMCL for Limo-class footprint |
| `slam_toolbox_params.yaml` | 08 | Async slam_toolbox |
| `nav2_params.yaml` | 09 | Nav2 stack params (v_max 1.0 m/s, radius ~0.20 m) |

Prefer adapting upstream Nav2 + [limo_ros2](https://github.com/agilexrobotics/limo_ros2) configs when available; keep these as course overlays.
