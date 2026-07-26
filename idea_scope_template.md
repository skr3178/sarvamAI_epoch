# IDEA_SCOPE.md

> This document is the control plane for the build. If a proposed change does not improve the active milestone’s acceptance test or the chosen rubric strategy, place it in the parking lot.

## 0. Scope status

| Field | Value |
|---|---|
| Event | |
| Team | |
| Build starts | |
| Submission deadline | |
| Demo duration | |
| Current milestone | M0 |
| Scope owner | |
| Last updated | |

### Status language

- **Specified:** described here but not implemented.
- **Implemented:** code exists.
- **Working locally:** golden path runs in the development environment.
- **Verified:** acceptance tests have passed.
- **Demo-ready:** reset, fallback, timing, and presentation have been rehearsed.

## 1. Idea lock

| Decision | Locked answer |
|---|---|
| One-sentence product | |
| Specific user | |
| Situation and repeated job | |
| Current workaround | |
| Hard input | |
| Final usable output or state change | |
| Sarvam parameter | Voice Experience / Document Intelligence / Dubbing |
| Team’s unfair advantage | |
| Creativity thesis | |
| Delight thesis | |
| Decisive demo proof | |

### Why this idea

#### Asymmetric fit

Why this problem, team, event capability, and moment form an unusually strong intersection.

#### Decisive proof

What judges will see that proves the product works, matters, and is different.

## 2. User and job

### User

- Who:
- Context:
- Frequency:
- Existing behaviour:
- Existing cost, delay, risk, or frustration:

### Job to be done

> When `[situation]`, the user needs to `[completed job]`, so that `[valuable outcome]`.

### Definition of completion

The job is complete only when:

1.
2.
3.

Advice, transcription, extraction, search results, or a chat response alone do not count unless they are themselves the final usable output.

## 3. Product contract

### Golden path

1.
2.
3.
4.
5.

### Inputs

| Input | Format/source | Hard characteristics | Validation |
|---|---|---|---|
| | | | |

### Outputs and state changes

| Output/state change | Consumer | Required format | Proof of completion |
|---|---|---|---|
| | | | |

### Memory boundary

What the product must remember:

- within one interaction:
- across sessions:
- across users or team handoffs:
- what it must deliberately forget:

### Human review boundary

- What can be automated:
- What requires confirmation:
- What must be escalated:
- How uncertainty is exposed:

## 4. Creativity and Delight

### Obvious version

Describe the predictable implementation most teams would build.

### Structural creative mechanic

What changes how the user completes, understands, trusts, coordinates, or experiences the job?

### Delight moment

The exact moment that should cause the user or judge to react.

### Why it is meaningful

Explain why the Delight behaviour improves the job rather than decorating the interface.

### Ideas deliberately rejected

| Rejected mechanic | Reason |
|---|---|
| | |

## 5. Event and sponsor dependency

### Verified capability matrix

| Required capability | Product/API/model | Exact endpoint/access | Supported languages/inputs | Limits | Verification source |
|---|---|---|---|---|---|
| | | | | | |

### Load-bearing dependency

The demonstrated hard case on which the sponsor technology materially improves the product:

### Replacement test

If replaced with a generic stack:

- what remains commodity:
- what degrades:
- how the demo proves the degradation is material:

### Unsupported assumptions

List capabilities that must not enter the critical path because they are unavailable, deprecated, unverified, or inaccessible at the event.

## 6. Rubric strategy

The Sarvam rubric scores every parameter independently. There is no single overall project level. Record a separate current level, target, and proof for every row.

Every team is evaluated on the five product parameters. Select the single Sarvam capability most central to completing the user's job. Additional capabilities do not add points.

Do not add an API/Developer Experience branch, merge Dubbing into a generic Language branch, or award evidence for API count.

One level equals one base point: L1 = 1, L2 = 2, L3 = 3, L4 = 4, and L5 = 5. Weighted points equal level points multiplied by the row's multiplier. The maximum score is 50 points.

| Rubric dimension | Multiplier | Current evidence | Target level | Target weighted points | Observable proof | Work required | Milestone |
|---|---:|---|---:|---:|---|---|---|
| Job-to-be-done completion | 2.5× | | | | | | |
| Memory and Context | 1× | | | | | | |
| Creativity | 1.5× | | | | | | |
| Impact | 1.5× | | | | | | |
| Delight | 1× | | | | | | |
| Selected Sarvam parameter: Voice / Document / Dubbing | 2.5× | | | | | | |
| **Total** | | | | **/50** | | | |

### Level anchors

#### Job-to-be-done completion

- **L1:** 0–25% task success; demonstration only, with no reliably usable outcome.
- **L2:** 26–50% task success; the workflow runs, but the output remains broken, fake, incomplete, or unusable.
- **L3:** 51–75% task success; a useful part of the job is completed and at least one usable artifact exists.
- **L4:** 76–89% task success on a production-like workflow; most of the job is completed, with final human review permitted.
- **L5:** 90%+ across at least three repeated cases; the declared job is completed end to end with a final usable output and no judge intervention.

#### Memory and Context

- **L1:** every interaction starts from zero.
- **L2:** identifiers survive, but working context does not.
- **L3:** the complete current task survives for an authenticated user.
- **L4:** relevant history survives sessions, channels, or handoffs.
- **L5:** governed continuity combines current task, relevant history, and business rules while preserving permissions and tenant boundaries.

#### Creativity

- **L1:** obvious first implementation, reference reproduction, or generic wrapper.
- **L2:** cosmetic or loosely attached twist.
- **L3:** one meaningful, non-obvious product choice.
- **L4:** several original choices reinforce one distinctive end-to-end solution.
- **L5:** a surprising but coherent reframing that unlocks a materially better possibility.

#### Impact

- **L1:** no credible beneficiary, baseline, frequency, or outcome.
- **L2:** real problem but weak value case or less than 5% movement.
- **L3:** defensible baseline and plausible 5–10% movement on a meaningful metric.
- **L4:** major bottleneck with a defensible path to 10–30% movement.
- **L5:** top-priority problem with a credible path to more than 30% movement or an equivalent step-change.

#### Delight

- **L1:** first-time use is confusing, brittle, or unrecoverable.
- **L2:** functional but mechanical and builder-guided.
- **L3:** clear, coherent, pleasant, and independently usable on the main flow.
- **L4:** anticipates the user and recovers gracefully without losing progress.
- **L5:** hard work disappears; difficult tasks and demonstrated failures feel calm, intentional, and unusually well judged.

#### Voice Experience

Advance the level through demonstrated performance on real Indian speech: accents, code-switching, noise, intent, emotion, turn-taking, barge-in, partial words, corrections, pacing, prosody, and intelligent follow-ups.

#### Document Intelligence

Advance the level through demonstrated performance on real Indian documents: reading order, structure, handwriting, mixed scripts, tables, layout, degraded capture, source traceability, and controlled uncertainty.

#### Dubbing

Advance the level through audience-aware adaptation, speaker identity, pronunciation, emotion, pace, timing, overlaps, music, scene cuts, and publication readiness.

### Sarvam strength

The Sarvam parameter—Voice Experience, Document Intelligence, or Dubbing—in which this project intends to be exceptional:

### Competence floor

Dimensions that must work adequately but will not receive disproportionate build time:

### Evidence boundaries

Map each piece of evidence to the one rubric dimension it actually proves. Do not double-count the same behaviour when the rubric separates business outcome, continuity, creativity, impact, experience quality, and medium-specific craft.

### Rubric traps

Behaviours that may look impressive without satisfying the actual rubric:

## 7. Technical plan

### Smallest architecture

```text
[Input]
   ↓
[Sarvam parameter]
   ↓
[Minimum application logic/state]
   ↓
[Final artifact or system update]
```

### Components

| Component | Responsibility | Owner | Existing/new | Critical path? |
|---|---|---|---|---|
| | | | | |

### Data and state

| Entity/state | Required fields | Storage | Lifetime |
|---|---|---|---|
| | | | |

### External dependencies

| Dependency | Why needed | Setup verified? | Failure fallback |
|---|---|---|---|
| | | | |

### Secrets and access

Reference required credentials and setup locations. Never place secret values in this document.

## 8. Time-boxed build ladder

Replace relative times with the actual event clock after confirming the schedule.

### M0 — Feasibility and setup

**Target:** Before serious product construction.

**Purpose:** Kill unknown critical dependencies early.

Required:

- credentials and API access work;
- one representative hard input reaches the primary API;
- response shape and latency are understood;
- unsupported assumptions are removed;
- repository starts and can be reset.

Acceptance test:

> One real input successfully completes the riskiest external call.

Stop condition:

> If the critical capability cannot work by `[TIME]`, switch to `[FALLBACK]` or kill the idea.

### M1 — One-hour MVP

**Deadline:** Build start + 60 minutes.

**Purpose:** Complete the ugly end-to-end golden path.

**Rubric intent:** Reach at least Job-to-be-done completion L3. Do not call a zero-task demo or broken L2 workflow an MVP.

Required:

- one real input;
- minimum sponsor/API processing;
- minimum application logic;
- one final usable output or state change;
- saved evidence that the run completed.

Explicitly excluded:

- polished UI;
- multiple personas;
- broad language coverage;
- analytics dashboards;
- speculative agents;
- optional integrations;
- presentation work.

Acceptance test:

> A teammate who did not implement the feature can run one input through the complete job without editing code or manually repairing the output.

Demoable result:

Rubric vector after M1:

| Parameter | Demonstrated level | Evidence |
|---|---|---|
| Job-to-be-done completion | At least L3 | |
| Memory and Context | | |
| Creativity | | |
| Impact | | |
| Delight | | |
| Sarvam parameter | | |

### M2 — Reliable repeated completion

**Deadline:** `[ACTUAL TIME]`

**Purpose:** Move from one happy path to dependable task completion.

Required:

- three representative cases pass;
- one unseen or judge-like case passes;
- one recoverable failure is handled;
- uncertainty is visible;
- required state or memory persists;
- the golden path remains resettable.

Acceptance test:

> At least three consecutive cases produce the required final output without builder intervention.

Rubric evidence added:

Rubric vector after M2:

| Parameter | Demonstrated level | Next smallest lift |
|---|---|---|
| Job-to-be-done completion | | |
| Memory and Context | | |
| Creativity | | |
| Impact | | |
| Delight | | |
| Sarvam parameter | | |

### M3 — Sarvam parameter excellence

**Deadline:** `[ACTUAL TIME]`

**Purpose:** Prove the event-specific hard edge.

Required:

- the selected hard input is in the demo;
- sponsor capability is visibly load-bearing;
- the Sarvam parameter reaches its target level;
- the generic or obvious version has been surpassed.

Acceptance test:

> The hard case succeeds and the team can explain precisely why it is meaningfully harder than the commodity case.

Rubric evidence added:

### M4 — Creativity and Delight

**Deadline:** `[ACTUAL TIME]`

**Purpose:** Add the memorable product behaviour without destabilizing the core.

Required:

- structural creative mechanic works;
- Delight moment is observable;
- the behaviour improves the completed job;
- it does not introduce a new critical dependency.
- Creativity evidence is distinct from Delight evidence.

Acceptance test:

> A first-time user encounters the Delight moment during the normal golden path without prompting from the presenter, and the running product separately demonstrates the non-obvious choice claimed under Creativity.

Rubric evidence added:

### M5 — Demo hardening and submission

**Deadline:** Reserve the final `[DURATION]`.

Required:

- demo state resets;
- live and fallback inputs exist;
- API and network failure plan exists;
- demonstration fits the time limit;
- before-and-after value is explicit;
- submission assets are complete;
- no new product features are added.

Acceptance test:

> Two consecutive timed rehearsals complete successfully, including one using the fallback path.

## 9. Test plan

### Golden cases

| Case | Why representative | Expected final output | Status |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

### Unseen hard case

Who chooses it:

What makes it difficult:

Success criteria:

### Failure cases

| Failure | Expected behaviour | User recovery | Tested? |
|---|---|---|---|
| Ambiguous input | | | |
| Unsupported input/language | | | |
| API timeout/failure | | | |
| Contradictory correction | | | |

## 10. Demo contract

### One-sentence setup

### 60–120 second proof

| Time | What happens | What the judge sees | Rubric evidence |
|---:|---|---|---|
| 0–10s | | | |
| 10–30s | | | |
| 30–60s | | | |
| 60–90s | | | |
| 90–120s | | | |

### Live input

### Fallback input

### Memorable moment

### Final artifact/state shown

### Claims we can prove

- 

### Claims we must not make

- 

## 11. Risk register

| Risk | Probability | Damage | Earliest test | Mitigation | Fallback | Owner |
|---|---|---|---|---|---|---|
| | | | | | | |

### Pre-mortem

It is judging time and the project has failed because:

1.
2.
3.

## 12. Non-goals

The following are explicitly outside the build:

1.
2.
3.

Any change to these requires an explicit scope decision.

## 13. Parking lot

| Idea | Potential value | Why not now | Revisit after |
|---|---|---|---|
| | | | |

## 14. Team execution

| Person/agent | Ownership | Current task | Acceptance test | Blocked by |
|---|---|---|---|---|
| | | | | |

### Coordination rules

- One owner per critical-path component.
- Integration occurs continuously, not at the final checkpoint.
- The golden path must remain runnable.
- New work begins only after the active milestone’s acceptance test is preserved.

## 15. Current state

### Active milestone

### Implemented

- 

### Working locally

- 

### Verified

- 

### Demo-ready

- 

### Current blocker

### Next single action

## 16. Decision log

| Time | Decision | Evidence/reason | Scope impact |
|---|---|---|---|
| | | | |