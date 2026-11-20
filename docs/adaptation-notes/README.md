# Adaptation notes

PhysiBot prefers **adapting existing OSS examples** over inventing greenfield
robot stacks. These notes point at upstream sources to wrap or vendor lightly
into `code/ros2_ws`.

| Note | Focus |
|------|--------|
| [`limo.md`](limo.md) | AgileX Limo Pro ROS 2 / Orin |
| [`nav2.md`](nav2.md) | Navigation2 localization & nav |
| [`isaac-lab.md`](isaac-lab.md) | Isaac Lab + ROS 2 Humble bridge |

Student-facing ladder: `labs/`. Do not copy large third-party trees wholesale
without license review; submodule or document `apt`/`vcs` import steps when
freezing a term SHA.
