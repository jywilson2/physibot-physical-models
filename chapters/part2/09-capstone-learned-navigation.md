# Part 2 · Chapter 09 — Capstone: learned navigation

> **License:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).  
> **Hardware:** simulation required; physical Limo Pro optional per cohort.  
> **Maps from classical:** adapts Ch. 14 options for the latent world-model track (Nav2 options stay on the classical track).

## Learning outcomes

1. Integrate world-model training, neural mapping, latent rollout planning, and (optional) on-robot fine-tune into one demo.
2. Deliver a short report + reproducible Docker / Lab procedure (no giant weight blobs in git).
3. Demonstrate safety literacy and an honest limitations checklist for learned navigation.

## 9.1 What “done” looks like

Evidence that you can **navigate with a latent world model** on a Limo-class platform:

- Containers / Lab pins match `STATUS.md`.
- A narrative connects Part 1 physical models → latent dynamics → planned rollouts.
- Neural / learned occupancy is shown as a first-class artifact.
- Risks listed before physical motion.

## 9.2 Capstone options (sketch)

Choose **one** primary option (mixing only with instructor approval).

### Option A — World model + latent planner (sim)

Train / adapt a teaching-scale WM in Isaac Lab; demonstrate goal reach via latent rollout in sim with metrics and failure analysis.

### Option B — Neural mapping focus

Deliver a high-quality learned occupancy artifact and show how the planner queries it; ablate map quality vs. navigation success.

### Option C — On-robot fine-tune (physical optional)

Start from a sim-validated checkpoint; perform a supervised fine-tune on Orin (or sim-only analogue); report before/after with intervention counts.

## 9.3 Deliverables (sketch)

| Deliverable | Spec |
|-------------|------|
| Demo | Reproducible sim path; physical optional |
| Report | Equations → artifacts → behavior; contrast with Nav2 track optional |
| Safety | Checklist from P2-06; e-stop drill if physical |
| Artifacts | Checkpoint IDs + metrics on shared storage, not git LFS dumps |

## 9.4 Rubric weights (placeholder)

| Criterion | Weight (draft) |
|-----------|----------------|
| Technical correctness of WM / planner story | 30% |
| Neural mapping / evaluation honesty | 25% |
| Reproducibility (pins, scripts, logs) | 20% |
| Safety & limitations | 15% |
| Clarity of report / demo | 10% |

Final weights TBD in professor review (`STATUS.md` open questions).

## Pedagogical defaults (sketch)

- Simulation required for every cohort.
- Physical Limo optional; fine-tune encouraged when hardware is assigned.
