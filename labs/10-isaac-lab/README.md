# Lab 10 — Isaac Lab (stub / docs)

**Chapter:** 10 — Learning with Isaac Lab  
**Hardware:** sim / optional DGX Spark  
**Image:** NVIDIA Isaac Lab `ros2` profile (not the everyday student Compose file)

## Status

Documentation stub. Do **not** invent a full Isaac Lab task suite — adapt an
existing wheeled / locomotion example and attach the course workspace.

## Student path (when lab hosts are ready)

1. Follow NVIDIA Isaac Lab Docker guide (`ros2` profile → ROS 2 Humble).
2. Mount `code/ros2_ws` into the Lab container (pattern TBD per term).
3. Prefer DGX Spark hosts for heavy training (Ch. 13); laptops for lightweight demos only if GPU permits.

## Pointers

- `docs/adaptation-notes/isaac-lab.md`
- [Isaac Lab Docker](https://isaac-sim.github.io/IsaacLab/main/source/deployment/docker.html)
- Course pin: **Humble** (see `STATUS.md`)

## Open items

- [ ] Pin Isaac Lab release tag for the term
- [ ] Document exact `container.py` / Compose attach steps for this repo
- [ ] Choose one upstream locomotion example to adapt
