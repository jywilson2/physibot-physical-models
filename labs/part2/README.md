# PhysiBot Part 2 labs — learned navigation (sketch)

Alternate-track lab ladder for the latent world-model Part 2. **Sketch only** —
procedures name upstream sources to adapt; full training pipelines come later.

Sim-first. Prefer Isaac Lab / ROS 2 Humble / AgileX Limo examples over greenfield
stacks. Classical Nav2 labs (`labs/07`–`09`) remain for the other track.

| Lab | Chapters | Theme | Status |
|-----|----------|-------|--------|
| [`01-isaac-world-model`](01-isaac-world-model/) | P2-01–02 | World-model training in Isaac Lab | Outline |
| [`02-neural-mapping`](02-neural-mapping/) | P2-03 | Learned occupancy / neural mapping | Outline |
| [`03-latent-rollout-planning`](03-latent-rollout-planning/) | P2-04–05 | Planning via latent rollout | Outline |
| [`04-limo-on-robot-finetune`](04-limo-on-robot-finetune/) | P2-06–07 | Limo on-robot fine-tuning | Outline |

Narrative spine: [`chapters/part2/00-outline.md`](../../chapters/part2/00-outline.md).

## Design rules

- No hard GPU-time caps; Spark/Orin booking and safety still apply.
- Do not require Nav2 as a runtime dependency for these labs.
- Keep Apache-2.0 for lab ops / code overlays; chapter prose stays CC BY-NC 4.0.
