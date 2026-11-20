# Chapter 14 — Capstone: physical models on Limo Pro

> **License:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).  
> **Hardware:** lab assignment — **simulation required**; physical Limo Pro optional per cohort.  
> **Lab code:** entire [`code/ros2_ws/`](../code/ros2_ws/), [`docker/`](../docker/), Isaac Lab artifacts from Ch. 10/13 as needed.

## Learning goals

1. Integrate estimation, mapping/localization, navigation, and a structured or learned physical model into one coherent demo.
2. Deliver a short technical report plus a reproducible Docker-based demonstration.
3. Demonstrate safe operation and an honest limitations checklist.

## 14.1 What “done” looks like

PhysiBot’s capstone is not a new robot stack. It is evidence that you can **reason with physical models** while driving a Limo-class system through the course toolchain:

- Containers build cleanly from this repository.
- A narrative connects equations → parameters → observed behavior.
- Risks are listed before anything moves in the physical world.

## 14.2 Capstone options

Choose **one** primary option. Mixing is allowed only with instructor approval.

### Option A — Nav2 + calibrated dynamics

Identify a simple dynamic/lag model (Ch. 04) from sim and/or hardware bags. Improve tracking (feedforward, tuned accel limits, or a small custom controller node) and show before/after path error on the same Nav2 goals.

### Option B — Learned residual dynamics / policy

Train a residual or policy in Isaac Lab (Ch. 10; Spark encouraged, Ch. 13). Deploy into **simulation** with clear interfaces to ROS 2. Physical deployment is a stretch goal under Ch. 11–12 safety rules—not required unless the cohort track says so.

### Option C — Localization robustness

Stress AMCL (or the course localizer) under added noise, latency, and partial FoV. Quantify failure/recovery with logged metrics and propose covariance / particle parameter changes grounded in Ch. 06–07 theory.

## 14.3 Required deliverables

| Deliverable | Spec |
|-------------|------|
| Reproducible demo | `docker compose` instructions from a clean clone; README section in your handin |
| Report | 4–6 pages PDF or DOCX (course Quarto/Pandoc toolchain welcome) |
| Demo evidence | ≤ 3 min video **or** scheduled live lab demo |
| Limitations checklist | `STATUS`-style honesty: what is stubbed, unsafe, or unvalidated |

Report structure (suggested):

1. Problem and physical-model thesis (½ page)
2. Method and equations (1–2 pages)
3. Experiments and metrics (1–2 pages)
4. Sim-to-real / safety discussion (½–1 page)
5. Limitations and next steps (½ page)

## 14.4 Rubric (course default weights)

| Criterion | Weight | Looks like |
|-----------|--------|------------|
| Correctness | 30% | Methods match claims; runs reproduce |
| Physical-model reasoning | 25% | Clear priors, parameters, residuals |
| Reproducibility | 20% | Compose/build documented; seeds logged |
| Safety & ethics of claims | 15% | No overclaim on physical readiness |
| Clarity | 10% | Figures readable; citations present |

Instructor may adjust weights per cohort; announce any change in week 1 of the capstone.

**Physical robot:** simulation is **required**; physical Limo Pro time is **optional** unless the cohort LMS page states otherwise.

## 14.5 Milestone plan — sample calendar

> **Sample calendar only.** Dates below are placeholders for syllabus planning. Replace with the term’s LMS deadlines; do not treat these as authoritative.

| Milestone | Sample week (15-week term) | Deliverable |
|-----------|----------------------------|-------------|
| Proposal | Week 12 | 1-page option, metrics, hardware need |
| Mid-capstone checkpoint | Week 13 | Container builds; one baseline plot |
| Final demo + report | Week 15 (exam week) | Report + ≤3 min video or live demo + limitations |

Use Chapters 01–13 as a library: cite them; do not paste them.

## 14.6 Cross-links you will likely need

- Docker workflow: Ch. 01, [`docker/compose.yaml`](../docker/compose.yaml)
- Kinematics / dynamics: Ch. 03–04
- Estimation / localization / maps / Nav2: Ch. 06–09
- Isaac Lab / Sparks: Ch. 10, 13
- Sim-to-real / Orin: Ch. 11–12
- Adaptation notes: [`docs/adaptation-notes/`](../docs/adaptation-notes/)

## 14.7 Academic integrity and licensing

- Narrative excerpts you write for the report should respect third-party licenses when you quote.
- Course narrative is CC BY-NC 4.0; your report remains your academic work under institutional rules.
- Code you contribute back to this repo should be Apache-2.0 compatible.

## 14.8 Capstone kickoff exercises

1. Pick an option and write a one-sentence physical-model thesis.
2. List the three riskiest dependencies (packages, hardware, data).
3. Draft your limitations checklist **before** results exist—then update it at the end.

## 14.9 Further reading

- Your own annotated bibliography from the semester
- Nav2, Isaac Lab, and AgileX docs as cited in earlier chapters
- Capstone examples from prior cohorts (when available on LMS)

## Pedagogical defaults (resolved)

- Rubric weights above are the course default; physical robot optional unless LMS says otherwise.
- Due dates: use the **sample calendar** in §14.5 until the term LMS publishes real dates (clearly marked as sample).
- Handin URL / video size limits: LMS only.
