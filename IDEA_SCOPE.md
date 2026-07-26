# IDEA_SCOPE.md

> This document is the control plane for the build. If a proposed change does not improve the active milestone's acceptance test or the chosen rubric strategy, place it in the parking lot.

## 0. Scope status

| Field | Value |
|---|---|
| Event | Sarvam Epoch Buildathon — July 26, 2026 |
| Team | Solo builder |
| Build starts | 10:30 AM (scope locked 11:10 AM) |
| Submission deadline | 4:30 PM |
| Demo duration | ~3 minutes |
| Current milestone | M1 |
| Scope owner | skr |
| Last updated | 11:10 AM |

### Status language

- **Specified:** described here but not implemented.
- **Implemented:** code exists.
- **Working locally:** golden path runs in the development environment.
- **Verified:** acceptance tests have passed.
- **Demo-ready:** reset, fallback, timing, and presentation have been rehearsed.

## 1. Idea lock

| Decision | Locked answer |
|---|---|
| One-sentence product | A voice receptionist that takes a patient's story in their mother tongue, asks the right follow-ups, books the right doctor, and hands the clinician a minute-readable English intake note. |
| Specific user | Walk-in/call-in patient at an Indian clinic (speaks a regional language, no clinical vocabulary) + the doctor/nurse who receives the note |
| Situation and repeated job | Every OPD visit starts with an unstructured symptom story that a receptionist must turn into: the right doctor, the right slot, and a note the doctor can absorb in under a minute |
| Current workaround | Paper token + verbal retelling to a rushed receptionist; the patient repeats the story again to the doctor; nothing is written down before the consult |
| Hard input | Rambling, code-switched (e.g. Hindi–English), somatic symptom description with mid-stream corrections ("3 din se… nahi nahi, ek hafta ho gaya") from a patient with no clinical vocabulary |
| Final usable output or state change | (1) Booked appointment in mock scheduler; (2) English intake note: structured fields, urgency flag, audio-linked verbatim quotes, per-field confidence, clinician-only "areas to consider" |
| Sarvam parameter | **Voice Experience** (Saaras v3 depth on code-switch/corrections; Bulbul v3 spoken turns; Sarvam-30B follow-ups + structuring) |
| Team's unfair advantage | Solo speed on Python/web glue; pre-thought safety boundary and entity-confidence QA design (imported from eval-harness idea) |
| Creativity thesis | Asking-around-symptoms follow-up mechanic + audio-linked evidence + per-field entity confidence + refusal-as-feature (the agent never diagnoses — enforced in code) |
| Delight thesis | Being understood while unwell: confirm-back in the patient's language, honest same-turn escalation on red flags, and a note the doctor trusts because every claim links to the patient's own voice |
| Decisive demo proof | Judge role-plays a patient in a regional language, rambles, self-corrects; the note assembles live on the doctor screen with confidence flags; judge plants "chest pain + sweating" → same-turn escalation, no diagnosis ever offered |

### Why this idea

#### Asymmetric fit

Real, high-frequency job (every OPD visit in India); the hard input (code-switched rambling symptom talk) is exactly the case Saaras v3 is differentiated on; record-then-process fits solo constraints; no rubric parameter is structurally forfeited.

#### Decisive proof

An unscripted judge utterance survives: correction handled, entities captured with confidence, red flag escalated same-turn, appointment booked, doctor note readable in under a minute — three repeatable runs without builder intervention.

## 2. User and job

### User

- Who: OPD patient (regional-language speaker) + receiving clinician
- Context: clinic front desk / phone; noisy; patient unwell and anxious
- Frequency: every visit; dozens/day per clinic
- Existing behaviour: verbal retelling, paper tokens, no pre-consult note
- Existing cost: queue time, doctor time lost re-eliciting history, missed red flags at the desk

### Job to be done

> When a patient arrives with a health complaint told in their own words and language, the clinic needs to capture it accurately, triage urgency, book the right doctor, and hand the clinician a minute-readable note, so that the consult starts informed and emergencies are not sat in queues.

### Definition of completion

The job is complete only when:

1. An appointment exists in the (mock) scheduler with the right doctor/slot;
2. An English intake note exists with structured fields, urgency flag, verbatim audio-linked quotes, and per-field confidence;
3. Any red-flag symptom triggered a same-turn escalation message rather than a routine booking.

## 3. Product contract

### Golden path

1. Patient taps record, tells their story in their language (record-then-process);
2. Saaras transcribes+translates; Sarvam-30B extracts fields and picks ONE best follow-up question;
3. Bulbul asks the follow-up in the patient's language (with confirm-back of what was understood); patient answers; loop (max 3–4 turns);
4. Red-flag check runs on every turn in code; if triggered → escalation message + urgent slot, loop ends;
5. Booking confirmed by voice in the patient's language; doctor screen shows the assembled English note with confidence flags and playable quote snippets.

### Inputs

| Input | Format/source | Hard characteristics | Validation |
|---|---|---|---|
| Patient speech | Browser mic, webm/wav clips per turn | Code-switch, rambling, self-corrections, no clinical vocabulary | Non-empty transcript; re-ask once on empty/garbled |
| Patient identity (lightweight) | Spoken name or typed phone number | Repeat visits must resume | Exact-match lookup in local store |

### Outputs and state changes

| Output/state change | Consumer | Required format | Proof of completion |
|---|---|---|---|
| Intake note | Doctor | English; structured JSON rendered to note view; per-field confidence; quote audio links | Visible on doctor screen, readable <1 min |
| Booking | Patient + clinic | Mock scheduler entry (doctor, slot, urgency) | Slot visibly occupied; spoken confirmation |
| Escalation | Clinic staff | Same-turn banner + spoken handoff message | Fires on planted red flag, skips routine booking |

### Memory boundary

- Within one interaction: full turn history, corrected values overwrite earlier ones (corrections are memory evidence, kept visible as strikethrough)
- Across sessions: patient record keyed by phone/name; returning patient resumes prior intake; doctor sees delta ("new since last visit")
- Across users/handoffs: doctor view is read-only over the same record
- Deliberately forget: nothing clinical is auto-deleted in MVP; no real PII beyond demo data

### Human review boundary

- Automated: capture, structuring, follow-up choice, slot proposal
- Requires confirmation: final booking (patient voice-confirms)
- Escalated: any red-flag match → human/urgent pathway, same turn
- Uncertainty exposure: per-field confidence flags (name/age/duration/medication); low-confidence fields highlighted for the doctor, never silently guessed

## 4. Creativity and Delight

### Obvious version

A translate-and-transcribe chatbot that fills a form and calls it triage.

### Structural creative mechanic

(1) The agent asks **around** symptoms (onset, severity, what makes it worse) but structurally cannot diagnose — the refusal is enforced by a code-level output filter, not a prompt; (2) every field in the doctor note carries **entity-level confidence** and links back to the **patient's own audio** for verification — the note is evidence, not paraphrase.

### Delight moment

The patient corrects themselves mid-ramble; the agent's confirm-back uses the corrected value, and the doctor screen shows the old value struck through. Planted red flag → the agent honestly says (in the patient's language) it cannot help with this over booking and escalates immediately.

### Why it is meaningful

Trust is the product: the doctor trusts the note because it's auditable; the patient trusts the agent because it never pretends to be a doctor.

### Ideas deliberately rejected

| Rejected mechanic | Reason |
|---|---|
| Live streaming / barge-in | Solo + time; record-then-process locked |
| Real diagnosis/advice | Safety boundary; kills JTBD credibility |
| Real telephony/WhatsApp | Unprovisioned; mock scheduler is faithful enough |
| Standalone eval harness (Idea 2) | Imported only as per-field confidence QA |

## 5. Event and sponsor dependency

### Verified capability matrix

| Required capability | Product/API/model | Exact endpoint/access | Supported languages/inputs | Limits | Verification source |
|---|---|---|---|---|---|
| STT + translate on code-mixed speech | Saaras v3 | api.sarvam.ai speech-to-text(-translate), REST | 23 langs; modes: transcribe/translate/verbatim/codemix | clip-based REST | Handbook + M1 live smoke test |
| Spoken agent turns | Bulbul v3 | api.sarvam.ai text-to-speech | 11 output langs, 30+ voices | pick one demo language pair | Handbook + M1 live smoke test |
| Follow-ups + structuring | Sarvam-30B (105B fallback for hard turns) | api.sarvam.ai chat completions | JSON-mode structuring | latency on 105B | Handbook + M1 live smoke test |

### Load-bearing dependency

Saaras v3 on code-switched, self-correcting, noisy patient speech. If the transcript loses the correction or the entities (age, duration, medication names), everything downstream is decoration.

### Replacement test

- Commodity: web UI, scheduler mock, note rendering
- Degrades: code-switch transcription quality, Indic TTS naturalness, Indic-tuned follow-up reasoning
- Demo proof: the demo input IS the hard case; a generic STT visibly mangles the code-switched correction

### Unsupported assumptions

Do not depend on: streaming STT, barge-in, speaker cloning, telephony, real EHR/ABDM integration, Sarvam Creative Dubbing access.

## 6. Rubric strategy

| Rubric dimension | Multiplier | Current evidence | Target level | Target weighted points | Observable proof | Work required | Milestone |
|---|---:|---|---:|---:|---|---|---|
| Job-to-be-done completion | 2.5× | L0 (scope only) | L4 | 10 | 3 clean repeated unscripted runs → booking + note | M1 core loop, M5 repetition | M1, M5 |
| Memory and Context | 1× | L0 | L3–L4 | 3–4 | Returning patient resumes; doctor sees delta; corrections persisted | Patient store + resume flow | M4 |
| Creativity | 1.5× | L0 | L4 | 6 | Ask-around mechanic + audio-linked evidence + coded refusal | M2 follow-ups, M3 evidence UI | M2, M3 |
| Impact | 1.5× | L0 | L4 | 6 | OPD queue/doctor-time metric + data-exhaust narrative in demo script | Demo script + one slide-line | M6 |
| Delight | 1× | L0 | L4 | 4 | Confirm-back with correction honored; honest escalation | M2 loop polish | M2 |
| Voice Experience | 2.5× | L0 | L4 | 10 | Code-switch + correction survives to note; natural Bulbul turns; intelligent follow-up | M1 API proof, M2 depth | M1, M2 |
| **Total** | | | | **39–40/50** | | | |

JTBD floor for a credible demo: **L3** (one full run → real note + booking) by end of M1. Disproportionate-gain parameter: **Voice Experience**. Keep merely competent: Impact (narrative), UI polish.

## 7. Execution plan (11:10 → 4:30)

### M1 — 11:10–12:10 · Hardest dependency + ugly end-to-end
- Tasks: smoke-test chat/TTS/STT APIs with the event key; Python FastAPI backend; one recorded Hindi(-mix) clip → Saaras translate → 30B structuring → JSON note → red-flag check (WHO emergency-signs list, hardcoded with citation) → Bulbul spoken confirmation; CLI/plain page, hardcoded everything else.
- Artifact: `app/` that turns one audio file into a note + booking + spoken reply.
- Acceptance test: one command processes a real recorded clip end to end; note contains age/duration entities; planted "chest pain" clip triggers escalation.
- Rubric evidence: JTBD L3 floor; Voice dependency proven.
- Biggest risk after: multi-turn loop unbuilt.
- If behind: drop TTS reply, text-only confirmation (note is the artifact).
- Parking lot: UI styling, language auto-detect.

### M2 — 12:10–1:10 · Conversation loop + follow-ups + escalation
- Tasks: browser mic record-then-process turn loop; 30B picks ONE best follow-up/turn (max 3–4 turns); confirm-back in patient language via Bulbul; code-level no-diagnosis output filter; booking mock (doctor roster + slots).
- Acceptance: unscripted rambling input with a self-correction → corrected value in note; red flag mid-conversation → same-turn escalation, no booking.
- If behind: fixed 2-turn script (story + one follow-up).

### M3 — 1:10–2:10 · Doctor screen + evidence hybrid
- Tasks: doctor view; note assembles per turn; per-field confidence (name/age/duration/meds) from 30B self-report + heuristics; verbatim quotes with per-turn audio playback; "areas to consider" clinician-only section (symptoms-to-explore, never diagnosis).
- Acceptance: every load-bearing field shows confidence; clicking a quote plays the patient's audio for that turn.
- If behind: confidence on 3 fields only; quotes without per-field alignment (per-turn audio).

### M4 — 2:10–3:00 · Memory + safety hardening
- Tasks: JSON patient store keyed by phone; returning-patient resume ("last visit you reported…", delta view for doctor); corrections history; escalation + refusal tests as a small pytest file.
- Acceptance: second session with same phone resumes context and doctor sees delta; safety tests pass.
- If behind: resume without delta view.

### M5 — 3:00–3:45 · Integration + repeated cases + recovery
- Tasks: full golden path ×3 with different personas (one per language claimed); garbled-audio re-ask recovery; reset button; run from a second device on LAN (public link only if trivial).
- Acceptance: 3 consecutive clean runs, no builder touch.
- If behind: cut to 1 language, 2 personas.

### M6 — 3:45–4:30 · Demo hardening ONLY
- No new features. Reset state script; fallback pre-recorded input clips; screen-recorded fallback video of golden path; push to GitHub; 3-minute demo script; two timed rehearsals.

## 8. Safety boundary (non-negotiable)

- The agent NEVER diagnoses, advises, or reassures — enforced by an output filter that strips/regenerates any patient-facing text matching diagnosis/advice patterns; "areas to consider" is clinician-only.
- Red-flag list (citable, hardcoded): WHO IMCI/emergency general danger signs + Manchester-style adult flags: chest pain with sweating/breathlessness, severe breathing difficulty, uncontrolled bleeding, unconsciousness/unresponsive, seizure now, signs of stroke (face droop/arm weakness/speech), severe dehydration in a child, high fever with stiff neck, poisoning/overdose, severe injury. Match on both transcript and translated text, every turn, in code.
- Escalation is same-turn and honest: "This needs a doctor now — I'm flagging staff immediately."

## 9. Non-goals

No live streaming/barge-in; no real telephony/WhatsApp/SMS; no diagnosis or medical advice; no real EHR/ABDM; no auth; no more than 2 demo languages; no dubbing/document features.

## 10. Parking lot

Language auto-detect on first utterance; per-word audio alignment; vitals capture; multi-clinic routing; ABDM export; consent flow copy; Idea-2 standalone leaderboard.

## 11. Demo script (3 min) + evidence map

1. (0:00) One line: job + who it's for → **Impact**
2. (0:20) Judge as patient: rambling code-switched story with self-correction → confirm-back honors correction → **Voice Experience**, **Delight**
3. (1:10) One intelligent follow-up; answer; booking confirmed by voice → **JTBD**
4. (1:40) Doctor screen: note, confidence flags, click quote → patient audio plays → **Creativity**
5. (2:10) Planted red flag run: same-turn escalation, no booking, no diagnosis → **JTBD**, **Delight**
6. (2:40) Returning patient resumes; doctor sees delta → **Memory**. Close with metric + data-exhaust line → **Impact**

Likely judge question: *"How do I know the note is right?"* → Every field carries confidence and links to the patient's own audio; low-confidence fields are flagged for the doctor, and in code the agent refuses to produce anything it can't source from the patient's words.

## 12. Next single action

Run M1 API smoke tests (chat, TTS, STT round-trip) with the event key.
