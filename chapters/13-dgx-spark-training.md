# Chapter 13 — DGX Spark training workflows

> **License:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).  
> **Hardware:** **lab NVIDIA DGX Sparks** (two available) — instructor/lab backends; students are not assumed to own Sparks.  
> **Lab code:** Isaac Lab containers on Spark hosts; [`docs/adaptation-notes/isaac-lab.md`](../docs/adaptation-notes/isaac-lab.md).

## Learning goals

1. Explain why PhysiBot includes DGX Sparks (capacity and turnaround, not personal ownership).
2. Run or submit an Isaac Lab training job on a Spark using containerized workflows aligned with NVIDIA docs.
3. Sync checkpoints and metrics into the course artifact layout (not into git blobs).
4. Compare laptop vs. Spark wall-clock for the same configuration.

## 13.1 Why Sparks exist in this course

Isaac Lab workloads that are merely “possible” on a laptop become **iterable** on a Spark: larger batch sizes, more parallel environments, faster hill-climbing on rewards and domain-randomization schedules. PhysiBot’s two lab Sparks are shared infrastructure—like a microscope room.

### Generic lab-queue guidance (no secrets)

Treat Sparks like any shared GPU instrument:

1. **Book a slot** via the lab’s queue / calendar (URL on LMS—not in git).
2. Use **course accounts** only; do not share passwords.
3. Write outputs to the **shared filesystem** path staff publish for the term (see artifact layout below).
4. Leave the machine cleaner than you found it: stop containers, free GPUs, delete scratch that is not cited in your handin.
5. Prefer shorter teaching configs first; scale one axis per booking (Ch. 13 lab).

Exact hostnames, queue scripts, and mount points stay lab-local. Student everyday ROS work remains on [`docker/compose.yaml`](../docker/compose.yaml). Sparks are for Chapter 10-scale jobs done properly and for capstone training. Pin Isaac Lab **`v3.0.0`** on Sparks unless staff announce a newer verified tag.

## 13.2 Containerized training aligned with Isaac Lab

Follow the same upstream path as Chapter 10:

- [Isaac Lab Docker guide](https://isaac-sim.github.io/IsaacLab/main/source/deployment/docker.html)
- Lab `container.py` / Compose profiles (`base`, `ros2`, …)

On Sparks:

1. Use the **pinned Isaac Lab tag** for the term (see `STATUS.md` / adaptation notes).
2. Mount datasets and outputs on lab shared storage—not `$HOME` clutter without a plan.
3. Match CUDA / driver expectations documented for that Lab release on the Spark image.
4. Keep ROS 2 Humble alignment if you bridge; many training jobs need no ROS at all.

## 13.3 Artifact layout (recommended)

```text
/lab/physibot/runs/<netid>/<experiment_id>/
  config.yaml          # frozen training config
  meta.yaml            # Lab SHA, PhysiBot SHA, seed, host, UTC time
  metrics.jsonl        # scalar logs
  checkpoints/         # large binaries (gitignore / not in course repo)
  notes.md             # human narrative
```

`meta.yaml` example fields: `isaac_lab_git`, `physibot_git`, `docker_image`, `seed`, `n_envs`, `wall_clock_s`.

## 13.4 Lab 13 — Scale the Chapter 10 job

1. Book a Spark slot; load the course environment module or container instructions provided by staff.
2. Re-run the Chapter 10 teaching config **unchanged** for a fixed iteration budget; record wall-clock and GPU utilization.
3. Scale one axis only (e.g. double `num_envs` *or* longer training—not both) and record the new metrics.
4. Copy `meta.yaml` + `metrics.jsonl` + a small plot into your handin; leave heavy checkpoints on shared storage with a path citation.
5. Write half a page: what became faster, what became bottlenecked (data, GPU, host CPU, I/O).

## 13.5 Comparing laptop vs. Spark

| Question | How to answer |
|----------|---------------|
| Same seed, same config? | Required for fair wall-clock compare |
| Is the image identical? | Digest / tag must match |
| Did power modes differ? | Note host governor / MIG if any |
| Was the laptop thermal-throttled? | Mention qualitatively |

Turn in a table with three rows: laptop (or “N/A”), Spark baseline, Spark scaled.

## 13.6 Bridging back to ROS / Orin

Training on a Spark does not deploy itself. Export the policy/residual in the format chosen in Chapter 10, then:

1. Validate in Isaac Lab play / eval mode.
2. Validate in ROS sim with Nav2 still responsible for global navigation (unless capstone says otherwise).
3. Only then consider Orin deployment under Chapter 12 safety rules.

## 13.7 Exercises

1. Why is committing checkpoints to GitHub a bad idea even when LFS is available?
2. Give two reasons a Spark run might be *slower* than a laptop for a tiny config.
3. *(Grad)* Design a minimal learning-rate or domain-randomization sweep that fits one booking slot; justify the single varying factor.

## 13.8 Further reading

- Isaac Lab Docker + training tutorials
- Lab-internal Spark onboarding doc (LMS; may include secrets—keep out of git)
- [`docs/adaptation-notes/isaac-lab.md`](../docs/adaptation-notes/isaac-lab.md)

## Pedagogical defaults (resolved)

- Booking / accounts / shared FS: LMS only (generic process above).
- Isaac Lab tag on Sparks: **`v3.0.0`** unless staff override.
- Optional queue templates may ship later without credentials.
