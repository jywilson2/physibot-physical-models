# Lab 12 — Orin Nano deploy (stub / docs)

**Chapter:** 12 — Orin Nano deploy  
**Hardware:** AgileX Limo Pro + Jetson Orin Nano  
**Image:** on-robot (not student laptop Compose)

## Status

Documentation stub. Physical robot appears only in late course work.

## Intended workflow

1. Flash / confirm Ubuntu + ROS 2 Humble on Orin Nano per AgileX + NVIDIA guides.
2. Install / overlay course packages + vendor `limo_ros2` drivers (`humble` branch).
3. Reuse Nav2 / localization graphs from Labs 07–09 with driver remaps.
4. Document lab DDS / `ROS_DOMAIN_ID` conventions (hostnames/secrets stay out of git).

## Pointers

- Upstream: https://github.com/agilexrobotics/limo_ros2 (`humble`)
- Docs: https://github.com/agilexrobotics/limo_ros2_doc
- `docs/adaptation-notes/limo.md`

## Open items

- [ ] Lab-specific network checklist
- [ ] Verify Humble driver launch names against pinned SHA
- [ ] Smoke script that only checks topic presence on robot (instructor-run)
