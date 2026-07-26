# Personal Idea Shortlist — Sarvam Epoch Buildathon (July 26, 2026)

Constraints locked so far: **solo builder · record-then-process audio (no live streaming) · build sprint 10:30–4:30**.
Rubric: 6 parameters, L1–L5 each. Weights: JTBD 2.5× · Memory 1× · Creativity 1.5× · Impact 1.5× · Delight 1× · Sarvam parameter 2.5×. Max 50.

---

## Idea 1 — Medical first-pass intake voice receptionist

**One-liner:** A voice receptionist that takes a patient's story in their mother tongue, asks the right follow-ups, books the right doctor, and hands the clinician a minute-readable English intake note.

- **User:** walk-in/call-in patient at an Indian clinic + the doctor/nurse receiving the note
- **Hard input:** rambling, code-switched, somatic symptom descriptions with mid-stream corrections, from a patient with no clinical vocabulary
- **Output/state change:** booked appointment (mock scheduler) + English intake note with urgency flag, audio-linked verbatim quotes, and a clinician-only "areas to consider" section
- **Sarvam parameter:** Voice Experience (Saaras v3 depth; Bulbul v3 voice; sarvam-30b/105b for follow-ups + structuring)
- **Safety boundary (critical):** the agent NEVER diagnoses, advises, or reassures the patient — enforced in code, not just prompt. Red flags escalate same-turn. Triage red-flag list must come from a citable protocol (WHO emergency signs / Manchester Triage), sourced before building.
- **Library lineage:** #76 (therapist pre-session intake, Beast), #68 (clinic scheduling), #20, #25
- **Data-exhaust story (Impact narrative only, not build scope):** every intake mints consented, code-switched, outcome-labeled medical interaction data — among the scarcest speech data classes globally
- **Demo:** judge role-plays a patient in a regional language, rambles, corrects themselves; note assembles live on the doctor screen; judge plants "chest pain + sweating" → same-turn escalation
- **Biggest risks:** exactness on age/duration/medication names; over-reaching into assessment (kills JTBD); protocol sourcing before 11:30

### Rubric projection (solo, 6h, honest)

| Parameter | Weight | Floor | Target | Notes |
|---|---|---|---|---|
| JTBD completion | 2.5× | L3 (7.5) | L4 (10) | End-to-end loop is buildable; L4 needs 3 clean repeated runs on unscripted input |
| Memory & Context | 1× | L2 (2) | L3–L4 (3–4) | Returning patient resumes prior intake; doctor sees delta. Time-risk area |
| Creativity | 1.5× | L3 (4.5) | L4 (6) | Asking-around-symptoms mechanic + audio-linked evidence + refusal-as-feature |
| Impact | 1.5× | L3 (4.5) | L4 (6) | OPD queues, doctor time, clear metric + data-exhaust narrative |
| Delight | 1× | L3 (3) | L4 (4) | Understood-while-unwell; confirm-back; honest same-turn escalation |
| Voice Experience | 2.5× | L3 (7.5) | L4 (10) | Real code-switch/correction depth; record-then-process sacrifices barge-in (caps ceiling) |
| **Total** | | **~29/50 (58%)** | **~36–40/50 (72–80%)** | No parameter structurally forfeited |

---

## Idea 2 — Indic voice eval harness for Sarvam (library card #81, Beast)

**One-liner:** A public benchmark measuring whether Indic speech-to-text holds up on code-mixed, noisy, real-world audio — scoring entity accuracy (amounts, names, dates) per condition, not just WER, with a live-scoring stage panel.

- **User:** ML engineer putting a voice agent on a live line, holding a vendor sheet with one context-free WER number
- **Hard input:** same utterances across 5 controlled conditions (clean / phone-band 8kHz / noisy / code-switch / mid-utterance correction)
- **Output:** per-condition, per-entity-type leaderboard + honest failure catalogue (10 worst utterances, playable) + one-command reproducible runner
- **Sarvam parameter:** Voice Experience (the harness is the proof instrument; judges examine condition design + the entity scorer, which is your own code)
- **Key insight:** WER is the wrong metric for consequential jobs — a transcript that gets a rupee amount or a name wrong is useless at an excellent-looking WER
- **Demo:** judge speaks a Hinglish sentence with a rupee amount and a name; harness scores live; WER looks fine, entity score catches the error WER hid
- **Synergy with my data-scarcity thesis:** the hand-built condition test set IS scarce valuable data; the harness is the instrument that prices it
- **Biggest risks:** hand-writing reference transcripts eats hours before any code; a leaderboard is a weak stage demo (live panel must be built early); ffmpeg/sox degradation pipeline is the unusual dependency

### Rubric projection (solo, 6h, honest)

| Parameter | Weight | Floor | Target | Notes |
|---|---|---|---|---|
| JTBD completion | 2.5× | L3 (7.5) | L3–L4 (7.5–10) | Runner + real numbers = job done; thin utterance counts cap credibility |
| Memory & Context | 1× | L1 (1) | L2 (2) | **Structurally weak** — versioned runs barely qualify as continuity |
| Creativity | 1.5× | L4 (6) | L4–L5 (6–7.5) | Entity-accuracy-vs-WER framing is genuinely non-obvious and structural |
| Impact | 1.5× | L3 (4.5) | L4 (6) | "Own the reference everyone cites"; every Indic voice team benefits |
| Delight | 1× | L2 (2) | L2 (2) | **Structurally weak** — card itself says leaderboards don't please crowds |
| Voice Experience | 2.5× | L3 (7.5) | L4 (10) | Scored on condition design + scorer quality, not API calls |
| **Total** | | **~28.5/50 (57%)** | **~33.5–37.5/50 (67–75%)** | ~2 parameters forfeited by design |

---

## Head-to-head verdict

- **Idea 1 has the higher ceiling and the safer floor**: no rubric parameter is structurally dead, and the demo is emotionally legible to judges in 3 minutes.
- **Idea 2 has spiky brilliance** (Creativity + Impact + a killer live moment) but forfeits ~5–6 weighted points on Memory + Delight before writing a line of code, and reference-transcript authoring is a hidden time sink for a solo builder.
- **Hybrid option worth considering:** build Idea 1, and steal Idea 2's entity-accuracy idea as Idea 1's internal QA — show the doctor screen flagging per-field confidence on names/durations/amounts. That imports the eval harness's best insight as Creativity evidence without paying its Delight/Memory tax.

**Status:** Idea 1 was presented as an Idea Lock; approval pending. Next step on approval → generate IDEA_SCOPE.md with hour-by-hour milestones.
