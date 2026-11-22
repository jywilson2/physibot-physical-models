# Adaptation: learned navigation (Part 2 sketch)

## Intent

Alternate Part 2 replaces the classical **AMCL → SLAM → Nav2** runtime arc with:

1. Latent **world-model** training (Isaac Lab),
2. **Learned occupancy / neural mapping** (first-class lab),
3. **Planning via latent rollout**,
4. **On-robot fine-tuning** on Limo Pro / Orin Nano (Sparks for heavy jobs).

Classical Nav2 adaptation notes ([`nav2.md`](nav2.md)) remain for the other track.

## Prefer adapting (do not greenfield)

| Layer | Upstream starting points |
|-------|--------------------------|
| Training | Isaac Lab pin in [`isaac-lab.md`](isaac-lab.md) (`v3.0.0`, Humble `ros2` profile) |
| Robot / drivers | AgileX [`limo_ros2` humble](limo.md) @ course SHA |
| Everyday ROS sim | `physibot_bringup` `description` / `sim_diff_drive` (no Nav2 profile required) |
| Deploy | Classical Orin lab checklist; overlay learned-nav nodes later |

## Non-goals this sketch pass

- Vendoring large model weights or full training pipelines.
- Deleting Nav2 packages from `code/` / `labs/07`–`09`.
- Pinning a single paper’s codebase as “the” course WM (open for professor choice).

## Open pin questions

See **Part 2** section in [`STATUS.md`](../../STATUS.md): teaching WM family, map representation, planner default, and term-specific Lab tutorial names.
