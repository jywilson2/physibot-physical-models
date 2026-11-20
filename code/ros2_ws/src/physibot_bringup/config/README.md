# Bringup configs

| File | Lab | Notes |
|------|-----|-------|
| `amcl_params.yaml` | 07 | AMCL for Limo-class footprint |
| `slam_toolbox_params.yaml` | 08 | Async slam_toolbox |
| `nav2_params.yaml` | 09 | Nav2 stack params (v_max 1.0 m/s, radius ~0.20 m); header comments diff vs Nav2 Humble + AgileX open_class |

Prefer adapting upstream Nav2 Humble defaults and AgileX classroom examples
([`agilex_open_class` nav2.yaml](https://github.com/agilexrobotics/agilex_open_class/blob/8e799754af623c3cec954b74b186d63d6ce8fa62/limo/limo_bringup/param/nav2.yaml))
over rewriting this tree. `limo_ros2` humble pin
(`dcc5a8637f83236ed6778af86ad826e46a20cd92`) has no in-tree Nav2 YAML — drivers only.
See [`docs/adaptation-notes/nav2.md`](../../../../../docs/adaptation-notes/nav2.md).
