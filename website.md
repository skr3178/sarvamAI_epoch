<!--
Local copy of the Sarvam Epoch Buildathon Builder Handbook.
Source: https://growthx.club/docs/sarvam
Fetched: 2026-07-26
Includes the rendered handbook pages plus all five embedded machine-readable
sources (organizer context, build playbook, rubric, idea library, IDEA_SCOPE
template, copilot prompt). The handbook is GrowthX IP (Terms clause 04) —
this copy is for personal build-day reference only; do not republish.
-->

# Sarvam Epoch Buildathon · Builder Handbook (local copy)

**Contents**

1. [Handbook pages](#part-1--handbook-pages) — logistics, welcome, rules, rubric overview, Sarvam docs, submission, demo prep, after, FAQ, terms
2. [Build playbook](#part-2--build-playbook-growthx-explains) — four-layer stack, Sarvam fast paths, comms channels, mocks, common gaps, six-hour build-plan prompt, references
3. [Event Reality Brief](#part-3--event-reality-brief-organizer-context) — `organizer-context-source`
4. [Full rubric](#part-4--full-rubric) — `rubric-source`
5. [Idea Library (82 cards)](#part-5--idea-library) — `idea-library-source`
6. [IDEA_SCOPE.md template](#part-6--idea_scopemd-template) — `idea-scope-template-source`
7. [Hackathon Idea + Scope Copilot prompt](#part-7--hackathon-idea--scope-copilot-prompt) — `hackathon-copilot-prompt-source` (identical to the local `prompt.md`)


---

# Part 1 · Handbook pages

# sarvam epoch buildathon

presented by

Let's build...

Powered by



Supported by

01 / Logistics

# Walk in. Plug in. Build.

Venue, check-in, Wi-Fi, and what to bring. Everything you need before 10 AM.

DateSun, July 26

Time10 AM – 6:30 PM IST

VenueRazorpay Arena

Venue

### Razorpay Arena

Coming soon · gate / floor / check-in point

[Open in Google Maps →](https://maps.app.goo.gl/Hc5r1Noyuf5nVbLE8)

Wi-Fi

### Connect on the floor.

Network · Coming soon

Password · Coming soon

## What to bring

Laptop + charger

Headphones

Charged phone — to test your agent on a real device

Soft copy of government or company ID

02 / Welcome

# Why GrowthX buildathons are built differently.

🚀

Everyone ships

**Everyone who walks in ships something.** The whole day is built around getting you to a working demo.

👥

The room

The people around you are some of the best builders in India, solving **problems that move millions.**

🎯

Build to win

You get the exact scoring parameters before you write a line, so **you build straight at what wins.**

🔥

Intensity

The intensity comes from the room. **This will be intense. That's the point. Trust us.**

## Four things happen today.

10:00 AM

Kickoff

Kickoff.

What's happening

Context, rules, the Sarvam platform walkthrough. Then you pick your problem.

10:30 AM

Build

Build.

What's happening

Six hours of focused build. Solo or teams. On Sarvam. Submissions close at 4:30 PM.

4:30 PM

Submit

Submit.

What's happening

Submit your build. Final entries are locked for the demo lineup.

5:30–6:30 PM

Demo

Demo.

What's happening

Top teams demo on stage. Winners announced. Top 10 present at Sarvam Epoch.

03 / Rules

# Rules.

Here are the rules we'll be operating within.

| \# | Rule |
|----|----|
| 01 | **Build on Sarvam.** The platform is the constraint; everything else is your choice. The main Sarvam layers are Doc AI and Voice. Instead of building your own agent, use Sarvam Agents for complex workflows between systems — or just write the backend logic yourself. The Sarvam API gives you the complete platform, and Sarvam Conversations is real-time voice: call and speak, at much lower latency. |
| 02 | **Solo or teams.** Build solo or as a team of up to 5. Every team member must register and be approved individually. |
| 03 | **Build on-site.** The build happens in the room. Remote participation is not allowed. |
| 04 | **No company demos.** If your company builds in this space, you can't demo your existing product. Build something new today. |
| 05 | **Submit on time.** A fixed window opens after the build sprint. Late submissions are not considered. |
| 06 | **One submission per team.** No multiple entries. |
| 07 | **Judges' decision is final.** |

## What counts as a valid starting point

Qualifies

- A project started from zero today
- A Sarvam product or model configured from scratch during the buildathon
- An idea you've sketched but never deployed
- Helper tools and BaaS — Supabase, Sheets, Firebase, Clerk
- AI coding assistants writing the code
- Standard starter scaffolding — Next.js, Vite, FastAPI

Does not qualify

- A finished build submitted with only cosmetic changes
- A pre-built agent with minor tweaks done today
- Your existing product in its original form
- Remote contributors or code written off the floor
- A build already demoed or pitched at another event
- Builds on a stack other than Sarvam

If it's borderline, flag it.

Submit anyway and flag "borderline starting point" in your notes. Mentors verify before the lineup is locked. Hiding the origin is an auto-disqualification.

04 / Idea Library

# Paste this into your AI assistant. Ten minutes later, leave with the right idea and a scope built to win.

It learns what your team is unusually good at, compares ideas against the judging rubric, and turns the strongest direction into a buildable scope. You finish with one chosen idea and an `IDEA_SCOPE.md` you can start building from.

Copy focused prompt →

Preview all … prompt lines

[Browse the idea library ↓](#idea-library)

01 Understand your edge Surface the strengths, access and lived experience only your team has.

02 Choose against the rubric Compare directions on proof, scoring leverage, feasibility and risk.

03 Scope it to build Lock one user, one job, one outcome and the next build milestone.

05 / Rubric

# The rubric.

## How to read L1–L5.

Each level raises the standard of proof. Judges score the demonstrated product, not the pitch, architecture diagram, or number of APIs connected.

L1

Floor

The parameter is absent, unproven, or present only in its most obvious form.

L2

Baseline

A basic attempt is visible, but important gaps limit the claim.

L3

Working

A credible middle standard is demonstrated with relevant evidence.

L4

Strong

The parameter is distinctly strong and survives realistic challenge.

L5

Exceptional

An exceptional benchmark that is difficult to reproduce or dismiss.

Read the complete description and example for the level. The headline is only a quick label; it is not enough to score the product by itself.

## How points and weightages work.

**One level equals one base point:** L1 = 1 point, L2 = 2 points, L3 = 3 points, L4 = 4 points, and L5 = 5 points. Multiply those level points by the parameter multiplier below.

Judges score all five Product parameters and exactly one selected Sarvam parameter. Voice Experience, Document Intelligence, and Dubbing share the same Sarvam slot; the two capabilities a team did not select contribute no points. The maximum weighted score is **50 points**.

Scroll horizontally to compare weighted points →

| Parameter                 | Multiplier | L1  | L2  | L3  | L4  | L5   |
|---------------------------|------------|-----|-----|-----|-----|------|
| Job-to-be-done completion | 2.5×       | 2.5 | 5   | 7.5 | 10  | 12.5 |
| Memory and Context        | 1×         | 1   | 2   | 3   | 4   | 5    |
| Creativity                | 1.5×       | 1.5 | 3   | 4.5 | 6   | 7.5  |
| Impact                    | 1.5×       | 1.5 | 3   | 4.5 | 6   | 7.5  |
| Delight                   | 1×         | 1   | 2   | 3   | 4   | 5    |
| Selected Sarvam parameter | 2.5×       | 2.5 | 5   | 7.5 | 10  | 12.5 |

Detailed example

### A Voice team scores 35.5 out of 50.

The judges award JTBD L4, Memory and Context L3, Creativity L4, Impact L3, Delight L2, and Voice Experience L4. The weighted calculation is:

**JTBD:** 4 × 2.5 = 10
**Memory and Context:** 3 × 1 = 3
**Creativity:** 4 × 1.5 = 6
**Impact:** 3 × 1.5 = 4.5
**Delight:** 2 × 1 = 2
**Voice Experience:** 4 × 2.5 = 10

**Total: 10 + 3 + 6 + 4.5 + 2 + 10 = 35.5/50, or 71%.** Document Intelligence and Dubbing are not added because Voice Experience is this team's single selected Sarvam parameter.

## Sarvam parameters.

Choose the one Sarvam capability most central to completing your user's job: Voice Experience, Document Intelligence, or Dubbing.

Start here

### Depth on one capability beats breadth across several.

Every team must demonstrate at least one Sarvam capability. Judges score the single capability most central to completing the user's job. Additional capabilities do not add points.

If the job genuinely requires another capability, use it because the product needs it—not because you expect another score. Get the central capability working deeply first.

Scroll horizontally to compare L1 through L5 →

| Sarvam parameter | L1 · Floor | L2 · Baseline | L3 · Working | L4 · Strong | L5 · Exceptional |
|----|----|----|----|----|----|

## The five product parameters.

Every project is evaluated on Job-to-be-done completion, Memory and Context, Creativity, Impact, and Delight.

Scroll horizontally to compare L1 through L5 →

| Parameter | L1 · Floor | L2 · Baseline | L3 · Working | L4 · Strong | L5 · Exceptional |
|-----------|------------|---------------|--------------|-------------|------------------|

06 / Sarvam Docs

# Sarvam docs.

Everything you need to configure your build on the Sarvam stack.

Quickstart

Get your API key from the dashboard, install the Python or JS SDK, and make your first call in under 5 minutes. Do this in the first 15 minutes of the build — everything else depends on it.

[Quickstart →](https://docs.sarvam.ai/api/getting-started/quickstart)

Models

Know the lineup before you pick: **Saaras v3** (STT, 23 languages), **Bulbul v3** (TTS, 30+ voices), **Sarvam-30B** and **Sarvam-105B** (chat), **Mayura** + **Sarvam-Translate** (translation), **Sarvam Vision** (documents).

[Models →](https://docs.sarvam.ai/api/getting-started/models)

Speech to text

Saaras v3 handles code-mixed and regional speech with five output modes: transcribe, translate, verbatim, transliterate, codemix. Use REST for clips, Streaming for live voice, Batch for long files. Turn on speaker diarization if two people talk.

[STT guide →](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/overview)

Text to speech

Pick the Bulbul voice deliberately for your domain — calm for banking, warm for healthcare, brisk for commerce. Tune pitch, pace, and loudness. For live agents, stream over WebSocket instead of waiting on full clips.

[TTS guide →](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/overview)

Chat completion

Sarvam-30B for speed, Sarvam-105B for the hard reasoning turns. If latency matters, run 30B on easy turns and escalate to 105B on hard ones. Both are tuned for deep Indic language understanding.

[Chat guide →](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/overview)

Translation

Mayura covers 11 languages with context preservation; Sarvam-Translate extends to all 23 with long-form accuracy. Transliteration and language detection live here too — use detection on the first utterance to auto-switch languages.

[Text processing →](https://docs.sarvam.ai/api/api-guides-tutorials/text-processing/overview)

Doc AI Studio

Two Studio workflows: **Extract** locates the fields you name; **Digitise** converts every page — printed or handwritten — into structured text. The Studio accepts PDF, JPEG, and PNG up to 50 MB and 10 pages per project. The separate Sarvam Vision API guide documents 200 MB per file with the same 10-page PDF cap.

[Doc AI Studio →](https://docs.sarvam.ai/docai/getting-started/overview)

Voice agent integrations

Building a phone or realtime agent? Follow the official guides for Twilio, Exotel, LiveKit, and Pipecat instead of wiring telephony from scratch. The cookbook has full example agents — collections, government schemes, tutoring, loan advisory.

[Integrations →](https://docs.sarvam.ai/api/integration/build-voice-agent-with-twilio) [Cookbook →](https://docs.sarvam.ai/api/cookbook/guides/call-analytics-pipeline)

Creative studio

Content transformation pipelines — agentic document translation across languages and video dubbing with the original speaker's voice preserved. The move for localisation-heavy builds.

[Studio →](https://docs.sarvam.ai/creative/studio-overview)

AI-assisted building

Point your coding assistant at Sarvam: the MCP server, llms.txt index, and agent skills give Claude Code or Cursor the full API context. Append `.md` to any docs URL for the markdown version.

[Developer tools →](https://docs.sarvam.ai/api/developer-tools/mcp)

07 / Submission

# Submission.

Submission window

### Coming soon.

The window times and submission link will be shared on the floor.

What happens after

### Coming soon.

The shortlisting and demo timeline will be updated here.

08 / Demo Prep

# Three minutes. One thread from problem to outcome.

The judge should follow a single story: business problem → current pain → your agent → business outcome.

| Time | What |
|----|----|
| 30 sec | **Business context.** Name the problem in plain words. No tech, no jargon. |
| 30 sec | **Workflow breakdown.** What happens manually today. How many people, how much time, where the friction lives. |
| 2 min | **Live demo — the centerpiece.** One real interaction. Narrate the key moments. Have a recording ready if the live run drops. The demo is the close — end on the working product. |

Keep in mind

- Lead with the business problem, not the technology
- Name the metric you're moving
- One outcome, not ten features
- Practice the cold open — land it in one breath
- Close on impact, not the stack

Mistakes to avoid

- Opening with the tech stack
- Generic "anyone can use this" framing
- No baseline, no way to claim impact
- Live demo with no fallback recording
- Ending on the architecture

09 / After

# The build was never the goal.

This morning you picked a problem because you believed it was worth solving. There's a metric hiding underneath it — and that metric is now the only thing that matters.

Tonight

### Push, share, reflect.

Get the code off your laptop. Post what you built. Write down how you decided under pressure.

This week

### Establish the baseline.

Go back to the workflow. Measure what was true before the agent, then measure what changes.

Resist

### Don't add features.

Every failed run is feedback. Every unexpected answer is insight. Every edge case is a clue.

10 / FAQ

# Questions, answered.

Read once at the start of the day. Check back when you hit an edge case.

Can I come with a team?

Yes — solo or as a team of up to 5. Every team member must register and be approved individually.

Do I have to use Sarvam?

Yes. The platform is the constraint we're building against. Everything around it is your choice.

Can I bring my own LLM or other APIs alongside Sarvam?

Yes. Use Claude, GPT, Gemini, or any API alongside the Sarvam stack — Sarvam must be the core of the build, not a garnish.

Can I use a project I've already started?

Helper utilities and personal libraries are fine. An existing agent built previously is not. Judges will ask.

Can I use ChatGPT, Claude, or Cursor during the build?

Use whatever helps you ship faster.

What counts as memory?

Your choice: conversational turns retained, knowledge recall accuracy, cross-session retention, or structured state quality. Define your framing when you demo — it maps to the Memory and Context parameter on the rubric.

Is food provided?

Yes — meals and refreshments are covered. Show up with your laptop, we'll handle the rest.

Do I need to be a GrowthX member?

No. The buildathon is open to everyone.

What if I can't make it last minute?

Mark "opt out" early so we can open the spot to someone else. No refunds for cancellations or no-shows.

What if my demo fails on stage?

Narrate the intended behaviour, recover, move on. Don't lose 30 seconds apologising. Judges have seen demos crash — recovery matters.

11 / Terms

# Terms & conditions.

The boring but necessary bits. By participating in the buildathon, you accept these terms.

| \# | Clause |
|----|----|
| 01 | **GrowthX runs the show.** GrowthX may modify, pause, reschedule, or cancel the event, and may disqualify any participant, at any time, without prior notice. |
| 02 | **Judging is final.** Scores come from the rubric and the judges panel. No re-scoring, no negotiation, no post-event lobbying. |
| 03 | **Your work, your IP.** Whatever you build at the buildathon is yours. GrowthX makes no claim on your code, your idea, or your product. |
| 04 | **This handbook is GrowthX IP.** The rubric, structure, copy, visual design, and idea library belong to GrowthX. Do not reproduce them without permission. |
| 05 | **Brand and name use.** "GrowthX", "Sarvam Epoch Buildathon", and associated marks are property of their respective owners. Sarvam AI and its marks belong to Sarvam AI. |
| 06 | **Eligibility.** The buildathon is open to builders registered for this event, aged 18 or above, and physically present on the build floor. |
| 07 | **Code of conduct.** Respect fellow builders, mentors, judges, and staff. Harassment of any kind means immediate removal from the event. |
| 08 | **Photo and video release.** The event is photographed and recorded. By participating, you grant GrowthX permission to use your image and likeness in event coverage and promotion. |
| 09 | **Verification consent.** By submitting, you consent to metric verification. This includes read-only analytics access, database spot checks, and contact checks with your signups. Refusing verification zeroes that parameter. |
| 10 | **No guarantees.** Participating, submitting, or winning does not guarantee prizes, funding, investment, or hiring. |
| 11 | **Liability.** You are responsible for your laptop, data, code, accounts, and conduct. Back up your work. |
| 12 | **Third-party tools and updates.** Sarvam AI, partner tools, model APIs, and hosting providers have their own terms. Agreeing to those is on you. GrowthX may update these terms before or during the event. |

That's it.

---

# Part 2 · Build playbook (GrowthX explains)

GrowthX explains

### Sarvam is the capability layer.

Speech, document intelligence, translation and dubbing are how your product understands or produces Indian-language information. They are not the whole product. Behind the capability sits the job: the rules, state, correction path, action and final artifact that make the result useful.

Teams that stop at an API response ship capability demos. Teams that build the full stack around it complete a job. Before you write a prompt, sketch the four layers of your build.

#### The four-layer stack

| Layer | What sits here | Fast defaults | Setup |
|----|----|----|----|
| **Interface** | How the user supplies speech, a document or media—and receives the result | Browser microphone, camera/file input, a simple review screen and native audio/video players. Use telephony only if the route already works. | 5–30 min |
| **Backend logic** | Sarvam calls, orchestration, task rules, corrections, validation and actions | A small Node/Python service; Convex functions when shared or real-time state helps. Keep one golden path in one process first. | 30 min–2 hr |
| **Database** | Users, sessions, source files, confirmed facts, corrections and output versions | Convex for real-time state, Supabase for Postgres, or SQLite/local JSON for one user and one demo. | 10–30 min |
| **Comms/output** | How the result is confirmed, reviewed, handed off or shared after inference | Resend email, Telegram, Slack/Discord webhook, a download or a shareable result link. | 5–20 min |

**The split inside the backend:** Sarvam handles the language or document capability. Your application handles state, business rules, proof, recovery and the write-back to the system the user actually cares about.

#### Pick one Sarvam parameter fast path

Judges score the single Sarvam capability most central to completing the user's job. Additional capabilities add no points, so go deep on the medium that carries the job.

##### Voice Experience

Start with the browser mic. Use Saaras v3 streaming for input, Sarvam Translate or Mayura only when translation is part of the job, and Bulbul v3 for supported spoken output. Instrument capture → STT → reasoning/translation → TTS → playback. Build interruption, correction and recovery before telephony.

##### Document Intelligence

Start with one camera/file upload and Sarvam Vision’s asynchronous API job flow. Keep page and block provenance visible. The public Vision API model guide documents a 10-page PDF limit per job and 200 MB per file, so split larger inputs. OCR is input; the finished job must reconcile, explain, transform or act. Doc AI Studio is a separate surface with its own 50 MB and 10-page project limits.

##### Dubbing

Use Sarvam Creative Dubbing if event access is provided; otherwise compose transcription, translation/adaptation, a stable named Bulbul voice and ffmpeg. Keep the source short enough to finish live. Measure render time, terminology and timing—not merely whether the audio changed language.

#### Comms channels that work in the build window

Pick the channel your user already lives in. The communication should confirm the completed outcome, not become a second product.

| Channel | Tool | Setup | Notes |
|----|----|----|----|
| Email | Resend | 5 min | Default for confirmations and reviewer links. |
| Telegram | Bot API | 5 min | Fastest bot channel: token, chat ID, one API call. |
| Slack | Incoming webhook | 2 min | Internal escalations, reviewer pings and operator handoff. |
| Discord | Incoming webhook | 2 min | Same shape as Slack. |
| Push | ntfy.sh | 5 min | No-signup demo alerts and completion notifications. |
| Artifact | Download or share link | 5–15 min | Default for extracted documents, receipts and dubbed media. |
| Outbound voice | Existing phone route | Variable | Use only when the number and routing path are already provisioned. |

Do not attempt these during the build

Do not start unprovisioned WhatsApp or SMS, real government/banking/hospital/payment integrations, KYC, a new telephony route, or production auth. Do not claim all 22 languages have the same spoken-output coverage. Do not claim same-speaker cloning from the base APIs; use Creative Dubbing only if the event has actually provided that surface. Do not use an unverified product such as Sarvam Edge, and do not build a vector database for knowledge that fits in the system prompt.

#### Mocks: do not spend build hours on external systems

A faithful mock counts when the real integration is not the capability being judged. Define the exact request, response and failure shapes your agent needs.

##### Business-system mock

Use Beeceptor or Mockoon for a registry, dispatch system, CRM, school, hospital or government workflow. One endpoint with success and correction paths is enough.

##### Failure and latency

Use httpstat.us or a tiny local route for success, failure and timeout. Make recovery visible instead of hiding it in logs.

##### Permissioned source data

Use public-domain, permissioned or community-approved documents, recordings and media. Keep the original attached so provenance can be inspected.

**Default:** local JSON when the shape is tiny, Beeceptor for a hosted endpoint in minutes, and Mockoon when you need multiple repeatable routes. Use real systems only when integration itself is the job.

#### Gaps teams hit and how to dodge them

These are the silent time-sinks. You often discover them only after the interface is already built.

| Gap | Easy fix | Cost if ignored |
|----|----|----|
| API access or credits | Run the smallest real request before UI work. | Hours built around an unavailable capability. |
| Speech coverage mismatch | Lock an exact tested input language, output language and named voice. | The live demo cannot speak or silently changes mode. |
| Vision is asynchronous | Build upload → job ID → polling → result with one tiny file first. | A frozen upload screen during judging. |
| Document job bounds | Crop or split to the declared tested unit. | An unseen judge file exceeds the public limit. |
| Telephony not provisioned | Use browser audio. | Half a day on numbers, routing and provider policy. |
| Latency is invisible | Timestamp every hop and show p50/p95 or render time. | “Instant” cannot be defended. |
| Names, numbers or corrections drift | Keep canonical shared state and ask for explicit confirmation. | The facts with real consequences diverge. |
| Long media render | Use a 20–45 second source and preflight ffmpeg immediately. | The demo finishes after judging ends. |
| Cultural or religious authority | Use approved sources, consent, provenance and reviewer corrections. | A harmful answer presented as truth. |
| Real auth | Hardcode one dev user unless identity is the job. | A day lost to login. |
| Observability | Structured logs plus one on-screen status/metrics card. | Failures cannot be explained or recovered. |

Built on localhost? Submit a live URL.

Your judges need a public, resettable link. Deploy the smallest working surface early or expose the local app through a safe tunnel. Do this before the final hour, then test the link from a different device.

#### The whole thing in one slide

**Sarvam is one capability layer. Your product has four:** Interface (how the user supplies speech, a document or media), Backend (what happens next), Database (what the product remembers), and Comms/output (how the result becomes useful).

Pick one Sarvam parameter and prove it deeply. Build one complete job against a faithful mock, preserve corrections and provenance, measure the hard axis, and show the final artifact or state change. If the golden path is not working after hour one, cut scope.

#### Generate your build plan

Use this only after Idea Lock is approved and `IDEA_SCOPE.md` exists. It turns the locked scope into milestone-by-milestone execution without reopening idea selection.

Sarvam six-hour build plan

Copy

```
You are my senior build partner at the Sarvam Epoch six-hour AI Buildathon. I must ship a working product, submit a public URL, and prove it live in three minutes.

AUTHORITATIVE SOURCES
1. Open https://growthx.club/docs/sarvam and read the event schedule, rules, exact rubric ladders, Sarvam documentation links, and build constraints.
2. Read IDEA_SCOPE.md in my current project. It is the control plane for the build.
3. Do not reload or restate the complete Idea Library. Idea selection is over.

SCOPE GATE
- If IDEA_SCOPE.md is missing or the Idea Lock is not explicitly approved, stop. Tell me to finish the handbook's Hackathon Idea and Scope Copilot first. Do not invent or silently broaden the scope.
- If it exists, begin by stating: the locked user, completed job, hard input, final output/state change, selected Sarvam parameter, active milestone, acceptance test, non-goals, and remaining build time.
- If work has already started, continue from the active milestone. Do not regenerate the day from hour one.

RUBRIC CONTRACT
- Five Product parameters are scored independently: Job-to-be-done completion, Memory and Context, Creativity, Impact, and Delight.
- Exactly one Sarvam parameter is scored: Voice Experience, Document Intelligence, or Dubbing.
- Additional capabilities and API count add no points.
- L1-L5 is independent per parameter. Never call the whole project “L3.”
- One level equals one base point: L1 = 1 point, L2 = 2, L3 = 3, L4 = 4, and L5 = 5.
- Weighted points equal level points multiplied by the parameter multiplier: JTBD 2.5×, Memory and Context 1×, Creativity 1.5×, Impact 1.5×, Delight 1×, and the single selected Sarvam parameter 2.5×.
- The maximum weighted score is 50 points.
- Never use one proof to raise two parameters.
- Hour one must target at least JTBD L3: one correct, usable artifact or state change from a real end-to-end loop.
- JTBD L5 requires 90%+ success across at least three repeated cases without judge intervention.

BUILD RULES
- De-risk the hardest dependency before UI breadth or polish.
- Keep one runnable golden path after every milestone.
- Mock external systems faithfully. Avoid unprovisioned messaging, telephony, KYC, production auth, and real high-risk integrations.
- Verify exact language, model, input, output, quota, and event-account access before depending on them.
- Preserve the locked non-goals. Put every new feature request in the parking lot unless I explicitly rescope.
- When blocked, simplify or route around the blocker before redesigning the product.
- Distinguish implemented, working locally, acceptance-tested, public-link verified, and demo-ready.

OUTPUT 1 · SCOPE AND EVIDENCE CHECK
Create a compact target vector:

| Parameter | Current evidence | Target | Next distinct proof |
|---|---|---|---|

Use the exact handbook thresholds. Identify the JTBD floor, the selected Sarvam parameter, the one Product parameter with disproportionate upside, and the dimensions that should stay merely competent.

OUTPUT 2 · EXECUTION PLAN
If the build has not started, plan six one-hour milestones from 10:30 AM to the 4:30 PM submission lock. If it has started, convert the remaining time into equivalent milestones without restarting completed work.

For every milestone give:
1. exact tasks in order;
2. the runnable artifact produced;
3. one acceptance test that must pass before moving on;
4. the distinct rubric evidence created;
5. the largest live-demo risk after this milestone;
6. “if behind, cut to this”;
7. explicit parking-lot items.

Milestone requirements:
- M1: prove the hardest Sarvam dependency and complete one ugly, hardcoded end-to-end job.
- M2-M4: deepen the locked mechanic and the highest-leverage rubric evidence without breaking M1.
- M5: integrate the final surface, repeat representative cases, verify recovery, and test the public URL from another device.
- M6: no new features. Reset state, fallback inputs/recording, submission assets, three repeated runs, and two timed rehearsals only.

Do not mechanically assign one different rubric parameter to every hour. Add work only when it creates the next visible proof in the target vector.

OUTPUT 3 · BUILD CONTROL
End with:
- the next single action;
- a checkpoint table with Implemented / Working locally / Acceptance-tested / Public-link verified / Demo-ready;
- stop conditions that trigger scope cuts;
- the three-minute demo script;
- an evidence map assigning each exact demo moment to one rubric parameter;
- one likely judge question and a concise evidence-backed answer.

During the build, reread IDEA_SCOPE.md before proposing changes and protect the active milestone's acceptance test.
```

#### References

**Sarvam:** [API quickstart](https://docs.sarvam.ai/api/getting-started/quickstart) · [speech to text](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/overview) · [text to speech](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/overview) · [translation](https://docs.sarvam.ai/api/api-guides-tutorials/text-processing/overview)

**Document and media:** [Sarvam Vision](https://docs.sarvam.ai/api/getting-started/models/sarvam-vision) · [Document Intelligence](https://docs.sarvam.ai/docai/getting-started/overview) · [Creative Studio and Dubbing](https://docs.sarvam.ai/creative/studio-overview) · [ffmpeg](https://ffmpeg.org/documentation.html)

**Backend and data:** [Convex](https://docs.convex.dev/) · [Supabase](https://supabase.com/docs)

**Comms:** [Resend](https://resend.com/docs) · [Telegram Bot API](https://core.telegram.org/bots/api) · [Slack webhooks](https://api.slack.com/messaging/webhooks) · [ntfy.sh](https://ntfy.sh/)

**Mocks:** [Beeceptor](https://beeceptor.com/) · [Mockoon](https://mockoon.com/) · [httpstat.us](https://httpstat.us/)

---

# Part 3 · Event Reality Brief (organizer context)

# Sarvam Epoch Buildathon · Event Reality Brief

This brief is extracted from the current Builder Handbook and paired with the official Sarvam documentation links below. The complete rubric, Idea Library, and `IDEA_SCOPE.md` template follow separately in this copied bundle.

## Event

- **Event:** Sarvam Epoch Buildathon
- **Date:** Sunday, July 26, 2026
- **Venue:** Razorpay Arena
- **On-site window:** 10:00 AM–6:30 PM IST
- **Kickoff:** 10:00 AM
- **Build sprint:** 10:30 AM–4:30 PM
- **Submission lock:** 4:30 PM. The exact submission link and floor mechanics are announced on-site.
- **Demos and winners:** 5:30–6:30 PM. Top teams demo; the top 10 present at Sarvam Epoch.
- **Demo format:** three minutes: 30 seconds of business context, 30 seconds of current workflow/pain, and two minutes of live product demonstration. Keep a fallback recording ready.
- **Eligibility:** registered, approved builders aged 18 or above who are physically present.
- **Team size:** solo or up to five people; every member must be registered and approved.

## Build rules

- Build a new project on-site that day. Helper utilities, BaaS, standard scaffolding, and AI coding assistants are allowed.
- Sarvam must be core to the product, not a garnish. Other models and APIs may support it.
- Existing company demos, previously built agents with small tweaks, off-floor code, remote contributors, and projects already demoed elsewhere do not qualify.
- One submission per team. If the starting point is borderline, disclose it for mentor review.
- Builders retain the IP in what they create. The handbook, rubric, structure, copy, visual design, and Idea Library are GrowthX IP.

## Judging contract

- Every team is judged independently on five **Product parameters**: Job-to-be-done completion, Memory and Context, Creativity, Impact, and Delight.
- The team selects exactly one scored **Sarvam parameter**: Voice Experience, Document Intelligence, or Dubbing.
- Judges score the single Sarvam capability most central to completing the user's job. Extra Sarvam capabilities do not add points.
- L1–L5 is evaluated separately for every parameter. There is no single overall project level.
- The same proof cannot raise two parameters. Assign evidence to the behaviour it actually demonstrates.
- Use the complete bundled rubric as the scoring source of truth.

## Verified Sarvam capability surface

Verify access from the event account before making any capability a critical dependency.

- **Saaras v3 speech-to-text:** input support across 23 languages; REST, streaming, and batch surfaces are documented.
- **Bulbul v3 text-to-speech:** output support across 11 languages with 30+ documented voices.
- **Sarvam Translate:** translation across 23 languages. Mayura supports 11 languages.
- **Sarvam Vision API:** document understanding across 23 languages. The API model guide documents a maximum of 10 PDF pages and 200 MB per file.
- **Doc AI Studio:** Extract and Digitise workflows for PDF, JPEG, and PNG. The Studio overview documents 50 MB per file and 10 pages per project. Do not confuse this Studio limit with the Vision API file limit.
- **Creative Studio:** the Studio overview describes dubbing and voice-preservation workflows, with voice cloning labelled beta. Do not assume Studio-only or beta behaviour exists in the public base APIs or in the event account; verify first.
- **Voice agents and realtime speech:** use the official integration/cookbook surfaces where applicable and measure actual latency before promising “instant” or “realtime.”

## Official Sarvam sources

- Quickstart: https://docs.sarvam.ai/api/getting-started/quickstart
- Current model catalogue and language coverage: https://docs.sarvam.ai/api/getting-started/models
- Saaras v3 model guide: https://docs.sarvam.ai/api/getting-started/models/saaras-v3
- Bulbul v3 model guide: https://docs.sarvam.ai/api/getting-started/models/bulbul-v3
- Sarvam Vision model guide: https://docs.sarvam.ai/api/getting-started/models/sarvam-vision
- Speech-to-text overview: https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/overview
- Text-to-speech overview: https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/overview
- Text processing and translation: https://docs.sarvam.ai/api/api-guides-tutorials/text-processing/overview
- Doc AI Studio overview: https://docs.sarvam.ai/docai/getting-started/overview
- Creative Studio and dubbing overview: https://docs.sarvam.ai/creative/studio-overview
- Voice-agent integrations: https://docs.sarvam.ai/api/integration/build-voice-agent-with-twilio
- Sarvam developer tools and MCP: https://docs.sarvam.ai/api/developer-tools/mcp

## Known unknowns to resolve on the floor

- Exact submission URL and any additional form fields.
- Which beta, Studio, telephony, or realtime surfaces are enabled for the event account.
- Live quotas, concurrency, rate limits, pricing/credits, and any event-specific overrides.
- Whether a chosen language pair is supported end to end across every required input and output surface.

Do not invent answers to these unknowns. De-risk the hardest dependency in the first hour and keep a fallback that still completes the declared user job.

---

# Part 4 · Full rubric

# Sarvam Buildathon — full rubric draft

Status: copy draft for the HTML rubric.

## Rubric architecture

Every team is evaluated on the same five common parameters:

1. Job-to-be-done completion
2. Memory and Context
3. Creativity
4. Impact
5. Delight

The rubric begins with the Sarvam parameters:

- Voice Experience
- Document Intelligence
- Dubbing

Every team must demonstrate at least one Sarvam capability. Judges score the single capability most central to completing the user's job. Additional capabilities do not add points. Depth on one capability beats breadth across several.

## How to read the rubric

Each row describes what the product looks and feels like at L1 through L5. Read the complete description and example for the level; do not score from the headline alone. The examples are illustrations of the standard, not a checklist of features every team must copy.

## Points and weightages

One level equals one base point: L1 = 1 point, L2 = 2 points, L3 = 3 points, L4 = 4 points, and L5 = 5 points.

Weighted points = level points × parameter multiplier.

| Parameter | Multiplier | L1 points | L2 points | L3 points | L4 points | L5 points |
|---|---:|---:|---:|---:|---:|---:|
| Job-to-be-done completion | 2.5× | 2.5 | 5 | 7.5 | 10 | 12.5 |
| Memory and Context | 1× | 1 | 2 | 3 | 4 | 5 |
| Creativity | 1.5× | 1.5 | 3 | 4.5 | 6 | 7.5 |
| Impact | 1.5× | 1.5 | 3 | 4.5 | 6 | 7.5 |
| Delight | 1× | 1 | 2 | 3 | 4 | 5 |
| Selected Sarvam parameter | 2.5× | 2.5 | 5 | 7.5 | 10 | 12.5 |

Judges score all five Product parameters and exactly one selected Sarvam parameter. Voice Experience, Document Intelligence, and Dubbing share the same 2.5× Sarvam slot. Unselected capabilities add no points. The maximum weighted score is 50 points.

### Detailed scoring example

A team selects Voice Experience and receives these levels:

| Parameter | Level | Calculation | Weighted points |
|---|---:|---:|---:|
| Job-to-be-done completion | L4 | 4 × 2.5 | 10 |
| Memory and Context | L3 | 3 × 1 | 3 |
| Creativity | L4 | 4 × 1.5 | 6 |
| Impact | L3 | 3 × 1.5 | 4.5 |
| Delight | L2 | 2 × 1 | 2 |
| Voice Experience | L4 | 4 × 2.5 | 10 |

Total = 10 + 3 + 6 + 4.5 + 2 + 10 = **35.5/50, or 71%**. Document Intelligence and Dubbing do not contribute points because Voice Experience is the team's single selected Sarvam parameter.

---

# Product parameters

## 1. Job-to-be-done completion

**The question:** Did the product produce the correct, usable outcome?

This ladder is locked and reproduced verbatim.

### L1
0–25% task success. Demo only, with no reliably usable outcome.

The agent gives canned responses or talks through the workflow, but does not complete the declared job.

Example: the agent talks about modifying an order but does not check the order, does not write to a support queue, does not update a sheet, and does not create any usable output. In hiring, it says it screened a candidate, but no scorecard, ATS update, rejection, shortlist, or next-step decision is created.

### L2
26–50% task success.

The agent runs, but the output is broken, fake, incomplete, or unusable.

Example: in payments, it pulls the wrong transaction, gives a made-up refund status, or tells the user that money has been reversed without checking the payment record. In quick commerce, it says the delivery slot has changed, but nothing changes in the support queue, sheet, dispatch mock, or order system.

### L3
51–75% task success on mocked, sandbox, or staged surfaces.

The agent completes a useful part of the declared job and creates at least one usable artifact.

Example: the agent verifies an order against a mocked order DB, writes to a mocked dispatch system, updates a sandbox support queue, creates a scorecard, drafts a support note, or classifies a payment dispute. Staged WordPress, sandbox Gmail, dummy ATS, mocked CRM, Airtable, Notion, or Google Sheets also sit here.

### L4
76–89% task success on a production-like demo workflow.

The agent completes most of the declared job across a realistic workflow. Human review may still be needed for final approval.

Example: the agent drafts the refund ticket inside a support queue, but a support lead must approve the refund. In hiring, it runs the first-round screen and drafts the scorecard in the ATS, but a recruiter must manually review and move the candidate. In payments, it classifies the dispute and prepares the escalation, but ops must confirm before the case moves.

### L5
90%+ task success across a minimum of three repeated test cases.

The agent completes the declared job end to end using mocked, sandbox, staged, or live demo surfaces, and produces a final usable output without judge intervention.

Example: in quick commerce, the agent verifies the order, identifies missing items, checks refund eligibility, writes back to the support queue, updates the order or ticket, and escalates only exceptions. In payments, it verifies identity, pulls the UTR, classifies failed-but-debited, refund-pending, fraud, or unrecognised transaction, gives the correct next step, and creates the right dispute record. In hiring, it detects the role, runs the right screen, scores the candidate using the right rubric, updates the ATS, and advances or rejects without HR involvement.

---

## 2. Memory and Context

**The question:** Does the product carry forward the right identity, history, task state, permissions, and business rules?

Memory is business continuity, not merely remembering chat messages. It includes what is happening now, what has happened before with this user or case, and what the business allows. It must preserve relevant context without leaking one user's or organisation's information to another.

Score only persisted, governed continuity here. Natural conversational flow inside one exchange belongs to Voice Experience, and describing an authentication scheme without demonstrating carried context does not establish Memory and Context.

### L1
Every interaction starts from zero.

The product does not retain the current task, user identity, prior answers, document state, or business context. The user repeatedly supplies the same details, and any handoff or restart loses everything.

Example: a customer gives the order ID, explains that the milk and bread are missing, and confirms that the bag arrived sealed. When the flow moves from the voice agent to the refund screen, it asks for the order ID again, forgets which items were missing, and makes the customer repeat the entire complaint from the beginning.

### L2
It remembers identifiers, but not the working context.

The product can hold one or two fields such as a name, phone number, case ID, document ID, or preferred language during the current interaction. It does not reliably retain the user's actual goal, prior decisions, permission scope, or the state of the job. Handoffs pass identity at best and re-ask everything that matters.

Example: a payment assistant remembers the caller's phone number and UTR, but loses the ₹4,200 amount, the transaction date, the fact that the account was debited, and the caller's request for a dispute. When the case moves to classification, the assistant knows who the user is but still asks, “What happened with your payment?”

### L3
It maintains the complete current task for an authenticated user.

The product knows who the user is, what they are allowed to access, what has already been supplied, and what remains to be done inside one session or workflow. It uses earlier answers instead of repeating questions. Relevant current-task context survives ordinary steps, but older history, a new session, a new channel, or a handoff is incomplete or lost.

Example: during one GST notice session, the product retains the trader's identity, the uploaded notice, the preferred Kannada explanation, the extracted deadline, and a corrected business name. The user can move from explanation to reply drafting without repeating anything. When the user returns the next day to ask whether the reply was sent, however, the product has no record of the case and starts a fresh upload flow.

### L4
It uses relevant history and carries context across sessions, channels, or handoffs.

The product combines the current task with useful prior history: previous tickets, documents, transactions, corrections, preferences, decisions, or unresolved actions. A handoff receives a concise, accurate state rather than the entire raw transcript, and the next component continues without making the user restart. Authentication and permissions remain intact.

Example: a customer begins a missing-order complaint on a voice call and continues on WhatsApp after the call drops. WhatsApp opens the same case, knows which order and items are disputed, carries forward the photograph already collected, replies in the customer's preferred language, and asks only for the one confirmation still needed before the refund can be reviewed.

### L5
It delivers governed business continuity across the whole product.

The product reliably combines three layers: the current task, the relevant history of this user or case, and the business rules that govern the next step. Context survives every demonstrated session, channel, tool, and handoff. Corrections propagate, stale information is distinguishable from current information, and access stays within the authenticated user's permissions and organisation boundaries.

Example: a lending assistant recognises a returning applicant, resumes the incomplete application at the correct step, and uses the latest income document instead of an older superseded upload. When the eligibility policy changes, it applies the current rule, records why the decision changed, and hands the reviewer a concise case summary rather than a raw transcript. A second applicant using the same device cannot see or retrieve any part of the first applicant's case.

---

## 3. Creativity

**The question:** How uniquely and non-obviously was the problem solved?

Creativity can come from the idea, the problem framing, the interaction mechanic, or the way the solution uses Sarvam. It is not visual polish, implementation difficulty, or the number of APIs connected. A team that chooses an idea from the library can still reach L5 by taking it somewhere nobody could predict from the card.

### L1
The build is the obvious first implementation.

It closely reproduces a reference agent, idea-card flow, tutorial, or generic wrapper. The problem statement is enough to predict the entire demo. Changing the logo, persona, language, or UI theme is not a creative contribution.

Example: a government-scheme bot asks for age, income, state, and occupation, then reads back a list of matching schemes. The team has changed the colours, added a friendly avatar, and translated the responses, but the product is still the exact form-and-results flow anyone would predict from the problem statement.

### L2
There is a twist, but it is cosmetic or loosely attached.

The team adds one variation beyond the obvious build, but it does not materially change how the problem is understood or solved. The novelty may create a demo moment without making the product more coherent or useful.

Example: a GST notice interpreter adds an animated avatar, celebratory transitions, and a choice of dramatic voice styles. Once those effects are removed, the product is still only “upload a notice and receive a summary”; the twist does not change what the trader understands, decides, or does next.

### L3
The solution contains one meaningful, non-obvious choice.

The team has taken a recognisable point of view. At least one mechanic, workflow choice, or use of the Sarvam stack changes how the user solves the problem, rather than decorating the expected solution. The rest of the product may still be conventional.

Example: the obvious contract product translates every clause into simpler language. This product instead lets a shop owner ask, “What can hurt me in this deal?” in their own language, connects each risky clause to the owner's payment terms and inventory exposure, and produces a short negotiation checklist they can use on the next supplier call. The core product changes from translation to decision support.

### L4
The solution is distinctive from end to end.

Several original choices reinforce one another across the problem framing, interaction, and product workflow. The use of Sarvam is purposeful rather than ornamental. Another competent team given the same problem would be unlikely to arrive at the same product.

Example: a factory operator does not stop work to search an English manual or type a clean fault description. The product listens to the machine noise and the operator's code-mixed explanation, identifies the likely fault, retrieves the exact manual section, and talks the operator through the repair one safe step at a time while their hands remain occupied. The input, diagnosis, and teaching interaction all reinforce the same point of view.

### L5
The solution reframes what people thought the product could be.

The idea produces a genuine “I did not know you could solve it that way” reaction, yet feels coherent and inevitable once demonstrated. Its originality is not a gimmick: the non-obvious approach unlocks a materially better possibility for the user. The team has created a memorable product category or interaction that cannot be inferred from the idea card alone.

Example: the expected compliance product translates a new RBI circular and summarises it. This product turns every changed rule into short, role-specific simulated customer conversations, lets frontline staff respond in their everyday language, identifies where their decisions violate the new rule, and gives the compliance head an evidence trail of exactly which teams and scenarios need retraining. The circular becomes an operating system for behaviour change rather than another document to read.

---

## 4. Impact

**The question:** If this product did not exist—or was taken away—whose outcome gets worse, by how much, and how often?

Impact scores the value of solving the problem, not whether this build currently works. A high-impact problem can have a weak prototype, and a flawless prototype can solve a low-impact problem. The team must name the beneficiary or payer, the current baseline, the frequency of the problem, and one metric that moves.

### L1
No credible impact case is articulated.

The team describes the technology or a broad social good but cannot name who experiences the problem, how often it occurs, what it costs today, or which outcome changes.

Example: the team says the product will “empower Bharat with AI” and shows a large number of regional-language users. It cannot say which user faces the problem, how many times that user faces it in a month, what they currently lose or spend, or whether success should change completion, cost, revenue, risk, access, or turnaround time.

### L2
The problem is real, but the value case is weak or unproven.

The team names a user and a metric, but the frequency, current cost, or path from the product to the outcome is mostly assumed. The likely movement is small, below 5%, or limited to a convenience metric that is not important to the beneficiary.

Example: a multilingual FAQ assistant answers a handful of internal questions for a ten-person team. The builders claim that it will save time, but they have not measured current question volume, the time spent per answer, or whether faster answers change support cost, resolution time, conversion, access, or risk. Even if the assistant works perfectly, the business outcome is likely to remain almost unchanged.

### L3
There is a clear case for meaningful value.

The team can defend who benefits, how often the problem occurs, what the current process costs, and a plausible 5% to below 10% movement on one meaningful metric. For public-service or everyday-life products, an equivalent movement in access, completion, turnaround time, error rate, or avoidable loss counts.

Example: a regional compliance team receives eight relevant circulars in an average month and currently spends about two working days interpreting each one for branch teams. The product could reduce that work to one day per circular. The team shows the current staff hours, the monthly volume, and the number of delayed branch updates, then connects the proposed reduction to a plausible 5–10% improvement in compliance turnaround time.

### L4
The product targets a major, measurable bottleneck.

The team shows a defensible path to 10 to 30% movement on an important operating, revenue, cost, risk, access, or service metric. The affected user or payer is explicit, the baseline is credible, and the value survives reasonable challenge to the assumptions.

Example: an MSME has ₹1.8 crore sitting in invoices that are more than 60 days overdue, and its finance team spends 90 hours a month chasing the same buyers. The product prioritises the accounts most likely to pay, conducts regional-language follow-ups, and escalates disputed invoices with the correct evidence. The team can show how a defensible reduction in days-sales-outstanding would release enough working capital to change inventory purchasing and payroll decisions even if adoption is lower than planned.

### L5
The product addresses a top-priority problem with transformational value.

The problem is tied to a critical metric or previously inaccessible outcome, with a credible path to more than 30% movement or an equivalent step-change in cost, revenue, risk, access, or service delivery. The team can show why this is a priority now, why the affected organisation or user would act, and what adoption at meaningful scale looks like.

Example: a lender processes hundreds of thousands of routine collection calls each month, while trained agents spend the same time on simple reminders, genuine hardship, and disputed debt. The product resolves routine cases in the borrower's language, detects hardship or disagreement, and routes only those cases to specialists with the complete context. The team shows the portfolio size, present call cost, resolution baseline, expected recovered value, and adoption path, making the case for a step-change rather than a generic “AI will reduce costs” claim.

---

## 5. Delight

**The question:** At the user's real point of friction, does the product create confidence, clarity, and forward movement?

### L1
The product mishandles the moment of friction.

The user becomes more confused, anxious, or stuck. The product may hide uncertainty, offer false reassurance before it knows the answer, expose raw system output, or end without a usable next step. The builder must explain what to do.

Example: while reading a photographed GST notice, the product repeatedly says “nothing to worry about” before it has classified the document. It later reveals a serious filing issue as a block of extracted fields and confidence scores, with no explanation, deadline, or next action. The reassurance was unearned and the user is now less certain than before.

### L2
The result is usable, but the care is generic.

The product completes the happy path and may add polite language, a friendly voice, animation, or “don't worry” copy. It does not respond to the user's actual concern, explain why the situation is or is not serious, or adapt the next step to the case.

Example: a GST notice assistant produces an accurate English summary and a generic “consult a professional” message. It does not identify the response deadline, distinguish a system mismatch from a genuine filing failure, or explain what the shop owner can verify now. The answer is functional, but the reassurance could have been attached to any notice.

### L3
The product removes the obvious friction.

A first-time user can complete the main flow without builder intervention. The product communicates status honestly, presents the result in the right form and language, and gives a concrete next action. It is context-aware on the common path, but its care stops at the immediate result or becomes generic when the case is uncertain.

Example: a notice interpreter highlights the disputed amount, response deadline, and one recommended next action in Kannada, then creates a reply the shop owner can send to their CA. The owner understands what happened without the builder speaking. When one photographed page is unreadable, however, the product says “processing failed” instead of identifying the page to retake or preserving the completed work.

### L4
The product handles the user's hardest moment with judgment.

The experience identifies the real point of anxiety or friction and responds with the correct emotional weight. It tells the truth without being alarming, reassures only where the evidence supports reassurance, explains what happens next, and recovers without discarding progress. The user feels that the product understands both the job and the situation.

Example: a shop owner uploads a genuine GST notice. The product does not pretend it is harmless. It calmly explains why the notice matters, shows the source lines and response window, distinguishes what is verified from what is uncertain, and gives three ordered options: verify the mismatch, prepare the missing records, or escalate to the CA. If one page is unreadable, it preserves the analysis, names that page, and explains exactly what to retake.

### L5
The product anticipates the pain point and stays with the user through resolution.

The product does everything L4 requires, then goes beyond the immediate interaction. It predicts the next concern, preserves continuity, makes follow-up effortless, and keeps the user informed until the difficult job has a controlled path forward. The support is specific to the user's situation—not a pile of extra features—and every demonstrated edge feels intentional.

Example: a bakery owner photographs a dense four-page GST notice received on WhatsApp. The product gives a concise Kannada explanation, shows why the amount may be valid, and turns the next steps into a case with the response deadline, required records, and a draft message to the CA. The owner can ask follow-up questions without repeating the notice, see whether each action is complete, and receives a reminder before the deadline. When she corrects one business detail, the explanation, case, and draft all update. She is not falsely cheered up or left in the cold; she knows what happened, what will happen next, and how to return if she is still unsure.

---

# Sarvam parameters

Voice, Document Intelligence, and Dubbing are alternatives—not three extra boxes every team needs to tick.

Build deeply on the capability most central to completing the user's job. Every team must demonstrate at least one Sarvam capability. Judges score the single capability most central to completing the user's job.

Additional capabilities do not add points. Get the central capability working deeply first. If the job genuinely requires a second capability, explain why to your mentor before spending time on it; judges may record it as a qualitative differentiator when comparing the top teams. If it is ornamental or force-fitted, ignore it. Depth on one capability beats breadth across several.

## Branch A. Voice Experience

**The question:** Does the voice feel human-grade and appropriate for the declared job?

### L1
The voice works, but the agent feels like a generic phone tree.

Speech-to-text breaks on anything outside neutral speech. Accents, hindi-english code-switching, and background noise produce garbled transcripts that the agent answers anyway. Intent detection is literal. It latches onto the first phrase it hears and misses the real ask. There is no emotional read. A calm caller and a panicked caller get the same flat reply. Turn-taking is broken. The agent talks over the user or freezes when interrupted, and a correction forces the conversation to restart from the top. Pacing stays at one speed regardless of the moment.

The agent works through a fixed question list with no logic between them. There are no real follow-ups, only the next item on the script. The voice itself sounds robotic, with no natural pauses or prosody. Word choice is thin: fillers, repetition, and stock phrases like "I understand your concern" used everywhere.

Example: a candidate joins a hiring call and says "haan, I worked at a B2B SaaS for two years, mostly retention work." The agent replies "could you tell me about your most recent role?" and reads the next three questions from a fixed list. It misses the hindi switch, misses the retention signal, and never follows up. In payments, the agent says "I understand your concern" without sounding urgent or specific to the stuck transaction.

### L2
The voice is usable, but still feels scripted and shallow.

The agent handles neutral speech on a happy path. Heavy accents, code-switching, or noisy lines trip the transcript. Intent detection works for direct asks but misses hedged or layered ones. There is no real emotional read. The agent says the right words for a complaint but does not sound like it senses one. Turn-taking is basic. The agent finishes its turn, the user finishes theirs, but interruptions throw it off and only clean corrections get recovered. Pacing barely shifts.

The agent asks obvious follow-ups instead of smart ones, repeats confirmation lines, and does not know when to be brief or when to slow down. The voice is understandable but flat. Word choice is generic, with stock phrases recycled across very different moments.

Example: in quick commerce, the agent answers "where is my order," but sounds the same whether the user is calm, angry, confused, or asking for a refund. In hiring, it captures candidate answers but asks the same three follow-ups regardless of seniority or role.

### L3
The voice feels functional and domain-aware, but not yet polished.

The agent handles most clean speech and some accent variation. Layered complaints, mixed-language sentences, or unclear speech still break it. Intent detection works for direct asks and obvious follow-ups. The agent picks up obvious emotion or urgency and changes its reply slightly based on the situation. Turn-taking is decent. It handles simple interruptions and recovers from clean corrections, but loses context if the user redirects mid-stream. Pacing modulates slightly between sections of the call.

The agent asks useful, role-specific or domain-specific follow-ups and clarifies missing information. The script seams show in pushback or emotional moments. Prosody is decent. Domain wording is in place. There are fewer fillers, but stock phrases still leak through under pressure.

Example: in hiring, the agent asks role-specific questions and follows up on one answer. In payments, it explains the next step clearly but still sounds slightly scripted when the user pushes back. In quick commerce, it handles a refund ask but stumbles when the user asks two questions at once.

### L4
The voice feels like a competent operator for the declared job.

The agent handles accents, most code-switching, and noisy phone lines without breaking the transcript. Intent detection catches the real ask under hedging or rambling. The emotional read is strong. The agent picks up frustration, urgency, hesitation, and mild anger, and adjusts its tone in the same call. Turn-taking is clean. It handles barge-in without losing context and recovers from corrections without restarting. Pacing varies for the moment: brisk for simple tasks, calm for complaints, careful for payments, sharper for interviews, direct during escalation.

Each follow-up builds on the last answer rather than running down a list. The agent knows when to be brief and when to slow down. The voice has natural pauses and controlled modulation. Word choice is tight. The agent does not over-talk.

Example: in payments, the agent slows down when explaining refund timelines and confirms the next step clearly. In hiring, it probes the candidate's answer like a real interviewer. In quick commerce, it gives fast answers without sounding cold and handles a user changing their mind mid-call without restarting the flow.

### L5
The voice feels human-grade for the declared job.

The agent holds up on real-world indian speech: accents, hindi-english code-switching, noisy phone lines, partial words, and self-corrections do not break the transcript. Intent detection catches the actual ask under hedging, rambling, or incomplete phrasing. The emotional read is sharp. The agent picks up frustration, urgency, hesitation, and confusion, and adapts mid-call without sounding theatrical. Turn-taking is clean and natural. It handles barge-in without losing context, knows when to stop talking, and recovers fluidly from corrections, mid-stream redirects, and "no wait, actually" moments. Pacing shifts deliberately: brisk for confirmations, slower for sensitive moments, real pauses where needed.

Each follow-up builds on the last answer instead of running down a list. The agent knows when to comfort, when to be firm, when to ask one more question, when to wrap, and when to escalate. The voice sounds present, with natural prosody and real modulation. Word choice is tight. No filler, no jargon dump, no repeated stock phrases. It does not sound like it is reading a script. It sounds like it knows the user, the job, and the business rule behind the answer.

Example: a candidate completes a first-round screen and feels like they spoke to a thoughtful interviewer. A payments caller asks about a failed ₹4,200 UPI payment from two days ago, fumbles for the UTR, and the agent offers to find it by amount and timestamp. The agent picks up rising frustration, softens, slows down, confirms the dispute reference in one clean line, and offers to send the case ID on whatsapp. The caller hangs up clear on what happened, what is being done, and when to expect resolution.

---

## Branch B. Document Intelligence

**The question:** How well does the product understand and represent real Indian documents?

This branch evaluates document-medium execution: the classes of documents the system can handle, preservation of reading order and structure, handwriting and mixed-script handling, layout and table reconstruction, and source traceability. Job-to-be-done completion separately evaluates whether the business facts and final outcome are correct.

### L1
It works only when the document is already easy.

The product depends on clean, digital, text-layer PDFs or copied text. It loses reading order, headings, tables, checkboxes, or page relationships. Scans, photographs, handwriting, and mixed scripts make the output unusable.

Example: a compliance tool reads the selectable text in a digitally generated circular, but loses the relationship between headings, clauses, footnotes, and the cells of a regulatory table. The output contains most of the words, yet a reviewer cannot tell which exception belongs to which rule or trace a statement back to the correct page.

### L2
It handles clean scans and simple layouts.

The product can process a legible scan or photograph with one language and conventional formatting. Basic paragraphs survive, but handwriting, low light, skew, stamps, multi-column reading order, or dense tables break the representation. The output requires significant manual cleanup before another system can use it.

Example: a wage register is digitised correctly when it is typed, evenly lit, and photographed flat. On the register workers actually use, handwritten overtime entries disappear, merged cells shift wages into the wrong employee's row, and a stamp covering one number is silently treated as text. A supervisor must compare and repair the sheet line by line.

### L3
It handles representative real-world documents with one meaningful difficulty.

The product preserves usable reading order and structure across ordinary scans or phone photographs and handles at least one hard class relevant to the use case: handwriting, tables, mixed scripts, degraded scans, or complex forms. Extracted regions remain connected to their source page or location. A more difficult combination still causes visible errors.

Example: a contract tool handles an ordinary phone photograph, keeps the clause table attached to the right section, and lets the user open the source page for every extracted clause. It also preserves signatures and page boundaries. When handwritten changes overlap printed payment terms, however, the tool merges the two versions and cannot show which language was added later.

### L4
It is robust across the difficult document conditions the user actually encounters.

The product handles combinations of handwriting, mixed Indic scripts, multilingual text, complex layouts, tables, stamps, folds, skew, poor lighting, faded print, or overwriting without flattening the document's meaning or structure. Uncertain regions are visibly identified and easy to inspect against the source.

Example: a field-inspection form contains printed Kannada instructions, handwritten English measurements, checked and crossed-out boxes, an approval stamp, and a table photographed at an angle under poor light. The product reconstructs the reading order and table structure, keeps each measurement attached to the correct item, and links every field to its source region. One value hidden by the stamp is marked for review instead of being guessed.

### L5
It reaches expert-grade document understanding on the hardest Indian material.

The product holds up on severely degraded, handwritten, historical, or heritage documents; mixed scripts and languages; dense tables; marginalia; corrections; seals; and damaged originals. It produces a structured, searchable representation that preserves the document's relationships and provenance, not merely a text dump. The system knows which regions are uncertain and makes review precise.

Example: a handwritten archival ledger contains faded ink, Marathi and English entries, margin corrections, stamps, damaged corners, and tables that continue across several pages. The product turns it into a searchable structured record while preserving the page, row, column, and source region for every entry. Competing readings remain visible as uncertainty, so an archivist can review only the difficult regions rather than transcribing the entire ledger again.

---

## Branch C. Dubbing

**The question:** Does the dubbed media feel authored and performed for this audience?

This branch evaluates spoken-media adaptation: translation and cultural adaptation for speech, speaker identity, pronunciation, emotion, pace, timing, overlaps, music, scene cuts, and publication readiness. Job-to-be-done completion separately evaluates whether the declared dubbing job produced the correct, usable final artifact.

### L1
The audio is replaced, but the media no longer works.

The output is a literal or broken conversion of the source. Meaning, names, numbers, or key terms are damaged. Voices are robotic or assigned to the wrong speakers. Timing ignores the source, dialogue runs across cuts, and music or original speech competes with the dub.

Example: a two-person interview becomes one flat Hindi voice for both speakers. It mispronounces both names, translates a product term into the wrong meaning, continues the first answer over the next on-screen question, and leaves the original dialogue loud enough to compete with the dub. A fluent listener can tell that words were replaced, but can no longer follow the performance.

### L2
The dubbed media is understandable on a simple clip, but feels overlaid.

Straightforward speech is translated and voiced well enough to follow. Domain terms, code-mixing, idiom, jokes, names, or emotional passages produce obvious mistakes. Speaker separation is basic, pronunciation is inconsistent, and timing is approximate rather than shaped to the scene.

Example: a clean educational clip is understandable in Tamil when one teacher speaks slowly to camera. In the next segment, English technical terms are repeatedly mispronounced, the student and teacher receive the same voice, and translated sentences continue after the on-screen speaker has stopped. The information is present, but the result feels like audio placed on top of a video rather than a finished dub.

### L3
The dub is natural and audience-aware on representative media.

The adaptation preserves the essential meaning, tone, and important terminology in spoken language that fits the declared audience. Speakers remain distinguishable, common names and code-mixed terms are pronounced credibly, and dialogue broadly follows segment timing. Emotion, rapid exchanges, overlaps, music, or difficult cuts still reveal synthetic seams.

Example: a finance explainer keeps familiar English product terms inside natural Bengali, preserves the teacher's patient explanatory tone, gives the host and caller distinct voices, and follows the edit closely enough to watch comfortably. A fast interruption causes the voices to collide, and a warning about fraud is delivered with the same emotional weight as the introduction, revealing where the synthetic seams remain.

### L4
The dub feels native to the audience and faithful to the performance.

The adaptation preserves intent, register, terminology, idiom, code-mixing, humour, and regional phrasing without copying source-language syntax. Speaker identity, pronunciation, emotion, emphasis, pace, and temporal alignment remain consistent across varied scenes. Dialogue sits cleanly with music and effects, and uncertain names or phrases are isolated for targeted review.

Example: a founder's Hindi-English product video becomes conversational Telugu rather than source-language sentences spoken with Telugu words. The dub preserves the jokes, familiar English product vocabulary, the founder's emphasis, and the contrast between the interviewer and founder. It stays aligned through quick cuts and sits naturally over the music bed; reviewers identify only two names that need local pronunciation fixes instead of asking for the segment to be rewritten.

### L5
The dub is publication-ready across real Indian language and media complexity.

The adaptation handles regional variation, code-mixing, incomplete speech, idiom, cultural references, domain language, and audience-specific register with native judgment. It preserves each speaker's identity, intention, humour, restraint, and emotional arc. Rapid exchanges, overlaps, music, ambience, scene cuts, and difficult timing remain coherent, and the finished piece can be published without a full human rewrite, re-recording, or remix.

Example: a code-mixed financial education video includes jokes, rapid speaker changes, market terminology, interrupted sentences, music, and examples that make sense only in the source culture. The Marathi version replaces those examples with equally clear local ones without changing the lesson, preserves each speaker's personality and emotional arc, and remains coherent through overlaps and scene cuts. Fluent reviewers can publish the complete piece without rewriting the script, re-recording the voices, or remixing the audio.

---

# Builder pro tips

| Parameter | Evidence that earns the level |
|---|---|
| Job-to-be-done completion | The correct, usable outcome is produced across repeated cases. |
| Memory and Context | Identity, task state, relevant history, permissions, and business rules survive where they should—and do not leak where they should not. |
| Creativity | The running solution contains a surprising, coherent, non-obvious angle. |
| Impact | A defensible baseline, beneficiary or payer, frequency, and material movement on one meaningful metric. |
| Delight | A first-time user completes a difficult flow with unusual ease and recovers without builder help. |
| Voice Experience | Real Indian speech, interruptions, emotion, pacing, and follow-ups hold up in a live conversation. |
| Document Intelligence | An unseen difficult document is represented with structure, source traceability, and controlled uncertainty. |
| Dubbing | Fluent reviewers accept unseen dubbed media as natural, performance-faithful, technically coherent, and publication-ready. |

---

# Part 5 · Idea Library

# Sarvam Epoch Buildathon: the idea library

82 cards. Bring your own idea or pick one of these.

Every card names the one thing that is hard about it, because that is what you are scored on. Each declares one central Sarvam capability. The rubric scores Voice Experience, Document Intelligence, or Dubbing; additional capabilities add no points. Calling six Sarvam surfaces shallowly scores below taking one to its hard edge, so each card marks the surface where the depth goes.

Difficulty is honest. Starter means scopeable with a clear demo path. Beast means you might not finish, and a defensible partial is an acceptable outcome.

The four-layer stack, the full tool menu, the mocks, the traps that eat hours, and the references are in the handbook sections document, shown alongside every card.


---

# Use the library as a starting point, not a brief

The 82 ideas below are examples of how to think, not projects to copy line for line. Use them to understand the kinds of problems Sarvam can solve, then find the version that exists in your own work, industry or lived experience. Start with one real user, one broken moment, one clear input and one useful output. Your idea should depend meaningfully on a Sarvam capability, push at least one capability deeply and work on inputs you did not prepare in advance. The rubric does not reward ideas taken from this library, and your own insight may give you a stronger starting point. Pick a card if it helps you move faster, combine parts of several cards or ignore the library entirely. Its purpose is to give you direction and reduce time spent browsing. By 11:30, commit to a problem. By 12:15, have something running.

---

# Business


## 01 ·
GST notice interpretation for regional small traders

**Starter · domain · Document Intelligence**

> Photograph a tax notice, find out what is actually owed and by when, and get it explained in your own language.

**Why this one.** A tax notice does not arrive as a clean PDF. It arrives as a phone photo of a printed letter that has been stamped, folded, and annotated in pen by whoever opened it. The axis is fidelity on the two fields that carry consequence: the amount and the deadline. Everything else on the notice can be paraphrased loosely and nobody is harmed. Get the deadline wrong by a week and you have caused the problem you were hired to solve, so the top bands need the system to refuse a date it cannot read rather than produce a confident guess.

**The scenario.** Bhavesh runs a hardware wholesaling business in Rajkot and does his own filing with help from a part-time accountant. A notice arrives in dense legal English referencing sections he has never read. He does not know whether this is a routine mismatch or something that becomes a recovery proceeding. He photographs both pages on his phone at a slight angle, in shop lighting.

**What you will need**
- Camera capture for a photographed notice, not a file picker expecting a clean PDF
- Doc AI extraction of the fields that matter: notice type, amount, deadline, section referenced, responding office
- Per-field confidence, with a refusal state on amount and deadline specifically
- Plain-language explanation of what this notice is and what happens if ignored
- Output in the trader's language, read aloud as well as written
- Two real notice types, so the demo is not one hardcoded template
- One notice held back unseen for the demo
- A stated number on your own held-back notices: field accuracy on amount and deadline, and how often you refused a field rather than guessing it
- One-pager: the workflow, the integration surface, what you store from a photographed notice, what you redact, and who can see a field the system refused to read, a deploy-or-pilot verdict, and why you declared Document Intelligence rather than Voice Experience when the output is also read aloud

**Your demo moment.** A judge photographs a notice you have never seen. The system pulls the deadline, says plainly what happens if it passes, and on the one figure that is genuinely smudged it says it cannot read that field instead of inventing a number.

**Scores on:** Job-to-be-done and Sarvam parameter. **Weak on:** Creativity, since this is card 01 and everyone has seen it. The refusal behaviour is what separates you.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam Doc AI, pulling notice type, amount, deadline, section referenced and responding office out of a photographed, stamped, folded, pen-annotated letter. This is where the depth goes and where the score is.
- **Supporting** Sarvam-30B for interpreting what the notice type means in practice · Mayura for the trader's language · Bulbul for reading it aloud. All three are plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Next.js or Vite web app, one screen, extracted fields plus an audio play button · plain React with Vite · a single HTML page with a `capture="environment"` file input and an `<audio>` tag, which is genuinely all this card needs
- **Backend** Next.js route handlers · a small FastAPI or Express service · Convex functions · localhost plus a Beeceptor tunnel at 4pm, holding the confidence thresholds and the refusal state on amount and deadline
- **Data** Convex · Supabase · SQLite on disk · or none, hold the one notice in memory, since a single-session demo does not need persistence, for extracted notices, per-field confidence and the refusal queue
- **Comms** Resend · Loops · Telegram bot · ntfy.sh, delivering the trader a written copy with the deadline in the subject line
- **Mock or external** No external system needed · Beeceptor if you want to show the notice written into an accountant's tracker
- **Specific to this build** Four or five real notices, redacted and photographed in shop lighting, before 11:30. Use two actual GST form shapes (a scrutiny notice and a demand or show-cause notice) so the demo is not one hardcoded template.

**Know before you pick this.** To reach the top bands the input has to be a photographed or scanned notice, not a text-layer PDF. Get four or five real notices, redacted, before 11:30.

---


## 02 ·
Overdue invoice recovery for MSMEs

**Challenging · domain · Voice Experience**

> A calling agent that chases a corporate customer's accounts payable desk and comes back with a commitment, not a conversation.

**Why this one.** The person who answers at accounts payable is a junior who has been trained to deflect, and who will switch between English and their own language depending on how the call is going. The axis is commitment extraction from an evasive exchange: pulling a specific date and a specific amount out of someone whose job is to avoid giving either. Tone is irrelevant here. What matters is whether the agent recognises "we will process it soon" as a non-commitment and asks again, in the language the deflection came in.

**The scenario.** Sunita runs a packaging unit in Nashik that supplies three large FMCG customers. Her ninety-day receivables are the reason she cannot pay her own suppliers on thirty. She has one person who spends afternoons calling accounts payable desks and writing "will check" in a notebook. She uploads her aged receivables list.

**What you will need**
- Outbound calling from an aged receivables list
- Conversation designed to extract three fields: a date, an amount, and a named person accountable
- Non-commitment detection, so "soon" and "we will see" trigger a follow-up rather than ending the call
- Code-switch handling, since the deflection often arrives in a different language from the greeting
- Escalation when the caller says the invoice was already paid or is disputed
- Three tool calls: read the invoice and its ageing from the mocked ledger, write the commitment with the clerk's exact words quoted, schedule the follow-up for the day after the promised date
- A stated number over your scripted evasive calls: how many produced a real date and amount, and how many non-commitments were logged as refusals rather than accepted as answers
- One-pager: the workflow, the integration surface, what you record about a named junior at the customer's accounts payable desk, what you quote verbatim, and who is told the call was recorded, a deploy-or-pilot verdict, and why Voice Experience remains primary even when the deflection arrives mid-call in another language

**Your demo moment.** A judge plays an evasive accounts payable clerk and refuses to give a date, switching language halfway. The agent does not accept the non-answer, asks again, and either gets a date or logs the refusal as a refusal.

**Scores on:** Job-to-be-done and Memory and Context. **Weak on:** Delight, since nobody enjoys this product, they just need it.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras streaming, transcribing an evasive accounts payable clerk who switches language mid-deflection, and holding the exact words of the non-commitment. This is where the depth goes and where the score is.
- **Supporting** Sarvam-30B for non-commitment classification and extraction of the date, amount and named person · Bulbul for the agent's outbound voice. Plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Twilio or Exotel outbound, dialling from the aged receivables queue · Plivo · LiveKit or Pipecat if you want barge-in for when the clerk talks over the agent · a browser mic session against a teammate playing the clerk, which is enough to prove the extraction works
- **Backend** Sarvam Agents if you want the chase checkpointed and reopenable · Convex functions · a small Express or FastAPI service · plain code with retry logic, running the queue, the commitment records and the follow-up scheduling
- **Data** Convex · Supabase · Postgres direct · SQLite on disk, for invoices, commitments with the exact language quoted, and follow-up dates. Persistence is real here, the follow-up when a promised date passes is part of the product
- **Comms** Resend · Loops · Telegram bot · Slack webhook, for Sunita's daily digest of commitments obtained and refusals logged
- **Mock or external** Beeceptor · Mockoon · WireMock Cloud for the receivables ledger you read from and write back to · httpstat.us with `?sleep=5000` if you want the write to hang while the clerk is still on the line
- **Specific to this build** An aged receivables list with real ageing buckets, and a written evasive-clerk script with a scripted language switch, so you are not waiting on a human every iteration.

**Know before you pick this.** This is adjacent to Sarvam's Collection Agent cookbook. What makes it different is B2B, an evasive intermediary rather than a debtor, and commitment extraction rather than persuasion. Lead with those or you are building the reference agent.

---


## 03 ·
Noise-robust machine diagnostics for factory floors

**Challenging · technical · Voice Experience**

> An operator describes what the machine is doing, in their language, next to the running machine, and gets a diagnosis grounded in an English-only manual.

**Why this one.** Three hard things stack here and all three test Voice Experience. The floor is loud. The operator code-mixes, using English part names inside a vernacular sentence. And the vocabulary is domain specific, so "bearing," "spindle," and a six-character part number all have to survive. The axis is accuracy on domain vocabulary under realistic machine noise, followed by a spoken clarification when a consequential part number is uncertain.

**The scenario.** Imran supervises a knitting floor in Tiruppur. A machine starts making a sound he recognises as bad but cannot name. The OEM manual is a 400-page English PDF, the service engineer is a day away, and every hour of silence costs a shift. He stands next to the machine and describes the noise out loud in Tamil, using the English part names he knows.

**What you will need**
- Voice capture that works next to running machinery, with the noise floor as a designed condition not an accident
- Domain vocabulary handling for part names and alphanumeric part numbers spoken in code-mix
- Diagnosis grounded in a real OEM manual, in the system prompt rather than a vector database
- A visible refusal and spoken clarification path when a part name or number is uncertain
- Spoken response, because the operator's hands are busy and dirty
- A recorded set of noisy floor audio for testing, so you are not iterating in a quiet room
- Three tool calls: look up the fault against the manual text held in the system prompt, write the diagnosis with its cited manual section, raise a spares order when a confirmed part is implicated
- A stated number from your own noisy clips: part-name and part-number accuracy at realistic floor volume, and how many diagnoses the system declined rather than guessed
- One-pager: the workflow, the integration surface, what the build refuses to diagnose and where it tells the operator to stop the machine and wait for the engineer, a deploy-or-pilot verdict, and why Voice Experience is primary

**Your demo moment.** Play factory floor noise at realistic volume. A judge describes a fault in a mixed sentence with an English part number in it. The system gets the part number right and returns a cited diagnosis, then asks for the number again instead of guessing when the next clip is genuinely unclear.

**Scores on:** Sarvam parameter and Impact. **Weak on:** Creativity, unless the noisy domain-vocabulary test is real rather than clean speech with a sound effect added at demo time.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras, transcribing a Tamil fault description with English part names and a six-character alphanumeric part number in it, over a running knitting machine. This is where the depth goes and where the score is.
- **Supporting** Sarvam-30B for diagnosis against the manual text · Bulbul for the spoken answer and clarification, because his hands are dirty. Plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** A PWA with push to talk and large touch targets for gloved hands · a simple native shell if someone on the team already ships one · a laptop with an external mic carried to the floor, which is the fastest way to test the noise condition today
- **Backend** A small Node or Python service · Next.js route handlers · Convex functions · plain code with retry logic, doing the diagnosis lookup against the manual held in the system prompt rather than a vector database
- **Data** Convex · Supabase · SQLite · or none for a single-session demo, for transcripts, cited manual sections, confidence and refused part numbers
- **Comms** Telegram bot · Slack or Discord webhook · ntfy.sh, notifying the maintenance lead when a diagnosis suggests a part order
- **Mock or external** httpstat.us with `/random/200,500,503` and `?sleep=5000` to test a flaky shed connection mid-diagnosis · Beeceptor for a spares-order endpoint the diagnosis hands off to
- **Specific to this build** One real OEM service manual for a single named machine, as a PDF, in the system prompt. Manufacturers and manual archive sites publish these, find the one for a machine you can name rather than a generic maintenance guide. Plus 15 to 20 recordings of someone describing faults with actual machine noise behind them, made before you write any code.

**Know before you pick this.** Record 15 to 20 clips of someone describing faults with actual machine noise behind them, before you start. Building this in a quiet room and testing it on the floor at 3:30 is how this card fails.

---


## 04 ·
Multilingual video documentation for Indian SaaS

**Starter · domain · Dubbing**

> Turn an English product walkthrough into localised videos without translating the UI labels and technical terms users still see in English.

**Why this one.** The Dubbing axis is selective adaptation against a moving screen. You do not translate "webhook," "API key," "OAuth," or a button label that remains English in the product UI. Translate them and the narration becomes actively wrong because the learner is looking for a different label. The dubbed line also has to land while the named control is still on screen, so terminology, pronunciation and segment timing all have to hold together.

**The scenario.** Nikhil runs support at a Bengaluru SaaS company selling to small businesses in tier 2 and tier 3 towns. Adoption stalls after signup because every product walkthrough is in English. His source is a five-minute screen recording with English UI labels, code snippets and a narrator moving quickly between settings.

**What you will need**
- Ingest a real screen-recorded walkthrough and recover a timestamped transcript
- A protected-term list for code, identifiers and on-screen UI labels, with pronunciation guidance for the terms that remain English
- Segment-level adaptation that keeps each instruction inside the interval where its control is visible
- A stable named voice per target language, with three supported spoken languages rather than an unsupported coverage claim
- A reviewer view showing source and dubbed video side by side, protected terms highlighted and drift per segment
- One deliberately hard segment mixing prose, code, a UI label and a fast screen transition
- Three tool calls: read a source segment, render the dubbed segment per language, record a terminology or timing conflict against the glossary
- A stated number over the asset: protected-term accuracy, pronunciation review and worst segment drift in milliseconds
- One-pager: the workflow, the integration surface, publication rights, a deploy-or-pilot verdict, and why Dubbing is primary rather than treating translation or batch orchestration as a separate scoring branch

**Your demo moment.** Play the same thirty seconds in the source language and a target language. The narration keeps "API key" and the exact button label, pronounces both consistently and lands the instruction while the button is still visible. Then show the drift and terminology report for the full asset.

**Scores on:** Sarvam parameter and Job-to-be-done. **Weak on:** Impact, unless you can state a real activation or ticket-volume baseline.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam's Dubbing surface, or Saaras timestamped transcription plus Sarvam Translate and a stable named Bulbul voice, adapting each segment while English UI labels stay exact and the instruction remains aligned to the screen. This is where the depth goes and where the score is.
- **Supporting** Sarvam-30B for protected-term detection and constrained rewrites when a translated line overruns its visual segment. Plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Video upload, side-by-side source and dubbed players, a protected-term review and a per-segment drift table: Next.js · SvelteKit · or one HTML page with two video elements and a table
- **Backend** A local Node or Python pipeline driving ffmpeg · Next.js route handlers · Convex functions, doing segmentation, constrained adaptation and per-segment rendering
- **Data** Convex · Supabase · SQLite · or a JSON manifest beside the asset, for segments, protected terms, target tracks, review status and drift measurements
- **Comms** Slack webhook · Discord webhook · Resend · ntfy.sh, posting a summary when a render finishes with terminology or timing conflicts flagged
- **Mock or external** ffmpeg locally for cutting and remuxing. No downstream system is needed
- **Specific to this build** A screen recording you own with English controls, a code snippet and one quick transition. Lock a sixty-second demo cut before rendering the full asset in multiple languages.

---


## 05 ·
Pre-signing contract comprehension for small businesses

**Challenging · domain · Document Intelligence**

> Photograph a contract before you sign it and find out which clauses decide how badly this can go.

**Why this one.** Summarising a contract is easy and nearly useless. The axis is risk ranking: identifying the small number of clauses that determine downside, which are usually termination, exclusivity, indemnity, penalty, jurisdiction, and auto-renewal, and ordering them by what they actually cost this signer. The second axis is honest scope. This is not legal advice, the system has to say so, and it has to decline rather than guess when a clause references a schedule that is not in the photographed pages. Confident wrongness here is worse than silence, because someone signs on the strength of it.

**The scenario.** Meera is about to sign a distribution agreement for her food brand in Indore. Twelve pages, English, with a schedule referenced on page 4 that the other party has not sent. She has no lawyer on retainer and the counterparty wants it signed this week. She photographs all twelve pages.

**What you will need**
- Multi-page photographed contract ingestion, pages possibly out of order
- Clause identification and classification into the categories that carry downside
- Risk ranking with a plain-language statement of what each clause means for this signer
- Missing-reference detection, so a schedule referenced but not supplied is flagged rather than ignored
- Explicit non-advice framing and a refusal path on clauses it cannot parse
- Output in the signer's language, written and spoken
- Two contract types so the demo is not one template
- A stated number on ten contracts you labelled by hand: classification accuracy on the clause categories that carry downside, and how often a missing schedule was caught rather than ignored
- One-pager: the workflow, the integration surface, the non-advice boundary, what a signer must still take to a lawyer, and what happens to the contract images after the session, a deploy-or-pilot verdict, and why Document Intelligence remains primary even when the ranked list is also spoken in the signer's language

**Your demo moment.** A judge hands over a contract you have never seen with a schedule deliberately missing. The system ranks the three clauses that matter, and separately says it cannot assess a clause because the schedule it depends on was not provided.

**Scores on:** Job-to-be-done and Delight, since ranked risk beats a wall of summary. **Weak on:** Sarvam parameter unless the input is genuinely photographed rather than a clean PDF.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam Doc AI, extracting twelve photographed contract pages that may arrive out of order, including the page that references a schedule nobody sent. This is where the depth goes and where the score is.
- **Supporting** Sarvam-30B for clause classification, risk ranking and missing-reference detection · Mayura plus Bulbul for the signer's language. Plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Web app with multi-page camera capture and a ranked list that expands per clause · plain React with Vite · a single HTML page with a multi-file input and a printable ranked list, which is what Meera actually carries into the meeting
- **Backend** Next.js route handlers · a small FastAPI or Express service · Convex functions · localhost with a tunnel, doing page ordering, clause classification, the risk ranking and the refusal path
- **Data** Convex · Supabase · SQLite on disk · or none, hold one contract in memory for a single-session demo, for contracts, clauses, risk rankings and flagged missing references. Page images go to Convex file storage · Supabase Storage · the local filesystem
- **Comms** Resend · Loops · Telegram bot, delivering the ranked risk list so it survives the meeting
- **Mock or external** No external system needed · Beeceptor if you want the ranked risk list posted into a shared deal folder
- **Specific to this build** Ten real template agreements of one type, redacted, printed and photographed. A distribution agreement, a rental agreement or a home loan sanction letter all work, pick the one you can source ten of. Deliberately remove a referenced schedule from one of them before the demo.

**Know before you pick this.** To reach the top bands the input has to be photographed or scanned, not a text-layer PDF. This card also covers rental agreements and home loan agreements, so pick whichever document you can source ten real examples of.

---


## 06 ·
Section 138 notice drafting for cheque bounces

**Challenging · domain · Voice Experience**

> Describe what happened in your own words and get a legally correct demand notice, or a clear reason why one cannot be drafted yet.

**Why this one.** The axis is mapping a lay narration onto a legal template that has required elements, and refusing to draft when an element is missing. A valid demand notice needs specific facts: the cheque, the date, the amount, the reason for return, the date of return intimation, and the underlying liability. A trader telling the story will supply four of those six and skip the two that matter. A system that drafts anyway produces a document that fails, and the person relying on it loses the remedy. So the product is really a structured interview that will not proceed until the record is complete.

**The scenario.** Ganesh supplies auto parts in Aurangabad. A customer's cheque has come back and he has the return memo from his bank in his hand. He does not know the notice window is short, does not know what the notice must contain, and cannot afford a lawyer for something this size. He explains what happened in Marathi.

**What you will need**
- Voice intake that lets the trader narrate freely rather than filling a form
- Required-element checklist tracked across the conversation, with the interview driving toward the gaps
- Hard refusal to draft while a required element is missing, naming which one and why it matters
- Extraction of the cheque details from a photographed return memo, to avoid asking for what is already on paper
- Generated notice in correct legal English, with a plain-language version in the trader's language so they know what they are sending
- Deadline stated explicitly, counted from the right event
- Three tool calls: read the cheque details off the photographed return memo into the checklist, generate the notice once every required element is present, log a refusal to draft naming the element that is missing
- A stated number over ten narrations, several deliberately incomplete: how often the missing element was named correctly, and how often the system drafted when it should have refused
- One-pager: the workflow, the integration surface, the non-advice boundary and what the trader must still take to a lawyer before anything is sent, a deploy-or-pilot verdict, and why you declared Voice Experience rather than Document Intelligence when the return memo is read from a photograph

**Your demo moment.** A judge narrates a bounce and deliberately omits the return intimation date. The system does not draft. It names the missing element, explains why the notice fails without it, and asks for it. Supply it and the notice appears.

**Scores on:** Job-to-be-done and Memory and Context, since the checklist has to survive a rambling conversation. **Weak on:** Delight, and be careful of Impact if you cannot state what the alternative costs.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras, transcribing Ganesh telling the story his own way in Marathi, unstructured, so the interview can chase the missing element instead of handing him a form. This is where the depth goes and where the score is.
- **Supporting** Sarvam Doc AI for the photographed bank return memo, so you do not ask for what is already on paper · Sarvam-30B for element tracking and drafting · Mayura for the plain-language version he can read. Plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Web app with push to talk plus a photo upload for the return memo · a phone number via Twilio or Exotel if you want the intake to be a call he makes · a single HTML page with a record button and a file input
- **Backend** Sarvam Agents if you want the interview state checkpointed across a dropped session · Convex functions · a small Node or Python service holding the checklist as a state machine, which is what actually enforces the refusal to draft
- **Data** Convex · Supabase · SQLite · or none, hold the checklist in memory since one case is one session, for cases, element checklist state and drafted notices
- **Comms** Resend with the notice as an attachment and the plain-language version in the body · Telegram bot sending the same PDF · Loops
- **Mock or external** No external system needed · Beeceptor if you want the drafted notice logged into a case tracker
- **Specific to this build** A real Section 138 demand notice format as your template, and a real bank cheque return memo to photograph. Take the notice window and the required elements from the statute text itself, on India Code (indiacode.nic.in), not from the model, and not from a blog.

**Know before you pick this.** Do not assert legal deadlines you have not checked against a current source. Get the notice format and the window from something authoritative before you build the copy around it.

---


## 07 ·
Supplier verification calls for large orders

**Challenging · domain · Voice Experience**

> Before you send the money, an agent calls the supplier and comes back with the inconsistencies.

**Why this one.** The axis is cross-turn inconsistency detection. A supplier who is not what they claim will contradict themselves across a ten-minute call: the address changes, the years in business shift, the answer about who owns the unit does not match the answer given six turns earlier. Catching that requires holding every earlier claim while parsing the current one, in the supplier's language, and the whole call is worthless if the agent forgets turn two by turn eight. This is a Memory and Context card wearing a voice card's clothes.

**The scenario.** Aditya sources fabric for a garment unit in Surat and is about to place his largest order with a supplier he found online. He has a GSTIN, a phone number, and photographs of a unit that may or may not be theirs. He wants someone to call and ask the obvious questions before the advance goes out.

**What you will need**
- Outbound call in the supplier's likely language, opening without accusation
- A question set designed so several questions triangulate the same fact from different angles
- Cross-turn consistency checking, comparing every answer against every earlier answer
- Contradiction report naming the conflicting claims with the exact language quoted
- Evasion detection, distinct from contradiction, for questions answered without being answered
- Structured verdict: consistent, inconsistent with specifics, or unreachable
- Three tool calls: check a stated fact against the mocked business registry, write each claim to the ledger with the turn it came from, write the final verdict record
- A stated number over your scripted calls: how many planted contradictions were caught, and how many contradictions were raised that were not real
- One-pager: the workflow, the integration surface, what the report asserts about a named supplier, what it only quotes, and what the person on the call is told about being recorded, a deploy-or-pilot verdict, and why Voice Experience remains primary even when the whole call runs in the supplier's own language

**Your demo moment.** A judge plays a supplier and contradicts themselves once, early and subtly, then talks for another five turns. The report catches it and quotes both statements side by side.

**Scores on:** Memory and Context, decisively. **Weak on:** Creativity, and Impact needs a real order value to be meaningful.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam-30B, comparing every current answer against every claim made earlier in the call and quoting both sides of a contradiction. This is where the depth goes and where the score is, which is unusual for a voice card and is the point of this one.
- **Supporting** Saaras for transcription in the supplier's language, feeding the claim ledger · Bulbul for the outbound voice that asks without accusing. Plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Web app to enter a supplier, trigger the call and read the report · Twilio, Exotel or Plivo to place the call · a terminal script that dials and prints the contradiction report side by side, which is the whole demo
- **Backend** Sarvam Agents for per-turn state you can reopen after the call · Convex functions · a small FastAPI or Express service holding the claim ledger · plain code with a state machine
- **Data** Convex · Supabase · Postgres direct · SQLite, for suppliers, per-turn claims with the turn number, and contradiction records with both quotes. Keep the claims, the report is built from them
- **Comms** Resend · Loops · Telegram bot · Slack webhook, delivering the contradiction report before Aditya releases the advance
- **Mock or external** Beeceptor · Mockoon · WireMock Cloud for a business registry to check stated facts against · httpstat.us if you want the registry lookup to time out mid-call
- **Specific to this build** A written contradiction script with one planted inconsistency, subtle enough to impress and verifiable by a judge in ten seconds, plus a GSTIN and unit photographs for the supplier you are pretending to check.

**Know before you pick this.** Write your contradiction script before you build. The demo lives or dies on whether the planted inconsistency is subtle enough to be impressive and clear enough for a judge to verify in ten seconds.

---


## 08 ·
Financial report explanation for small business owners

**Starter · domain · Document Intelligence**

> Photograph your own balance sheet and finally find out whether you can take money out of the business.

**Why this one.** The axis is number fidelity under Indian accounting conventions. A scanned P&L uses lakhs and crores, brackets for negatives, Schedule III headings, and a column layout that a naive extraction will silently transpose. Getting a figure wrong here is not a cosmetic error, because the owner is about to make a decision on it. The second axis is answering the question actually being asked. The owner does not want the balance sheet explained, they want to know whether they can pay themselves this month, and the product is the translation between those two things.

**The scenario.** Rekha runs a small chemicals trading business in Vijayawada. Once a year her CA walks her through a P&L and balance sheet in forty minutes, she nods, and she leaves understanding none of it. She photographs six pages of the signed statements and wants to ask plain questions of them.

**What you will need**
- Multi-page scanned financial statement extraction with column structure preserved
- Correct handling of lakhs and crores, bracketed negatives, and Schedule III headings
- Number verification, so extracted totals are checked against their own subtotals and mismatches surface
- Question answering in plain language, in the owner's language, on top of the extracted figures
- Refusal on any figure the extraction is not confident about, rather than answering from a bad number
- Three plain questions the demo answers: can I take money out, where did the money go, and am I more or less exposed than last year
- A stated number on your own scanned pages: figure-level accuracy against the printed statement, how many subtotal checks failed, and what the system did when one did
- One-pager: the workflow, the integration surface, what you store of a business's financials, who can see them, and what the build refuses to answer when a figure failed its own subtotal check, a deploy-or-pilot verdict, and why you declared Document Intelligence rather than Voice Experience when the answers are spoken in the owner's language

**Your demo moment.** A judge asks "can I take money out of this business" of a scanned statement the system has never seen. It answers in plain language, cites the two figures it used, and the subtotal check confirms those figures add up.

**Scores on:** Delight and Job-to-be-done. **Weak on:** Creativity. The self-verifying arithmetic is your differentiator, so make it visible.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam Doc AI, extracting six scanned statement pages with the column structure intact, lakhs and crores read correctly, bracketed negatives kept negative and Schedule III headings not transposed. This is where the depth goes and where the score is.
- **Supporting** Sarvam-30B for the subtotal verification pass and the plain-language answers · Mayura plus Bulbul for Rekha's language. Plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Web app with multi-page capture and a question box over the extracted figures · plain React with Vite · a notebook or a terminal REPL over the extracted table, if you would rather spend the four hours on number fidelity than on layout
- **Backend** Next.js route handlers · a small FastAPI or Express service · Convex functions · Cloudflare Workers, running the subtotal check and the refusal on any figure the extraction is not confident about
- **Data** Convex · Supabase · SQLite · or none, hold the extracted line items in memory for a single-session demo, for statements, line items with confidence and the verification results
- **Comms** Resend · Loops · Telegram bot, sending the answers with the cited figures attached
- **Mock or external** No external system needed · Beeceptor if you want the answers written back into an accounting tool
- **Specific to this build** Real signed statements from a small listed company. Every listed company publishes the audited annual report on its own investor relations page, take one, print two pages and photograph them, because the printed scan is the input this card is scored on. Do not feed it the original text-layer PDF.

**Know before you pick this.** To reach the top bands the input has to be photographed or scanned, not a text-layer PDF. This card also covers annual report explanation for retail investors, so pick the reader you can describe most specifically.

---


## 09 ·
Handwritten wage register digitisation for informal labour

**Challenging · domain · Document Intelligence**

> Photograph a handwritten wage and attendance register, get structured records out, and have every unreadable cell escalated instead of filled.

**Why this one.** Doc AI's hard edge is handwriting and scans, and this is the purest handwriting case in the library: several hands on one page, struck-through corrections, overwritten numbers, faded ink, phone camera at an angle. The optimisation axis is refusal. A register that silently invents a wage figure is not a slightly worse product, it is a liability, and the person harmed by the invented number is the worker least able to contest it. The top bands go to the team whose system reliably says it cannot read a cell, and whose confidence scores hold up when a judge tests them.

**The scenario.** Harpreet runs a hosiery unit in Ludhiana with about 40 workers, most of them seasonal migrants. His supervisor keeps the muster roll in a hardbound notebook, in a mix of Gurmukhi and English numerals, with corrections struck through and rewritten in the margin whenever a shift changes. When a worker disputes a payment, Harpreet has a notebook and no way to answer "what did this person earn across March." He photographs six pages on his phone.

**What you will need**
- Camera capture or upload for photographed register pages
- Doc AI extraction into structured rows: worker, days present, rate, amount, period
- Per-field confidence with a stated threshold and an explicit refusal state
- Escalation queue that shows the cropped cell image, not the whole page
- Two calls out: fetch the prior period's rows for the same worker to reconcile against and surface contradictions, and post an unreadable cell into the escalation queue
- One page held back unseen, for the demo
- Ground truth on 3 pages so you can state real accuracy instead of a vibe
- One-pager: the workflow, the integration surface, provenance (which fields are machine-read, which human-confirmed, which refused, and who carries the loss when a wage figure is read wrong), a deploy-or-pilot verdict, and why you declared Document Intelligence rather than another branch

**Your demo moment.** A judge hands over a scanned page the system has never seen. It extracts the rows, and on the one cell the judge can see is genuinely illegible it declines and names the field instead of producing a plausible number.

**Scores on:** Sarvam parameter and Job-to-be-done. **Weak on:** Delight, unless the escalation flow is genuinely one-tap.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam Doc AI (docs.sarvam.ai) for handwritten Gurmukhi and Devanagari extraction from photographed register pages. This is where the score is. The refusal state that carries the axis, the threshold and the decision to decline a cell, is your own code wrapped around the response, not something Doc AI hands you.
- **Supporting** Sarvam-30B for same-worker matching and plain-language contradiction explanations, as plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Camera capture plus file upload, and `<input type="file" capture="environment">` is the entire capture feature · Next.js or React with Vite · a plain HTML page with a fetch call is enough. One screen plus a review panel for escalated cells, and the review panel is where the interface time belongs.
- **Backend** Convex functions (convex.dev) for thresholds, the refusal state and reconciliation · Next.js route handlers · a small FastAPI or Express service · Cloudflare Workers (developers.cloudflare.com/workers) · localhost plus a tunnel (beeceptor.com/local-tunnel)
- **Data** Convex (convex.dev) for extracted rows, per-field confidence and the refusal queue, with Convex file storage for page images · Supabase Postgres plus Supabase Storage (supabase.com) · SQLite plus the local filesystem · Cloudflare R2 or S3 if all you need is somewhere to put images
- **Comms** Resend (resend.com) emailing the supervisor the cells needing a human read · Telegram bot (core.telegram.org/bots) · Slack webhook (api.slack.com/messaging/webhooks) · or the in-app escalation queue on its own
- **Mock or external** Mockoon (mockoon.com) or Beeceptor (beeceptor.com) for the prior-records system you reconcile against · httpstat.us to make that lookup slow or failing while a page is mid-extraction
- **Specific to this build** Real photographed register pages, varied on purpose: two with multiple hands, two with struck-through corrections, one faded, one skewed, one held back unseen. Write them yourself in two different pens if sourcing fails.

**Know before you pick this.** You need 10 to 15 photographed handwritten pages before 11:30, deliberately varied: two with multiple hands, two with struck-through corrections, one faded, one skewed. If you do not have them you will lose the morning sourcing them. Write them yourself in two different pens if you have to.

---



## 10 ·
Regional-language customer support for consumer brands

**Starter · domain · Voice Experience**

> Support in eight languages that resolves the same complaint the same way in all eight.

**Why this one.** The axis is cross-language consistency of outcome, not tone. The same complaint arriving in Bengali, Marathi, and Kannada has to reach the same resolution, the same refund decision, and the same escalation threshold. Most multilingual support fails here: the English path gets a refund and the Odia path gets an apology, because the intent classifier is weaker in the language with less training data. That inconsistency is the product problem, and demonstrating that you fixed it is a better demo than any tone comparison.

**The scenario.** Priya runs customer experience for a home care brand selling across India. She can staff English and Hindi. Complaints arriving in Bengali or Kannada either go unanswered or get routed to whoever on the team happens to speak something close. She has a resolution policy document and no way to apply it consistently.

**What you will need**
- Inbound support in at least four languages, detected rather than menu-selected
- A single resolution policy in the system prompt, applied identically across languages
- Consistency harness: the same five complaints, scripted in every supported language, asserting identical outcomes
- Escalation threshold that fires at the same point regardless of language
- Three tool calls: check entitlement against the mocked order and returns system, write the ticket with the language recorded so drift can be audited later, raise the escalation
- Refusal path for languages you do not support, stated clearly rather than half-served
- A stated number from the harness: how many of the same five complaints reached an identical resolution and an identical escalation decision in every language, and where they diverged
- One-pager: the workflow, the integration surface, who is allowed to approve a refund, what the agent decides alone, and what a customer is told when their language is not supported, a deploy-or-pilot verdict, and why Voice Experience remains primary even when the same policy has to hold in every language

**Your demo moment.** Run the same complaint in four languages back to back. All four reach the same resolution and the same escalation decision, shown side by side on one screen.

**Scores on:** Sarvam parameter and Job-to-be-done. **Weak on:** Creativity, since multilingual support is an expected build. The consistency harness is what lifts it.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras, detecting the language on the first utterance and transcribing at equal quality across four or more of them, because the drift you are trying to eliminate starts in the transcript. This is where the depth goes and where the score is.
- **Supporting** Sarvam-30B for intent classification and applying the one resolution policy · Bulbul for the spoken reply. Plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Phone via Twilio, Exotel or Plivo · a browser voice widget using the mic · a scripted harness that plays the same five recorded complaints in every language and prints the four outcomes side by side, which is the demo that actually scores here
- **Backend** Convex functions · Next.js route handlers · a small FastAPI service · Sarvam Agents if you want per-call run state, holding the single resolution policy in the system prompt and the escalation threshold in one place so it cannot diverge per language
- **Data** Convex · Supabase · SQLite on disk, for tickets with the language recorded, resolutions and the consistency test results. Keep these, the audit trail for drift is the product
- **Comms** Resend for the resolution confirmation · Slack or Discord webhook for escalations · Telegram bot · ntfy.sh
- **Mock or external** Beeceptor · Mockoon for the order and returns system you check entitlement against · httpstat.us with sleep to see what the agent says while the entitlement check hangs
- **Specific to this build** Five complaint scripts recorded by real speakers in each language you claim to support, before you build the agent. Check the coverage split first: Sarvam Translate and Saaras v3 each cover 23 languages, while Bulbul v3 produces 11, so confirm every demo language has both an ear and a voice.

**Know before you pick this.** Script your five test complaints in every language before you build the agent. The consistency harness is the score, and it is the thing teams skip because it produces no visible UI.

---


---

# Public Services


## 11 ·
Voice-guided government form completion

**Challenging · domain · Voice Experience**

> Speak your answers in your own language and get a correctly filled official form, with every name and place spelled the way the form requires.

**Why this one.** The axis is transliteration fidelity on proper nouns spoken aloud. Everything else on a government form is a bounded choice, a date, or a number. The part that gets forms rejected at the counter is the part no model can paraphrase: a person's name, their father's name, a village, a ward, a bank branch, all of which have to land in the exact script and exact spelling that matches the identity document already on record. This is not translation and it is not transcription, it is a third thing, and Sarvam ships a transliteration surface specifically for it. The top bands go to the team whose spoken "Sarita Devi, Chandrahati, Muzaffarpur" reaches the form in the same characters as her Aadhaar, and whose system offers spelling variants for confirmation rather than picking one silently.

**The scenario.** Sarita Devi needs a caste certificate renewed and is standing outside a block office in Muzaffarpur with a printed form, her Aadhaar card, and a passbook. The shop next to the office fills forms for a fee, in the range of ₹100 to ₹500 depending on the form, and gets her mother's name spelled differently every time. She cannot read the English field labels, but she knows every answer by heart.

**What you will need**
- Voice intake in the applicant's language, one field at a time, no on-screen form to read
- Transliteration of names and place names into the script the form demands, not translation of them
- Variant confirmation on every proper noun: offer two or three spellings and let the applicant pick against the ID they are holding
- Three tool calls: read the spelling off a photograph of the applicant's existing ID so the record becomes the authority instead of a guess, write each confirmed field to the application, submit the filled form to the mocked endpoint
- Field-level validation, so a date or a number that cannot be valid is caught before submission
- A filled, printable output that matches the real form layout
- Two genuinely different forms, so the demo is not one hardcoded template
- A stated number on twenty spoken names and places: how many reached the form character-identical to the ID, and how often the applicant chose a variant other than your first guess
- One-pager: the workflow, the integration surface, what you keep of an applicant's identity document, what you discard once the form prints, and who can see a spelling the applicant rejected, a deploy-or-pilot verdict, and why you declared Voice Experience rather than Document Intelligence when the ID is read from a photograph

**Your demo moment.** A judge speaks a name and a village with an awkward spelling, plus an ID photo showing how it is actually written. The filled form carries the ID's spelling, character for character, and the system shows the alternatives it considered rather than pretending there was only one.

**Scores on:** Job-to-be-done and Sarvam parameter. **Weak on:** Creativity, because form filling is the first idea anyone has. The transliteration confirmation loop is the only thing that separates you.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Mayura transliteration, putting spoken names and place names into the script the form demands and generating the spelling variants the applicant confirms against. This is where the score is.
- **Supporting** Saaras for the field-by-field vernacular intake, Sarvam Doc AI for reading the spelling off the photographed ID, Sarvam-30B for field validation and the confirmation prompts, Bulbul for reading each captured answer back. All plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Mobile web, push to talk, one field at a time, large type, plus a camera step for the ID: Next.js · React with Vite · a single HTML page with a script tag, a record button and a file input set to capture, which is the whole interface this card needs
- **Backend** Convex functions · Next.js route handlers · a small FastAPI or Express service · localhost with a tunnel, running the intake loop, the variant offer and the form fill
- **Data** Convex · Supabase · SQLite on disk · or none, hold it in memory, for applications, per-field values, the accepted spelling and the variants offered, since one filled form is a single session
- **Comms** Resend · Telegram bot · ntfy.sh, delivering the filled form as an attachment plus a copy the applicant can show at the counter
- **Mock or external** Beeceptor · Mockoon · WireMock Cloud, for the mocked submission endpoint
- **Specific to this build** Two real form layouts, redacted, taken from the issuing authority's own published form rather than retyped from memory, so the field set and the required script are the real ones.

**Know before you pick this.** Sarvam ships a Government Scheme reference agent, so this card starts at the creativity floor and you have to beat the cookbook deliberately. The way you beat it is the transliteration and confirmation loop, not the form filling. Also: do not assert what any specific form or certificate legally requires. Source the form layout and its mandatory fields from the issuing authority before you build copy around them.

---


## 12 ·
Court order interpretation for litigants

**Challenging · domain · Document Intelligence**

> Photograph the order you were handed and find out what the court actually directed, what it merely recorded, and what you have to do next.

**Why this one.** The axis is attribution inside a scanned legal document: separating what the court directed from what a party merely claimed. An order is mostly other people's assertions. The petitioner submitted, the respondent contended, the counsel relied on, and then somewhere near the end, in one or two sentences, the court actually ordered something. A summariser flattens all of it into one voice and hands the litigant a paragraph that says the opposite of the outcome. The top bands go to a system that tags every proposition with who advanced it, isolates the operative direction, and states next steps only from that direction. Same axis applies to a judgment, which is longer and has more submissions to wade through, so pick whichever document you can source.

**The scenario.** Ashok Verma has been to a district court in Kanpur four times over a property dispute and comes out each time with a stapled order he cannot read. The paper is a photocopy of a photocopy, typed in dense English with case-law citations, a seal across one corner, and a handwritten date at the top. His neighbour reads it and tells him he has won. His clerk reads it and tells him he has to appear again.

**What you will need**
- Camera capture for a photocopied order with a seal, skew and show-through from the reverse side
- Extraction that preserves paragraph structure, because the operative part is positional
- Attribution tagging: court direction, petitioner submission, respondent submission, recital of earlier proceedings
- Isolation of the operative direction, quoted verbatim before anything is paraphrased
- Next-steps extraction derived only from the operative part: what to do, by when, before which forum
- Plain-language explanation in the litigant's language, written and read aloud
- A refusal state for orders where the operative part cannot be located confidently, instead of guessing the outcome
- A stated number over ten documents you tagged by hand, ideally including one judgment so the demo generalises: paragraph-level attribution accuracy, and how often the operative direction was located or honestly refused
- One-pager: the workflow, the integration surface, provenance, meaning which paragraphs the machine attributed, which a human confirmed and which it refused, plus the non-advice boundary before the litigant acts on next steps, a deploy-or-pilot verdict, and why Document Intelligence remains primary even when the explanation is also translated and read aloud

**Your demo moment.** A judge hands over an order the system has never seen where an early paragraph records a claim the court later rejects. The system quotes the operative direction, labels the rejected claim as a submission rather than an outcome, and explains in the litigant's language what has to happen next.

**Scores on:** Sarvam parameter and Job-to-be-done. **Weak on:** Delight, and Impact unless you can describe what the litigant currently pays for a wrong reading.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam Doc AI, extracting from the photocopied order with paragraph structure preserved, because the operative part is positional. This is where the score is.
- **Supporting** Sarvam-30B for attribution tagging and operative-part isolation, Mayura plus Bulbul for the litigant's language. All plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Multi-page camera capture, then a result with the operative quote pinned at the top and an audio play button: Next.js · SvelteKit · plain HTML with a multiple file input and a play button, which is enough
- **Backend** Convex functions · Next.js route handlers · a small FastAPI or Express service · a terminal script that takes a filename and prints the tagged paragraphs, which is a legitimate 4pm demo for this card
- **Data** Convex · Supabase · SQLite on disk · or none, hold it in memory, for documents, per-paragraph attribution labels, operative quotes and the refusal queue; page images to Convex file storage, Supabase Storage, R2 or just the local filesystem
- **Comms** Resend · Telegram bot · Slack or Discord webhook, sending the plain-language version with the operative paragraph quoted at the top
- **Mock or external** No external system to mock. httpstat.us with sleep if you want a slow-extraction path to talk over
- **Specific to this build** Eight to ten real published orders and judgments, redacted. Indian Kanoon (indiankanoon.org) is the fastest place to pull real orders and judgments in bulk. Print two of them and photograph the printout, so you get genuine skew and show-through instead of a text-layer PDF.

**Know before you pick this.** To reach the top bands the input has to be a photographed or scanned document, not a text-layer PDF. Get eight to ten real orders before 11:30, deliberately including one photocopy with show-through and one with a handwritten annotation. Do not state limitation periods or appeal windows as fact in your output copy unless you have sourced them authoritatively, and say what forum the next step goes to only if the order itself says so.

---


## 13 ·
Voice-drafted police complaints

**Challenging · domain · Voice Experience**

> Describe what happened in your own words and walk in with a written complaint that names the offence, with your account preserved exactly as you told it.

**Why this one.** The axis is separation of the citizen's account from the system's characterisation. The facts a complainant narrates are evidence and must survive to paper unaltered, in their own words, including the parts that seem irrelevant. The legal category is a separate layer added on top, visibly labelled as the system's inference, never merged into the narration. Systems that blur the two produce a complaint that reads well and misstates what the person actually said, which is worse than no complaint at all because it is now on record. The build that scores is the one where a judge can point at any sentence and see whether the complainant said it or the machine added it.

**The scenario.** Kiran Sahu has had a neighbour repeatedly damage her boundary wall in Raipur and has been turned away twice, once because she described it as a fight and once because she could not say what offence she was reporting. She has photographs on her phone, a date she is sure of, and a version of events she has now told four people. She talks for six minutes in Chhattisgarhi-inflected Hindi.

**What you will need**
- Free narration intake, no form, no interruption until the person stops talking
- Verbatim preservation of the complainant's factual account, in their words, as the body of the complaint
- A separately labelled characterisation layer: what category of offence this appears to describe, marked as inference
- A gap check that asks only for facts a complaint needs and cannot infer, such as date, place, and who was present
- Generated complaint in formal English plus a read-back in the complainant's language so they can confirm before signing
- An explicit statement that the legal category is an aid, not a determination, printed on the document
- Photo attachments listed on the complaint rather than described in it
- A stated number on two recorded narrations: what share of the complainant's factual sentences survived word for word into the complaint, and how many system-written sentences ended up inside the narration block rather than the labelled inference block
- One-pager: the workflow, the integration surface, how the recording and the verbatim account are stored, who can see them, and what the build refuses to characterise as an offence, a deploy-or-pilot verdict, and why Voice Experience remains primary even when a formal English document comes out of a vernacular narration

**Your demo moment.** A judge narrates an incident with one detail that sounds trivial. The generated complaint still contains that detail, in the judge's own phrasing, and the offence category sits in a clearly separate block that the judge can see was added by the system.

**Scores on:** Job-to-be-done and Memory and Context, since a six-minute unstructured narration has to survive intact. **Weak on:** Delight, and Creativity if you present it as a form filler rather than a record-integrity tool.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras, transcribing a six-minute unstructured vernacular narration with restarts and self-corrections so the complainant's own words survive to paper. This is where the score is.
- **Supporting** Sarvam-30B for offence categorisation and the gap check, Mayura for the formal English draft and the vernacular read-back, Bulbul for reading it aloud. All plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** One long push-to-talk recording, then a review screen with the narration and the inference block visually separated: Next.js · React with Vite · a single HTML page using MediaRecorder and two columns, which is genuinely enough here
- **Backend** Convex functions · Next.js route handlers · a small FastAPI or Express service · localhost with a tunnel
- **Data** Convex · Supabase · SQLite on disk · or none, hold it in memory, for complaints, the verbatim narration, inference labels and attachment references; audio and photos to Convex file storage, Supabase Storage or the local filesystem
- **Comms** Resend · Telegram bot · ntfy.sh, delivering the complaint as an attachment with the read-back text in the body
- **Mock or external** No external system to mock
- **Specific to this build** A real complaint format as your template, plus two full six-minute narrations recorded before you build, one of them containing a mid-narration self-correction, so the input is not improvised on stage.

**Know before you pick this.** Do not name statute sections or assert what any offence legally requires unless you have sourced it authoritatively. Write the brief so the behaviour is the point: the demo lands on account-versus-inference separation, not on legal accuracy. If you want a section reference in the output, source it before publishing and label it as a suggestion.

---


## 14 ·
Voice-first RTI application drafting

**Starter · domain · Voice Experience**

> Say what you want to know and get a filed-ready information request that asks one answerable question of the right office.

**Why this one.** The axis is specificity tightening. People arrive with a grievance, and a grievance is not an information request. "The road has not been repaired" is unanswerable. "Provide copies of work orders issued for road repair in ward 14 between these dates" is answerable, and the difference between the two is a short conversation that most drafting tools skip. The system's job is to run that narrowing loop in the applicant's own language, refusing to ship a question that asks for an opinion, a reason, or a promise, and to name the office that actually holds the records. This is a small build with one hard behaviour in it, which is why it is a starter card that can still reach high bands.

**The scenario.** Mahendra Bishnoi has watched a stretch of road in Jodhpur get dug up and abandoned three times in two years. He knows what he wants: to know who was paid to do it. He does not know which department holds the records, does not want to write in English, and has twice started a draft and given up. He describes the road and the digging out loud in Marwari-inflected Hindi.

**What you will need**
- Voice intake of a grievance, with no expectation that the user knows what an information request is
- A narrowing loop that converts the grievance into one or more requests for specific records
- A rejection rule that refuses to include questions asking why, or asking the office to justify itself
- Two tool calls: look up the authority that actually holds the records in your own directory, write the finished application with the narrowing history attached, and show the routing reasoning so the applicant knows why it goes where it goes
- Generated application in the required format and language, plus a spoken summary of what was asked
- A tightening comparison the demo can show: the vague version, and the version that will actually get an answer
- A stated number over ten grievances: how many became answerable requests for specific records, and how many candidate questions your answerability rule threw out
- One-pager: the workflow, the integration surface, the procedural boundary, meaning which fees, timelines and appeal routes you assert and which the applicant must confirm at the office, a deploy-or-pilot verdict, and why Voice Experience remains primary even when the output is a formal drafted application

**Your demo moment.** A judge describes a vague complaint out loud. The system pushes back once, asks the one clarifying question that makes it answerable, and produces a request naming specific records and a specific office, with the before and after shown side by side.

**Scores on:** Job-to-be-done and Delight, because the narrowing loop is visibly the product. **Weak on:** Sarvam parameter, since the model work here is lighter than on the document cards. Make the loop rigorous or this stays mid-band.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam-30B, running the narrowing loop, the answerability rejection rule and the department routing with its reasoning shown. This is where the score is.
- **Supporting** Saaras for the vernacular intake, Mayura for the formal draft, Bulbul for the spoken summary. All plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Push to talk, a short conversational loop, then a printable application: Next.js · SvelteKit · a single HTML page with a record button and the browser's own print dialog, which is the entire printable path
- **Backend** Convex functions · Next.js route handlers · a small FastAPI or Express service · plain code with retry logic, since this is a three-step loop and needs no orchestration framework
- **Data** Convex · Supabase · SQLite on disk · or none, hold it in memory, for applications, the narrowing history showing each version of the question, and routing decisions
- **Comms** Resend · Telegram bot · ntfy.sh, sending the application to the applicant plus a copy on their phone
- **Mock or external** Beeceptor · Mockoon · WireMock Cloud, for the mocked directory of public authorities you route against
- **Specific to this build** A directory of public authorities you assemble yourself, ten to fifteen entries, each with the subject it actually holds records for, since the routing reason is the scored part. Name the authority in your output rather than printing a portal address you have not opened.

**Know before you pick this.** Do not assert fees, timelines, appeal routes, or what an authority is obliged to answer unless you have sourced them. The demo should stand entirely on the narrowing behaviour, with any procedural figure marked as needing verification before publishing.

---


## 15 ·
Pension continuation calls for elderly claimants

**Beast · domain · Voice Experience**

> An outbound call that reaches an elderly pensioner before their annual verification lapses, and gets through the conversation at their pace.

**Why this one.** The axis is intelligibility with elderly speakers, which is a distinct engineering problem from accent or code-mixing. The speech is quieter, slower, and full of long mid-sentence pauses that a normal endpointer reads as a finished turn, so the agent talks over the person and the call collapses. Add hearing loss, so the agent has to repeat without sounding like a loop, and add the most common real event on these calls: halfway through, a grandson takes the phone and answers in a different voice and often a different language. The top bands go to the team that tunes turn-taking for slow speech and handles the proxy handover without losing what the pensioner already said. Every November lakhs of pensions freeze over a missed annual life certificate, and the reason is almost never refusal, it is that nobody reached the person in a way they could follow.

**The scenario.** Bhargavi is seventy-nine and lives alone in Thrissur. Her pension is the only money that arrives. Every year a verification step has to be completed and every year she finds out it lapsed when the money stops. She takes the call on a landline handset held slightly away from her ear, speaks Malayalam slowly, pauses in the middle of sentences to think, and midway through hands the phone to her grandson.

**What you will need**
- Outbound calling from a list of claimants with a due verification
- Endpointing tuned for long mid-sentence pauses, so silence is not treated as the end of a turn
- Repetition that rephrases rather than replays for hearing difficulty, and barge-in that never talks over a slow speaker
- Proxy handover detection, so a second speaker taking the phone is recognised and the captured state carries over
- Slower, louder speech output with short sentences and one question per turn
- Three named exits: verification steps confirmed and understood, needs an in-person visit arranged, unreachable after retries
- Two tool calls: read the claimant's verification status before the call, write the outcome per claimant with the transcript kept so a family member can be told what was said
- A stated number on your recordings of older speakers: how often a mid-sentence pause was wrongly treated as the end of a turn, and how many turns the agent talked over
- One-pager: the workflow, the integration surface, what you say to a proxy who takes the phone, what the build refuses to confirm as done on the pensioner's behalf, and how the transcript is stored and shared with family, a deploy-or-pilot verdict, and why Voice Experience remains primary even though the claimant list is also a queue

**Your demo moment.** A judge takes the call, speaks slowly with a five-second pause in the middle of an answer, then hands the phone to a second person who continues in a different language. The agent waits through the pause, does not restart, follows the handover, and finishes with a correct outcome written per claimant.

**Scores on:** Sarvam parameter and Impact. **Weak on:** Creativity, since outbound reminder calls are a familiar shape. The pause tolerance and the handover are the whole card.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras streaming with endpointing tuned for slow, quiet, disfluent speech, so a long mid-sentence pause is never read as the end of a turn. This is where the score is.
- **Supporting** Bulbul for slower paced output, Sarvam-30B for handover detection, state carry-over and exit classification. All plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** An outbound phone call and no screen at all: Twilio · Exotel · Plivo, or LiveKit / Pipecat / the Sarvam streaming APIs directly if you want hands-on control of endpointing and barge-in. Exotel is usually less friction on Indian numbers, and one number pointed at a webhook is the whole interface
- **Backend** Convex functions · a small FastAPI or Express service handling the telephony webhooks · Sarvam Agents if you want a call you can reopen from a checkpoint · plain code with a small state machine, which is enough for three exits
- **Data** Convex · Supabase · SQLite on disk · or none, hold it in memory, for claimants, per-turn transcripts, speaker changes and outcomes; the claimant queue can be a hardcoded array for the demo
- **Comms** Resend · Telegram bot · Slack webhook · ntfy.sh, sending the family contact a summary of what the pensioner was told, or a Sarvam TTS callback over the same telephony line if that contact has no email
- **Mock or external** Beeceptor · Mockoon · WireMock Cloud for the mocked verification status system you read and write; httpstat.us with sleep for a write that hangs mid-call
- **Specific to this build** Two or three recordings of genuinely older speakers, captured over a landline or a speakerphone rather than a laptop mic, with real mid-sentence pauses and one handover to a second speaker part way through. This fixture is what the card lives or dies on.

**Know before you pick this.** Two traps. First, recruit two or three genuinely older speakers before noon and record them, because building this against your own voice guarantees failure at 3:30. Second, do not assert the deadline, the month, or the rules of any specific verification scheme in your output copy. The card's behaviour is what scores, and any date or scheme rule has to be sourced authoritatively before publishing.

---


## 16 ·
Generic medicine substitution at the pharmacy counter

**Starter · domain · Document Intelligence**

> Photograph the prescription and find out whether the same molecule is available for less, or be told plainly that the handwriting cannot be read.

**Why this one.** The axis is look-alike discrimination against a closed vocabulary. Doctors' handwriting is the hardest handwriting there is, and drug names cluster: names that differ by one or two characters, names that share a prefix, names where the strength is the only distinguishing token. Free-form transcription is the wrong tool. What scores is decoding against a fixed formulary, producing a ranked candidate set rather than a single string, and refusing outright when the top two candidates are different molecules. Patients pay 3 to 10 times more for a branded drug when an equivalent generic exists, so the value is obvious, but a confident wrong read on a drug name is the single most dangerous output in this whole library. Refuse loudly.

**The scenario.** Pramila Mohanty is at a pharmacy counter in Bhubaneswar with a prescription for her husband's three ongoing medicines, written fast in blue ink on a clinic pad with the clinic's name printed at the top. The bill comes to more than she expected. She has no way to know that two of the three have identical generic equivalents, and the counter has no reason to tell her.

**What you will need**
- Camera capture at counter lighting, prescription pad on a glass counter, glare included
- Handwritten extraction constrained to a formulary vocabulary rather than open transcription
- A ranked candidate set per line, with the strength and the dosage form treated as separate fields
- A hard refusal rule: if the top candidates are different molecules, refuse the line and show the cropped image
- Two tool calls: look up generic equivalents by molecule, strength and form, and fetch price and availability from the mocked endpoint, shown per line
- Plain-language output in the patient's language, read aloud, framed as something to ask the pharmacist
- A held-back prescription for the demo, ideally from a different prescriber's hand
- A stated number on fifteen handwritten lines from at least three hands: how many resolved to the correct molecule, and your refusal rate on the rest
- One-pager: the workflow, the integration surface, the escalation to the pharmacist, what the build refuses to decide, and the rule that no line is ever presented as a substitution decision, a deploy-or-pilot verdict, and why you declared Document Intelligence rather than Voice Experience when the comparison is read aloud

**Your demo moment.** A judge photographs a prescription the system has never seen. It resolves two lines to specific molecules with equivalents and a price comparison, and on the third line, which is genuinely ambiguous, it declines and shows the cropped handwriting instead of picking the more common drug.

**Scores on:** Impact and Sarvam parameter. **Weak on:** Creativity, since this is a well-known idea. Your differentiator is the constrained decode and the refusal, not the price table.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam Doc AI, extracting handwritten prescription lines under counter lighting and decoding them against a closed formulary vocabulary rather than transcribing them freely. This is where the score is.
- **Supporting** Sarvam-30B for candidate ranking, the refusal rule and the plain-language framing, Mayura plus Bulbul for the patient's language. All plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Mobile web with camera capture and a per-line result carrying a clear refusal state and an audio button: Next.js · React with Vite · a single HTML page with a file input set to capture and three result rows, which is all this needs
- **Backend** Convex functions · Next.js route handlers · a small FastAPI or Express service · localhost with a tunnel
- **Data** Convex · Supabase · SQLite on disk · or none, hold it in memory, for prescriptions, per-line candidates with scores and refusals. The formulary itself is happier as a JSON file you load at boot than as rows in a database
- **Comms** Resend · Telegram bot · ntfy.sh, sending the comparison as something the patient can show at the counter
- **Mock or external** Beeceptor · Mockoon · WireMock Cloud, for the mocked price and availability lookup
- **Specific to this build** A real published generic formulary as your constrained vocabulary. The National List of Essential Medicines is the usual starting point and already splits molecule, strength and dosage form, which is exactly the field split this card needs. Plus ten to fifteen real handwritten prescriptions from at least three different hands.

**Know before you pick this.** To reach the top bands the input has to be a photographed or scanned document, not a text-layer PDF. Collect ten to fifteen real handwritten prescriptions before 11:30, from at least three different hands. Also: never present the output as a substitution decision. It is a question the patient asks the pharmacist, and the copy has to say so.

---


## 17 ·
Pre-submission EPF claim verification for workers

**Challenging · domain · Document Intelligence**

> Photograph your documents before you file and find out which mismatch will get your claim rejected.

**Why this one.** The axis is same-entity resolution across scripts and transliteration variants. One in three final settlement claims is rejected over tiny name, Aadhaar or KYC mismatches, and almost none of those are fraud. They are the same person written four ways: an initial expanded on one document and abbreviated on another, a surname before the given name, a Devanagari spelling on a bank passbook that transliterates two ways into English, a father's name where a suffix has been dropped. Deciding whether two strings are the same human, across scripts, is a Sarvam-shaped problem and a genuinely hard one. The build that scores does not just flag differences, it classifies each one as cosmetic or blocking, and it is honest when it does not know which.

**The scenario.** Rajesh Mahto worked eleven years at a plant near Dhanbad and is filing for final settlement after leaving. He has his Aadhaar, a bank passbook, an appointment letter, and a printed member passbook, all photographed on his phone. His name appears with a middle name on one, without it on another, and in Devanagari on the passbook. He has filed once and been rejected with a reason he could not decode.

**What you will need**
- Multi-document photographed intake, four or five documents of different sizes and layouts
- Field extraction per document: name, father's or spouse's name, date of birth, account number, identifier numbers
- Cross-script matching, so a Devanagari name and its English spellings are compared as the same field
- Per-mismatch classification: cosmetic, likely blocking, or unknown, with the reason stated
- A ranked fix list in the worker's language, spoken as well as written, ordered so the claim unblocks fastest, with what to correct and where
- A refusal state on any field where a document is illegible, rather than assuming a match
- Two tool calls: read the claim status from the mocked system, write the ranked fix list against the worker's record so a second attempt starts from it
- A stated number on document sets you labelled yourself, one held back with a planted transliteration variant: how many mismatches were classified correctly as cosmetic or blocking, and how many you honestly marked unknown
- One-pager: the workflow, the integration surface, what you store from five identity documents, what you redact, and who can see a field you refused to read, a deploy-or-pilot verdict, and why Document Intelligence remains primary even when the hard part is matching one name across two scripts

**Your demo moment.** A judge supplies a document set where the same name is spelled two ways across scripts and one date of birth is genuinely different. The system calls the transliteration variant cosmetic with a reason, calls the date of birth blocking, and refuses on the one field where the photograph is unreadable.

**Scores on:** Sarvam parameter and Impact. **Weak on:** Delight, unless the fix list is short, ordered and obviously actionable.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam Doc AI, extracting fields across four or five photographed documents of different sizes and layouts, including the Devanagari passbook. This is where the score is.
- **Supporting** Mayura transliteration for cross-script name comparison, Sarvam-30B for mismatch classification and fix ordering, Bulbul for the spoken version. All plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Multi-document camera capture with a per-document label, then a ranked mismatch list: Next.js · SvelteKit · plain HTML with a multiple file input and a table, which is genuinely enough
- **Backend** Convex functions · Next.js route handlers · a small FastAPI or Express service · a terminal script over a folder of images, which demos fine when the mismatch list is the output
- **Data** Convex · Supabase · SQLite on disk · or none, hold it in memory, for document sets, per-field values with confidence, mismatch records and classifications; images to Convex file storage, Supabase Storage or the local filesystem
- **Comms** Resend · Telegram bot · ntfy.sh, sending the full fix list plus a short version the worker can carry
- **Mock or external** Beeceptor · Mockoon · WireMock Cloud, for the mocked claim status system
- **Specific to this build** Redacted real document layouts, at least one carrying the name in Devanagari and one with an initial expanded on one document and abbreviated on another. Plant the transliteration variant deliberately: a set where every string already matches proves nothing.

**Know before you pick this.** To reach the top bands the input has to be a photographed or scanned document, not a text-layer PDF. Do not assert which mismatches an institution actually rejects on as though it were policy. Present classifications as the system's assessment, and source any specific rule authoritatively before publishing.

---


## 18 ·
Cybercrime complaint filing for scam victims

**Challenging · domain · Voice Experience**

> Talk through what happened while it is still happening, and get a complete complaint with the money trail in the right order.

**Why this one.** The axis is chronology reconstruction from a non-linear account. A scam victim does not narrate in order. They start at the moment they realised, jump to the first call, come back to a link, mention a second transfer they had forgotten, and correct an amount twice. Speech under panic is fast, fragmented, and full of self-corrections, which is exactly the condition Saaras is built for. The product's job is to rebuild a defensible sequence of events out of that, ask only for the links in the chain that are missing, and put the transaction trail at the front because that is the part that decays fastest. A system that just transcribes the panic produces a complaint nobody can act on.

**The scenario.** Bhaskar Deka in Guwahati got a call about a delivery, tapped a link, entered a code, and watched two debits leave his account within four minutes. It is now twenty minutes later. He has the SMS alerts open on his phone, a call log with an unknown number in it, and no ability to write any of this in English while his hands are shaking.

**What you will need**
- Voice intake designed for fast, fragmented, self-correcting speech, with no forced turn structure
- Event extraction into a timeline with timestamps, amounts, counterparties and channels, the transaction trail captured first from spoken SMS content or a photographed alert, before narrative detail
- Reordering into a defensible sequence, with a visible before-and-after of what the person said versus the reconstructed order
- Correction handling, so a figure stated then revised resolves to the revised value with both retained
- Gap prompting limited to missing links in the chain: how the money moved, and to what
- Generated complaint in the required format plus a read-back in the victim's language
- Two tool calls: submit the complaint to the mocked endpoint, and trigger an immediate bank action on the named escalation exit instead of filing a form
- A stated number on two scripted narrations: how many events landed in the correct order against the sequence you wrote, and whether every revised figure resolved to the revised value
- One-pager: the workflow, the integration surface, what you store of a victim's transaction data, how fast it is handed on, and what the build refuses to characterise as a category of offence, a deploy-or-pilot verdict, and why you declared Voice Experience rather than Document Intelligence when the transaction alerts arrive as photographs

**Your demo moment.** A judge narrates a scam out of order and revises one amount mid-sentence. The system produces an ordered timeline with the corrected figure, shows the original narration order alongside it, and asks for exactly the one missing link rather than restarting the interview.

**Scores on:** Memory and Context and Job-to-be-done. **Weak on:** Delight, since nobody wants to be here, and Creativity unless the reconstruction is visibly the product.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras, transcribing fast fragmented speech under panic so the self-corrections survive into the transcript instead of being smoothed away. This is where the score is.
- **Supporting** Sarvam-30B for event extraction, reordering and correction resolution, Sarvam Doc AI for photographed transaction alerts, Mayura plus Bulbul for the read-back. All plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Push to talk plus a camera step for transaction alerts, and a timeline view: Next.js · React with Vite · a single HTML page with MediaRecorder and an ordered list, which is the timeline
- **Backend** Convex functions · Next.js route handlers · a small FastAPI or Express service · localhost with a tunnel
- **Data** Convex · Supabase · SQLite on disk · or none, hold it in memory, for cases, extracted events with both the stated and the resolved value, and the reconstructed timeline
- **Comms** Resend · Telegram bot for the complaint and the timeline, Slack or Discord webhook · ntfy.sh for the immediate-action escalation path
- **Mock or external** Beeceptor · Mockoon · WireMock Cloud for the mocked complaint submission endpoint and the mocked bank action trigger; httpstat.us with sleep for the bank action that hangs
- **Specific to this build** Two scripted scam narrations recorded before you build, one deliberately out of order with an amount stated and then revised, plus two photographed transaction alert screenshots. Improvising the narration at 4pm is how this demo falls apart.

**Know before you pick this.** Do not assert reporting windows, statute sections, or which category a given scam falls under as fact. If your copy tells the victim to act fast, that is fine as behaviour, but any specific window or section has to be sourced authoritatively before publishing. Also script two full scam narrations before you build, one deliberately out of order, so you are not improvising the demo.

---


## 19 ·
Consumer forum complaint drafting for product disputes

**Challenging · domain · Voice Experience**

> Describe the dispute in your language, get a formal complaint in English, and hear back exactly what that English says before you sign it.

**Why this one.** The Voice Experience axis is correction and confirmation in a high-consequence conversation. The complainant narrates freely, code-switches, revises dates and amounts, then hears the finished English complaint explained back in their own language. The system must notice a spoken correction, preserve the final value and ask for explicit confirmation on facts, relief and figures instead of treating a fluent read-back as consent. Translation and document extraction support the flow; the scored surface is whether the conversation lets a person safely verify what they are about to sign.

**The scenario.** Shalini Deshmukh bought a water purifier in Nagpur that failed twice inside the warranty period, and the service centre has stopped answering. She has the invoice, two service job cards, and a WhatsApp thread. She is willing to file, but she is not willing to sign an English document she cannot read, because the last one she signed said something she did not intend.

**What you will need**
- Vernacular intake of the dispute narrative, plus photographed invoice and job cards for the facts
- Formal English drafting in the register a consumer complaint requires, with facts, relief sought and amounts
- Spoken read-back generated from the finished English draft, not from the original narration, with interruption and correction supported
- Round-trip check comparing the vernacular read-back against the English draft on facts, relief and figures, flagging any divergence
- Amounts and dates treated as protected values that must appear identically in both versions
- A visible diff when the round trip fails, so the complainant sees what changed rather than being told it is fine
- Two languages supported, so the check is proven and not a single-path coincidence
- A stated number across both languages: how many facts, figures and relief statements survived the round trip identically, and what the check caught when you changed one amount in the English draft on purpose
- One-pager: the workflow, the integration surface, the non-advice boundary and what the complainant must still take to a professional before signing an English document, a deploy-or-pilot verdict, and why Voice Experience is primary even though invoices and job cards support the conversation

**Your demo moment.** Generate the English complaint and begin the spoken vernacular read-back. The complainant interrupts to correct an amount in a code-mixed sentence; the agent updates the draft, reads the changed clause again and requires explicit confirmation before marking it ready to sign.

**Scores on:** Sarvam parameter and Job-to-be-done. **Weak on:** Impact, unless you can describe what a badly drafted complaint currently costs this complainant.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras streaming and Bulbul, handling free narration, code-switches, mid-read-back interruption, correction and explicit confirmation without losing which amount or clause is current. This is where the score is.
- **Supporting** Mayura and Sarvam Translate for the draft-to-vernacular round trip · Sarvam-30B for drafting and comparison · Sarvam Doc AI for invoice and job-card facts. Plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Voice intake plus document upload, with draft and read-back side by side and the check result between them: Next.js · SvelteKit · a two-column HTML page with the divergence highlighted in a span, which is the entire interface
- **Backend** Convex functions · Next.js route handlers · a small FastAPI or Express service · plain code with retry logic, since the round trip is two calls and a comparison
- **Data** Convex · Supabase · SQLite on disk · or none, hold it in memory, for cases, English drafts, per-language read-backs, protected values and round-trip check results
- **Comms** Resend · Loops · Telegram bot, sending both versions together so they always travel as a pair
- **Mock or external** No external system to mock
- **Specific to this build** A real consumer complaint format as your template, plus a real invoice and two service job cards photographed rather than typed, so the facts the draft asserts come out of documents and the protected values have somewhere real to come from.

**Know before you pick this.** Do not assert monetary limits, jurisdictions, fees, or limitation periods for any forum. Write the copy so the round-trip behaviour is the point, and mark every procedural figure as needing an authoritative source before publishing.

---


## 20 ·
Voice data entry for community health workers

**Beast · technical · Voice Experience**

> Capture a whole day of household visits in one offline recording, then get discrete register-ready records when the phone reconnects, with the boundaries in the right places.

**Why this one.** The axis is record boundary segmentation in continuous dictation. This is not one form filled by voice; it is a fifteen-minute monologue covering eleven households, captured on the walk home and processed when the phone reconnects. The hard part is knowing where one household ends and the next begins. There are no pauses to rely on, because a tired person dictating from memory pauses mid-record and runs straight through into the next one. Field values leak across boundaries, and a leaked haemoglobin reading or a leaked child's age is a bad record in a government register. The team that scores is the one whose segmentation is explicit, testable and correctable in one tap on a long real dictation rather than three clean sentences.

**The scenario.** Sabita Bariha covers a cluster of hamlets outside Balangir. She visits households through the morning, remembers what she saw, and writes it into three different registers in the evening because the network in the hamlets is unusable. She dictates the whole morning into her phone on the walk back, in Odia, in one long stretch, switching to English for the numbers and the drug names.

**What you will need**
- Long-form offline audio capture on the device, with transcription and record generation explicitly pending until reconnect
- Segmentation of one continuous dictation into per-household records, with explicit boundary decisions
- Field extraction per record, with code-mixed numbers and English clinical terms inside Odia sentences
- Leak detection: a value that could belong to either of two adjacent records is flagged, not assigned
- One-tap boundary correction in review, splitting or merging records without re-dictating
- Two tool calls on reconnect: write each segmented record to the mocked register endpoint in the register's own field set, and re-read to resolve a record someone has already entered
- One real long dictation, ten minutes or more, recorded before you build, as your test fixture
- A stated number on that dictation, labelled by hand: how many household boundaries were placed correctly, and how many values you flagged as belonging to either record rather than assigning them
- One-pager: the workflow, the integration surface, what a leaked field costs inside a government register, what the build refuses to assign, and who can correct a record after sync, a deploy-or-pilot verdict, and why Voice Experience remains primary even though the offline queue and the sync are half the build

**Your demo moment.** Record or load a long unscripted dictation while the device is offline and show it queued honestly. Reconnect; the system produces the right number of records, puts the numbers in the right ones, flags the one value that genuinely could belong to either household and lets the worker fix a boundary in one tap.

**Scores on:** Sarvam parameter and Impact. **Weak on:** Delight, unless the boundary correction is genuinely one tap, and Creativity if you frame it as voice forms rather than as segmentation.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras for long-form code-mixed transcription of one continuous ten-minute recording after reconnect, preserving the evidence needed for explicit household-boundary decisions. This is where the score is.
- **Supporting** Sarvam-30B for boundary segmentation, field extraction and leak detection. Plumbing, even though it is doing clever work. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** One long record button, then a review list of segmented records with split and merge: a PWA with a service worker · a Capacitor or WebView shell · plain HTML with MediaRecorder and IndexedDB, which covers the offline capture on its own
- **Backend** Convex functions for sync and conflict handling · Next.js route handlers · a small FastAPI or Express service · Cloudflare Workers
- **Data** This is the one card where persistence is the product, so do not skip it: IndexedDB · SQLite on the device, for the offline queue and raw audio, then Convex · Supabase · Postgres direct as the server of record after sync
- **Comms** Resend · Telegram bot · ntfy.sh, emailing the supervisor the day's records after sync and pushing a sync-complete confirmation
- **Mock or external** Beeceptor · Mockoon · WireMock Cloud for the mocked register or HMIS write endpoint; httpstat.us with sleep to test sync on a bad connection
- **Specific to this build** One real dictation of ten minutes or more, unscripted, covering several households with no clean pauses, recorded before you build. Short tidy clips will make your segmentation look solved when it is not. Build against a plausible register field set and mark it as needing verification against the real register.

**Know before you pick this.** Two hard requirements before 11:30. Record at least two long dictations, one over ten minutes with no rehearsed pauses, because short clean clips will make your segmentation look solved when it is not. And do not assert what any government register actually requires field by field. Build against a plausible field set and mark it as needing verification against the real register before publishing.

---


## 21 ·
Scholarship eligibility matching for rural families

**Starter · domain · Voice Experience**

> Answer a handful of spoken questions and find out which scholarships you actually qualify for, and which you do not, with the reason.

**Why this one.** The axis is elimination efficiency: asking the fewest questions that rule out the most schemes. Eligibility criteria sit scattered across hundreds of central, state and category-specific schemes, and the naive build asks thirty questions and returns a list. The good build orders its questions by how much of the space each answer eliminates, so a parent is done in six or seven questions, and it reports the negative result with a reason, because "you do not qualify for this one, because the income limit is lower than what you told me" is more useful and more trustworthy than a shortlist with no working shown. Do it in the parent's language, over voice, on a phone held by someone who will not read a table.

**The scenario.** Renuka in Warangal has a daughter finishing Class 10 and has heard three different things from three neighbours about what help is available. She has an income certificate, a caste certificate, and a phone. She cannot read the state portal, and the last time someone filled a form for her it went to a scheme her daughter was never eligible for.

**What you will need**
- A scheme dataset with structured, machine-checkable eligibility criteria, not prose descriptions
- Question ordering by eliminative power, computed rather than hardcoded
- Voice intake in the parent's language, one question at a time, with answers read back
- Negative results with reasons, naming the criterion that failed and the value that failed it
- A near-miss list, for schemes ruled out by one criterion, so the family knows what to check
- Next steps per qualifying scheme: what document, which office, what deadline if the scheme states one
- A stated number, not a claim: questions asked to reach a complete answer against a naive full questionnaire on the same dataset, and how many schemes each answer eliminated
- One-pager: the workflow, the integration surface, what you store of a family's income and category answers, and what the build refuses to assert about a scheme whose criteria you could not source, a deploy-or-pilot verdict, and why Voice Experience remains primary even though the eliminative ordering is arithmetic over a dataset

**Your demo moment.** A judge answers six spoken questions. The system returns the qualifying schemes, and for two it did not return, it names exactly which criterion ruled them out. Then show the question count against a naive full questionnaire on the same dataset.

**Scores on:** Job-to-be-done and Delight. **Weak on:** Creativity, decisively, and Sarvam parameter unless the eliminative ordering is real logic rather than a fixed script.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam-30B for eliminative question ordering and criterion-level reasoning on the negative results, so every "you do not qualify" names the criterion and the value that failed it. This is where the score is.
- **Supporting** Saaras for the vernacular intake, Bulbul for the questions and the read-backs. All plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Push to talk, one question per screen, results grouped into qualifies, near miss and ruled out: Next.js · React with Vite · a single HTML page with three result lists, which is enough for six questions
- **Backend** Convex functions · Next.js route handlers · a small FastAPI or Express service · plain code with a scoring function, since the eliminative ordering is arithmetic over the dataset and needs no framework
- **Data** Convex · Supabase · SQLite on disk · or none, hold it in memory: the scheme dataset is a JSON file you load at boot, and the session, the answers and the elimination trace per scheme can live in memory for one demo
- **Comms** Resend · Telegram bot · ntfy.sh, sending the shortlist with the documents needed and a copy to carry to the office
- **Mock or external** No external system to mock
- **Specific to this build** A dataset of fifteen to twenty schemes with structured machine-checkable criteria, each criterion carrying the source it came from. Take criteria from the issuing authority's own published page and treat an unsourced criterion as unpublishable. Do not print a portal address in builder or user copy unless you have opened it and confirmed it.

**Know before you pick this.** Sarvam ships a Government Scheme reference agent, so this card starts at the creativity floor and you have to beat the cookbook deliberately. Elimination efficiency and reasoned negative results are how you beat it. Also: do not state income limits, quotas, or deadlines for any named scheme unless you have taken them from the issuing authority. Structure the dataset so every criterion carries its source, and treat unsourced criteria as unpublishable.

---


## 22 ·
Bank and asset succession navigator for heirs

**Beast · domain · Document Intelligence**

> Photograph what the deceased left behind and get one reconciled document plan that satisfies every institution, with the differences between them named.

**Why this one.** The axis is requirement reconciliation across institutions. Families spend 6 to 18 months chasing bank accounts, mutual funds, EPF and insurance because every institution has a different process, and the actual work is not any single claim, it is realising that nine claims need overlapping but non-identical document sets. One wants an indemnity on a specific stamp value, one wants a different declaration format, one accepts a nomination and one does not. So the build extracts requirements out of each institution's own claim form, computes the shared core set once, and then produces the per-institution delta. Nobody builds this because it is unglamorous, which is exactly why it scores: it is the only card in the batch whose output is a plan rather than a document.

**The scenario.** Debjani Sen's father died in Kolkata four months ago. On the table in front of her are two bank passbooks, a mutual fund statement, an insurance policy booklet, an EPF slip, a Bengali-language will typed on a typewriter, and the death certificate. Every institution has given her a different list, two of them verbally, and she has re-photocopied the death certificate eleven times.

**What you will need**
- Multi-document photographed intake across wildly different layouts: passbooks, statements, a policy booklet, a typed vernacular will
- Asset inventory extraction: institution, account or policy identifier, holder name, nomination present or absent
- Requirement extraction from each institution's own claim form, as structured requirements rather than prose
- Reconciliation into a shared core document set plus a per-institution delta, conflicts between institutions named explicitly, ordered by dependency so anything that unblocks several claims at once comes first
- Plain-language plan in the family's language, written and spoken, one institution per section
- A refusal state on any asset where the identifier or holder name cannot be read, rather than a plan built on a guessed account number
- Two tool calls: read each institution's claim status from the mocked endpoint, write claim progress so the plan survives the months this takes
- A stated number against two or three institutions' own published forms, which is also how the delta becomes real: how many requirements you extracted correctly, and how many genuine conflicts between institutions you named
- One-pager: the workflow, the integration surface, what you keep of a dead person's account identifiers, who in the family can see the plan, and what the build refuses to assume about a document it could not read, a deploy-or-pilot verdict, and why Document Intelligence remains primary even though the output is a reconciliation plan rather than a document

**Your demo moment.** A judge hands over a mixed pile including a typed vernacular will and a photographed passbook. The system returns an asset inventory, one core document list, and a per-institution delta that names the two places where the institutions contradict each other, with the whole plan ordered so the shared documents come first.

**Scores on:** Job-to-be-done and Impact. **Weak on:** Delight, since the output is a plan and plans are dry. Make the ordering visibly the product or this reads as a checklist generator.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam Doc AI, extracting across wildly different photographed layouts: two passbooks, a fund statement, a policy booklet and a typewritten Bengali will. This is where the score is.
- **Supporting** Sarvam-30B for requirement structuring, reconciliation, conflict naming and dependency ordering, Mayura plus Bulbul for the family's language. All plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Multi-document capture with labels, then a plan view of inventory, core set and per-institution delta: Next.js · SvelteKit · plain HTML with a multiple file input and three sections, which is all the plan needs
- **Backend** Convex functions · Next.js route handlers · a small FastAPI or Express service · Sarvam Agents if you want the reconciliation run checkpointed and reopenable
- **Data** Convex · Supabase · Postgres direct · SQLite on disk, for assets, extracted identifiers with confidence, structured requirements per institution, the reconciled plan and claim progress. Claim progress is the one thing here that genuinely outlives the session, so keep a store
- **Comms** Resend · Telegram bot · Slack webhook, sending the plan as a per-institution set of sections and nudging as claims close
- **Mock or external** Beeceptor · Mockoon · WireMock Cloud, for the mocked institution status endpoints
- **Specific to this build** Real published claim or transmission forms from two or three institutions, because the delta is only real if the requirements came out of the institutions' own forms. Also one typewritten vernacular document, photographed: a typed Bengali page is a different extraction problem from a handwritten one, and this pile needs both kinds.

**Know before you pick this.** To reach the top bands the input has to be a photographed or scanned document, not a text-layer PDF. Do not assert succession law, stamp values, or what any institution accepts in place of a succession certificate. Extract requirements from the institution's own published form and cite it, and treat anything you cannot cite as a gap in the plan rather than an assumption inside it.

---


---

# Health and Education


## 23 ·
Cross-hospital medical records digitisation for chronic patients

**Beast · domain · Document Intelligence**

> Photograph a chronic patient's entire paper file, from four hospitals and nine years, and get one chronology out of it.

**Why this one.** The axis is chronological reconstruction across many hands. A chronic patient's file is not one document, it is sixty documents written by different people, in different scripts, on different letterheads, most of them handwritten, several undated or dated only by a rubber stamp. The hard problem is not reading any single page, it is deciding which pages describe the same episode, which order they happened in, and which of two entries is a repeat of the other rather than a new event. A pile of correctly extracted pages with no timeline is worth almost nothing to the doctor holding it. One assembled chronology, with the pages it cannot place shown separately rather than jammed into a guessed slot, is the whole product.

**The scenario.** Sulochana has been treated for a long-term condition for nine years, first at a district hospital near Chandrapur, then at two private clinics, and now at a large hospital in Nagpur. She carries a cloth bag with a plastic folder in it: discharge summaries, handwritten follow-up notes on prescription pads, three lab slips stapled together, and one page that is a photocopy of a photocopy. At every new consultation the doctor gets eight minutes and reads the top four pages. She empties the folder onto a table and photographs it page by page.

**What you will need**
- Bulk camera capture for sixty-odd pages of mixed size, including pages photographed at an angle in bad light
- Doc AI extraction from handwritten clinical notes and prescription pads, not just printed discharge summaries
- Document typing and episode resolution, so a discharge summary, a follow-up note and a lab slip are handled as different shapes, and two pages describing one visit merge rather than duplicate
- Timeline assembly with an explicit "cannot place" bucket for undated or unreadable pages
- Per-field confidence, and a refusal state on anything that reads as a dose, a quantity or a frequency
- Two tool calls: write the assembled chronology to the mocked hospital records endpoint, and read it back so the next visit appends rather than duplicates
- Ten to fifteen real pages sourced and redacted before 11:30, two of them in different hands, one held back unseen for the demo
- A stated number on pages you dated by hand: how many landed in the right position on the chronology, and how many you honestly left in the unplaced bucket
- One-pager: the workflow, the integration surface, the escalation path to the treating doctor and the rule that no dose, quantity or frequency is ever stated unless it was read off the page, a deploy-or-pilot verdict, and why Document Intelligence remains primary even when the patient-facing version is translated

**Your demo moment.** A judge hands over a page from the middle of the file that the system has never seen. It places the page in the right position on the chronology, or says plainly that it cannot date it and puts it in the unplaced bucket, and it does not overwrite an existing entry with a duplicate of the same visit.

**Scores on:** Memory and Context, decisively, plus Sarvam parameter. **Weak on:** Delight, unless the chronology is genuinely readable in one screen rather than a table dump.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam Doc AI, reading sixty pages of handwritten follow-up notes, prescription pads and stapled lab slips in several hands, including the photocopy of a photocopy. This is where the depth goes and where the score is.
- **Supporting** Sarvam-30B for document typing, episode resolution, dating and duplicate detection · Mayura for a patient-facing version in Sulochana's own language. Plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Mobile web with rapid multi-page capture, one vertical chronology and an unplaced tray at the bottom · plain React with Vite · a single HTML page with a multi-file input pointed at a folder of phone photos, which skips the capture UI entirely and loses you nothing
- **Backend** Next.js route handlers · a small FastAPI or Express service · Convex functions · Sarvam Agents if you want the sixty-page run resumable rather than restarted, doing typing, episode grouping and the unplaced bucket
- **Data** Convex · Supabase · Postgres · SQLite on disk, for pages, extracted entries with confidence, episode groupings and the unplaced bucket. Persistence is not optional on this card, the chronology is the artefact. Page images to Convex file storage · Supabase Storage · Cloudflare R2 · the local filesystem
- **Comms** Resend emailing the chronology as a single PDF she can carry to the next consultation · Telegram bot sending the same PDF · Loops
- **Mock or external** Mockoon · Beeceptor · WireMock Cloud for a hospital records endpoint you write the assembled record into
- **Specific to this build** Ten to fifteen real pages, sourced and redacted before 11:30, deliberately including two in different hands, one prescription pad, one undated page and one photocopy of a photocopy. Clean printed discharge summaries will cap your score.

**Know before you pick this.** To reach the top bands the input has to be a photographed or scanned document, not a text-layer PDF. Handwriting is the point here, so a folder of clean printed discharge summaries will cap you. Source and redact real pages before the sprint. Second, and non-negotiable: any clinical content in your output has to come from the document in front of you, never from the model's memory. Do not let the system name a drug, a dose or a frequency it has not read on the page, and make the refusal visible in the demo rather than hidden in a log.

---


## 24 ·
Pre-purchase insurance policy comprehension

**Challenging · domain · Document Intelligence**

> Photograph the policy wording before you pay, and find out what it will not cover.

**Why this one.** Around 25% of health insurance claims are rejected because the buyer never knew the exclusions. So the axis is recall on the negative space: finding everything the document declines to cover, including the items that are not in the exclusions list because they are buried in a waiting-period clause, a sub-limit, a room-rent cap or a definition that quietly narrows a covered term. Summarising a policy is easy and produces a comfortable, wrong feeling. The scored behaviour is completeness against a set you can check: pick five exclusions in the wording yourself, and see how many your system finds without being told they exist. A missed exclusion is the whole failure mode of the product.

**The scenario.** Anjali is buying a family floater in Bhubaneswar for herself, her husband and her mother. The agent has sent her a 46-page policy wording and told her on the phone that everything is covered. She has printed it because she reads better on paper, and the printout is now marked up in pen with three question marks. She photographs the pages she does not understand.

**What you will need**
- Multi-page photographed policy wording ingestion, pages possibly out of order
- Extraction of the four structures that create exclusions: the exclusions list, waiting periods, sub-limits and caps, and narrowing definitions
- A recall harness with a stated number: five exclusions you located by hand, asserted against every run, and how many of them the system finds on an unseen wording without being told they exist
- Plain-language restatement of each exclusion as "this is what will not be paid, and when"
- Personalisation against the buyer's own stated situation, so a maternity waiting period surfaces for one buyer and a pre-existing condition clause for another
- Output in the buyer's language, written and read aloud
- Two policy wordings from different insurers so the demo is not one template, one held back unseen
- One-pager: the workflow, the integration surface, what the build refuses to say about a medical condition and where it names an ambiguity in the wording instead of resolving it in the buyer's favour, a deploy-or-pilot verdict, and why Document Intelligence remains primary even when every exclusion is restated in the buyer's language

**Your demo moment.** A judge picks an exclusion out of an unseen policy by hand and asks whether it is covered. The system already listed it, in plain language, with the page it came from, and it also names the two clauses that narrow a term the buyer assumed was broad.

**Scores on:** Job-to-be-done and Impact, since the rejected-claim number is real and stateable. **Weak on:** Creativity, because document explainers are the most crowded shape in the library. Your recall harness is the differentiator, so put it on screen.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam Doc AI, extracting a photographed 46-page policy wording with pages out of order, including the sub-limit tables and the definitions section where the quiet exclusions hide. This is where the depth goes and where the score is.
- **Supporting** Sarvam-30B for exclusion discovery across the four structures and personalisation to Anjali's stated situation · Mayura plus Bulbul for the buyer's language. Plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Web app with multi-page camera capture and a single "what will not be paid" list ordered by likelihood of mattering to this buyer · plain React with Vite · a static HTML page with a file input and one ordered list, with the recall harness score printed at the top
- **Backend** Next.js route handlers · Convex functions · a small FastAPI or Express service · Cloudflare Workers, walking the four exclusion structures and asserting the recall harness on every run
- **Data** Convex · Supabase · SQLite · or none, hold one wording in memory for a single-session demo, for wordings, extracted clauses, the exclusion set and the harness results
- **Comms** Resend · Loops · MailerLite · Telegram bot, delivering the exclusions list before she talks to the agent again
- **Mock or external** No external system needed · Beeceptor if you want the exclusions list posted into a buyer's checklist
- **Specific to this build** Two real family floater policy wordings from different insurers. Insurers publish these openly on their own product pages, download them, print the pages and photograph the print, because a text-layer PDF caps this card. Then pick five exclusions by hand as your recall harness before you write any code.

**Know before you pick this.** To reach the top bands the input has to be a photographed or scanned document, not a text-layer PDF. Do not state what a policy covers as advice, and do not have the system assert anything about a medical condition. It reports what this document says and refuses where the wording is genuinely ambiguous, naming the ambiguity instead of resolving it in the buyer's favour.

---


## 25 ·
Cross-language interpretation between nurses and patients

**Beast · domain · Voice Experience**

> Two people who share no language, one instruction that has to survive intact in both directions, confirmed back before anyone walks away.

**Why this one.** This is the hardest card in the library and the one that fails the swap test most completely. Metro hospitals staff nurses from Kerala and Goa; patients arrive from Bihar and UP. Neither side has a shared language, and the thing being communicated is not small talk, it is when to take something, how much, what to do if it hurts, and what to report immediately. Today that gap is bridged by a ward boy who half speaks both, or by nodding.

The axis is closed-loop readback. Every other interpretation build stops at relay: nurse speaks, patient hears something. Relay is not the job, because neither party can tell whether the relay worked. The scored behaviour is the loop closing: the patient repeats the instruction back in their own language, the system carries that repetition back to the nurse in hers, and it compares the patient's restatement against the original instruction and flags a mismatch out loud when the quantity, the frequency, the timing or a negation has drifted. Dropping a "not" is the failure that matters, and it is invisible in a one-directional demo. Doing that inside a live conversational rhythm, in a language pair where the clinical vocabulary in the patient's language is thin to non-existent, with Saaras v3 accepting 23 languages and Bulbul v3 producing 11, is a genuine speech-stack stress test rather than a claimed one.

The second axis, and it is what lifts this from strong to winning: the loop has to survive a shift handover. The instruction given on the morning shift is the context for the evening one, and the next nurse does not speak the previous nurse's language either.

**The scenario.** Reshma trained in Thrissur and has worked the ward at a large Gurugram hospital for two years. Her Hindi is functional for directions and useless for instructions. Ramkishun was brought in from a village outside Chhapra; he speaks Bhojpuri, understands some Hindi when it is slow, and cannot read. She has to give him a discharge instruction, and she has to know he has understood it, because the alternative is a readmission. She puts a phone between them on the bedside table and taps once.

**What you will need**
- One shared device, two speakers, no headsets and no menu on either side, with the patient's language detected on their first utterance including a dialect that is close to but not Hindi
- Bidirectional streaming relay with a stated latency budget, because a three-second gap kills the conversation and the nurse gives up and nods
- Readback prompt in the patient's language, then comparison of the restatement against the original instruction on four dimensions, quantity, frequency, timing and negation, with the mismatch spoken to the nurse in her language naming which one drifted rather than a generic "please repeat"
- Hard refusal on any number the system is not confident it heard, escalating to the nurse rather than relaying a number it guessed
- Instruction history per patient, carried across shifts, so the next nurse sees what was already said, in her own language
- Three tool calls: read patient context from the mocked hospital system, write the instruction record with its readback result, raise the failed-readback alert to the ward
- Three or four people willing to play patients in a language nobody on your team speaks, recruited before noon
- A stated number on scripted readbacks where a word was dropped on purpose: how many drifts you caught across the four dimensions, and how many numbers you refused rather than relayed
- One-pager: the workflow, the integration surface, the escalation path to the nurse and the rule that no number is relayed unless the system is confident it heard it, a deploy-or-pilot verdict, and why Voice Experience remains primary even when the content is crossing two languages

**Your demo moment.** A judge plays the patient, in a language nobody on the team speaks, and deliberately repeats the instruction back slightly wrong, dropping one word. The system catches it, tells the nurse in her language exactly which part drifted, and does not let the conversation end until the readback matches. Then a second judge arrives as the next shift and is shown what was already agreed, in a third language.

**Scores on:** Sarvam parameter and Memory and Context, both at the top of the ladder if the readback loop is real. **Weak on:** nothing structurally, which is why it is a beast. The exposure is scope: teams try to interpret an entire consultation and end up demonstrating nothing verifiable. Do one instruction type end to end instead.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras streaming for bidirectional transcription and dialect detection, with Bulbul streaming as its other half, inside a latency budget tight enough that Reshma does not give up and nod. This is where the depth goes and where the score is.
- **Supporting** Sarvam-30B for the readback comparison on quantity, frequency, timing and negation, and for the mismatch sentence spoken back to the nurse in her language. Plumbing, even though it carries the cleverness. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** One tablet or phone flat on the bedside table, one tap to start, two large speaker indicators, no per-turn buttons and no language menu on either side · LiveKit or Pipecat for real control of the audio path and barge-in · Sarvam streaming APIs called straight from a plain web page with getUserMedia, which is fewer moving parts on a five-hour clock
- **Backend** Sarvam Agents for per-instruction run state that survives a shift change · Convex functions · a small Node or Python websocket service · plain code with a state machine, holding the instruction record and the handover view
- **Data** Convex · Supabase · Postgres, for patients, instructions, per-turn transcripts tagged by language and speaker, readback results and handover state. Persistence is not optional here, the shift handover is the second axis
- **Comms** Resend emailing the ward lead a per-patient log of instructions given and readbacks that failed · Telegram bot into the ward group · Slack webhook · ntfy.sh for the failed-readback alert
- **Mock or external** Mockoon · Beeceptor for a hospital information system you read patient context from · httpstat.us with `?sleep=5000` to hear what the device says out loud when the network stalls mid-relay
- **Specific to this build** Three or four people willing to play patients in a language nobody on your team speaks, recruited before noon. An instruction script with generic placeholders the nurse fills live, never invented drug names or doses. And confirm your language pair against the coverage split before you commit: Saaras v3 accepts 23 languages while Bulbul v3 produces 11, so a pair can work in one direction and fail in the other.

**Know before you pick this.** Every clinical specific in your build has to come from a source you can show, or from the nurse's own spoken words in the moment. Do not populate a demo with invented drug names, doses or frequencies. Write your instruction script with generic placeholders that the nurse supplies live, and make the system refuse and escalate on any safety-critical number it is not confident about rather than relaying its best guess. A demo where the interpreter confidently relays a wrong dose is a failed demo no matter how good the audio is, and judges in this room will test for exactly that.

---


## 26 ·
Plain-language explanation of lab reports

**Challenging · domain · Document Intelligence**

> Photograph the report you just collected, understand it tonight instead of on Thursday, and get told plainly when the honest answer is "ask the doctor."

**Why this one.** The axis is grounding every value in the range printed on the same page. A lab report is a value, a unit and a reference range, and the reference range varies by lab, by method, by age and by sex. A build that recognises a test name and then explains the value against a range the model remembers from training is not a useful product, it is a confident hazard, and it will be wrong for exactly the small-town lab whose patients need it most. So the scored behaviour is strictly local: read the value, read the range printed beside it, place one against the other, and where the range is not printed or not legible, say so and stop. Small labs still hand out slips with values entered in pen against a preprinted form, which is where Doc AI has to actually work. Everything else on this card is presentation.

**The scenario.** Manju collects a report from a neighbourhood lab in Jodhpur on a Saturday evening. Her appointment is on Thursday. The slip is a preprinted form with the values filled in by hand, one column smudged, and a note added at the bottom in the technician's writing. She has already typed two of the values into her phone and read three pages that frightened her. She photographs the slip instead.

**What you will need**
- Camera capture for a handwritten or part-handwritten lab slip, in evening light, held in one hand
- Doc AI extraction of the row structure: test name, value, unit, and the printed reference range from the same row
- A hard rule that no range is ever supplied from anywhere except the document, with an explicit "range not printed" state
- Plain-language placement of each value relative to its own printed range, with no diagnosis and no cause
- A stated boundary: what this tool does, what only the doctor does, and which findings mean "call now, do not wait for Thursday" as a category rather than as a clinical claim
- Question answering over the extracted rows, in the patient's language, spoken as well as written
- Two slips from different labs with different layouts, one handwritten, one held back unseen for the demo
- A stated number on rows you transcribed by hand: value and unit accuracy, how often the printed range stayed attached to its own row, and how often you returned "range not printed" instead of a placement
- One-pager: the workflow, the integration surface, the escalation category, what only the doctor decides, and the rule that no range, cause or diagnosis comes from anywhere but the page, a deploy-or-pilot verdict, and why you declared Document Intelligence rather than Voice Experience when the questions and answers are spoken

**Your demo moment.** A judge hands over an unseen handwritten slip. The system reads the rows, places each value against the range printed on that same slip, and on the smudged row it declines and shows the cropped cell rather than producing a plausible number. Then the judge asks a question in a regional language and hears the answer.

**Scores on:** Delight and Job-to-be-done, because the waiting is the pain and you remove it. **Weak on:** Creativity, and Impact unless you can describe the current wait honestly rather than quantify it invented.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam Doc AI, reading a preprinted slip with values entered in pen, in evening light, held in one hand, with the row structure preserved so each value stays attached to the reference range printed beside it. This is where the depth goes and where the score is.
- **Supporting** Sarvam-30B for plain-language placement, boundary enforcement and question answering over the extracted rows and nothing else · Bulbul for the spoken version · Mayura if the patient's language needs it. Plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Mobile web, single capture, one row per value with a plain sentence under each, plus a question box and a play button · plain React with Vite · a single HTML page with a `capture="environment"` file input and an `<audio>` tag, which is the entire interface Manju needs on a Saturday night
- **Backend** Next.js route handlers · a small FastAPI or Express service · Convex functions · localhost with a Beeceptor tunnel, enforcing the rule that a range only ever comes from the page and the "range not printed" state when it does not
- **Data** Convex · Supabase · SQLite · or none, one slip in memory is enough for a single-session demo, for extracted rows with confidence, the range-not-printed queue and question history
- **Comms** Resend emailing a written copy to take to the appointment with the unreadable rows listed for the doctor · Telegram bot · ntfy.sh
- **Mock or external** No external system needed · Beeceptor if you want the unreadable rows handed to a clinic front desk
- **Specific to this build** Two real slips from different labs with different layouts, one of them a preprinted form with the values written in by hand, redacted, plus one deliberately smudged row so the refusal is demonstrable. Small neighbourhood labs are where these layouts come from, so source the handwritten one from an actual local lab slip rather than a hospital's printed report.

**Know before you pick this.** To reach the top bands the input has to be a photographed or scanned document, not a text-layer PDF, and handwriting is where the marks are. On content: never let the model supply a reference range, a normal value, a cause or a diagnosis from memory. If the range is not on the page, the correct output is that it cannot say. Have a stated escalation category for anything safety-critical and make the demo show the system refusing at least once.

---


## 27 ·
Comparing conflicting medical opinions across languages

**Challenging · domain · Document Intelligence**

> Two doctors, two languages, two sets of dense terminology, and one clear list of where they actually disagree.

**Why this one.** The Document Intelligence axis is attributed claim extraction across two messy source documents. A patient is holding a typed English opinion and a photographed handwritten note in another script, and the only safe comparison is one where every extracted finding and recommendation traces back to the correct doctor and line. The system must preserve uncertainty, align differently worded claims and report three buckets: agreement, a stated difference, and present in only one opinion. It never says which doctor is right, and any illegible or unaligned claim stays visibly unresolved rather than being translated into false certainty.

**The scenario.** Deepthi is in Hyderabad managing her father's care. The first opinion is a typed note in English from a hospital consultant, dense with abbreviations. The second is a handwritten note in Telugu from a doctor her uncle trusts in their home town. Her father is waiting on a decision, the family is arguing on a group call, and nobody in the family can hold both notes side by side. She photographs both.

**What you will need**
- Ingestion of two photographed opinions in different languages, one of them handwritten
- Normalisation of each opinion into structured claims: what was found, what was recommended, what was ruled out, what was left open
- Cross-language claim alignment, so the same recommendation phrased two ways is recognised as one claim
- Three-bucket output: agreed, differs with the difference stated, present in only one opinion
- A stated refusal to adjudicate, and a refusal on any claim it cannot confidently align rather than forcing it into a bucket
- A question list for the next consultation, generated from the differences, in the family's language
- Two real opinion pairs in different language combinations, one pair held back unseen for the demo
- A stated number on pairs you aligned by hand: how many differently worded statements were matched to one claim, how many false conflicts you raised, and how many claims you left unaligned
- One-pager: the workflow, the integration surface, line-level provenance, the rule that the build never adjudicates or ranks a doctor, and what leaves as a question for the next consultation rather than as a conclusion, a deploy-or-pilot verdict, and why Document Intelligence is primary while cross-language rendering is supporting work

**Your demo moment.** A judge supplies an unseen pair where the two doctors use completely different terminology for the same recommendation. The system reports it as agreement, not conflict, then correctly isolates the one place they genuinely differ, and hands over three questions to ask the next doctor.

**Scores on:** Sarvam parameter and Job-to-be-done. **Weak on:** Delight, unless the three-bucket view is genuinely calm to look at, which matters more here than on any other card in the batch.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam Doc AI and Sarvam Vision, recovering attributed claims from a typed English opinion and a photographed handwritten note, preserving line-level source traceability and refusing illegible text. This is where the depth goes and where the score is.
- **Supporting** Mayura and Sarvam Translate for cross-language normalisation · Sarvam-30B for claim alignment and three-bucket sorting · Bulbul if the family wants the comparison read aloud. Plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Web app with two capture slots side by side and a three-bucket comparison on one screen · plain React with Vite · a static two-column HTML page, which is easier to make calm to look at than a framework layout and calm is what this card is judged on
- **Backend** Next.js route handlers · a small FastAPI or Express service · Convex functions · Cloudflare Workers, doing normalisation into claims, alignment, and the refusal to force a claim into a bucket
- **Data** Convex · Supabase · SQLite · or none, two documents in memory is a legitimate answer here, for opinions, extracted claims, alignment pairs with confidence and the unaligned queue
- **Comms** Resend emailing the comparison and the question list so the group call has one document · Telegram bot into the family group · Loops. Do not attempt WhatsApp, even though that is where the argument is happening, verification takes days
- **Mock or external** No external system needed · Beeceptor if you want the question list pushed to a mocked appointment endpoint
- **Specific to this build** Two real opinion pairs in different language combinations, one member of each pair handwritten, redacted. If you cannot source them, a clinician you know can write both sides for you in an afternoon, which is faster than hunting.

**Know before you pick this.** To reach the top bands the input has to be a photographed or scanned document, not a text-layer PDF. This build reports differences and never resolves them. Do not let it recommend a course of action, rank the doctors, or state a clinical fact that is not written in one of the two documents. Any claim it cannot align with confidence goes into an unaligned list for the doctor, not into a bucket.

---


## 28 ·
Personalised mock tests for competitive exam students

**Challenging · domain · Voice Experience**

> A test series that gets harder in exactly the places you keep getting things wrong, in the language you think in.

**Why this one.** The Voice Experience axis is understanding a student's reasoning, not merely transcribing the selected answer. The student thinks aloud in Bhojpuri and Hindi, inserts the exam's English terminology, pauses, self-corrects and may circle back to an earlier step. The agent must follow that explanation, ask one precise follow-up when the reasoning is ambiguous and explain the misconception conversationally without translating away the term the student will see on the paper. Longitudinal storage still drives the product, but it scores under Memory and Context; the Sarvam parameter is the quality of the spoken reasoning exchange.

**The scenario.** Rupesh is in his second year of NEET preparation in Muzaffarpur, studying from a secondhand set of books and free videos. His father runs a shop. The coaching institute nearby quotes a package he is not going to buy, and the value in that package is not the classes, it is the test series and the report that comes after each test. He thinks in Bhojpuri and Hindi, reads the paper in English, and has been getting a particular class of problem wrong for four months without anyone telling him why.

**What you will need**
- A real question bank for one subject and one syllabus unit, not the whole exam
- Attempt capture with the student's reasoning spoken in their language, not just the chosen option, because a student explaining out loud is where the misconception actually surfaces
- Misconception extraction from the reasoning, stored as a named durable fact about the student rather than a wrong-answer count
- Question generation targeted at a stored misconception from an earlier session
- Explanations in the student's language, with the exam's own terminology retained so the paper is still readable
- Three tool calls: read this student's stored misconceptions, write a newly named one with the session that evidenced it, generate the next question set aimed at the oldest unresolved one
- A session-five state seeded before the demo, with sessions one to four already in the store
- A stated number across the seeded sessions: how often the misconception you named predicted what the student actually got wrong next time
- One-pager: the workflow, the integration surface, what you store about a student's reasoning, who can see the misconception profile, and what the build refuses to claim about their chances in the exam, a deploy-or-pilot verdict, and why Voice Experience is primary while longitudinal tracking scores separately under Memory and Context

**Your demo moment.** A judge is shown session five. The system says, unprompted, that this student made a specific reasoning error in session one and again in session three, generates a question aimed at it, and the student's spoken explanation is diagnosed in their own language. Then it shows the four earlier sessions that produced that conclusion.

**Scores on:** Memory and Context, decisively, since that is the only thing separating this from a free question bank. **Weak on:** Creativity, badly, unless the longitudinal memory is real.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras streaming and Bulbul, following a code-mixed, self-correcting explanation, asking a targeted follow-up and returning feedback in the student's language while preserving the exam's English terminology. This is where the depth goes and where the score is.
- **Supporting** Mayura and Sarvam Translate for terminology-controlled explanations · Sarvam-30B for naming the misconception and generating a question aimed at it. Plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Mobile web, one question at a time, push to talk for the reasoning, plus a "what I keep getting wrong" view · a Telegram bot as the entire interface, no web app at all, which is closer to how he already uses his phone · a single HTML page with a record button
- **Backend** Convex functions · Next.js route handlers · a small FastAPI service · plain code with a cron for session scheduling, holding the misconception store and the targeted generation
- **Data** Convex · Supabase · Postgres · SQLite on disk, for students, sessions, attempts with spoken reasoning, and named misconceptions with the sessions that evidenced them. Persistence is not optional on this card, the seeded sessions one to four are the score
- **Comms** Telegram sending the daily question set, because that is where the student already is · Resend · ntfy.sh
- **Mock or external** No external system needed · Beeceptor if you want the daily set delivered through a mocked coaching backend
- **Specific to this build** A published previous-year NEET paper for one subject and one syllabus unit as the question base, which the testing agency publishes after each cycle, plus four seeded prior sessions with real spoken reasoning in them before 11:30.

**Know before you pick this.** Sarvam ships a Tutor reference agent, so this card starts at the creativity floor. Building a tutor that answers questions in Hindi is the reference implementation with a new noun on it, and it will be scored as such. The only escape route is vernacular plus longitudinal memory: the build has to demonstrably remember where this learner struggled several sessions ago and act on it now. Seed four prior sessions before 11:30 and demo session five. A demo that shows only a first session is a low score, and no amount of interface polish rescues it.

---


## 29 ·
Career counselling for tier 3 and tier 4 town students

**Challenging · domain · Voice Experience**

> A counsellor that asks the questions nobody asked you, then only names colleges that actually exist in its list.

**Why this one.** The axis is eliciting constraints the speaker does not know are relevant. This is not the evasive-caller problem, where someone is withholding on purpose. It is the opposite: a seventeen year old genuinely does not know that the distance from home, whether there is a girls' hostel, whether the family will permit a move, the fee structure across four years, and what happens if a scholarship does not come through are the five facts that determine the answer. Asked "what do you want to study," they give an aspiration they heard from a cousin. So the conversation has to work indirectly, in their dialect, drawing out constraints through concrete questions about their actual life rather than an intake form they will answer wrong. The counter-discipline is equally scored: commission-driven counsellors work by naming institutions, so this build must never name a college, a fee or a cutoff that is not in the dataset you supplied it, and must say "not in my list" rather than produce a plausible name.

**The scenario.** Sunil is in class 12 in Deoghar. His marks are decent. His information about what to do next comes from two cousins, a WhatsApp forward, and a man who visited the school with brochures and a form to sign. He has never spoken to anyone who asked what he could actually afford or how far from home his family would let him go. He calls a number a teacher gave him and speaks in the Hindi he actually speaks.

**What you will need**
- Inbound or outbound voice in the student's dialect, with detection rather than selection
- An indirect elicitation script that reaches five constraints through concrete life questions, never as a form
- Constraint state held across a rambling twenty-minute conversation, with contradictions surfaced gently and re-asked
- A real dataset of institutions with fees, location and entry requirements, and a hard rule that nothing outside it is ever named
- Three tool calls: look up institutions in that closed dataset, check scholarship eligibility against the mocked endpoint, log every out-of-list request so the refusals are auditable
- An explicit "not in my list" response, distinct from "no match found"
- Recommendations expressed as trade-offs against the elicited constraints, in the student's language, spoken
- A written summary the student can show a parent, since the parent is the actual decision maker
- One-pager: the workflow, the integration surface, what the build refuses to name when it is not in the dataset, and where every fee and cutoff on the parent's summary came from, a deploy-or-pilot verdict, and why Voice Experience remains primary even when the parent-facing summary is translated

**Your demo moment.** A judge plays a student who opens with an aspiration that does not fit their constraints, and volunteers none of the five constraints. Over the call the agent surfaces all five without ever reading out a form, then asks about a college that is not in the dataset and gets told plainly that it is not in the list rather than a confident invention.

**Scores on:** Job-to-be-done and Impact, since the current alternative is a commission. **Weak on:** Sarvam parameter unless the dialect handling is genuinely load-bearing, so pick a dialect your team can test with a real speaker.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras, transcribing the Hindi a class 12 student in Deoghar actually speaks across a rambling twenty-minute call with no form and no menu. This is where the depth goes and where the score is.
- **Supporting** Sarvam-30B for planning the indirect elicitation and reasoning about trade-offs against the dataset · Bulbul for the counsellor voice · Mayura for the parent-facing summary. Plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Phone inbound via Twilio, Exotel or Plivo, because these students have phones and not laptops · LiveKit or Pipecat if a long call needs barge-in · a browser mic session with a teammate playing Sunil, which is enough to demo the elicitation if telephony eats your morning
- **Backend** Sarvam Agents for twenty-minute call state and checkpointing · Convex functions · a small FastAPI service · a plain state machine, holding the five constraints and enforcing the closed list
- **Data** Convex · Supabase · SQLite · a CSV of institutions loaded into memory with a JSON log on disk, for elicited constraints with the turn each came from and every out-of-list request logged
- **Comms** Resend and Telegram delivering the parent-facing summary in the family's language, since the parent is the decision maker · Slack webhook for a counsellor queue
- **Mock or external** Beeceptor · Mockoon for a scholarship-eligibility endpoint · httpstat.us with sleep, to hear what the agent says while eligibility is checked
- **Specific to this build** A real published institution list for one district or one state, with fees, location and entry requirements, loaded as a closed list. State counselling authorities and admission brochures publish these as PDFs, take one and parse it, and do not top it up from the model.

**Know before you pick this.** Never assert a fee, a cutoff, a seat count or an admission rule the dataset does not contain. Log every out-of-list question and show that log in the demo, because "what it refused to say" is the part of this build a judge can verify in ten seconds.

---


## 30 ·
Plain-language explanation of property documents

**Beast · domain · Document Intelligence**

> Photograph the deed and the old revenue records, and get an obsolete regional legal register turned into sentences you can act on.

**Why this one.** Property fraud is India's largest civil case category, and the mechanism is simple: people sign documents they cannot fully read. But the reason they cannot read them is not that the language is dense English, it is that the register is archaic regional legalese, often handwritten decades ago by a clerk, using revenue and tenure vocabulary that has fallen out of everyday use and has no modern equivalent in casual speech. The axis is rendering an obsolete technical register into modern plain speech without smoothing away the terms that carry legal weight. Those two pull against each other, which is what makes this a beast: paraphrase too freely and you delete the meaning, preserve too literally and you have reproduced the problem. The scored behaviour is the middle path, plus honesty about the gap: this document says X, the term X means this, and here is what the document does not tell you.

**The scenario.** Mangesh is buying a plot on the edge of Kolhapur from a family that has held it for three generations. What he has been given is a typed sale deed draft plus photocopies of older Marathi revenue records, handwritten, in a hand nobody at the counter reads quickly. Two names on the older records do not appear anywhere on the draft. The seller says that is normal. He photographs everything on the table.

**What you will need**
- Multi-page capture across mixed inputs: a typed draft plus handwritten photocopies of older records
- Doc AI extraction from degraded handwritten regional-script pages, including faded and photocopied ones
- An archaic-term glossary built from the documents themselves, each term explained in modern plain speech with the original retained alongside
- Party and identifier extraction across documents, with names appearing in one document and not another surfaced as an open question
- Plain-language statement of what the document does say, a separate list of what it does not say, explicit non-advice framing, and a refusal path on pages it cannot read
- Output in the buyer's language, spoken as well as written
- Five to ten real record pages sourced and redacted before 11:30
- A stated number on pages you transcribed by hand: field and party-name accuracy on the handwritten records, and how many pages you refused rather than rendered
- One-pager: the workflow, the integration surface, the non-advice boundary, the rule that nothing ever says title is clear, and what the buyer takes to a lawyer as an open question, a deploy-or-pilot verdict, and why Document Intelligence remains primary even when rendering an archaic register is half the work

**Your demo moment.** A judge hands over an unseen handwritten record page. The system extracts it, explains two archaic terms in plain modern speech while keeping the original words visible, and flags the name that appears on the old record and nowhere on the draft as an open question for a lawyer, without claiming the deal is safe or unsafe.

**Scores on:** Sarvam parameter and Impact, both genuinely available here. **Weak on:** Delight, and the real risk is scope. One plot, one district's record format, finishable. "India's land records" is a screenshot.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam Doc AI, extracting decades-old handwritten Marathi revenue records that reach you as faded photocopies, alongside a typed deed draft. This is where the depth goes and where the score is.
- **Supporting** Sarvam-30B for archaic-register rendering, glossary building and open-question detection · Mayura plus Bulbul for the buyer's language. Plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Web app with multi-page capture and a split view, original page beside the plain-language rendering, terms tappable · plain React with Vite · a static HTML page with the page image on the left and the rendering on the right, which is all the split view is
- **Backend** Next.js route handlers · a small FastAPI or Express service · Convex functions · localhost with a tunnel, doing party matching across documents, the glossary and the refusal path on unreadable pages
- **Data** Convex · Supabase · SQLite · or none, one plot's documents held in memory, for documents, extracted parties and identifiers, the glossary and the open-questions list
- **Comms** Resend emailing the plain-language version plus the open-questions list, so it survives the meeting with the seller · Telegram bot · Loops
- **Mock or external** No external system needed · Beeceptor if you want the open-questions list handed to a lawyer's intake endpoint
- **Specific to this build** Five to ten real record pages from one district's format, redacted, sourced before 11:30. In Maharashtra that means the 7/12 extract, the mutation entries and an older handwritten record-of-rights page. State land-record portals issue these but the formats differ by state, so commit to one district and get pages you can actually read as photocopies, not clean digital exports.

**Know before you pick this.** To reach the top bands the input has to be a photographed or scanned document, not a text-layer PDF, and here the scanned handwritten records are the whole difficulty. Do not assert legal rules, registration procedure or what makes title valid. This build explains what the documents in front of it say, lists what they do not say, and sends the buyer to a lawyer with better questions. Anything it cannot read is named, not filled in.

---


## 31 ·
Voice explanation of bank products for first-time customers

**Challenging · domain · Voice Experience**

> Describe in your own words what you think you bought, and find out what the papers say you actually bought.

**Why this one.** The axis is reconciling a customer's spoken understanding against the product's actual terms and naming the mismatch out loud. First-time banking customers are aggressively mis-sold: an insurance-linked product described as a savings account, or a mutual fund and SIP pitch wrapped in returns language that hides lock-in and charges. Every existing product explainer starts from the document. This one starts from the customer's sentence, "I put money in every month and I can take it out whenever I want," and its job is to find the specific place where that belief and the paperwork diverge. That requires holding a lay mental model and a set of terms in the same head and diffing them. It is also a thin-vocabulary problem: lock-in, surrender value, exit load and expense ratio have no settled everyday word in most Indian languages, so the explanation has to be built out of ordinary speech without borrowing the jargon that caused the confusion, while still teaching the one or two English terms the customer will need at the branch counter.

**The scenario.** Padmavathi is 58 and runs a small tailoring business in Warangal. A relationship manager visited her twice and she signed for something described to her as a savings plan with better interest. Her passbook does not look like she expected, and the money she thought she could withdraw for her daughter's admission is apparently not available. She has the policy document and a phone, and she explains what she thought she was buying, in Telugu, in her own words.

**What you will need**
- Voice intake for a lay description of the product, in the customer's language, with elderly and hesitant speech as a designed condition
- Extraction of the customer's beliefs as a structured mental model: what goes in, what comes out, when, and what it costs
- One tool call for the actual terms: fetch them from the mocked product catalogue, or read them off the document she is holding
- A mismatch report, belief against term, with each divergence stated as a consequence in ordinary speech rather than a definition
- No-jargon construction of the spoken explanation, because she is not going to read a report, plus the two or three English terms she needs at the counter, taught rather than translated away
- A second product type supported, so mutual fund and SIP mis-selling is covered as well as insurance-linked products
- Named next actions, including what she can and cannot undo, framed as questions to ask the bank rather than as advice
- A stated number on ten scripted lay descriptions: how many real divergences you found against a list you wrote by hand, and how many you raised that were not there
- One-pager: the workflow, the integration surface, the non-advice boundary, the rule that no charge or lock-in is stated unless it is in the document in front of you, and what she is told to ask rather than told to do, a deploy-or-pilot verdict, and why you declared Voice Experience rather than Document Intelligence when the policy document is photographed

**Your demo moment.** A judge describes, in a regional language and in lay terms, a product they believe they bought, getting two things wrong. The agent restates the divergence in ordinary speech, names the consequence for the specific thing they wanted the money for, and does it without using a single term the customer did not already use.

**Scores on:** Delight and Impact, since the mismatch moment is the product. **Weak on:** Creativity, because this sits next to the Loan Advisory reference agent. The belief-versus-terms diff is what pulls you off the floor.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras, transcribing a 58 year old speaking hesitant Telugu about something she does not have the vocabulary for, well enough that her actual belief is recoverable from the sentence. This is where the depth goes and where the score is.
- **Supporting** Sarvam-30B for mental-model extraction and the belief-versus-terms diff · Sarvam Doc AI for the policy document if she photographs it · Bulbul for the spoken explanation, because she will not read a report. Plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Phone via Twilio or Exotel · a mobile web voice widget with push to talk plus an optional photo of the document · a single HTML page with a record button and a file input, which is enough because the output is spoken anyway
- **Backend** Convex functions · Next.js route handlers · a small FastAPI service · plain code, running the diff and generating the counter questions
- **Data** Convex · Supabase · SQLite · or none, one customer in one session needs no store, for extracted beliefs, product terms and mismatch records with her own words quoted
- **Comms** Resend and Telegram sending the mismatch summary and the counter questions in her language · ntfy.sh · Bulbul over Twilio or Exotel if you want the product to call her back
- **Mock or external** Beeceptor · Mockoon · WireMock Cloud for a product catalogue with real term structures behind it
- **Specific to this build** Two real product documents as the source of terms, one insurance-linked and one mutual fund scheme document, because lock-in, surrender value, exit load and expense ratio have to be quoted from paper and never from memory. Insurers and fund houses publish both openly on their own product pages.

**Know before you pick this.** This card absorbs the mutual fund and SIP jargon decoder, so support both product types and pick whichever you can source real documents for. It also sits directly against Sarvam's Loan Advisory cookbook agent, which means it starts at the creativity floor: an agent that explains a financial product in Hindi is the reference build. Lead with the mismatch, not the explanation. And do not state charges, lock-in periods or tax treatment that are not in the document or catalogue in front of you.

---


## 32 ·
Legal rights explainer for interstate migrant workers

**Challenging · domain · Voice Experience**

> Ask in your own language what you are owed here, and get the answer for the state you are actually standing in.

**Why this one.** The axis is jurisdiction resolution: the same question has a different correct answer in every state, and a generic national answer is not a partial answer, it is a wrong one. Minimum wage, registration requirements, which office takes a complaint, and what protections apply are all set locally, and the worker asking has moved from one jurisdiction to another and knows the rules of neither. So the build has to establish two facts before it can answer anything, where the worker is now and what work they do, then answer only from the corpus for that state, and refuse when that state is not loaded. The input side is the other half: the question arrives in Bhojpuri, Odia, Santali or a dialect that sits between two named languages, spoken by someone with no legal vocabulary at all, often on a bad line from a labour chowk. That combination, thin legal vocabulary in a low-resource dialect plus a hard jurisdictional gate, is not something a generic stack does.

**The scenario.** Bhuban came to Panipat from a village in Ganjam district eight months ago and works through a contractor. He is paid in cash, weekly, less than he was promised, and he does not know whether that is legal here, whether he was supposed to be registered, or who he would even complain to. He does not know the local language. He calls a number written on a poster at the chowk and asks in Odia.

**What you will need**
- Inbound voice in low-resource languages and dialects, over a poor line, with no menu
- Establishment of the two gating facts, current state and type of work, through conversation rather than a form
- A per-state corpus of real notifications and rules for two states only, loaded as source text
- Answers grounded only in the loaded corpus with the source named, a hard rule against stating any wage figure, entitlement or deadline that is not in it, and a clear refusal when the state is not loaded
- The complaint path as concrete next steps, which office, what to carry, what to say, in the worker's language, with one tool call handing the grievance to the mocked filing endpoint
- Spoken output, and a Telegram or SMS-style written version he can show the contractor
- A replayable set of recorded questions in at least two dialects, made before you start building
- A stated number over that question set: how many answers cited a real line in the corpus, and how many times the jurisdiction gate refused instead of answering anyway
- One-pager: the workflow, the integration surface, the non-advice boundary, what the worker must still take to the labour office, and the rule that nothing is called an entitlement unless it is in the corpus you loaded, a deploy-or-pilot verdict, and why Voice Experience remains primary even when the written version travels to the contractor

**Your demo moment.** A judge asks the same question twice in a regional language, once as a worker in state A and once in state B, and gets two different, correctly sourced answers. Then they ask as a worker in a third state and the system says plainly that it does not have that state's rules rather than answering anyway.

**Scores on:** Impact and Sarvam parameter. **Weak on:** Delight, and Creativity unless the jurisdictional gate is visibly the product rather than a filter behind it.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras, transcribing Odia, Bhojpuri or Santali from a labour chowk over a compressed phone line, from a speaker with no legal vocabulary at all. This is where the depth goes and where the score is.
- **Supporting** Sarvam-30B for the jurisdiction gate and grounded answering over the loaded corpus · Bulbul for the spoken answer · Mayura for the written version he can show the contractor. Plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Phone inbound via Twilio, Exotel or Plivo, designed for a feature phone on a noisy street · playback of your own recorded dialect questions straight into the pipeline, which is how you will actually iterate between now and 4pm
- **Backend** Convex functions · Next.js route handlers · a small FastAPI service · plain code with the two-state corpus in the system prompt, enforcing the gate and the refusal
- **Data** Convex · Supabase · SQLite · flat JSON per state on disk, for calls, resolved jurisdiction, questions asked, sources cited and every refusal logged
- **Comms** Telegram for the written version and the complaint checklist · ntfy.sh · Resend for a worker-collective coordinator digest. Not SMS, India needs DLT registration and it will eat the day
- **Mock or external** Beeceptor · Mockoon for a grievance-filing endpoint the call hands off to · httpstat.us to prove what the agent says when that filing stalls
- **Specific to this build** Real labour notifications and rules for exactly two states, loaded as source text, which state labour departments publish as notification PDFs. Two states sourced properly beats twenty-eight guessed. Plus a replayable set of recorded questions in at least two dialects, made before you write code.

**Know before you pick this.** Do not assert a minimum wage, an entitlement, a registration rule or a time limit that is not in the corpus you loaded, and do not let the model fill a gap from memory. Two states done properly, with sources on screen, beats twenty-eight states of confident guessing. Show the refusal in the demo.

---


## 33 ·
English interview coaching for first-generation students

**Challenging · domain · Voice Experience**

> Practise the interview out loud, get judged on what you said, and get told how to say it better in the language you think in.

**Why this one.** The axis is separating what was said from how it sounded. A candidate with strong technical skills and weak spoken English fails corporate interviews, and the reason coaching does not fix it is that every automated tool conflates the two: it hears an accent and a hesitation and scores the answer down, which is exactly the bias the student is already losing to. This build has to hold the two apart. Score the substance strictly, in English, on correctness and structure, with mother-tongue accent and disfluency explicitly not penalised. Then deliver the fluency feedback in the student's own language, because feedback about English delivered in English is the least useful sentence in education. Doing that means transcribing heavily accented, code-mixed, hesitant English accurately enough that the substance is even visible, which is the Saaras case rather than a generic one.

**The scenario.** Ravi is in his final year at a college in Jabalpur. He can write the code, and in his own language he can explain exactly why his approach works. In the campus mock interview he said four sentences in twelve minutes, two of them in Hindi, and stopped. The placement cell told him to improve his communication and gave him a PDF. He puts on headphones and starts a practice round.

**What you will need**
- Spoken interview practice in English, with heavy accent, code-mixing and long hesitations as designed conditions
- Substance scoring on the technical content, stated separately and explicitly accent-blind
- Delivery feedback on the specific things that are fixable: filler patterns, an incomplete sentence structure, a habitual grammar error
- Feedback delivered in the student's own language, with the English phrasing to use offered verbatim
- One tool call each way against a stored per-student error profile: read the two or three habits that recur, write a newly evidenced one with the session it came from
- A "say it again this way" loop, where the student repeats the improved phrasing and the system compares
- Four prior sessions seeded before the demo with real recorded audio, so session five can be shown, plus one round of real domain questions for the student's actual field
- A stated number: substance scores against answers you graded by hand, shown to hold when the same answer is delivered with a heavier accent, and how often each named habit recurred across the seeded sessions
- One-pager: the workflow, the integration surface, what you store of a student's recorded audio, who can see the score, and what the build refuses to penalise, since accent and disfluency are explicitly out of scope, a deploy-or-pilot verdict, and why Voice Experience remains primary even when the feedback itself arrives in another language

**Your demo moment.** A judge answers a technical question in heavily accented, code-mixed English. The system scores the substance correctly and says so, gives the fluency correction in a regional language, and then notes that this same filler habit appeared in sessions two and three and shows those sessions.

**Scores on:** Memory and Context and Impact. **Weak on:** Creativity, since interview practice is a crowded product space. The accent-blind substance score plus the cross-session error profile is your whole case.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras, transcribing heavily accented, code-mixed, hesitant English accurately enough that the technical substance underneath it is even visible to score. This is where the depth goes and where the score is.
- **Supporting** Sarvam-30B for accent-blind substance scoring and delivery diagnosis · Mayura plus Bulbul for feedback in Ravi's own language, since feedback about English delivered in English is useless. Plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Mobile web with headphones, one question at a time, a replay of the student's own audio beside the improved phrasing · a plain HTML page using MediaRecorder and two `<audio>` tags · a terminal loop that records and prints, if you would rather spend the hours on the error profile
- **Backend** Convex functions · Next.js route handlers · a small FastAPI service · plain code, holding the per-student error profile and the "say it again this way" comparison
- **Data** Convex · Supabase · Postgres · SQLite on disk, for sessions, transcripts, substance scores and named recurring habits with the sessions that evidenced them. Persistence is not optional, the seeded sessions are the entire case
- **Comms** Resend emailing a weekly progress note naming the habits that improved and the ones that did not · Telegram bot · ntfy.sh
- **Mock or external** No external system needed · Beeceptor if you want the progress note posted into a placement cell tracker
- **Specific to this build** One real domain question set for the student's actual field, written by someone who has taken that interview, plus four seeded prior sessions with real recorded audio in them rather than typed placeholders, so session five has something honest to point at.

**Know before you pick this.** Sarvam ships a Tutor reference agent, and an English-practice bot is close enough to it that this card starts at the creativity floor. The escape route is vernacular plus longitudinal memory: the build has to demonstrably remember the specific habit this learner had several sessions ago and show that it is tracking it. Seed four sessions before 11:30 and demo session five. A demo that shows only a first session is a low score.

---


## 34 ·
Online course lecture localisation for tier 3 and tier 4 students

**Beast · technical · Dubbing**

> Take a 50-minute English lecture and produce a watchable localised version where the audio still lands on the right slide at minute 47.

**Why this one.** The Dubbing axis is alignment and performance control across a long asset. Localising a two-minute clip is a demo. Localising a full lecture is an engineering problem: translated speech runs to a different length than the source, and that difference compounds, so by the end the narration is describing the previous slide, the on-screen equation, or a line of code that has already scrolled away. Fixing that means segmenting on the visual, not on the sentence, holding each segment to its own time budget and preserving pronunciation and teaching emphasis. Resumable jobs, retries, cost and throughput are required delivery evidence for the long-form dub, not a separate scoring branch. A team that produces one beautiful three-minute clip has not done this card.

**The scenario.** Ashim is in his second year of an engineering course in Siliguri and is trying to follow a well-known recorded lecture course. He can read the slides. He cannot follow academic English spoken at lecture pace, so he pauses every forty seconds, loses the thread, and gives up around week three. He has one lecture open, 50 minutes long, slides changing every couple of minutes, with code on screen.

**What you will need**
- A real full-length lecture, not a trimmed clip, with slides and on-screen text that change
- Transcription with timestamps, then segmentation aligned to visual changes rather than to sentence boundaries
- Per-segment time budgets, with compression or stretching applied inside the segment and reported, not hidden
- A drift metric measured at the start, middle and end of the asset, and shown as a number
- A resumable, idempotent job pipeline: per-segment state, retry on failure, resume without redoing completed segments
- Four named calls the pipeline exposes: submit an asset or a playlist, read per-segment status, retry a single failed segment without redoing completed ones, fetch the finished asset
- Stated throughput and cost per lecture hour, measured rather than estimated
- One deliberately hard segment, dense speech over a slide change, held back for the demo
- One-pager: the workflow, the integration surface, the licence on the source lecture and what you may republish, plus what the pipeline reports when it had to rewrite or retime speech to hold a segment budget, a deploy-or-pilot verdict, and why Dubbing is primary while resumability is delivery evidence

**Your demo moment.** Play minute 47 of a localised full lecture. The narration is on the correct slide, the drift number is on screen, and then a judge kills a segment job mid-run and the pipeline resumes from that segment rather than restarting the lecture.

**Scores on:** Sarvam parameter and Job-to-be-done. **Weak on:** Delight, since the output is a video player, and Creativity unless the drift control is visibly the invention rather than a wrapper over a dubbing call.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam's Dubbing API with Saaras timestamped transcription and Bulbul synthesis, orchestrated as a resumable per-segment pipeline over a 50-minute asset. This is where the depth goes and where the score is, and on this card the orchestration is part of the surface, not separate from it.
- **Supporting** Sarvam-Translate for the segment text · Sarvam-30B only on the hard segments where hitting the time budget needs a rewrite rather than a faster read. Plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Web app: submit a URL or upload, a job dashboard with per-segment state, a player with the drift number visible · a CLI with a progress table plus the output file opened in any player · a JSON status endpoint plus `curl`, which is a legitimate way to prove the delivery pipeline once the dubbed asset itself is strong
- **Backend** A worker queue you can kill and restart mid-run: Convex scheduled functions · Cloudflare Queues · BullMQ on Redis · Celery, with a per-segment idempotency key so a retry does not redo completed segments. ffmpeg for the cutting and the remux
- **Data** Convex · Supabase · Postgres · SQLite on disk, for assets, segments with timings and drift, job state, retry counts and measured cost per hour. Persistence is the card, resume is impossible without it. Segment audio to Convex file storage · Cloudflare R2 · S3 · the local filesystem
- **Comms** Slack or Discord webhook posting per-lecture completion with drift and cost · Resend for the batch summary · ntfy.sh for a failed segment
- **Mock or external** httpstat.us with `/random/200,500,503` and `?sleep=5000` to prove the retry and resume paths are real rather than claimed · Beeceptor's local tunnel for a live URL without deploying
- **Specific to this build** One real full-length lecture with frequent slide changes and on-screen code, downloaded before 11:30. MIT OpenCourseWare (ocw.mit.edu) and NPTEL both publish full course recordings that fit. A talking-head lecture removes the alignment problem and with it your score.

**Know before you pick this.** Pick and download your lecture before 11:30, and pick one with frequent slide changes and on-screen code, because a talking-head lecture removes the entire alignment problem and with it your score. Milestone 1 is one segment dubbed end to end, not the pipeline.

---


---

# Everyday


## 35 ·
Voice-first UPI for feature-phone migrant workers

**Beast · technical · Voice Experience**

> Send money home over a plain phone call, in your own language, with no screen to read and no menu to navigate.

**Why this one.** The axis is recoverability of a mis-hear before an irreversible action. This is the worst realistic input condition in the library: telephony-grade narrowband audio, a codec in the path, a construction site behind the speaker, and a caller who says amounts in a mix of their own language and English digits. No team is going to make word error disappear on that channel, so claiming accuracy is the losing move. The top bands go to the team that designs so a wrong transcription is always caught before money moves: read-back in the speaker's language, digits spoken back one at a time, a confidence gate that re-asks instead of guessing, and an abort word that works at any point. Cash agents take 2 to 5 per cent for solving the reading problem, which is the number this has to beat.

**The scenario.** Sujit works on a construction site in Kochi and sends money home to his family in Odisha every month. He has a feature phone with no data plan, so he hands cash to the agent outside the site gate and accepts the cut, because the number-based payment flow on his phone talks to him in English. He dials in from the site corridor at the end of a shift, with a mixer running twenty feet away, and says the amount in Odia.

**What you will need**
- Inbound call over a real telephony path, not a browser microphone, so the audio you test on is the audio you ship on
- Amount and payee recognition in a regional language with English digits mixed in
- Mandatory read-back before anything commits, in the speaker's language, digits spoken individually
- A confidence gate on the amount specifically, where a low score forces a narrower re-ask rather than a guess
- An abort word that works mid-flow, including during the read-back
- Three tool calls against the mocked rail: resolve the payee, submit the transfer, poll its status, and nothing is submitted until the read-back is confirmed
- A recorded corpus of amounts and payee names spoken over an actual phone line, collected before you build, deliberately degraded: codec compression, site noise, one dropped second
- A stated number off that corpus: how often the amount was mis-heard, and how often the read-back or the confidence gate caught it before a commit
- One-pager: the workflow, the integration surface, recording consent and what you redact before a transcript is stored, who can hear a recording of someone moving money, a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** A judge calls in from a real phone in a noisy corridor and says an amount. The read-back is correct and the transfer commits. Then the judge says something deliberately ambiguous, and instead of committing, the system re-asks a narrower question. Then the judge says the abort word halfway through a read-back and everything stops.

**Scores on:** Sarvam parameter and Impact. **Weak on:** Delight, because there is no screen to be delightful on. The confirmation loop is the whole product.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras streaming on narrowband telephony audio, with a confidence signal on the amount that is good enough to gate a commit on. This is where the score is.
- **Supporting** Sarvam-30B for amount and payee slot extraction, Bulbul for the read-back voice. All plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** An inbound phone call and nothing else. No app, no screen, no press-one menu, feature phone as the only client: Exotel · Twilio · Plivo. Exotel is usually less friction on Indian numbers, and one number pointed at a webhook is the entire interface
- **Backend** Convex functions · a small FastAPI or Express service handling the telephony webhooks · plain code with an explicit commit state machine, which is what the abort path actually needs
- **Data** Convex · Supabase · SQLite on disk · or none, hold it in memory, for payees, per-attempt transcripts with confidence, and committed versus aborted transfers. A hardcoded payee list is fine for a demo
- **Comms** An SMS receipt over Twilio or Exotel since there is no screen to show one on · a Sarvam TTS callback reading the receipt aloud · Telegram to the family member who does have a screen
- **Mock or external** Beeceptor · Mockoon for the payment rail, never a live one; Razorpay test mode if you want true response shapes and webhooks; httpstat.us with sleep to test what the voice says while a transfer is pending
- **Specific to this build** A recorded corpus of amounts and payee names spoken over an actual phone line, with site noise and one dropped second, collected before 11:30. Laptop-microphone audio will lie to you about accuracy all morning.

**Know before you pick this.** Record your test corpus over an actual phone call before 11:30. Tuning on laptop-microphone audio and discovering the telephony codec at 3:30 is how this card fails. And do not wire a real payment rail, mock it.

---


## 37 ·
Socratic homework coach that refuses to give the answer

**Challenging · domain · Voice Experience**

> A voice tutor that will not tell you the answer, and that remembers exactly where you went wrong last week.

**Why this one.** The axis is productive withholding under pressure, held across sessions. Sarvam ships a Tutor reference agent, so a tutor that explains things is the obvious build and starts at the creativity floor. The escape is that refusing to answer IS the product. A student under time pressure will plead, claim the teacher asked for it, get angry, ask for "just the first step" five times, and rephrase the problem as a hypothetical example to trick the answer out. Holding the line while still moving the student forward is much harder than answering, and it has to be enforced as a check on the output, not as a hopeful line in a prompt. The second half is longitudinal: the coach names this student's specific misconception, and session three opens on it.

**The scenario.** Sneha is in class 9 in Bhopal, stuck at nine in the evening on a word problem in her workbook. Her cousin usually just solves it, and so does every chat app on her phone. Tonight she opens the coach with the workbook flat on the table and starts by asking it to please just tell her the answer, because she has three more sums to finish.

**What you will need**
- Voice tutoring in the student's language, with maths vocabulary arriving code-mixed
- A hard no-answer rule enforced outside the prompt, as a guard on generated output before it is spoken
- Adversarial pressure handling: pleading, authority claims, hypothetical reframing, and repeated requests for one more step
- Per-student misconception records that name the specific error, not "weak in algebra"
- Session two and session three that open from the stored misconception and test whether it is actually gone
- A photographed workbook page, so the student never has to read the problem aloud
- Three recorded sessions for the same student, so a judge can see the arc rather than a first meeting
- A stated number off your adversarial script: how many attempts reached an answer out of how many were tried, and which route got closest
- One-pager: the workflow, the integration surface, what you store about a school student, who can read the misconception record, and what the note home to a parent is allowed to contain, a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** A judge plays the student and spends two minutes trying every route to the answer, including claiming the teacher demanded it. The coach never yields and the student still ends up closer. Then the judge jumps to session three, where the coach opens with the exact error from session one and checks whether it has been fixed.

**Scores on:** Memory and Context and Job-to-be-done. **Weak on:** Creativity, because Sarvam ships a Tutor agent. The refusal and the longitudinal arc are the only things lifting this card off the floor.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam-30B for the Socratic policy, the answer-leak guard run as a check on generated output before it is spoken, and misconception extraction. This is where the score is.
- **Supporting** Saaras for the student's code-mixed speech, Bulbul for the tutor voice, Sarvam Doc AI for the photographed workbook page. All plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Push to talk plus a camera capture for the workbook page: Next.js · React with Vite · a single HTML page with a record button and a file input, which is enough for a tutoring turn
- **Backend** Convex functions · Next.js route handlers · a small FastAPI or Express service. Whatever you pick, keep the leak guard as its own function that can reject and regenerate, not a line in the prompt
- **Data** Convex · Supabase · Postgres direct · SQLite on disk, for students, sessions, misconception records and every blocked answer-leak attempt. This is the one card where a store is mandatory, because session three reading session one's misconception is half the score
- **Comms** Resend · Loops · Telegram bot, sending the parent a weekly note on what the student got stuck on, with no answers in it
- **Mock or external** No external system to mock
- **Specific to this build** A real class 9 textbook exercise set, photographed from the book rather than retyped, three recorded sessions for the same student with the misconception carried across them, and a written adversarial script: pleading, an authority claim, a hypothetical reframing, and five separate requests for just the first step.

**Know before you pick this.** Sarvam ships a Tutor reference agent, so a demo showing only a first session is a low score no matter how good the conversation is. Build and record three sessions for one student, with the misconception carried across them, and get that done before 2:30. Also attack your own answer-leak guard: prompt instructions alone will leak the answer to a determined student inside five turns.

---


## 38 ·
Scam pattern detection for elderly relatives

**Challenging · domain · Voice Experience**

> A layer on an elderly parent's calls that recognises a scam by its shape rather than its script, and pulls a family member in while the call is still live.

**Why this one.** The axis is manipulation structure detection independent of wording. Around 90 per cent of cybercrime victims in Bengaluru are seniors, and digital arrest scams have caused large losses, which means the scripts work and they change constantly. A keyword list is obsolete in a week and useless the moment the call arrives in a different language. What does not change is the structure: a manufactured authority, an urgency clock, an instruction to stay on the line, an instruction to tell nobody, then an escalation to payment or remote access. Detecting that shape from live speech, in whichever language it arrives, and doing it before the escalation step, is the whole build. The benign lookalike matters as much: a genuine bank verification call also asks for details, and a system that screams at both gets uninstalled.

**The scenario.** Kamala is 74 and lives alone in Pune. Her son is in another city. A caller says he is from a courier company about a parcel in her name, then hands her to a second person claiming to be police, who tells her to stay on the line and not to tell anyone in the family. Her phone is lying face up on the dining table on speaker.

**What you will need**
- Live call audio transcribed continuously, in whichever language the caller uses
- The pattern written as structure, not vocabulary: authority claim, urgency, isolation instruction, secrecy instruction, escalation to payment or screen sharing
- A score that rises as the structure completes, so one suspicious phrase is not enough and four in sequence is
- Intervention while the call is live: a spoken prompt to the senior in her language, plus an immediate alert to the family member
- A benign set including a genuine bank verification call, so the demo shows the quiet case too
- Three scam scripts recorded in three languages, plus two ordinary calls, before you start building
- Two tool calls when the score crosses: alert the named family member with the reason and the current score, and write the call record with the per-window scores behind it
- A stated number: detections across your scam set and false positives across the benign set, reported separately for the language you did not tune on
- One-pager: the workflow, the integration surface, what audio is captured off a live call, whose consent covers capturing it, who can replay it and how long it is kept, a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** Play a scam call the system has never heard, in a language you did not tune on. The score climbs at the isolation instruction and the family member's phone rings before payment is ever mentioned. Then play a real bank verification call and the system stays silent.

**Scores on:** Sarvam parameter and Impact. **Weak on:** Delight, and Creativity collapses if you present this as a blocklist of phrases.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam-30B for structural pattern scoring across a rolling window, scoring the shape of the manipulation rather than its vocabulary. This is where the score is.
- **Supporting** Saaras streaming for continuous multilingual transcription, Bulbul for the spoken warning to the senior. All plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** A monitored call rather than an intercepted one: a bridged or recorded call over Exotel · Twilio · Plivo, or a recording played into the same pipeline, plus a family view that can be one HTML page with a rising score on it
- **Backend** Convex functions · a small FastAPI or Express service · plain code with a rolling window over transcript chunks, which needs no orchestration framework
- **Data** Convex · Supabase · SQLite on disk · or plain JSON files on disk, for monitored calls, per-window pattern scores, interventions and every false positive on the benign set. Keep the benign-set results, they are your evidence
- **Comms** An outbound call and message to the family member over Twilio or Exotel · Telegram bot for the live running transcript · ntfy.sh or a Slack webhook if you want an alert in seconds with no setup
- **Mock or external** No external system to mock
- **Specific to this build** Three scam scripts you write and record yourself, in three languages, plus two ordinary calls including a genuine bank verification call for the quiet case. Never use recordings of real victims. Also settle in one sentence what you actually hooked into, bridged or recorded, and say it at the start of the demo.

**Know before you pick this.** Be honest about what you actually hook into. Bridging or recording a call is buildable in five hours; sitting inside the phone's dialler is not. Say which one you built, in one sentence, at the start of the demo, because a judge who works it out for themselves will discount everything after it.

---


## 39 ·
Handwritten prescription verification for patients

**Beast · domain · Document Intelligence**

> Photograph the prescription in your hand and find out what it says, or be told clearly and specifically which line cannot be read safely.

**Why this one.** The axis is calibration of the abstain rate. Doc AI's real hard edge is handwriting, and this is the highest-consequence handwriting in the library: a mis-read here reaches a person's body through a pharmacy counter. Note that a system which abstains on everything is perfectly safe and completely useless, and one that never abstains is dangerous. So the score is not refusal, it is whether the threshold discriminates. A judge should be able to hand over a line that merely looks messy and get it read correctly, then hand over a line that is genuinely ambiguous between two similar-looking names and watch the system decline and name both candidates. Confidence has to be a number that moves the right way under testing, and the team should be able to state a real error rate on the lines they did answer and a real abstain rate on the lines they did not.

**The scenario.** Rukmini is standing at a pharmacy counter in Patna holding a three-line prescription written in her doctor's hand. The pharmacist has just read the middle line out as something different from what she remembers being told in the consulting room, and is already reaching for a box. She photographs the slip on the counter under the shop's tube light, at an angle, with the pharmacist's pen still resting on it.

**What you will need**
- Camera capture of a handwritten prescription at phone quality, uneven light, slight skew
- Doc AI extraction per line, with per-line and per-token confidence
- An abstain state that is per line rather than per document, so two readable lines are still useful
- A look-alike check as one named tool call: put each captured token against the published confusable-names reference you loaded, and where it comes back with a pair, abstain and name both candidates rather than choosing
- A held-out set with ground truth confirmed by the prescriber, so you can state two real numbers: the error rate on the lines you answered, and the abstain rate on the lines you did not
- Spoken output in the patient's language, because the person holding the phone may not read
- Framing that says plainly this verifies against the pharmacist and the doctor and replaces neither
- One-pager: the workflow, the integration surface, the escalation path back to the pharmacist and the prescriber, what the build refuses to decide, and where every clinical string was sourced from, a deploy-or-pilot verdict, and why you declared Document Intelligence rather than another branch

**Your demo moment.** A judge photographs a handwritten prescription the system has never seen. It reads two lines, and on the third it abstains and names the two candidates it is stuck between rather than picking one. Then the judge hands over a line that merely looks illegible, and it reads that correctly, which is what proves the abstain was discrimination and not a hedge.

**Scores on:** Sarvam parameter, decisively. **Weak on:** Delight, and Creativity if this presents as OCR with a spinner. Your stated error and abstain rates are what make this a beast card rather than a demo.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam Doc AI on handwritten prescriptions, with per-line and per-token confidence you can actually set a threshold against. This is where the score is.
- **Supporting** Sarvam-30B for look-alike candidate reasoning and plain-language phrasing, Mayura plus Bulbul for the patient's language. All plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Camera capture with a per-line result carrying an explicit unreadable state and an audio button: Next.js · React with Vite · a single HTML page with a capture input and three result rows, which is the whole thing
- **Backend** Convex functions · Next.js route handlers · a small FastAPI or Express service · a terminal script over a folder of images, which is how you should be running your calibration sweep anyway
- **Data** Convex · Supabase · SQLite on disk, for page images, per-line extractions with confidence and abstain records. Your ground-truth set is happiest as a CSV in the repo beside the images rather than as rows in a database
- **Comms** Resend · Telegram bot · ntfy.sh, sending the patient or a family member the readable lines plus the flagged line, worded as a question to ask the pharmacist
- **Mock or external** No external system to mock
- **Specific to this build** A published confusable-drug-name reference, not one you write from memory: the ISMP list of confused drug names is the standard published source for look-alike pairs, so find the current version, cite it in your output, and do not paste an address you have not opened. Plus 15 to 20 real handwritten prescriptions, redacted, in several hands, with ground truth confirmed by the prescriber on the held-out set.

**Know before you pick this.** To reach the top bands the input has to be a photographed or scanned document, not a text-layer PDF, and specifically handwritten, which is Sarvam Doc AI's real hard edge. Collect those prescriptions before 11:30 in several different hands. And do not assert any drug name, dose, reference range or substitution rule from your own knowledge: every clinical string in this build, including the look-alike pairs, must be sourced from an authoritative published reference before this goes in front of anyone, and the interface copy must say the output is to be checked with a pharmacist. The behaviour being scored is the calibrated abstain, not your pharmacology.

---


## 40 ·
Active safety check-ins during solo cab rides

**Beast · technical · Voice Experience**

> During a late-night ride the phone asks a short question out loud, and works out from how she answers whether to escalate.

**Why this one.** The axis is distress discrimination against an expensive false positive. Sharing a trip link is passive: it tells someone where you were after the fact. An active layer has to make a judgment, and the content of the answer is close to useless, because "I am fine" is exactly what a frightened person says with a driver a foot away. The signal is paralinguistic: a whisper, a clipped one-word answer, a change in rate or tremor measured against her own baseline, combined with context like a stopped car or a route deviation. And the false positive is not free. Two wrong escalations and the feature is switched off forever, so the top bands need a stated precision and recall on the team's own labelled recordings, plus a near miss in the demo that the system deliberately does not escalate.

**The scenario.** Ananya finishes a late shift and books a cab from Gurugram close to midnight. Her phone is face up in her lap, the driver has taken a turn off the mapped route without saying anything, and her mother has the trip link and is asleep. The check-in asks her a short question in Hindi, quietly, and she has to answer it with the driver listening.

**What you will need**
- A periodic spoken check-in in her language, answerable in one word, phrased so it does not announce itself to a driver sitting beside her
- A silent path: a codeword or a tap that reads as an ordinary answer
- Paralinguistic features alongside content: volume, whisper detection, speech rate, hesitation, all measured against a baseline she records at the start of the ride
- Your own labelled recording set covering calm, annoyed, distracted and distressed answers, with a stated precision and recall off it rather than a claim
- Graded escalation as three named tool calls: read the mocked trip feed for a stop or a route deviation, notify the named contact, then open a control-room case, each step cancellable by her
- One explicit non-escalation case in the demo, so the judge sees the discrimination
- One-pager: the workflow, the integration surface, what audio is kept from a ride nobody escalated, who can listen to it, and who is allowed to trigger a control room on a machine judgment, a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** A judge answers a check-in irritably with a podcast playing, and nothing escalates. Then the judge answers the identical question in a whisper, and escalation fires within one turn, with the reason shown as the specific features that moved.

**Scores on:** Sarvam parameter and Impact. **Weak on:** Delight, and Job-to-be-done unless the silent path is genuinely usable with a driver listening.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam-30B for the combined content-plus-paralinguistics judgment and the graded escalation ladder, with a stated precision and recall on your own labelled set. This is where the score is.
- **Supporting** Saaras for the answer transcript and the acoustic pass, Bulbul for a deliberately calm check-in voice. All plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Mobile web with the screen kept awake, one large button, audio in and out: Next.js · React with Vite · a single HTML page using a wake lock, MediaRecorder and an audio element, which is genuinely all of it
- **Backend** Convex functions · Next.js route handlers · a small FastAPI or Express service · plain code with a timer and a state machine for the ladder
- **Data** Convex · Supabase · SQLite on disk, for rides, check-ins, extracted features and escalation decisions. Your labelled evaluation set belongs in a folder of clips with a CSV of labels, not in a database
- **Comms** An outbound call and message to the named contact over Twilio or Exotel · Slack or Discord webhook standing in for a control room · ntfy.sh for a push that needs no signup
- **Mock or external** Beeceptor · Mockoon · WireMock Cloud for a trip feed with a scripted route deviation. Do not touch a real ride-hailing API, and never wire a live emergency number to a simulated event
- **Specific to this build** Your own labelled recording set: calm, annoyed, distracted and distressed answers to the identical question, recorded with real people in vehicle noise or in a moving vehicle, before you write the classifier. Set the threshold from that set, not from the one take you rehearsed.

**Know before you pick this.** Record your labelled set with real people, in a moving vehicle or at least in vehicle noise, before you write the classifier, and set your threshold from that set rather than from the one take you rehearsed. Also, never wire a live emergency number to a simulated distress event.

---


## 42 ·
Voice-first digital task assistant for elderly parents

**Challenging · domain · Voice Experience**

> An elderly parent says what they need done, in their own words and their own time, and it gets done.

**Why this one.** The axis is patience: endpointing and repair on dysfluent elderly speech. 41 per cent of Indian elders own smartphones but only 5 per cent use online banking or health apps, and the reason is not that the apps are in English, it is that every voice assistant they have tried cuts them off. Older speech is slower, pauses mid-sentence to find a word, restarts, repeats, and corrects a number halfway through. Default endpointing treats a three-second pause as the end of a turn and confidently answers the first half of the sentence. The depth here is knowing when a turn has actually ended, taking the corrected value rather than the first one, and never once saying "sorry, please start again."

**The scenario.** Bimal Sen is 71, in Kolkata, and has three things to do: pay an electricity bill, book a diagnostic test, and check whether his pension has credited. His son installed three apps on his phone and he opens none of them. He speaks Bengali with English words for the bank and the bill, pauses for several seconds in the middle of a sentence to find the word for the test, and misspeaks one digit of an account number before correcting himself.

**What you will need**
- Endpointing tuned for long mid-sentence pauses, validated against real recordings of older speakers rather than your own voice
- Self-correction handling where the last stated value wins, and the assistant says back which value it took
- No dead ends: every failure path re-asks one narrower question instead of restarting the task
- Task state that survives an interruption, so a dropped call or a doorbell resumes at the right step
- Three named tool calls against mocked services, each with a spoken confirmation of what was actually done: pay the electricity bill, book the diagnostic test, check whether the pension has credited
- Recordings of at least three older speakers, including one who talks over the assistant
- A stated number off those recordings: how often a mid-sentence pause was cut off as the end of a turn, before and after you set the silence threshold
- One-pager: the workflow, the integration surface, what the assistant is allowed to do without a second confirmation, what the son can see of his father's calls, and what is stored about a bill or a health booking, a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** A judge speaks a request with a four-second pause in the middle and misspeaks a number before correcting it. The assistant waits through the pause, takes the corrected number, says it back, and completes the task. Then the judge interrupts mid-task, comes back, and it resumes at the right step rather than from the top.

**Scores on:** Job-to-be-done and Delight. **Weak on:** Creativity, since assistants for elderly parents are an expected build. Endpointing that genuinely waits is the differentiator, and it is invisible unless you demo the pause on purpose.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras streaming with endpointing and dysfluency handling tuned so a four-second mid-sentence pause is not read as the end of a turn. This is where the score is.
- **Supporting** Sarvam-30B for intent, slot repair and task state, Bulbul for a slower, clearer voice. All plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Mobile web, one very large button, high contrast, spoken summaries instead of a screen of text: Next.js · React with Vite · a single HTML page with one button and an audio element, which suits this user better than anything with routing in it
- **Backend** Convex functions · Next.js route handlers · a small FastAPI or Express service · Sarvam Agents if you want the interrupted task genuinely resumable from a checkpoint
- **Data** Convex · Supabase · SQLite on disk · or none, hold it in memory, for users, tasks, the full slot history including superseded values, and resumable task state. Server-side in-memory state is enough to demo a resume inside one session
- **Comms** An SMS or a Sarvam TTS callback to the son after each completed task over Twilio or Exotel · Telegram bot if he uses it · Resend for a weekly digest
- **Mock or external** Beeceptor · Mockoon · WireMock Cloud for the biller, the diagnostic lab and the pension enquiry; httpstat.us with sleep so you are forced to say something while a payment is pending
- **Specific to this build** Recordings of at least three older speakers, including one who talks over the assistant, made first thing and used to set the silence threshold. Default endpointing settings fail this card outright.

**Know before you pick this.** Default endpointing settings will fail this card outright. Record three older speakers first thing and tune the silence threshold against those clips. If you tune on a 25-year-old developer's speech you will build the same assistant they already refuse to use.

---


## 47 ·
Post-hospital discharge instructions in the patient's language

**Challenging · domain · Document Intelligence**

> Photograph the discharge summary and get back a day-by-day plan in the patient's language, with everything the summary does not actually settle listed as a question for the doctor.

**Why this one.** The axis is turning shorthand into a time-anchored plan, with the unexpanded parts escalated rather than smoothed over. A discharge summary is not prose, it is compressed notation written by one doctor for another, and translating it faithfully word for word produces a fluent document that is just as unusable in Marwari as it was in English. The job is to convert it into three concrete things: what to take and when, which date to come back, and which symptom means come back now. Readmissions happen when one of those three is misunderstood. Which is why anything the system cannot expand with confidence belongs on a questions list, not blended into the plan: a plan that reads beautifully and quietly drops one instruction is worse than one that admits a hole.

**The scenario.** Mangilal is discharged from a hospital in Bikaner after four days. He is handed two printed sheets in English medical shorthand, with the follow-up date filled in by hand at the bottom and a signature running across part of it. His daughter photographs both sheets in the corridor while they wait for the discharge clearance, and neither of them can read a line of it.

**What you will need**
- Multi-page photographed summary ingestion, including the handwritten follow-up date
- Extraction split into three separate outputs: a medication schedule with times, dated follow-up actions, and warning signs
- Shorthand expansion with an explicit unexpanded list, rather than a plausible guess
- Vernacular output that survives a listener who does not read: spoken, short sentences, one instruction at a time
- A completeness check that states what a discharge plan should contain and flags what this particular summary is missing
- Two real summaries from different hospitals, so you are not fitting one layout, with one held back unseen for the demo
- Two tool calls off the extracted plan: schedule the dated follow-up reminders, and send the question list to the doctor or to the family member who can ask on his behalf
- One-pager: the workflow, the integration surface, the escalation path back to the discharging hospital, what the build refuses to expand, and the published reference every expansion traces to, a deploy-or-pilot verdict, and why you declared Document Intelligence rather than another branch

**Your demo moment.** A judge hands over a discharge summary the system has never seen. Out comes a spoken day-by-day plan in the patient's language, plus a short list of things the summary does not settle, including one abbreviation the system explicitly declines to expand and sends to the doctor instead.

**Scores on:** Job-to-be-done and Impact. **Weak on:** Creativity, and Sarvam parameter unless the input is genuinely photographed, handwritten follow-up date included.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam Doc AI on the multi-page photographed summary, including the handwritten follow-up date at the bottom with a signature running across it. This is where the score is.
- **Supporting** Sarvam-30B for shorthand expansion, the completeness check and plan construction, Mayura plus Bulbul for the patient's language. All plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Multi-page camera capture, then a plan view with a play button per section: Next.js · SvelteKit · plain HTML with a multiple file input and three collapsible sections, which is the plan
- **Backend** Convex functions · Next.js route handlers · a small FastAPI or Express service · localhost with a tunnel
- **Data** Convex · Supabase · SQLite on disk · or none, hold it in memory, for summaries, extracted schedules and the unexpanded list. Reminder state is the only piece that wants to persist, and firing the reminder by hand in the demo is a legitimate shortcut
- **Comms** Resend · Telegram bot to the daughter with the plan and the question list, plus dated reminders over Twilio or Exotel · ntfy.sh · Cal.com if you would rather put the follow-up in a calendar than in a message
- **Mock or external** No external system to mock
- **Specific to this build** Two real discharge summaries from different hospitals, redacted, photographed rather than exported, at least one with a handwritten follow-up date. Every abbreviation expansion has to come from an authoritative published clinical reference, and anything not in that reference goes on the question list by default.

**Know before you pick this.** To reach the top bands the input has to be a photographed or scanned document, not a text-layer PDF. And do not expand a clinical abbreviation, dose, timing or warning sign from your own knowledge. Every expansion has to come from an authoritative published reference before this is published, and anything not in that reference goes on the question list by default. The behaviour being scored is the honest gap list, not your clinical vocabulary.

---


## 48 ·
Traffic e-challan verification for drivers

**Challenging · domain · Document Intelligence**

> Photograph the challan you were sent, find out whether it can be verified at all, and get told the one place it can actually be paid.

**Why this one.** The axis is authenticity verification rather than content extraction. Reading the notice is the easy half; the question the driver is actually asking is whether to trust it, and the honest answer from an image alone is frequently "I cannot tell." So the product has to separate what it can read from what it can verify: extract the checkable identifiers, put them against an authoritative lookup, and where the lookup has nothing, say unverified with specific reasons rather than rendering a green tick. A system that confidently declares a forged notice genuine has done the scammer's work for them, and one that declares a real notice fake costs the driver a late fee. Three states, not two, is the design decision this card is really about.

**The scenario.** Rakesh drives a taxi in Kanpur and in one week receives two challan messages: an SMS with a shortened link and an amount, and a PDF naming a stretch of road he has not driven on this month. A printed notice has also been left under his wiper. He screenshots the SMS and photographs the printed notice on the bonnet of the car.

**What you will need**
- Ingest a photographed printed notice and a screenshotted SMS, not a clean PDF
- Extraction of the checkable identifiers: vehicle number, notice number, date, place, amount
- Two tool calls against the authoritative lookup, mocked for the sprint: verify the notice by its number and vehicle, and pull the outstanding list for that vehicle, with a real unverified state when either returns nothing or times out
- Consistency signals the image alone supports: vehicle number that is not his, a payment link on a domain that is not the official one, an amount inconsistent with the stated category
- Plain-language spoken explanation in the driver's language, with an explicit instruction never to pay through a link inside a message
- One genuine notice and one forged notice in your demo set, deliberately similar to look at
- One-pager: the workflow, the integration surface, provenance for every field you claim to have verified and for every field you could not, the official channel the driver is sent to instead, a deploy-or-pilot verdict, and why you declared Document Intelligence rather than another branch

**Your demo moment.** A judge hands over two notices that look alike. One comes back verified against the lookup. On the other the system does not say fake, it says unverified, lists the specific reasons, and names the official channel where the driver can check for himself.

**Scores on:** Job-to-be-done and Impact. **Weak on:** Creativity, and Delight unless the verdict is genuinely three states rather than a red or green tick.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam Doc AI on the photographed printed notice and the screenshotted message, pulling the checkable identifiers out of both. This is where the score is.
- **Supporting** Sarvam-30B for the consistency checks, the three-state verdict and the plain-language wording, Mayura plus Bulbul for the driver's language. All plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Camera capture plus screenshot upload, then a three-state verdict card with an audio button: Next.js · React with Vite · a single HTML page with a file input and a verdict block, which is enough for three states
- **Backend** Convex functions · Next.js route handlers · a small FastAPI or Express service · Cloudflare Workers
- **Data** Convex · Supabase · SQLite on disk · or none, hold it in memory, for notices, extracted fields, verification results and verdict history per vehicle, since one verification is a single session
- **Comms** An SMS or a Sarvam TTS callback with the verdict and the official channel over Twilio or Exotel · Telegram bot · Resend for a copy with the extracted fields
- **Mock or external** Beeceptor · Mockoon · WireMock Cloud for the authoritative lookup, returning found, not found and timeout; httpstat.us with sleep for the timeout case, which is the state every team skips and the one a judge will ask about
- **Specific to this build** One genuine notice and one forged notice, deliberately similar to look at, both photographed rather than exported. Name the official state or national challan channel in your copy instead of reproducing an address: a URL you have not opened, printed under the words "pay here", is the exact failure this card exists to prevent. Never open a link from a suspicious message during the demo.

**Know before you pick this.** To reach the top bands the input has to be a photographed or scanned document, not a text-layer PDF. Do not state a fine amount, an offence code, a payment window or an appeal route from your own knowledge: every such detail must be sourced from the official state or national channel before publishing, and the safest interface copy names that channel instead of reproducing its rules. Never open a link from a suspicious message during the demo.

---


## 50 ·
Aadhaar update navigator for citizens with cascading deadlines

**Challenging · domain · Document Intelligence**

> Show it every confusing message and letter you have received, and get back one ordered list with exactly one thing to do next.

**Why this one.** The axis is dependency ordering across cascading obligations. Each notice on its own is answerable, and plenty of tools will explain one. The difficulty is that they interact: the bank cannot complete its re-KYC until the underlying record is updated, and doing them in the wrong order means a wasted morning at a counter and occasionally a step that has to be redone. So the product is a sequencer, not an explainer. It normalises several partly overlapping obligations, works out what blocks what and shows why, collapses the two messages that are actually the same obligation, and surfaces exactly one next action with the documents needed to complete it. Sorting by deadline is not enough, because the most urgent item is sometimes the one that cannot be done yet.

**The scenario.** Sushila works as a nurse in Ranchi and in one month has collected four things she does not understand: a message about a biometric update, a message about linking a number, a letter from her bank about re-KYC, and a printed slip from a service centre she visited once and left confused. She photographs the two paper items and screenshots the two messages, all in one go.

**What you will need**
- Mixed-input ingestion: photographed letters, a printed counter slip, screenshots of messages
- Extraction into a normalised obligation shape: what is asked, by whom, by when, and what is needed to do it
- Dependency reasoning that states which obligation blocks which, with the reason visible rather than implied
- One ordered plan with exactly one next action, its document list, and where it can be done
- Duplicate and conflict collapsing, so two messages about the same obligation become one item
- An unknown state, so an obligation the system cannot classify is surfaced for a human instead of quietly dropped
- One tool call per obligation: ask the mocked status lookup whether that step has already been completed, so a finished item drops out of the plan rather than sitting at the top of it
- Spoken output in the citizen's language
- One-pager: the workflow, the integration surface, what identity documents you store and what you redact off the images, the issuing authority every obligation and dependency is sourced from, a deploy-or-pilot verdict, and why you declared Document Intelligence rather than another branch

**Your demo moment.** A judge drops in four photographed notices including a deliberate duplicate and one deliberately vague. Back comes a single ordered plan that explains why item two cannot be started until item one is complete, folds the duplicate into one entry, and puts the vague one in an unknown bucket rather than guessing at it.

**Scores on:** Job-to-be-done and Delight. **Weak on:** Sarvam parameter unless the inputs are genuinely photographed, and Creativity if this renders as a flat to-do list with the dependencies invisible.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam Doc AI, extracting across photographed letters, a printed counter slip and message screenshots submitted in one batch. This is where the score is.
- **Supporting** Sarvam-30B for normalisation, dependency reasoning and duplicate collapsing, Mayura plus Bulbul for the citizen's language. All plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Batch capture of several documents at once, then one ordered plan with an expandable why per item: Next.js · SvelteKit · plain HTML with a multiple file input and a details element per item, which gives you the expandable why for free
- **Backend** Convex functions · Next.js route handlers · a small FastAPI or Express service · plain code with a topological sort, which is what the dependency ordering actually is
- **Data** Convex · Supabase · SQLite on disk · or none, hold it in memory, for documents, normalised obligations, dependency edges and plan state. Keep the dependency graph as a configurable data file either way, so a wrong rule is a one-line fix
- **Comms** An SMS carrying only the next action over Twilio or Exotel · Telegram bot · ntfy.sh · Resend for the full plan
- **Mock or external** Beeceptor · Mockoon · WireMock Cloud, for a status lookup that reports whether a step has already been completed
- **Specific to this build** Four real inputs collected before you start: two photographed paper items, one of them a printed counter slip, and two message screenshots, with one deliberate duplicate and one deliberately vague. Source every dependency from the issuing authority and keep it in that configurable file, not in copy.

**Know before you pick this.** To reach the top bands the input has to be a photographed or scanned document, not a text-layer PDF. Do not encode any actual deadline, eligibility condition, fee or document requirement from your own knowledge. Source every rule and every dependency from the issuing authority before publishing, and until you have, keep the dependency graph as configurable data rather than baking it into copy. The sequencing behaviour is what is being scored, not the specific rules.

---


## 52 ·
Regulatory circular translation for tier 2 compliance teams

**Challenging · domain · Document Intelligence**

> Feed in the circular the day it lands and get back only the paragraphs that bind your entity, each one traceable to the line it came from.

**Why this one.** The axis is applicability filtering with paragraph-level traceability. A 40 to 100 page circular is mostly not about you. A small NBFC, a co-operative bank or a regional stockbroker needs the handful of paragraphs that touch its licence category, its size band and the products it actually sells, and the value the system creates is in what it correctly leaves out. That makes hallucination fatal in a very specific way: a compliance officer cannot act on an obligation they cannot trace, so every stated obligation has to point back to its paragraph with the line quoted beside it, and a paragraph whose applicability is genuinely unclear has to be marked unclear rather than asserted or dropped. This card is underrated because Impact is easy to earn honestly: a real compliance team can tell you how many days a circular currently takes to become an internal action list.

**The scenario.** Nabanita is the compliance officer at a co-operative bank in Guwahati with a two-person team and an audit the same week. A circular arrives as a scanned PDF, and she has to work out which paragraphs touch a bank of her size and licence, then hand her board something readable in Assamese as well as English. She runs the circular through the office multifunction printer's scanner and gets a skewed, slightly grey copy.

**What you will need**
- Scanned circular ingestion with page and paragraph numbering preserved, because traceability depends on it
- An entity profile: licence category, size band, products offered, so applicability has something concrete to be judged against
- A per-paragraph applicability verdict in three states: applies, does not apply, unclear
- Every stated obligation linked to its paragraph, with the source line shown next to it
- An action list derived only from applicable paragraphs, with dates taken from the circular rather than inferred
- A vernacular version for a board that does not read regulatory English, alongside the English original
- Two circulars from different regulators, so you are not fitting one house style, with one of them marked up by hand so you can state two numbers: how many paragraphs you correctly left out, and how many applicable ones you missed
- One tool call: post each newly applicable obligation, with its paragraph reference attached, into the compliance channel
- One-pager: the workflow, the integration surface, paragraph-level traceability, what the system marks unclear rather than asserting, and who signs off before an obligation reaches a board, a deploy-or-pilot verdict, and why you declared Document Intelligence rather than another branch

**Your demo moment.** A judge feeds in a scanned circular the system has never seen, with an entity profile it was not tuned on. It returns a short applicable set out of a long document, and for every obligation the judge can click straight through to the exact paragraph. One paragraph comes back marked unclear, with the reason stated.

**Scores on:** Job-to-be-done and Impact. **Weak on:** Delight, and Creativity unless the entity profile is genuinely doing the filtering rather than a keyword match wearing a profile's clothes.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam Doc AI for scanned circular extraction with page and paragraph numbering preserved, because the traceability this whole card rests on is positional. This is where the score is.
- **Supporting** Sarvam-30B for the applicability judgment and cited obligation extraction, Mayura for the vernacular board version. All plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Scanned upload, an entity profile form, and a filtered obligation list with the source paragraph beside it: Next.js · SvelteKit · a two-column HTML page with a file input and a hardcoded profile object, which is enough to prove the filtering
- **Backend** Convex functions · Next.js route handlers · a small FastAPI or Express service · a terminal script that takes a scan and an entity profile JSON and prints the applicable set, which is a completely legitimate 4pm demo for this card
- **Data** Convex · Supabase · SQLite on disk · or none, hold it in memory, for circulars, paragraphs, applicability verdicts, obligations with paragraph references and the entity profile, since one circular per run is a single session
- **Comms** Slack or Discord webhook posting new applicable obligations into the compliance channel · Resend for the board summary · Telegram bot if the team does not live in Slack
- **Mock or external** No external system to mock
- **Specific to this build** Two real published circulars from different regulators, scanned rather than downloaded as text, so the extraction is doing real work; put them through an office multifunction scanner if you want the skew and the grey. Every obligation the system states must be a quote or a citation from the document in front of it. Also one real compliance person on the phone before 11:30, for the current turnaround number that becomes your Impact score.

**Know before you pick this.** To reach the top bands the input has to be a photographed or scanned document, not a text-layer PDF, and scanned circulars are easy to source, so there is no excuse for a clean one. Do not restate a regulatory obligation, threshold, exemption or deadline from your own knowledge: every claim the system makes must be a quote or a citation from the document in front of it, and any rule that appears in your interface copy has to be sourced from the regulator before publishing. Also get a real compliance person on the phone before 11:30 and write down their current turnaround, because that number is your Impact score.

---


## 54 ·
YouTube video localisation for Indian creators

**Challenging · fun · Dubbing**

> Upload one video and ship it in supported languages with a consistent, consented voice and the narration still landing on the same cuts.

**Why this one.** The axis is performance and timing preserved across languages. Producing a translated audio track is a solved afternoon. What separates this build is that the localised version keeps a consistent consented voice, carries the creator's pace and emphasis, and fits inside the original timing so the words land on the cut and on the on-screen text they refer to. If Creative Dubbing with same-speaker capability is actually provisioned, preserving the creator's identity becomes an additional proof; otherwise do not claim cloning from the base voice APIs. Duration is the enemy, and the fix is rewriting the line to fit rather than speeding the audio into a chipmunk.

**The scenario.** Kavya runs a cooking channel in Jaipur, in Hindi, and her analytics show viewers in Tamil Nadu and West Bengal dropping off in the first minute. Studios quote her ₹10,000 to 25,000 per video for dubbing, which she cannot justify on an upload schedule. She uploads an eight-minute video with three quick cuts and a lot of on-screen text, including one stretch where she talks fast over a list.

**What you will need**
- Real video upload, transcribed with timings rather than a pasted script
- Segment-level translation constrained to fit the original segment's duration
- Target-language speech that carries the creator's delivery: pace, emphasis and energy, using a stable named voice; same-speaker identity only when Creative Dubbing access is actually provisioned
- Timing reconciliation that rewrites an over-long line instead of compressing the audio into a chipmunk
- A per-segment drift report in milliseconds, with the worst segment stated rather than hidden, so alignment is a measurement and not a claim
- A side by side player, original and localised, with the same cut visible in both
- One deliberately hard segment: fast delivery over on-screen text
- One-pager: the workflow, the integration surface, which voice you used, the permission and disclosure around it, whether same-speaker capability was actually provisioned, a deploy-or-pilot verdict, and why Dubbing is primary

**Your demo moment.** Play the same thirty seconds in the source and a supported target language over the same video. The cut lands on the same beat, the named target voice stays consistent and the drift report shows the worst segment rather than hiding it. If same-speaker Creative Dubbing is provisioned, add the consented identity comparison.

**Scores on:** Sarvam parameter and Delight. **Weak on:** Impact unless a real drop-off figure or the quoted dubbing cost is visible, and Job-to-be-done if you never render an actual video file.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam Creative Dubbing if event access is provisioned; otherwise Saaras, duration-constrained adaptation, a stable named Bulbul voice and ffmpeg, preserving pace, emphasis and cut alignment without claiming same-speaker cloning. This is where the score is.
- **Supporting** Saaras for the timed transcript, Mayura for duration-constrained segment translation. All plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Video upload, a side by side player with the original and the localised version, and a per-segment drift table: Next.js · React with Vite · a single HTML page with two video elements and a table, which is exactly the demo
- **Backend** Convex functions · Next.js route handlers · a small FastAPI or Express service · a local script driving ffmpeg, since rendering is a batch job and does not want to be a web request
- **Data** Convex · Supabase · SQLite on disk · or the local filesystem plus a JSON manifest per video and no database at all, for videos, segments with timings, per-language tracks and drift measurements; renders to Convex file storage, Supabase Storage, R2 or just a folder
- **Comms** Slack or Discord webhook when a render finishes · Resend with the download link · ntfy.sh for a push while you wait
- **Mock or external** ffmpeg locally for muxing. No external service needed
- **Specific to this build** A video you own, around eight minutes, with real cuts, on-screen text and one stretch of fast delivery over a list. Lock a sixty second demo cut before you render anything: four languages across eight minutes will eat the afternoon.

**Know before you pick this.** Have a video you own, with real cuts and on-screen text, ready before 11:30. Rendering eight full minutes in four languages will eat the afternoon, so lock a sixty second stretch as your demo cut and render the rest only if there is time left at 4:00.

---


## 55 ·
Government scheme explainer video localisation for rural rollout

**Challenging · domain · Dubbing**

> Take the English scheme explainer and ship versions people can actually answer questions about, in the languages the rollout needs, on launch day.

**Why this one.** The axis is output validated by listener comprehension rather than by translation similarity. Every localisation demo measures fidelity to the source, and a perfectly faithful rendering of bureaucratic English is still incomprehensible to the person the scheme exists for. So this build is judged at the receiving end: after hearing the localised version once, can a listener say who is eligible, what to bring, and where to go. That reframes the work as a loop rather than a pipeline, localise, test on a comprehension set, revise the register, watch the score move, and it is the only version of this card that does not collapse into a translation demo. The constraint that makes it hard is that register can change freely while facts cannot move at all.

**The scenario.** Pranab handles communications for a state department in Cuttack. A scheme launches with one English explainer video and one Hindi dub, and block-level officers immediately ask for Odia, because the people at the counter do not follow either. Historically that version arrives months after launch, if at all. He has the original video file and the official scheme text on his desk.

**What you will need**
- Ingest the original video with a timed transcript, plus the official scheme text as the single authority for every fact
- Localisation that changes register as well as language: short sentences, concrete nouns, no stacked clauses, aimed at one listen with no rewind
- A fact lock, so numbers, dates, names and eligibility statements carry through unchanged and every one is checkable against the source text
- A comprehension set: three questions per language, asked of a real listener, scored before and after your register revision and reported as two stated numbers rather than a direction of travel
- Honest language coverage stated against Sarvam's TTS list, with a language you cannot support declared rather than approximated
- A rendered video per language, not an audio file in a folder
- Two listeners per language, recruited before you start building
- One-pager: the workflow, the integration surface, the provenance of every fact in every language plus the official channel a listener is pointed to for anything the video does not settle, publication readiness, a deploy-or-pilot verdict, and why Dubbing is primary

**Your demo moment.** Play the original English explainer, then the Odia version, then let a judge ask the three eligibility questions of someone who has only heard the Odia one. They answer all three. Then show the comprehension score before and after your register revision, which is the number that makes this a build rather than a translation.

**Scores on:** Impact and Job-to-be-done. **Weak on:** Creativity, since this sits close to Sarvam's Government Scheme cookbook agent. The comprehension harness is the only thing that makes it yours.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam's Dubbing surface, or Saaras timed transcription plus Sarvam Translate and Bulbul, producing a finished localised video whose register, pronunciation, pacing and timing work for one-listen comprehension while facts remain locked. This is where the score is.
- **Supporting** Sarvam-30B for generating and scoring the comprehension questions and for constrained rewrites under the fact lock. Plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Video in, per-language render out, plus a comprehension test screen your tester actually uses: Next.js · React with Vite · two plain HTML pages, one to upload and one with three questions and radio buttons, which is all the harness needs
- **Backend** Convex functions · Next.js route handlers · a small FastAPI or Express service · a local script driving ffmpeg for the render pass
- **Data** Convex · Supabase · SQLite on disk · or the local filesystem plus a JSON file per language and no database at all, for videos, per-language scripts, fact-lock check results and comprehension scores; renders to Convex file storage, Supabase Storage, R2 or a folder
- **Comms** Slack or Discord webhook to the department channel on completion · Resend for the batch report with comprehension scores · Telegram bot for the per-language nudge
- **Mock or external** ffmpeg locally. No external service needed
- **Specific to this build** A real published scheme explainer video plus its official scheme text loaded as the single authority for every fact, because the fact lock checks against that text and nothing else. Two listeners per language recruited before noon, and a three-question comprehension set per language scored before and after your register revision. Check TTS coverage for your target language before you promise it.

**Know before you pick this.** Do not restate an eligibility rule, amount, date or document requirement from your own knowledge. Every fact in every language has to trace back to the official scheme text you loaded, and the fact lock is the mechanism that proves it, so build the lock before you build the pretty player. Recruit your listeners before noon: the comprehension score is the score, and you cannot fake it at 4:00.

---


---

# Business at scale


## 56 ·
UPI dispute callback verification at payments-platform scale

**Challenging · technical · Voice Experience**

> An outbound callback on a raised dispute that verifies who it is talking to, captures the transaction reference correctly, classifies the dispute, and confirms the next step.

**Why this one.** The axis is repair, not speed: landing a 12-digit UTR reference correctly when the caller says it in code-mixed digits and corrects themselves halfway through. A caller reading a reference off a screen does not read it cleanly. They chunk it, they mix "four five" with "chaar paanch," they say "seven eight, no sorry, seven nine," and they lose their place and restart from the middle. A system that keeps the first value, or splices the correction into the wrong position, writes a dispute against a transaction that does not exist. With 200K+ dispute callbacks a month, a small mis-capture rate is a large number of dead cases, and every one of them costs a second call. The top bands go to the team whose agent handles a mid-utterance self-correction, reads the final value back, and offers to find the transaction by amount and time when the caller cannot produce the reference at all.

**The scenario.** Kavitha runs dispute operations at a payments platform. Her callback queue asks every customer for the UTR, and a meaningful share of cases stall because the reference on file does not match anything. The agent calls Debasis in Sambalpur about a payment that did not reach the recipient. He reads the reference off his banking app in a mix of Odia and English digits, gets a digit wrong, corrects it mid-sentence, then asks whether the money is gone.

**What you will need**
- Outbound dialling from a queue of raised disputes
- Identity verification before any transaction detail is disclosed, with a stated rule for what counts as verified
- Digit capture that survives code-mixed number reading and mid-utterance self-correction
- Explicit read-back of the captured reference, with a confirm or correct turn
- Three tool calls: look up the transaction by its reference, search by amount and approximate time when the caller cannot produce a reference at all, and write the classified dispute to the mocked case system
- Dispute classification into named categories, plus a captured next step the caller agrees to
- A recorded self-correction set, the same 12-digit reference with the error in five different positions, and a stated number off it: how often the final captured value was correct, plus per-turn median and p95 on the same run, captured not estimated
- Per-turn transcript with the captured value at each turn, so a mis-capture is traceable
- One-pager: the workflow, the integration surface, recording consent, what you redact before a dispute transcript is stored, and who inside the operation can hear it, a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** A judge takes the call, reads a 12-digit reference in mixed Hindi and English digits, and corrects a digit in the middle without warning. The agent reads back the correct final value, and the dispute written to the mocked case system points at the right transaction.

**Scores on:** Sarvam parameter and Memory and Context. **Weak on:** Creativity, since dispute callbacks are a known build. The self-correction handling is the whole card.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras streaming for digit capture across code-mixed reading and mid-utterance self-correction. This is where the score is.
- **Supporting** Sarvam-30B for dispute classification and next-step extraction, Bulbul streaming for the outbound voice and the read-back. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Outbound dialling from the dispute queue: a number via Twilio or Exotel or Plivo · LiveKit or Pipecat or Vapi if you want barge-in and tight control of the audio path · Sarvam streaming APIs wired directly · a browser mic page that plays your recorded reference-reading clips into the pipeline, which is a completely legitimate fallback if telephony is eating your morning
- **Backend** Queue, verification state, case writes: Convex functions · Next.js route handlers · a small FastAPI or Express service · Sarvam Agents if you want the verification state checkpointed and a run you can reopen
- **Data** Disputes, the captured value at each turn, the final confirmed reference: Convex · Supabase · SQLite on disk · or none, hold the turn state in memory if you are only ever demoing one live call
- **Comms** The case ID and next step in writing after the call: Resend · Loops · a Telegram bot · a Slack webhook to the dispute desk
- **Mock or external** The transaction lookup and the case write: Beeceptor (hosted, no signup) or Mockoon (desktop) · Razorpay test mode if you want genuinely payment-shaped responses and error codes · httpstat.us with `?sleep=5000` to hang the lookup and hear what the agent says while it waits
- **Specific to this build** A recorded self-correction set: the same 12-digit reference read aloud with the error in five different positions, by two or three people who will read it badly on purpose.

**Know before you pick this.** Record your self-correction set before 11:30, and recruit two or three people who will read references aloud badly on purpose. Correcting a digit convincingly is harder than it sounds, so script the exact error positions rather than hoping a judge produces one. If it is proper nouns rather than digits that interest you, card 61 is the address and landmark card.

---


## 57 ·
Delinquent-borrower collections voice agent for consumer lending

**Beast · domain · Voice Experience**

> An outbound collections call that first works out whether the person who answered is actually the borrower, and says nothing about the debt until it knows.

**Why this one.** The axis is third-party disclosure control when you cannot tell who picked up. This is the re-point, and it matters, because the obvious version of this card is Sarvam's own Collection Agent cookbook and starts at the creativity floor. The re-pointed version is a different problem: on 12K+ outbound calls a day the handset is shared, and the voice that answers belongs to a spouse, a son, a neighbour, or the shop next door. Indian kinship and honorific terms do not settle it. "Bhai," "didi," "sahab," and "wo ghar pe nahi hai" all leave identity open, and a caller who says "haan boliye" is not confirming they are the borrower. So the agent has to establish identity from ambiguous vernacular before it discloses that a loan exists, hold the line when the third party pushes for details, and leave a message that says nothing about money. The 47-second hang-up is not the thing to optimise. Not disclosing a debt to the wrong person is.

**The scenario.** Nandini runs collections at a consumer lender. Her dialler opens with the borrower's name and the overdue amount in the first line, which means a neighbour who picks up learns both. The agent calls a number in Darbhanga. A woman answers, says the borrower is her husband and he is out, asks what the call is about, and then says "aap mujhe bata dijiye, main dekh leti hoon."

**What you will need**
- Outbound dialling from a delinquency queue, with a named disclosure rule the agent obeys
- Identity establishment from ambiguous vernacular, treating kinship and honorific terms as unresolved rather than as confirmation
- A hard non-disclosure state: while identity is unconfirmed, no amount, no product, no reason for the call, held when the third party pushes for details and held without being rude about it
- A callback-message path that leaves a request to call back and nothing else
- Confirmed-borrower path: reason for the call, hardship or dispute capture, and a specific commitment with a date
- Three tool calls, two of them gated on identity reaching confirmed: fetch the loan account the agent is holding and not yet allowed to mention, write the captured commitment with its date, and raise a breach alert on any turn where the gate was bypassed
- A transcript flag on every turn recording whether identity was confirmed at that point, so a disclosure breach is auditable
- Scripted third-party scenarios: spouse, adult child, wrong number, and a borrower pretending to be someone else
- One-pager: the workflow, the integration surface, third-party disclosure control and exactly what the agent says before it knows who picked up, with the citable current reference your posture rests on, a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** A judge plays a spouse and pushes three times for the amount, including once by claiming to be the borrower's authorised person. The agent does not disclose, leaves a callback request, and the transcript shows identity never reached confirmed. Then the judge plays the borrower, confirms identity, and the same agent proceeds to the full conversation.

**Scores on:** Sarvam parameter and Job-to-be-done. **Weak on:** Delight, and Creativity is at risk unless the disclosure control is genuinely load-bearing rather than a line in the prompt.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam-30B for speaker-identity inference from ambiguous vernacular replies and for gating disclosure on it. This is where the score is.
- **Supporting** Saaras streaming for transcription across code-switching and shared-handset audio, Bulbul for the outbound voice. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Outbound dialling from the delinquency queue: a number via Twilio or Exotel or Plivo · LiveKit or Pipecat or Vapi if you want barge-in, which matters when a third party talks over the agent · a browser mic page playing your scripted third-party scenarios, which is a completely legitimate fallback if telephony is eating your morning
- **Backend** Queue, gate state, commitment records. The disclosure gate belongs in code rather than only in the prompt, because a judge will attack it: Convex functions · Next.js route handlers · a small FastAPI or Express service · a plain state machine with three states (unknown, third party, confirmed borrower)
- **Data** Accounts, per-turn identity state, disclosure flags, captured commitments: Convex · Supabase · Postgres direct · SQLite on disk. Do not skip persistence here, the per-turn disclosure audit is the artefact you demo
- **Comms** The breach alert and the daily digest: a Slack webhook to the collections lead on any turn where the gate was bypassed · a Discord webhook, same shape · ntfy.sh if you want a push with no signup · Resend for the digest
- **Mock or external** The loan account lookup, so the agent holds detail it is not yet allowed to say: Beeceptor · Mockoon · WireMock Cloud if you want stateful behaviour
- **Specific to this build** Four scripted third-party scenarios recorded on a shared handset: spouse, adult child, wrong number, and a borrower pretending to be someone else. The third-party disclosure rule itself has to be sourced from a citable current reference you can show on screen, never asserted from memory.

**Know before you pick this.** This is Sarvam's Collection Agent cookbook. Build the cookbook version and you are at the creativity floor by definition, so lead the demo with the disclosure gate and the shared handset, not with persuasion or empathy. Separately: the specific regulatory requirement on third-party disclosure in collections has to be sourced from an authoritative current reference before you assert it in copy or on a slide. Describe the behaviour you built, not a rule you have not read.

---


## 58 ·
After-hours voice support for regional bank customers in Tier-2 towns

**Starter · domain · Voice Experience**

> Night support for a regional bank that understands how its customers actually speak, not how the language is written.

**Why this one.** The axis is dialect variation inside a single nominal language. A regional bank's 10pm to 6am calls get routed to an outsourced desk that answers in generic English, and the failure people describe as "tone" is usually comprehension: the caller is speaking Hindi, but it is Bhojpuri-inflected Hindi with local words for money, for the account, for the person who handles it at the branch. A stack tuned on textbook Hindi transcribes it into confident nonsense and the agent answers the nonsense. The second axis is scope at night: there is nobody to escalate to until 9am, so the agent has to know the boundary of what it can resolve alone and hand off with the record complete rather than half-solve something at 3am. Top bands go to the team that can show the same request understood in the local variant and in standard Hindi with the same outcome.

**The scenario.** Vandana runs service operations for a regional bank with most of its branches in small towns. After hours, calls go to a BPO that answers in English and reads from a national script. At 1am Sushila calls from Gorakhpur because her card has stopped working and she has a payment due in the morning. She explains it in the Hindi spoken there, with local words the national script has never seen, and the person on the line asks her to repeat herself four times.

**What you will need**
- Inbound voice on a phone line, with no language menu
- Four inquiry types named rather than counted, each fully resolvable at night: balance and last transactions, blocking a card after suspected misuse, the status of a failed payment, and the status of a cheque or a standing instruction. Everything else is explicitly out of night scope
- Dialect handling inside one language: local vocabulary, local number habits, and a compressed line
- A stated boundary with a clean handoff: the record captured, the morning callback promised, nothing half-done
- A comprehension test set: the same five requests recorded in the local variant and in standard Hindi, with a stated transcription accuracy for each side and the gap between them
- Three tool calls against the mocked core banking: read the account status, block the card, and write the overnight ticket with the transcript attached so the branch picks it up at 9am with context
- A refusal path for anything that needs a human, worded so the caller is not left guessing
- One-pager: the workflow, the integration surface, what a night agent is allowed to change on an account with nobody to escalate to until 9am, what the ticket keeps and who at the branch reads it, a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** Play two recordings of the same request back to back, one in the local variant and one in standard Hindi. Both are transcribed correctly and both reach the same outcome, side by side on one screen. Then a judge asks for something out of night scope and the agent hands off cleanly with the record already written.

**Scores on:** Job-to-be-done and Impact, since the alternative is a customer repeating herself at 1am. **Weak on:** Creativity, since after-hours support is an expected build. The dialect pairs are what lift it.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras for transcription across dialect variation inside one nominal language, on a compressed line. This is where the score is.
- **Supporting** Sarvam-30B for intent classification against the four in-scope types and for holding the scope boundary, Bulbul for the response voice. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** One inbound number, no IVR tree: Twilio or Exotel or Plivo (Exotel is India-native and usually less friction on Indian numbers) · LiveKit or Pipecat if you want tighter control of the audio path · Sarvam streaming APIs wired directly · a browser mic page that plays your paired dialect recordings straight in, which is a completely legitimate fallback if telephony is eating your morning
- **Backend** Tickets, the morning queue, the scope boundary: Convex functions · Next.js route handlers · a small FastAPI or Express service · Cloudflare Workers · localhost plus a tunnel, which is a legitimate answer at 4pm
- **Data** Tickets, transcripts, dialect tags, comprehension results: Convex · Supabase · SQLite on disk. The paired test results are the demo, so they need to live somewhere you can render side by side
- **Comms** The overnight queue handed to the branch at 9am: Resend with transcripts attached · Loops · MailerLite if Resend caps bite · a Telegram bot · a Slack webhook to the branch channel
- **Mock or external** The core banking lookup the agent reads account status from: Beeceptor · Mockoon · httpstat.us to force a 503 and see how the agent handles core banking being down at 2am
- **Specific to this build** Five requests recorded twice each: once by an actual speaker of the local variant, once in standard Hindi. Not an impression of the variant, a speaker of it. That paired set is the score.

**Know before you pick this.** You need speakers of the local variant, not people doing an impression of one. Recruit two or three before noon, not at 3:30, and record the paired test set early, because the paired comparison is the demo and it produces no visible UI until you build the screen for it.

---


## 59 ·
KYC-authenticated banking inquiries with private-banking register

**Challenging · domain · Voice Experience**

> A private-banking inquiry line that verifies the customer properly and speaks to them at the right level of formality in their own mixed language.

**Why this one.** Hinglish is the default register of Indian private banking, and the axis is formal register inside code-mixed speech. This is not brand-voice matching, which is what the original card rewarded. It is that formality carries real social weight: the choice between aap and tum, the honorific attached to a surname, the difference between "aapka account" and a construction that reads as familiar, are all decisions the agent makes on every turn, in a sentence that is half English. Get them wrong with a long-standing private-banking customer and it is a customer-relations incident, not a style nit. The second requirement is that the verification mechanism has to be visible in the demo, because a warm register that discloses balances to an unverified caller is the worse failure of the two.

**The scenario.** Reshma runs the private-banking service desk for a Tier-1 private bank in Howrah. Her relationship managers handle calls personally, which does not scale past their own working hours, and the overflow line answers in flat English that her customers notice immediately. Amiya Ranjan Sanyal, a customer of nineteen years, calls to ask about a fixed deposit maturing next week. He speaks in Bengali and English in the same sentence, and expects to be addressed the way his relationship manager addresses him.

**What you will need**
- Inbound call with a verification step before any account detail is disclosed, and a named rule for what counts as verified
- The verification mechanism visible in the demo: what was checked, what was not, and what the agent refused to say until it passed
- Register control across turns: pronoun choice, honorific and surname handling, and formality that holds inside a code-mixed sentence
- Register selection that follows the customer, so if they drop into a less formal register the agent does not mirror it downward
- Three tool calls, none of them fired until verification passes: look up the customer record, read the maturing fixed deposit's date and value, and write the inquiry record, with every figure read back in a way the customer can confirm
- A register test set: the same exchange scored for pronoun and honorific correctness turn by turn, reported as turns correct out of turns scored by two native speakers who are not on the team
- A named failure path for a verification that does not pass, worded so it does not accuse the caller
- One-pager: the workflow, the integration surface, what counts as verified and the citable current reference you take that from, what stays undisclosed until it passes, and who can hear the recording afterwards, a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** A judge calls and speaks half in English and half in an Indian language, and fails the first verification attempt on purpose. The agent declines to disclose anything, re-verifies, and then answers the inquiry with the honorific and the pronoun correct on every turn, shown against the turn-by-turn register scoring.

**Scores on:** Sarvam parameter and Delight. **Weak on:** Impact, unless you can state what the relationship-manager overflow actually costs the desk today.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam-30B for register and pronoun selection inside code-mixed generation, turn after turn. This is where the score is.
- **Supporting** Saaras for transcription across Hinglish and Benglish input, Bulbul for delivery at the chosen formality. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Inbound call plus a small operator screen showing verification state: Twilio or Exotel or Plivo · LiveKit or Pipecat for tighter control of the audio path · plain HTML with a script tag for the operator screen, or Next.js or React with Vite if one is already open · a browser mic page, which is a completely legitimate fallback if telephony is eating your morning and also the fastest way to replay the same exchange while you tune register
- **Backend** Verification state and the disclosure gate, which needs to be enforced in code and not only in the prompt: Convex functions · Next.js route handlers · a small FastAPI or Express service · a plain two-state gate (unverified, verified) you can point at
- **Data** Customers, verification attempts, per-turn register scores, inquiry records: Convex · Supabase · Postgres direct · SQLite on disk
- **Comms** A written confirmation of the inquiry and the answer given: Resend · Loops for a cleaner template · a Telegram bot if the customer prefers it · a Slack webhook to the relationship manager
- **Mock or external** The core banking and fixed-deposit lookup, so verification actually gates real-looking data: Beeceptor · Mockoon · WireMock Cloud
- **Specific to this build** A turn-by-turn register scorecard (pronoun choice, honorific, surname handling) and two or three native speakers who are not on the team and will score it honestly. The KYC and telephone-verification requirement has to be sourced from a citable current reference you can put on a slide, never asserted and never pointed at a guessed address.

**Know before you pick this.** The specific KYC and telephone-verification requirement has to be sourced from an authoritative current reference before you claim compliance with it. Describe the mechanism you built and what it checks. Separately, recruit two or three native speakers who will judge the register honestly, and do it before noon, because register errors are invisible to a team that does not speak the language.

---


## 60 ·
Cross-product cross-sell qualification for private banks

**Challenging · domain · Voice Experience**

> A qualification call that works out which of four products a customer actually needs, when the customer has no financial vocabulary at all.

**Why this one.** The axis is intent extraction with no domain terms present in the input. Nobody outside the industry says "liquidity requirement" or "unsecured credit line." They say "kuch paisa idhar-udhar pada hai," "beti ki shaadi teen saal mein hai," "har mahine kuch bacha leta hoon par kahan rakhoon pata nahi," and "gaadi lene ka soch raha hoon par abhi cash nahi hai." Each of those maps cleanly onto one of savings, lending, cards, or investment, and none of them contains a single financial term to key off. Across 40K+ prospects a month, the qualification job is that mapping, done in the prospect's own words, without leading them into vocabulary they do not have. A system that asks "are you looking for a term deposit or a systematic investment plan" has already failed, and the top bands go to the team whose agent qualifies without ever using a product word until the recommendation.

**The scenario.** Kartik runs cross-sell for a private bank with four product lines that each call the same customer separately. A prospect in Lucknow, Shakuntala, has been called three times this month by three teams. She has money sitting in a savings account, a daughter getting married in a few years, and a vague plan to buy a vehicle, and she has never used a financial term for any of it. She describes all three in one rambling answer to the first question.

**What you will need**
- Outbound call from a prospect list, with one conversation covering all four product lines rather than four calls
- Open questions in plain vernacular, with a hard rule against introducing product vocabulary before the recommendation
- Mapping from need described in everyday language onto the four product categories, with the mapping evidence quoted
- Multi-intent handling, since one answer often contains two needs and a timeline
- Timeline extraction from colloquial phrasing, because "teen saal mein" is the difference between two products
- Two tool calls: check each mapped need against the product eligibility rules, and write one structured record carrying a qualified or not-qualified verdict per product with the reason attached
- A negative case: a prospect who needs none of the four, correctly qualified out rather than pushed into something
- A stated number: correct product mapping across your fifteen vernacular descriptions, reported separately for the five you held back
- One-pager: the workflow, the integration surface, consent to make the call, what you keep about a prospect who qualified for nothing, and the line between recording a need and recommending a product, a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** A judge describes their situation in one long vernacular answer with no financial words in it at all. The agent comes back with two of the four products qualified, one explicitly not, and quotes the exact phrase that mapped to each.

**Scores on:** Job-to-be-done and Sarvam parameter. **Weak on:** Delight, since a cross-sell call is nobody's favourite call, and Creativity, since the use case is familiar.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam-30B for mapping everyday descriptions onto the four product categories, plus multi-intent and colloquial timeline extraction. This is where the score is.
- **Supporting** Saaras for transcription of long rambling vernacular answers, Bulbul for the outbound voice. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Outbound from a prospect queue plus a review screen showing the mapping evidence: Twilio or Exotel or Plivo · LiveKit or Pipecat or Vapi if you want barge-in · plain HTML with a script tag for the review screen, which only has to show a quote next to a verdict · a browser mic page, which is a completely legitimate fallback if telephony is eating your morning
- **Backend** The queue and the per-product verdicts: Convex functions · Next.js route handlers · a small FastAPI or Express service · Cloudflare Workers
- **Data** Prospects, per-product verdicts with the quoted evidence, extracted timelines: Convex · Supabase · SQLite on disk · or none, hold one prospect in memory, though the quoted evidence reads far better out of a table
- **Comms** Each qualified lead handed to the right product team: a Slack webhook to their channel · a Discord webhook, same one-liner · a Telegram bot · Resend for a daily lead digest
- **Mock or external** The product eligibility rules the verdicts are checked against: Beeceptor · Mockoon · or a JSON file checked into the repo, since eligibility rules are static and mocking them over HTTP buys you nothing
- **Specific to this build** Fifteen vernacular need descriptions written with zero financial vocabulary in them, five of them held back unseen until the demo.

**Know before you pick this.** Write fifteen vernacular need descriptions with no financial vocabulary in them before you build, and hold five back. Teams that write their test inputs after the prompt end up testing a system against language it was tuned on, and the demo falls over the first time a judge phrases it their own way.

---


## 61 ·
Quick-commerce order modification voice agent for peak dinner hours

**Challenging · technical · Voice Experience**

> A call that changes a live order: swap an item, fix the address, move the slot, and get the details right when they arrive fast and half in English.

**Why this one.** The axis is proper-noun and landmark fidelity in fast code-mixed speech. The original card rewarded p95 latency in the 7pm to 10pm spike, and latency is real, but it is not the thing that breaks. What breaks is the content: on 4M+ orders a day the modifications people call about are addresses, landmarks, and item names, and all three are proper nouns spoken quickly inside a code-mixed sentence. "Sai Mandir ke peeche wali gali, third house" is not a phrase a generic stack survives. Neither is a brand name in the middle of a Telugu sentence, or a building name that sounds like three other building names in the same locality. A modification written against a mis-heard landmark is a failed delivery with a confirmation attached to it, which is worse than no modification at all. The top bands go to the team whose capture of names and landmarks holds up when a judge speaks at real speed and does not slow down for the microphone.

**The scenario.** Devika runs order operations for a quick-commerce platform. Between 7pm and 10pm her support queue is mostly modifications, and the ones that go wrong go wrong on the address. Anand calls from Hyderabad to add two items and correct the drop point, because the rider went to the wrong gate last time. He gives the landmark in Telugu with the brand names in English, at the speed of someone cooking.

**What you will need**
- Four tool calls: identify the live order from the calling number rather than asking the customer to read an order number, resolve the item against the catalogue, commit the modification, and notify the rider when a drop point changes on an already assigned order
- Capture of item names, brand names and pack sizes spoken in code-mix, matched against a real catalogue
- Address and landmark capture with a match against known localities, and an explicit low-confidence state
- Read-back of the changed address or landmark before the modification is committed
- A modification window rule, so a request that arrives too late is refused with a reason rather than accepted and dropped
- Three modification types handled end to end: item change, address or landmark correction, slot change
- A test set of landmark utterances recorded at real speaking speed, including two genuinely ambiguous inside the same locality, with a stated landmark capture accuracy off it plus per-turn median and p95 across a scripted peak-hour run, captured not estimated
- One-pager: the workflow, the integration surface, what a caller is allowed to change once a rider is assigned, what you store about a customer's address and landmark, and who can hear the call, a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** A judge calls at speed, adds an item by brand name inside a non-English sentence, and gives a landmark rather than an address. The agent reads back the landmark correctly, the item resolves to the right catalogue entry, and the modification written to the mocked order system is correct.

**Scores on:** Sarvam parameter and Job-to-be-done. **Weak on:** Creativity, since order modification is the most familiar voice use case in the library. The landmark accuracy is the differentiator, so make the confidence state visible.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras streaming for proper-noun and landmark capture in fast code-mixed speech. This is where the score is.
- **Supporting** Sarvam-30B for catalogue matching, locality matching and modification-type classification, Bulbul streaming for the read-back. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Inbound on one number: Twilio or Exotel or Plivo · LiveKit or Pipecat or Vapi if you want barge-in and tight audio control, which is worth it when a customer talks at cooking speed · Sarvam streaming APIs wired directly · a browser mic page, which is a completely legitimate fallback if telephony is eating your morning and lets you replay the same landmark clip fifty times while you tune
- **Backend** The modification window rule and the order write: Convex functions · Next.js route handlers · a small FastAPI or Express service · Cloudflare Workers
- **Data** Orders, a catalogue subset, known localities, captured modifications with confidence: Convex · Supabase · Postgres direct · SQLite on disk. The catalogue and locality lists can just as easily be JSON in the repo
- **Comms** The rider channel when a drop point changes on an assigned order: a Telegram bot · a Slack or Discord webhook · ntfy.sh for a push with no signup · Resend for the customer's written confirmation
- **Mock or external** The order and dispatch system: Beeceptor · Mockoon · httpstat.us with `?sleep=5000` to inject a slow peak-hour commit and test what the agent says while it waits
- **Specific to this build** Landmark utterances recorded at real speaking speed, including two that are genuinely ambiguous inside the same locality, plus a catalogue subset with real-looking brand names and pack sizes rather than conveniently distinct ones.

**Know before you pick this.** Record your landmark set at real speaking speed before 11:30, and recruit two or three people who will give addresses the way they actually give them, before noon rather than at 3:30. If it is digit strings rather than names that interest you, card 56 is the reference-number card.

---


## 62 ·
Multilingual delivery confirmation with mid-call language switching

**Challenging · domain · Voice Experience**

> An outbound confirmation call that picks up the customer's language in the first seconds and keeps up when they switch mid-sentence.

**Why this one.** Saaras leads its own description with code-mixed and regional speech, and this card tests exactly that. Not "does it speak Tamil" but "does it survive a caller who opens in English, answers in Tamil, and gives the house number in English digits." The axis is switch recovery, not latency. Detecting language on the first utterance is the easy half. The hard half is turn four, when the caller switches without warning: whether the agent follows, whether it keeps the address it already captured, and whether the slot it writes back is still correct.

**The scenario.** Lakshmi runs delivery ops at a national logistics platform. Her outbound confirmation queue uses an English script, and in Coimbatore and Madurai the confirmation rate is poor enough that riders arrive at doors nobody is expecting. She triggers a batch. The agent calls Sundar, who picks up with "hello," answers the first question in Tamil, gives his house number in English digits, then asks about the time slot in Tamil again.

**What you will need**
- Outbound dialling from a queue of pending deliveries
- Language detection from the customer's first response, with no "press 1 for Tamil"
- Per-turn language state, so a switch on any turn is followed rather than restarting
- Correct capture of digits spoken in English inside a non-English sentence
- Four named exit paths: wrong number, reschedule, address change, no answer
- One tool call: write the confirmed slot, the captured address and the outcome code to mocked dispatch
- Per-turn transcript tagged by language, so a human can audit a disputed confirmation
- One-pager: the workflow, the integration surface, what gets written to dispatch on a partial or disputed confirmation and who corrects it when the slot is wrong, a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** A judge takes the call and deliberately switches language mid-sentence, unrehearsed. The agent follows without a restart, and the slot written to dispatch is correct.

**Scores on:** Sarvam parameter and Memory and Context. **Weak on:** Creativity, since the use case itself is familiar. The switch is what separates it.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras streaming (docs.sarvam.ai) for transcription and language detection on every turn, with Bulbul streaming for outbound speech and the voice switched mid-session rather than per call. This is where the score is. Per-turn language state, the thing that decides whether a switch on turn four is followed or restarts the call, is your own state machine.
- **Supporting** Sarvam-30B for intent and slot extraction across the four exits, as plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Phone: outbound via Twilio (twilio.com), Exotel (exotel.com) or Plivo (plivo.com), and Exotel is usually less friction for Indian numbers · LiveKit (livekit.io) or Pipecat (pipecat.ai) if you want tighter control of the audio path and barge-in · browser mic via getUserMedia as the fallback if telephony onboarding stalls, and it demos the switch honestly as long as you say the audio is not phone-band
- **Backend** Convex functions (convex.dev) for the queue, batch trigger and outcome writes · Next.js route handlers for the telephony webhooks · a small FastAPI or Express service · Cloudflare Workers (developers.cloudflare.com/workers) · localhost plus a tunnel (beeceptor.com/local-tunnel) for the webhook during the sprint
- **Data** Convex (convex.dev) for delivery records, per-turn language tags and outcomes · Supabase Postgres (supabase.com) · SQLite on disk · or none, hold it in memory and dump the tagged transcript to JSON, since the demo is one call
- **Comms** Resend (resend.com) for the post-call slot confirmation email · Telegram bot (core.telegram.org/bots) · Slack webhook (api.slack.com/messaging/webhooks) · ntfy.sh
- **Mock or external** Mockoon (mockoon.com) or Beeceptor (beeceptor.com) for the dispatch write endpoint · httpstat.us with sleep to inject a slow write and hear what the agent says while it waits
- **Specific to this build** A replayable switch sequence: pre-record the exact turns, English open, Tamil answer, English digits, Tamil again, and play them into the call so you are not waiting on a human for every iteration.

**Know before you pick this.** Recruit three or four people who will take a live call and switch language on purpose, and do it before noon, not at 3:30. Also script a fixed switch sequence you can replay, so you are not waiting on a human every iteration.

---


## 63 ·
Dormant D2C customer reactivation with brand personality intact

**Challenging · fun · Voice Experience**

> A reactivation call to lapsed customers that still sounds like the brand, in a language the brand has never spoken.

**Why this one.** The axis is brand register transfer into a language with no precedent. This is the interesting version of the original card, which asked whether the agent matched a brand voice in English. Here the brand has 240K+ lapsed customers and SMS and email reach 1 or 2 percent of them, so the channel has to be voice, and most of those customers do not want the call in English. The problem is that the brand has never spoken Marathi or Odia, so there is no reference material: no in-language copy, no tone guide, nothing to imitate. Translating the English script produces something grammatically fine and personality-free, which is exactly the failure. So the build is a judgement call made explicit: define what the personality consists of, generate in-language rather than translate, and prove the personality survived by showing a native speaker the translated baseline next to your output.

**The scenario.** Tanya runs retention at a D2C personal care brand with a distinct, slightly irreverent voice that its customers recognise in English. Reactivation goes out over SMS and email and almost nobody opens it. Suman in Raipur bought three times, then stopped fourteen months ago. She would take a phone call, but not one that sounds like a call centre reading a coupon code, and not one in English.

**What you will need**
- Outbound calling from a lapsed-customer list with purchase history attached
- A written definition of the brand personality as testable attributes, not adjectives
- In-language generation rather than translation of the English script, with the attributes as constraints, in two languages minimum so the claim is transfer and not one lucky script
- A naive baseline: the same script machine-translated, kept side by side so the difference is demonstrable
- Native-speaker scoring of both on the attributes, stated as a score per attribute for the baseline and for your output, so the claim is not the team's own opinion
- Personality that holds under an off-script turn, since a customer who asks something unexpected is where translated copy collapses
- A clean, non-pushy exit, because a reactivation call that will not end damages the brand it is defending
- Two tool calls: read the reactivation offer this customer is actually entitled to, and record the call outcome including an opt-out that holds
- One-pager: the workflow, the integration surface, consent to call a lapsed customer and a working opt-out, plus what the brand is committed to when a generated line makes an offer, a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** Play the machine-translated version and your generated version of the same call in the same language, back to back, to a native speaker in the room. They say which one sounds like a brand and point at why, against the attribute list on screen.

**Scores on:** Delight and Creativity, which is unusual for this block and is the reason to pick it. **Weak on:** Sarvam parameter, since the speech pipeline itself is not the hard part here, and Impact unless you use the 1 to 2 percent baseline honestly.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam-30B for in-language generation constrained by the personality attributes, rather than translation of the English script. This is where the score is.
- **Supporting** Mayura for the machine-translated baseline you are beating, Bulbul for delivery with voice and pacing chosen to fit the personality, Saaras for the customer's side. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Outbound plus a comparison screen for the baseline and your output: Twilio or Exotel or Plivo · LiveKit or Pipecat if you want tighter control of the audio path · plain HTML with two audio players and the attribute list beside them, which is all the comparison screen needs · a browser mic page, which is a completely legitimate fallback if telephony is eating your morning, and note that the A/B playback is the demo here rather than the live call
- **Backend** The list, the attribute scores, the exit rule: Convex functions · Next.js route handlers · a small FastAPI or Express service · plain scripts, since much of this build is generation you can run offline and cache
- **Data** Lapsed customers, purchase history, generated scripts per language, baseline scripts, native-speaker scores: Convex · Supabase · SQLite on disk · or a CSV you read at build time, which is plenty for a twenty-customer list
- **Comms** The offer discussed on the call, so the call has a real outcome: Resend · Loops · MailerLite · a Telegram bot
- **Mock or external** The offers and entitlement system the agent reads the reactivation offer from: Beeceptor · Mockoon · or a static JSON offer table
- **Specific to this build** One native speaker per language who is not on the team, available before noon, plus the personality written out as testable attributes on screen for them to score against. Pick languages someone in the room speaks, or you cannot iterate at all.

**Know before you pick this.** You need at least one native speaker per language who is not on the team, available before noon, to score the two versions. Without that the whole card reduces to the team asserting its own output is better, which no judge has to accept. Also pick languages someone in the room actually speaks, or you cannot iterate at all.

---


## 64 ·
Driver coordination voice agent for ride-hail and trucking fleets

**Starter · domain · Voice Experience**

> A status-check call to a driver who is driving, and who will give you four words before hanging up.

**Why this one.** The axis is fragment completion on a one-question budget. Dispatchers spend 8 hours a day on status calls, and the reason those calls are long is not the driver being difficult, it is that the driver is on a highway with the phone on speaker and answers in fragments: no verbs, no full place names, route shorthand, "do ghanta," "load utar gaya," "gaadi kharab." Each fragment implies a full status that has to be reconstructed rather than transcribed. And the agent gets roughly one clarifying question before the driver disengages, so the interesting design constraint is choosing which single missing field is worth asking about and inferring the rest. The register the original card cared about, brusque but respectful, matters here only because it is what keeps the driver on the line for that one question.

**The scenario.** Prakash dispatches for a mid-size fleet out of Amravati and spends his day calling drivers to ask where they are. Balwinder is on the highway south of the city with a delivery due tonight. Asked where he is, he says a route fragment and an hour count, mentions the load in three words, and does not volunteer whether he has eaten, refuelled, or hit the check post. Prakash needs a full status and has one question's worth of the driver's patience.

**What you will need**
- Outbound call to a driver on a moving vehicle, on speaker, with road noise as a designed condition
- Status record with named fields: location, expected time, load state, and any blocker
- Fragment completion, filling fields the driver implied rather than stated, with inferred values marked as inferred
- A one-question budget: the agent picks the single highest-value missing field and asks only that
- Register that keeps a driver on the line: direct, short, no pleasantries, no repeated confirmations
- Three tool calls: read the trip the driver is on, write the status record with the inferred fields flagged, and escalate a blocker to the dispatcher immediately rather than into a log
- A recorded set of terse driver replies with real road noise behind them, and a stated number off it: how many status fields were completed correctly, and how often an inferred value was wrong
- One-pager: the workflow, the integration surface, what is logged about a worker, who sees it, and how long it is kept, a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** Play road noise, and a judge answers three questions in fragments and refuses to elaborate. The agent produces a complete status record, marks which fields it inferred and which the driver stated, and asks exactly one follow-up rather than five.

**Scores on:** Job-to-be-done and Impact, since the 8 hours a day is the baseline the card is measured against. **Weak on:** Delight, and Creativity, since fleet status calls are a well-worn build.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam-30B for fragment completion, marking which fields were inferred rather than stated, and spending the one-question budget well. This is where the score is.
- **Supporting** Saaras for transcription of terse speech over road noise, Bulbul for a short, direct outbound voice. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Outbound to a driver on speaker plus a dispatcher board showing status records with inferred fields flagged: Twilio or Exotel or Plivo · LiveKit or Pipecat if you want tighter control of the audio path on a bad line · plain HTML for the board, or Next.js or React with Vite if one is open · a browser mic page with your road-noise clips mixed in behind, which is a completely legitimate fallback if telephony is eating your morning
- **Backend** The call queue, fragment inference, status writes: Convex functions · Next.js route handlers · a small FastAPI or Express service · Cloudflare Workers
- **Data** Trips, status records with stated versus inferred flags, blocker events: Convex · Supabase · SQLite on disk · Postgres direct
- **Comms** The dispatcher the moment a blocker is detected: a Telegram bot, which is the fastest of all · a Slack or Discord webhook · ntfy.sh for a push with no signup · Resend for the end-of-day roll-up
- **Mock or external** The fleet management system the status is written back to: Beeceptor · Mockoon · httpstat.us to make the write fail and see whether the status survives
- **Specific to this build** Fifteen to twenty terse replies recorded with real road noise behind them, by someone who actually talks like a driver on a highway. A team member speaking full sentences in a quiet room gives you a system that only works on full sentences in a quiet room.

**Know before you pick this.** Record fifteen to twenty terse replies with real road noise before you start, and get someone who actually talks like a driver on a highway to record them, before noon. A team member speaking in full sentences in a quiet room gives you a system that works only on full sentences in a quiet room.

---


## 65 ·
High-volume candidate screening that assesses skill, not English

**Beast · domain · Voice Experience**

> A phone screen conducted in the candidate's own language, so a strong candidate with weak English gets through.

**Why this one.** The axis is decoupling assessed competence from language proficiency, and this re-point makes the card better than the original rather than merely different. An enterprise pipeline runs 1,500+ phone screens a month at ₹300 to ₹500 each, and around 60 percent are filtered on basic criteria that do not need a human. The original card asked whether the screen felt human. The real failure is upstream of that: the filter is partly measuring English fluency, so a candidate who can do the job and cannot describe it in fluent English gets scored down on competence they actually have. Conducting the screen in the candidate's language changes what is being measured. That means eliciting evidence of skill through vernacular description, scoring the evidence and not the phrasing, and being able to show that the same candidate answering the same questions in two languages gets the same score. That last test is the card.

**The scenario.** Farah runs talent acquisition for a large enterprise with high-volume hiring across several states. Her screens are in English, and her hiring managers keep telling her that candidates who interview badly perform well once hired. Mahesh in Karimnagar has four years of hands-on experience, can explain exactly what he does in Telugu, and freezes when the same question arrives in English. On the current process he does not reach the manager.

**What you will need**
- Inbound or scheduled outbound screening call, conducted in the candidate's chosen language
- A competence rubric with named criteria and evidence requirements, plus an explicit language-proficiency field recorded separately and never folded into the competence score
- Evidence elicitation through vernacular description, with follow-ups that probe the claim rather than the wording
- Scoring against the evidence, with the quoted phrase attached to each criterion score
- A fairness harness: the same candidate profile answering the same questions in two languages, with a stated score agreement across the two versions and the largest gap you actually saw
- A refusal state, so a screen with insufficient evidence returns "not enough evidence" rather than a low score
- Two tool calls: read the candidate record and the role's criteria, and write the score sheet back to the mocked applicant tracking system in English with the original-language quotes preserved
- One-pager: the workflow, the integration surface, what is assessed, what is explicitly not assessed, and how a candidate contests an outcome, a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** Run the same scripted candidate answering the same questions twice, once in English and once in an Indian language, with the second version deliberately less fluent. Both screens produce the same competence score, and the language-proficiency field differs. Show both score sheets side by side with the evidence quotes.

**Scores on:** Impact and Job-to-be-done, and this is the strongest Impact story in the block because the harm being removed is specific and the person harmed is identifiable. **Weak on:** Delight, and Sarvam parameter is only as strong as the fairness harness, so build the harness before the interview flow.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam-30B for competence scoring against the rubric from vernacular evidence, with the quoted phrase attached to each criterion. This is where the score is.
- **Supporting** Saaras for transcription across languages and hesitant speech, Bulbul for the interviewer voice, Mayura for rendering quotes into English without losing the original. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Scheduled outbound or inbound, plus a recruiter screen showing score sheets with evidence quotes: Twilio or Exotel or Plivo · LiveKit or Pipecat or Vapi if you want barge-in · a browser mic page the candidate joins by link, which is both a completely legitimate fallback if telephony is eating your morning and an honest product answer for a screening tool
- **Backend** The fairness harness and score writes: Convex functions · Next.js route handlers · a small FastAPI or Express service · Sarvam Agents if you want each screen as a run you can reopen and re-score
- **Data** Candidates, per-criterion scores with quoted evidence, the separate proficiency field, harness results: Convex · Supabase · Postgres direct · SQLite on disk. The harness results are the score, so they have to survive a page refresh
- **Comms** The score sheet to the hiring manager, in English, with the original-language quotes attached: Resend · Loops · a Slack webhook to the hiring channel · a Telegram bot
- **Mock or external** The applicant tracking system the screen result is written back to: Beeceptor · Mockoon · WireMock Cloud
- **Specific to this build** Paired candidate answers scripted in both languages before 11:30, and two or three people who will deliver the less fluent version convincingly. The harness produces no UI of its own, so build it first and then build a screen for it.

**Know before you pick this.** The fairness harness is the score and it produces no visible UI, so teams skip it and lose the card. Script your paired candidate answers in both languages before 11:30, and recruit two or three people who will deliver the less fluent version convincingly, before noon rather than at 3:30. Do not claim a bias reduction you have not measured on your own paired set.

---


## 66 ·
Dealer and distributor support voice agent for industrial OEMs

**Challenging · technical · Voice Experience**

> A dealer calls in a regional language, says an English part number in the middle of the sentence, and gets the right part and the right order status.

**Why this one.** The axis is alphanumeric SKU fidelity inside regional-language speech. The original card cared about a brisk B2B tone. The real difficulty on 8K+ dealer calls a month is that tier-3 dealers conduct the whole call in Kannada or Marathi or Bengali, and every noun that matters is an English part number: a letter-and-digit string, spoken over a compressed line, from a printed catalogue, by someone who says B and V the same way and does not distinguish fifteen from fifty in a hurry. Getting the language right and the SKU wrong ships the wrong part to a dealer three hundred kilometres away. This is a different problem from domain vocabulary under noise, because the line is quiet and the vocabulary is not the issue: the issue is confusable alphanumeric characters inside a sentence in another language, and the disambiguation strategy the agent uses when two catalogue entries are one character apart.

**The scenario.** Sridhar runs dealer support for an industrial equipment OEM with a national distributor network. His support desk handles calls in English and Hindi, and dealers further out give up and WhatsApp a photo of the catalogue page instead. Basavaraj runs a dealership in Hubballi and needs the status of a pending order plus the availability of two spare parts. He calls, speaks Kannada throughout, and reads the part numbers off the printed catalogue in English.

**What you will need**
- Inbound call in the dealer's language, with dealer identity resolved from the calling number
- Alphanumeric capture of part numbers inside a non-English sentence, over a compressed line
- Confusable-character disambiguation with a strategy the agent states: read-back, character clarification, or a narrowing question
- Catalogue matching that surfaces near-miss entries instead of silently picking the closest one
- Three tool calls against the mocked ERP, none of them fired against an unconfirmed part number: resolve the part number to a catalogue entry, read stock for it, and read the status of the dealer's pending order
- A test set of part numbers containing deliberately confusable pairs, recorded inside regional-language sentences, with a stated capture accuracy off it and how often the disambiguation strategy recovered a first-pass miss
- Refusal to place or promise anything against an unconfirmed part number
- One-pager: the workflow, the integration surface, what the agent is allowed to promise a dealer against a confirmed part number and what it refuses on an unconfirmed one, who carries the cost of a wrong part shipped, a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** A judge calls, speaks a regional language throughout, and reads a part number that differs from another catalogue entry by one confusable character. The agent narrows it down, reads back the confirmed number, and returns the right order status. Then the judge reads a number that matches nothing and the agent says so rather than picking the nearest.

**Scores on:** Sarvam parameter and Job-to-be-done. **Weak on:** Delight, and Creativity, since dealer support is a known build. The confusable-pair handling is what separates it.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras for alphanumeric capture inside regional-language speech, over a compressed line. This is where the score is.
- **Supporting** Sarvam-30B for confusable-character disambiguation, catalogue matching and near-miss surfacing, Bulbul for the read-back in the dealer's language. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Inbound, dealer resolved from the calling number, plus a support-desk screen showing captured part numbers and near-miss candidates: Twilio or Exotel or Plivo · LiveKit or Pipecat for tighter control of the audio path · plain HTML with a script tag for the desk screen · a browser mic page, which is a completely legitimate fallback if telephony is eating your morning and the fastest way to replay a confusable pair
- **Backend** The tool-call gate that refuses to promise anything against an unconfirmed part number: Convex functions · Next.js route handlers · a small FastAPI or Express service · a plain state machine, since the gate is two states and a judge will test both
- **Data** Dealers, the catalogue subset, captured numbers with confidence, call records: Convex · Supabase · Postgres direct · SQLite on disk · the catalogue itself is fine as a CSV or JSON in the repo
- **Comms** The confirmed part numbers and order status in writing, so nothing rests on what was heard: Resend · Loops · a Telegram bot, which many dealers will actually read · a Slack webhook to the support desk
- **Mock or external** The ERP order status and stock endpoints: Beeceptor · Mockoon · WireMock Cloud if you want stock levels to change between calls · httpstat.us with `?sleep=5000` to make the stock call slow and see how the agent holds the line
- **Specific to this build** A mocked ERP parts catalogue with real-looking SKUs and deliberately confusable pairs in it (B against V, 15 against 50, O against zero), plus those numbers recorded inside regional-language sentences by someone who actually speaks the language.

**Know before you pick this.** Build your catalogue subset with confusable pairs in it before 11:30, and record part numbers read inside regional-language sentences by someone who actually speaks the language, recruited before noon rather than at 3:30. A catalogue of conveniently distinct SKUs makes the card look easy and scores like it.

---


## 68 ·
Appointment scheduling voice agent for multi-location clinic chains

**Challenging · technical · Voice Experience**

> A booking call that turns "agle mangalwar" into a real slot, on the right date, at the right branch.

**Why this one.** The axis is relative-date resolution across languages, which is a genuinely unsolved problem and nothing like the polished 2023 scheduling demo this card started as. A patient says "agle mangalwar", "next week Tuesday-ish", "parso", "adutha vaaram", and every one of those has to become an absolute date anchored to the moment of the call. Worse, the ambiguity is real rather than a parsing bug: "agle mangalwar" on a Monday means one thing to the caller and another to the calendar, and different languages carve the week differently. The failure mode is silent, a booking one week off that nobody notices until an elderly patient arrives at a closed clinic, so the top bands go to the team whose system resolves confidently where it can, asks exactly one clarifying question where it cannot, and reads the absolute date back in the caller's language.

**The scenario.** Farhan runs front-desk operations for a clinic chain headquartered in Akola, 10+ locations and roughly 30K appointment calls a month. Two receptionists per branch handle booking between walk-ins, and the ones who get dropped are the callers who do not speak the receptionist's language. Kusum calls on a landline, in Marathi, and says she wants to come "agle mangalwar, subah", at whichever branch is near the bus stand.

**What you will need**
- Inbound call with the caller's language detected on the first utterance, no menu
- A relative-date resolver with an explicit anchor (call date, day of week) and a stated rule for each ambiguous form
- One clarifying question on genuine ambiguity, never a silent guess
- Absolute-date read-back in the caller's language before the slot is held
- Branch disambiguation from a landmark rather than a branch code
- Three tool calls: look up slot availability at the disambiguated branch, hold the slot in the mocked EMR with the resolved absolute date, release it if the read-back is corrected
- A ground-truth test set of relative-date utterances across three languages, so you can state accuracy rather than assert it
- Warm reception register, which is table stakes here and not the score
- One-pager: the workflow, the integration surface, what a date resolved one week off actually costs when an elderly patient arrives at a closed clinic and how a mis-booked slot gets caught, a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** A judge speaks a deliberately ambiguous relative date in whichever supported language they like. The system either resolves it and reads the absolute date back, or asks one clarifying question, then books correctly. Then you show the resolution table: utterances, resolved dates, ground truth, and the ones you got wrong.

**Scores on:** Sarvam parameter and Job-to-be-done. **Weak on:** Creativity, since appointment booking is the most-built voice demo there is. The date resolver is the entire differentiator, so make it visible.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras streaming for transcription of temporal expressions in code-mixed speech, which is where the resolver either gets a clean input or does not. This is where the score is.
- **Supporting** Sarvam-30B for resolution against the stated anchor and for ambiguity detection, Bulbul for the absolute-date read-back. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Inbound on one number, no menu, plus a small page showing the resolution table: Twilio or Exotel or Plivo (a landline caller is the scenario, so test on a real line if you can) · LiveKit or Pipecat if you want tighter control of the audio path · plain HTML with a script tag for the table · a browser mic page, which is a completely legitimate fallback if telephony is eating your morning
- **Backend** The resolver, the anchor, the slot hold: Convex functions · Next.js route handlers · a small FastAPI or Express service · Cloudflare Workers. Keep the resolver as plain testable code, because you want to run it over your whole utterance list in one go
- **Data** Bookings, the ground-truth utterance set, the per-call resolution audit: Convex · Supabase · SQLite on disk · a CSV read at build time is genuinely enough for the ground-truth set
- **Comms** The confirmation with the absolute date in the subject line: Resend · Loops · a Telegram bot · ntfy.sh for the front desk
- **Mock or external** EMR slot availability and booking: Beeceptor · Mockoon · httpstat.us with `?sleep=5000` to test what the agent says while availability loads · the Cal.com API if you would rather book against a real scheduler than mock one
- **Specific to this build** 20 to 30 relative-date utterances across three languages with the correct absolute date written next to each, and the call date they are anchored to. That list is the score, so write it before you write the agent.

**Know before you pick this.** Write out 20 to 30 relative-date utterances across three languages, with the correct absolute date for each, before 11:30. That list is your score. Teams that build the agent first and the test set at 3:30 have no way to prove the thing the card is about.

---


## 69 ·
Fraud alert callback verification for neobank cardholders

**Challenging · domain · Voice Experience**

> An outbound call on a suspicious card transaction that comes back with a real yes or no while the money is still recoverable.

**Why this one.** The axis is telling a backchannel apart from actual consent. On an Indian phone call, "haan", "ji", "hmm" and "theek hai" are politeness tokens that keep the conversation moving, and they are not answers to "did you make this transaction." A system that counts them as a yes lets fraud through; a system that counts them as a no blocks a card in the middle of someone's evening. Both errors are consequential and irreversible in different directions, so the top bands go to the team whose agent treats an acknowledgement as a non-answer, re-asks in closed form, and logs the exact utterance it acted on. Today the workflow is emailing the cardholder and waiting, which is a workflow only if the money waits too.

**The scenario.** Ritika runs fraud operations at a neobank in Pune, watching a queue of 30K suspicious card transactions a day. Her only outbound tool is an alert email that is read hours later, if at all. The agent calls Devendra, who is standing in a market in Gorakhpur with traffic behind him, says "haan, haan" twice while trying to hear the question, and then says clearly that he did not make it.

**What you will need**
- Outbound call triggered off a flagged transaction, in the cardholder's language
- No disclosure of merchant or amount until identity is confirmed
- Closed-form confirmation with an explicit re-ask, so no decision rests on an open answer
- A backchannel classifier separating acknowledgement tokens from a real decision, per language
- Three tool calls, with the irreversible one gated: fetch the flagged transaction, block the card (only on an unambiguous denial), log the consent decision against the case
- Three named exits: confirmed genuine, confirmed fraud, unverified
- The exact utterance quoted on the record, since this call becomes evidence in a dispute
- Compressed-line handling, because this call happens outdoors and on speaker
- One-pager: the workflow, the integration surface, the false-positive cost (which real cardholders get blocked in error, what that costs them mid-evening, and how they get unblocked), a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** A judge answers with "haan haan" and "hmm" throughout, then denies the transaction once, clearly. The agent refuses to count any of the acknowledgements, blocks the card only on the clear denial, and shows the exact utterance it acted on.

**Scores on:** Sarvam parameter and Job-to-be-done. **Weak on:** Delight, since nobody wants this call. The honesty of the consent gate is what carries it.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam-30B for backchannel versus real consent classification, per language, feeding the irreversible-action gate. This is where the score is.
- **Supporting** Saaras streaming for transcription on a compressed outdoor line, Bulbul for the outbound voice and the closed-form re-ask. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Outbound triggered off a flagged transaction: Twilio or Exotel or Plivo · LiveKit or Pipecat or Vapi if you want barge-in, which matters when the caller is in a market and talking over you · a browser mic page playing your recorded backchannel patterns, which is a completely legitimate fallback if telephony is eating your morning
- **Backend** The gate. Put it in code, not only in the prompt, because a judge will ask what happens on a coin-flip answer: Convex functions · Next.js route handlers · a small FastAPI or Express service · a plain three-state machine (unverified, acknowledged but undecided, decided)
- **Data** Transactions, per-turn utterances, consent decisions with the quoted language: Convex · Supabase · Postgres direct · SQLite on disk. The quoted utterance is dispute evidence, so keep it rather than holding it in memory
- **Comms** Confirmation of the action taken, plus the fraud desk on every block: Resend for the cardholder · a Slack webhook to the desk · a Discord webhook, same shape · ntfy.sh for an on-call push with no signup
- **Mock or external** The card-block endpoint: Beeceptor · Mockoon · Razorpay test mode if you want genuinely payment-shaped responses · httpstat.us with `?sleep=5000` to test what the agent says while a block is in flight
- **Specific to this build** A backchannel token list per language, and recordings of the ambiguous pattern (acknowledge, acknowledge, then a clear answer) from two native speakers, with street noise behind them.

**Know before you pick this.** Write your backchannel token list per language before you build, and get two native speakers to record the ambiguous pattern (acknowledge, acknowledge, then answer) before noon. Also decide the gate rule out loud: this card is about an irreversible action, and a judge will ask what happens on a coin-flip answer.

---


## 70 ·
Insurance first-notice-of-loss voice intake for distressed callers

**Beast · domain · Voice Experience**

> A long structured loss intake that still comes out complete when the caller had an accident twenty minutes ago.

**Why this one.** The axis is completeness of a structured record out of disordered, disfluent speech. Under stress every input problem spikes at once: the caller loops back over the same thirty seconds, gives the vehicle number in three broken attempts, jumps from the collision to the hospital to the policy and back, and switches language without noticing. The record still has to come out with every field in the right place and nothing invented. Distress recognition is part of the axis rather than a separate feature, and this is where the generic voice-agent framing breaks: in a regional language the emotional vocabulary is thin, so the signal is not the word "scared", it is repetition, abandoned sentences and pace. 200K+ FNOL calls a month means this is the highest-volume genuinely hard call in the library.

**The scenario.** Shalini runs motor claims at an insurer in Jaipur, taking 200K+ first-notice-of-loss calls a month against a structured intake form that takes 20 minutes to complete properly. Her agents are trained to work the form top to bottom, and callers do not narrate top to bottom. Ramesh calls from the roadside outside Kota, engine still running, someone shouting behind him, and starts in the middle: the other truck, then his brother-in-law's name, then the vehicle number, twice, wrong the first time.

**What you will need**
- Inbound call with a field checklist tracked across the conversation, not a linear script
- Safety first: whether anyone is hurt, before any policy question
- Disfluency-tolerant extraction, so repeated and self-corrected values resolve to one value
- Out-of-order narration mapped to the right fields whenever the caller supplies them
- Distress detection from repetition, abandoned sentences and pace rather than keywords, with the agent shortening questions and slowing down in response
- A hard rule that a field the caller never supplied stays empty
- Three tool calls: look up the policy from the number the caller gives, write the structured loss record to mocked claims, hand off to a human at the stated distress threshold with the caller's own words carried across
- Per-turn transcript with field-level provenance, since a claim gets disputed later
- One-pager: the workflow, the integration surface, the escalation path with the distress threshold you used and the citable protocol you took it from, what the build refuses to decide (any injury or triage judgment), a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** A judge plays a shaken caller, narrates out of order, gives the vehicle number in three broken attempts and switches language twice unrehearsed. The finished record has the corrected vehicle number, the facts in the right fields, and the fields the caller never answered visibly empty rather than plausibly filled.

**Scores on:** Sarvam parameter and Memory and Context. **Weak on:** Delight, and Impact needs a real claim cycle-time baseline to mean anything.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras streaming for transcription of disfluent, looping, code-mixed speech under roadside noise. This is where the score is.
- **Supporting** Sarvam-30B for checklist state and resolving three broken attempts at a vehicle number into one value, Bulbul for pacing that shortens and slows in response to distress. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Inbound on one number: Twilio or Exotel or Plivo · LiveKit or Pipecat or Vapi if you want barge-in, which genuinely matters when the caller will not stop talking · a browser mic page playing your one scripted distressed narration, which is a completely legitimate fallback if telephony is eating your morning
- **Backend** Checklist state held across a long non-linear call: Convex functions · Next.js route handlers · a small FastAPI or Express service · Sarvam Agents if you want the intake checkpointed and a run you can reopen after a dropped call
- **Data** Claims, field-level provenance (which utterance filled which field), distress markers per turn: Convex · Supabase · Postgres direct · SQLite on disk. Provenance is the audit trail a disputed claim needs, so persist it
- **Comms** The claim acknowledgement and the human handoff: Resend with the reference number · a Slack webhook the moment a call goes to a human · a Telegram bot · an ntfy.sh topic as a pager for the claims desk
- **Mock or external** The policy lookup and the claims write: Beeceptor · Mockoon · WireMock Cloud · httpstat.us with `?sleep=5000` to hang the claims write mid-intake
- **Specific to this build** One fixed distressed narration recorded so you can replay it instead of waiting on a human every iteration, plus three or four people who will role-play a shaken caller. Every injury-triage question and the distress or escalation threshold has to come from a citable protocol you can show on screen, never from the model and never from your own judgment.

**Know before you pick this.** Any clinical content, any injury triage question and any distress or escalation threshold must come from a real protocol you can point to, not from the model and not from your own judgment, and the build must hand off to a human rather than guess. Separately: recruit three or four people who will role-play a shaken caller before noon, and script one fixed distressed narration you can replay, so you are not waiting on a human every iteration.

---


## 71 ·
Loan application status inquiry voice agent for lending platforms

**Starter · domain · Voice Experience**

> A caller who has never heard the word "disbursement" asks where their loan is and gets the exact truth, with no invented date.

**Why this one.** The axis is grounding a term-less question in the exact system state, and refusing to convert a stage into a date. The caller says "paisa kab aayega" or "file kahan atki hai"; the pipeline has stage names nobody outside the company uses. The agent has to map vague vernacular onto the precise record, say what that record means in the caller's own words, and never round "under review" up to "by Friday", because the invented date is exactly what generates the second call. With 100K+ applications a month and 40% of inbound support being "where is my loan?", the volume is real, and the discipline is the whole product.

**The scenario.** Tapan runs support at a lending platform in Dibrugarh where 40% of inbound calls are a status check on one of 100K+ applications a month. His agents open the same dashboard every time and read out a stage name that means nothing to the caller, then guess at a timeline to end the call politely. Bhaskar, a shopkeeper who applied last week, calls and asks in Assamese when the money will come, using no word that appears anywhere in the loan system.

**What you will need**
- Inbound call, language detected, no menu
- A phrasing map from real vernacular questions to exact pipeline states, built from collected phrasings rather than guessed
- The state read from a mocked origination system and stated exactly, never paraphrased upward
- A hard rule against inventing a date, a probability or a reassurance
- The one action the caller can actually take, if there is one, including the pending-document case
- Handoff to a human on disputes and on anything outside status
- Three tool calls: fetch the application state from the mocked origination system, log the outcome with that state quoted so drift is auditable, raise a handoff ticket on a dispute
- One-pager: the workflow, the integration surface, exactly what the agent will and will not state about an application (no date, no probability, no reassurance) and where it stops and hands over, a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** A judge asks the same question three ways in a regional language, using no domain term at any point, and gets the same exact state each time, the one action available to them, and no date the system cannot support.

**Scores on:** Job-to-be-done. **Weak on:** Creativity, hard, for the reason in the note below.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam-30B for mapping term-less vernacular questions onto the exact pipeline state, and for holding the no-invented-date rule. This is where the score is.
- **Supporting** Saaras for transcription, Bulbul for the reply in the caller's language. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Inbound on one number, language detected, no menu: Twilio or Exotel or Plivo · LiveKit or Pipecat if you want tighter control of the audio path · Sarvam streaming APIs wired directly · a browser mic page, which is a completely legitimate fallback if telephony is eating your morning and lets you fire the same question three ways in a minute
- **Backend** The state lookup and the refusal rule, which belongs in code so a judge can see it is enforced rather than requested: Convex functions · Next.js route handlers · a small FastAPI or Express service · Cloudflare Workers
- **Data** The phrasing-to-state map, calls, quoted states: Convex · Supabase · SQLite on disk · or a JSON file in the repo for the phrasing map, which is honestly fine and easier to review with a native speaker
- **Comms** The status in writing, using the same wording as the call: Resend · Loops · a Telegram bot · a Slack webhook for the disputes queue
- **Mock or external** The loan origination system, which you mock rather than integrate. Never point this at a real lender's system: Beeceptor · Mockoon · WireMock Cloud if you want the stage to advance between calls
- **Specific to this build** Real vernacular phrasings of "where is my loan", collected from people rather than invented by the team, each mapped to the exact pipeline state it should return.

**Know before you pick this.** This is adjacent to Sarvam's Loan Advisory cookbook agent, so you start at the creativity floor: built the obvious way, this is the reference agent with a different logo. The only way up is the term-less phrasing map and the visible refusal to invent a date, and you have to say that out loud in the demo or a judge will score you as the cookbook.

---


## 73 ·
Truck driver daily compliance check-in voice agent

**Challenging · domain · Voice Experience**

> A daily check-in call that captures a driver's licence and vehicle details correctly, including when he corrects himself halfway through the number.

**Why this one.** The axis is alphanumeric identifier capture with mid-utterance self-correction. A driver reads a licence or vehicle number over a highway line, in Bhojpuri or Punjabi-inflected Hindi with the letters spoken in English, and corrects himself in the middle: "MH one four, nahi nahi, one two, four seven". A generic stack keeps both attempts, or keeps the first, and the record then fails the audit it exists to satisfy. Across 4K+ active drivers these checks are legally required and skipped anyway, because an under-resourced ops desk cannot make four thousand calls, so the value is only real if the captured identifiers are exact.

**The scenario.** Sadhana runs the ops desk for a fleet operator in Bilaspur with 4K+ active drivers. Licence validity, medical fitness and hours-of-service checks are required, and in practice they happen when someone remembers or when an inspection is coming. Balbir is parked at a dhaba on the highway with the phone on speaker and the engine idling, and he starts reading out his licence number, gets a digit wrong, and corrects himself without pausing.

**What you will need**
- Outbound daily call queue across the driver list
- Alphanumeric capture designed for Indian licence and vehicle formats, with letters spoken in English inside a vernacular sentence
- Self-correction resolution that keeps the corrected value and discards the abandoned fragment, rather than merging them
- Read-back confirmation of every identifier in the driver's language
- Expiry and eligibility checks against a mocked compliance record, with the rules sourced not assumed
- Three tool calls: fetch the driver's compliance record, write the confirmed identifiers back against that driver, push a near-expiry or unreachable driver into the exception queue
- A photo fallback path when a value cannot be captured cleanly, so the call still ends in a record
- Per-call transcript retained, because the audit is the point
- One-pager: the workflow, the integration surface, what is logged about a driver, who inside the operator can see it, and how long it is kept, a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** A judge reads a licence number over highway noise and corrects himself mid-string, unrehearsed. The system reads back the corrected number, not a merge of the two attempts, and files it against the right driver.

**Scores on:** Sarvam parameter and Impact. **Weak on:** Delight and Creativity. This is a compliance product and it should look like one.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras streaming for alphanumeric capture under highway noise, with the letters spoken in English inside a vernacular sentence and a correction landing mid-string. This is where the score is.
- **Supporting** Sarvam-30B for resolving the correction to one value and for expiry logic, Bulbul for the read-back in the driver's language. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Outbound daily queue plus a web link for the photo fallback: Twilio or Exotel or Plivo · LiveKit or Pipecat if you want tighter control of the audio path · plain HTML with a file input for the photo page · a browser mic page playing your recorded licence-number clips, which is a completely legitimate fallback if telephony is eating your morning
- **Backend** The daily queue, correction resolution, expiry checks: Convex functions with scheduled functions · Next.js route handlers plus a cron · a small FastAPI or Express service with a scheduler · Cloudflare Workers with a cron trigger
- **Data** Drivers, identifiers with every capture attempt retained, the exception queue: Convex · Supabase · Postgres direct · SQLite on disk. Retain every attempt rather than only the final value, the audit trail is the product. For the fallback photo: Convex file storage · Supabase Storage · Cloudflare R2 · the local filesystem
- **Comms** The ops exception queue and the daily digest: a Telegram bot · a Slack or Discord webhook · Resend for the digest · ntfy.sh for a near-expiry push
- **Mock or external** The compliance record system: Beeceptor · Mockoon · WireMock Cloud
- **Specific to this build** 15 to 20 clips of licence and vehicle numbers read with highway noise behind them, including deliberate mid-string self-corrections. Hours-of-service and medical-fitness rules have to be sourced from a citable regulation or a real fleet's written policy you can show in the demo, never asserted from memory. Your build's job is capture and escalation, not legal interpretation.

**Know before you pick this.** Do not assert specific hours-of-service or medical-fitness rules. Source them from a real regulation or a real fleet's written policy and cite that source in the demo; the build's job is capture and escalation, not legal interpretation. Also record 15 to 20 clips of someone reading licence and vehicle numbers with highway noise behind them, including deliberate self-corrections, before you start building.

---


## 74 ·
Parent counselling voice agent for K-12 EdTech admissions

**Challenging · domain · Voice Experience**

> An admissions call that answers a parent's questions about English-medium schooling entirely in the parent's own language.

**Why this one.** The axis is explaining an English-medium product in the parent's language without condescension, and it is the actual tension in the conversation rather than a tone preference. The parent is asking, in Gujarati or Telugu, about an education whose whole proposition is English. Answer in English and you have confirmed their fear that this place is not for them. Answer in vernacular while leaking "learning outcomes", "assessment framework" and "curriculum" untranslated and you have done the same thing more politely. Across 20K+ parent inquiry calls a month the register has to be a senior teacher's, and every education term needs a deliberate decision: rendered properly in the parent's language, or left in English on purpose with one line explaining it.

**The scenario.** Deepa runs admissions for a K-12 chain in Vadodara and fields 20K+ parent inquiry calls a month with a team of six counsellors. The calls that convert are the ones where a parent feels talked with rather than sold to, and those take twenty minutes each. Sunil calls about his daughter and asks, in Gujarati, whether she will fall behind the children who already speak English at home. That is the question under every one of these calls, and the brochure does not answer it.

**What you will need**
- Inbound call with the parent's language detected, no menu
- A senior-teacher register held for the whole call, not a sales register
- An explicit glossary decision per education term: rendered in the parent's language, or deliberately left in English with a one-line explanation
- The anxious question answered directly rather than deflected to a brochure line
- Three tool calls: read the fee and eligibility facts from the mocked admissions system rather than improvising them, book the school visit, hand the call to a human counsellor with the transcript attached
- Handoff to a human counsellor for anything the system should not answer, with the transcript so they pick up where the call stopped
- One-pager: the workflow, the integration surface, what is claimed to a parent about their child's English and what is left to a human counsellor, a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** A judge asks in a regional language whether their child will fall behind children who speak English at home. The answer comes back in that language, in a teacher's register, and the two terms that had to stay in English are named and explained rather than dropped in untranslated.

**Scores on:** Delight and Job-to-be-done. **Weak on:** Sarvam parameter, unless the glossary decisions are explicit and you can show the list.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Bulbul for a senior-teacher register held across a twenty-minute call in the parent's language. This is where the score is.
- **Supporting** Saaras for transcription, Mayura for the education glossary rendering, Sarvam-30B for intent and the anxious-question path. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Inbound on one number, language detected, plus a page showing the glossary decisions: Twilio or Exotel or Plivo · LiveKit or Pipecat if you want tighter control of the audio path · plain HTML with a script tag for the glossary page, which is a two-column table · a browser mic page, which is a completely legitimate fallback if telephony is eating your morning
- **Backend** Intent routing, the glossary lookup, the visit booking: Convex functions · Next.js route handlers · a small FastAPI or Express service · Cloudflare Workers
- **Data** Inquiries, the glossary with a recorded decision per term, visit bookings, transcripts: Convex · Supabase · SQLite on disk · the glossary itself is better as a checked-in JSON or YAML file, because you want a native speaker reviewing it in a diff
- **Comms** The visit confirmation, a written version of the answers in the parent's language, and counsellor handoff: Resend · Loops · a Telegram bot · a Slack webhook to the counsellor channel
- **Mock or external** Admissions availability and fee data: Beeceptor · Mockoon · the Cal.com API if you would rather book the school visit against something real than mock the calendar
- **Specific to this build** Two parents, or two people who will play one convincingly, who will ask the awkward question ("will she fall behind the children who already speak English at home") in a regional language before noon. A judge will ask exactly that, and a canned answer is audible in three seconds.

**Know before you pick this.** Recruit two parents, or two people who will play one convincingly, who will ask the awkward question in a regional language, and do it before noon rather than at 3:30. A judge will ask that exact question, and a canned answer is audible in three seconds.

---


## 75 ·
Post-discharge patient check-in voice agent for hospital chains

**Challenging · domain · Voice Experience**

> Check-in calls at 24, 72 and 168 hours that catch the patient who is quietly getting worse.

**Why this one.** The axis is recall over precision on escalation, from folk symptom descriptions. Patients do not describe symptoms clinically. They say the pain has moved, that there is jalan, that they feel heavy, that they have not slept, and the language they say it in has no clinical register to fall back on. Mapping that onto a red-flag list is the entire job, and the two errors do not cost the same: an unnecessary nurse callback costs a few minutes, a missed red flag costs the thing the programme exists to prevent. With 200K+ discharges a year and a nurse queue reaching about 30% of patients, the top bands go to the team that tunes deliberately for recall, says so, and shows the false positives they chose to accept.

**The scenario.** Meenakshi runs the post-discharge nurse queue for a hospital chain in Varanasi covering 200K+ discharges a year. Calls are meant to go out at 24, 72 and 168 hours and reach about 30% of patients, so the ones who get missed are the ones who do not call back. Om Prakash, home in Ghazipur, is on his 72-hour call and describes in Bhojpuri that the jalan has spread and he has not slept, using no word that appears on any red-flag list.

**What you will need**
- Outbound calls at the three intervals with interval-appropriate questions
- Symptom capture in folk vernacular, mapped to a red-flag list sourced from a real discharge protocol
- Escalation tuned for recall, with the threshold stated and the accepted false positives visible
- Three tool calls: fetch the discharge record for the interval that is due, log the completed check-in, raise the red-flag escalation into the nurse queue carrying the patient's exact words rather than a paraphrase
- A hard refusal to advise, reassure, or say anything about medication
- Not-reached handling, so a missed call becomes a task rather than a silent gap
- Per-call record with the patient's phrasing quoted verbatim
- One-pager: the workflow, the integration surface, the escalation path with the recall threshold you used and the citable discharge protocol you took the red flags from, and what the build refuses to decide (it never advises, reassures or triages), a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** A judge describes a worsening symptom in folk vernacular that never uses a clinical word. The system escalates, and what lands in the nurse queue is the patient's own sentence rather than a summary that has already thrown away the useful part.

**Scores on:** Impact and Sarvam parameter. **Weak on:** Creativity, since check-in calls are an expected build. The recall tuning and the quoted handoff are the difference.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras for folk symptom descriptions on a phone line, in a language with no clinical register to fall back on. This is where the score is.
- **Supporting** Sarvam-30B for mapping those words onto the sourced red-flag list and for the recall-biased escalation decision, Bulbul for an unhurried call an unwell person can follow. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Outbound at the three intervals: Twilio or Exotel or Plivo · LiveKit or Pipecat if you want tighter control of the audio path · a browser mic page playing your one scripted worsening narration, which is a completely legitimate fallback if telephony is eating your morning
- **Backend** The 24, 72 and 168 hour schedule, plus the escalation threshold: Convex functions with scheduled functions · Next.js route handlers plus a cron · a small FastAPI or Express service with a scheduler · Cloudflare Workers with a cron trigger. For the demo you can compress the intervals to minutes, just say so
- **Data** Discharges, call attempts, symptom quotes verbatim, escalations: Convex · Supabase · Postgres direct · SQLite on disk
- **Comms** The nurse queue, carrying the patient's exact words rather than a summary: a Slack or Telegram message · a Discord webhook · an ntfy.sh topic as a pager · Resend for a daily ward summary
- **Mock or external** The discharge record system: Beeceptor · Mockoon · WireMock Cloud. Never point this at a real hospital system
- **Specific to this build** One fixed worsening narration you can replay, two people to role-play the patient before noon, and a red-flag list plus escalation threshold sourced from a citable discharge protocol you can show on screen. Do not take the clinical content from the model, from your own judgment, or from a URL you have not read.

**Know before you pick this.** Every clinical item, every red flag and the escalation threshold must come from a real discharge protocol you can cite, not from the model and not from you. The agent gives no advice at all: it listens and escalates rather than guessing. Recruit two people to role-play the worsening patient before noon, and script one fixed worsening narration you can replay.

---


## 76 ·
Therapist pre-session intake voice agent for mental health platforms

**Beast · domain · Voice Experience**

> A pre-session intake call that elicits risk markers in a language that has no words for them.

**Why this one.** The axis is eliciting a risk marker when the concept has no word in the language, and once re-pointed this is the hardest card in the batch. Anxiety, panic attack, intrusive thought, self-harm: several Indian languages have no everyday equivalent, and the borrowed English terms either carry stigma or simply do not land with the person you are asking. So you cannot ask the question. You have to ask around it, in behaviour and in the body: sleep, appetite, whether they can sit still, what happens in the chest, what they have stopped doing. Then those answers have to come back out as structure a therapist can read in a minute, with any risk marker escalated to a human rather than scored. Across 1,000+ therapists losing the first 20 minutes of every new-client session to intake basics, the value is obvious and the execution is genuinely hard.

**The scenario.** Aravind runs clinical operations for a mental health platform in Kochi with 1,000+ therapists on it. Every first session burns its opening 20 minutes on history, medication, sleep and living situation, which is the most expensive time in the whole relationship. Sreelatha has booked her first session and takes the intake call from Kozhikode, answering in Malayalam, with no vocabulary for what she has been feeling and her sister in the next room.

**What you will need**
- Scheduled or inbound call, client's language detected, with a text fallback
- A behavioural and somatic question set standing in for concepts with no vernacular term, sourced from a real intake protocol
- No clinical labels on the way in, full structure on the way out
- Privacy handling, since the client may not be alone: a path to defer, lower detail, or move to text
- Risk-marker detection that escalates to a human in the same turn rather than scoring, advising or continuing the script
- Explicit consent to record and to share the intake with the therapist
- Three tool calls: read the booked session from the mocked scheduler, deliver the structured intake to the therapist with the client's own words attached, page a human in the same turn when a risk marker fires
- A hard stop, stated in the prompt and enforced in code: the agent never assesses, diagnoses, reassures or advises
- One-pager: the workflow, the integration surface, the escalation path with the risk threshold you used and the citable intake protocol you took the question set and the markers from, and what the build refuses to decide (no assessment, no diagnosis, no reassurance), a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** A judge answers only in behavioural and bodily terms in a regional language, never naming a clinical concept. The intake still comes out structured and readable in under a minute. Then the judge plants a risk marker and the call escalates to a human within the same turn, with the exact words carried across.

**Scores on:** Sarvam parameter and Impact. **Weak on:** Delight, and it is easy to lose Job-to-be-done by over-reaching into assessment, which is the one thing this product must not do.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam-30B for mapping behavioural and somatic answers into structured intake, and for risk-marker detection against the sourced protocol. This is where the score is.
- **Supporting** Saaras for transcription, Bulbul for a calm, unhurried register. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Scheduled outbound or inbound, with a lower-detail path for a client who is not alone: Twilio or Exotel or Plivo · LiveKit or Pipecat if you want tighter control of the audio path · a browser mic page, which is a completely legitimate fallback if telephony is eating your morning and doubles as the private option here · a plain text chat path for the same reason, which this card genuinely needs rather than treats as a downgrade
- **Backend** The hard stop (never assess, diagnose, advise or reassure) enforced in code and not only in the prompt, plus same-turn escalation: Convex functions · Next.js route handlers · a small FastAPI or Express service · a plain state machine with the escalation as a terminal state
- **Data** Intakes, the question-set version, verbatim quotes, escalations with timestamps: Convex · Supabase · Postgres direct · SQLite on disk. Version the question set, because which version produced an intake matters here
- **Comms** Immediate human escalation and the intake handoff: a Slack webhook · an ntfy.sh topic as a pager, no signup · a Telegram bot · Resend for the structured intake to the therapist
- **Mock or external** The therapist scheduling system: Beeceptor · Mockoon · the Cal.com API if you want a real booking link
- **Specific to this build** A behavioural and somatic question set, every risk marker and every escalation threshold sourced from a real, citable intake protocol you can show. Not from the model, not from your own judgment, and not from a link you have not opened. If you cannot source one before 11:30, pick a different card.

**Know before you pick this.** Every question, every risk marker and every escalation threshold must come from a real, citable intake protocol, never from the model and never from your own judgment. The build must escalate to a human rather than guess, and must never assess, diagnose, advise or reassure. If you cannot source a protocol before 11:30, pick a different card, because inventing this content is worse than not building it.

---


## 77 ·
Shaadi RSVP collection voice agent for wedding planners

**Starter · fun · Voice Experience**

> A warm Hindi call that gets an actual plate count out of relatives who are never going to open a form.

**Why this one.** The axis is resolving vague vernacular plurals and kinship terms into an exact count. Nobody answers this question numerically. They say "hum sab aa rahe hain", "bhaiya ka pariwar bhi aayega", "chhote wale nahi aa payenge", and the caterer needs a number per function, split veg and non-veg. So the arithmetic has to be assembled out of kinship terms and vague plurals, resolved against a guest list, with one clarifying question rather than five, because the fifth question is where an aunty hangs up. WhatsApp form RSVPs sit at 12% completion across a 400+ guest list for exactly this reason, and a warm call in Hindi does far better.

**The scenario.** Nidhi plans weddings in Patna and has 400+ guests on a list for a date that is close. Her WhatsApp RSVP form is at 12% completion, the family's answer to every nudge is that they will tell her later, and the caterer wants numbers. She triggers the calls. A maasi in Bhagalpur picks up, is delighted to hear from someone about the wedding, and says the whole family is coming and that she will bring her brother's people too.

**What you will need**
- Outbound calling from a guest list that records relationships, not just phone numbers
- Kinship-term resolution onto named people already on the list, plus a path for people who are not on it
- A count per function, split veg and non-veg, with travel and stay if you want the extra credit
- Exactly one clarifying question on an ambiguous plural, then a read-back: "I am putting you down as four, correct me"
- A warm Hindi register an older relative will stay on the line for
- A live headcount board per function that a planner and a caterer can both look at
- The case where the person answering is speaking for people who should be called separately
- Two tool calls: write the resolved count against the named guests on the list, and send the read-back so the family can correct it
- One-pager: the workflow, the integration surface, a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** A judge plays an aunty and answers entirely in kinship terms and vague plurals, never a number. The board updates to an exact per-function count, and the read-back names the specific people the system thinks are coming.

**Scores on:** Delight and Job-to-be-done. **Weak on:** Impact, unless you cost out what a catering shortfall at the mehendi actually is.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam-30B for kinship-term resolution and headcount arithmetic out of vague plurals. This is where the score is.
- **Supporting** Saaras for relaxed, overlapping family speech, Bulbul for the warm Hindi register an older relative will stay on the line for. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Outbound plus a live headcount board: Twilio or Exotel or Plivo · plain HTML with a script tag polling for the counts, which is all the board needs · a browser mic page, which is a completely legitimate fallback if telephony is eating your morning
- **Backend** Kinship resolution and the count arithmetic: a single file of plain code with the guest list loaded in, which is honestly the right size for this · Convex functions · Next.js route handlers · a small FastAPI or Express service
- **Comms** The read-back sent so the family can correct it, and the planner when a count moves late: Resend · a Telegram bot, which is the fastest of all · a Slack webhook for the planner. Not WhatsApp, in any flavour, sandboxes included: verification takes days and it will eat your build
- **Data** Guest list with relationships, per-function counts, read-back corrections: a JSON guest list in the repo that the board reads live, which is faster than a database here · Convex · Supabase · SQLite on disk
- **Mock or external** Nothing to mock. There is no external system in this build, the guest list is the only data and you are writing it
- **Specific to this build** A guest list with real kinship structure, including two families where the same kinship term points to different people. That ambiguity is the demo, so build it in deliberately.

**Know before you pick this.** Build the guest list with real relationship structure before you start, including two families where the same kinship term points to different people, because that ambiguity is the demo. Recruit two people who will play a relative and answer only in plurals, before noon.

---


## 79 ·
Murder mystery party host voice agent for social experiences

**Challenging · fun · Voice Experience**

> A voice agent that hosts a 90-minute murder mystery party and plays every suspect in it.

**Why this one.** The axis is per-persona knowledge partitioning across a long session. Several suspects, each with a distinct voice, and, much harder, each with a distinct set of things they know, things they are hiding, and things they must never say. The failure mode is not a wobbly accent, it is the cook revealing something only the driver knows, which ends the game instantly and cannot be walked back. Ninety minutes of state, six players interrogating in Hinglish in whatever order they feel like, and the agent has to stay straight the whole way. Right now the format needs a human host, which means the one person who knows the plot is the one person who cannot play.

**The scenario.** Ishan ships a monthly subscription box to urban Indian subscribers, and the murder mystery edition is the one people post about. It goes out with printed clue cards and an audio file everyone skips, so in practice somebody reads a script aloud all evening and never gets to be a suspect. Six friends around a table at 11pm want to question the driver, then the cook, then the driver again, in Hinglish, and in no order anyone planned for.

**What you will need**
- Multiple suspect personas with distinct Bulbul voices, switched inside one session rather than one voice per call
- A per-persona knowledge partition: known, hidden, forbidden, and what each will admit under pressure
- Shared world state, so a fact revealed to one player is revealed to the table
- A host persona that runs phases, keeps the clock, and hands off to suspects
- Open interrogation in Hinglish, not a menu of questions
- A reveal condition that fires when the group has actually earned it, not on a timer
- A leak guard: a suspect asked about something outside their partition deflects in character rather than answering
- Printed clue cards that match the digital state exactly
- One-pager: the workflow, the integration surface, a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** A judge interrogates two suspects and deliberately asks the cook about something only the driver knows. The cook deflects in character, keeps her voice, and the game keeps its secret. Then the judge asks the driver and gets it.

**Scores on:** Memory and Context and Delight. **Weak on:** Impact, obviously. Do not dress this up as solving anything; it is a good time and that is the product.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam-30B for the per-persona knowledge partitions and the leak guard across ninety minutes. This is where the score is.
- **Supporting** Bulbul for distinct suspect voices switched inside one session, Saaras for Hinglish interrogation from several speakers at once. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** A laptop or speaker in the middle of the table. No telephony at all on this card: a browser mic page with push to talk is the whole interface and the right answer · LiveKit or Pipecat or Vapi if you want a genuinely hands-free room with barge-in · Sarvam streaming APIs wired directly
- **Backend** Phases, the clock, the partitions, the leak guard: plain code with a simple state machine, which is genuinely the right tool for a single-session game · Convex functions · Next.js route handlers · a small FastAPI or Express service
- **Data** Personas, partitions, revealed-fact state, phase and clock: none, hold all of it in memory for one ninety-minute session, which is exactly what this is · Convex or SQLite on disk only if you want to resume a game after a crash. Do not build persistence you will not show
- **Comms** The reveal packet and the recap: a printed handout, which suits the format better than any API · a Telegram bot for the reveal · Resend for the post-game recap with who suspected whom · a Discord webhook if the group has a server
- **Mock or external** Nothing. You are writing the mystery, so every fact in it is already yours. There is no system to mock
- **Specific to this build** The mystery, the per-persona partitions (known, hidden, forbidden) and the printed clue cards written before 11:30, and the cards actually printed. This card is won on the writing.

**Know before you pick this.** Write the mystery, the partitions and the clue cards before 11:30, and actually print the cards. This card is won on the writing, and a team that starts plotting at 3:30 demos a shapeless game with a great voice stack behind it.

---


## 80 ·
Bargaining buddy voice agent for practising haggling in Indian bazaars

**Challenging · fun · Voice Experience**

> A stubborn Hindi shopkeeper who refuses to budge, so you can practise haggling before you face a real one.

**Why this one.** The axis is persona and accent stability under adversarial pressure, and this is a legitimately hard Bulbul problem rather than a costume. The shopkeeper has to hold one regional accent for an entire negotiation, stay in character while the user actively tries to break him with flattery, English, meta questions and walking away, and concede along a believable curve instead of collapsing on the third ask or never moving at all. Persona drift is measurable here, which is what makes it a real test: the same character, ten turns apart, at three stubbornness levels, judged on whether he is still the same man. Foreign tourists and NRIs get fleeced because they never learned to do this, and you cannot learn it on a real shopkeeper without paying tuition.

**The scenario.** Aarti is an NRI back for three weeks and is going to the Sardar Market in Ajmer tomorrow to buy juttis. She knows she will pay triple, has been told to offer a third and walk away, has never done it, and does not want her first attempt to happen with a shopkeeper watching her hesitate. She opens the app and gets a bandhani seller who opens at 1200 and is not remotely interested in her opening offer.

**What you will need**
- A shopkeeper persona with a fixed regional accent held across the whole negotiation
- Escalating stubbornness levels, selectable, with a stated concession curve for each
- Character resistance to persona-breaking: flattery, switching to English, meta questions, asking the agent for advice
- The walk-away move actually working sometimes, because that is the lesson
- A post-round debrief in English: what the opening offer cost, which line moved him, what to say next time
- A drift check comparing the same persona early and late in a session, so stability is shown rather than claimed
- Two or three regional accents, so a user can practise for the market they are actually going to
- One-pager: the workflow, the integration surface, a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** A judge haggles, then tries to break character by switching to English and asking the agent for coaching mid-negotiation, and gets stonewalled in character with the accent intact. Then they walk away, and the shopkeeper calls them back at a lower price.

**Scores on:** Delight and Sarvam parameter. **Weak on:** Impact and Job-to-be-done. It is a practice tool, so say that plainly instead of inventing a market for it.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Bulbul for a persona holding one stable regional accent across a full negotiation, under a user actively trying to break it. This is where the score is.
- **Supporting** Saaras for the user's speech including heavily accented English, Sarvam-30B for the concession curve, character resistance and the English debrief. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** No phone number anywhere in this build. A browser mic page with push to talk and a price meter showing the current ask and the gap is the whole product: plain HTML with a script tag · React with Vite or Next.js if one is already open · LiveKit or Pipecat only if you want barge-in so a user can talk over the shopkeeper, which is arguably part of haggling
- **Backend** The concession curve per stubbornness level, character resistance, the drift check: plain code with a small state machine, which is the right size · Convex functions · Next.js route handlers · a small FastAPI or Express service
- **Data** Personas, concession curves, session transcripts, drift-check comparisons: none, hold the session in memory and render the transcript at the end, which is all a practice tool needs · Convex or SQLite on disk only if you want the drift comparison to survive a refresh
- **Comms** The debrief with the lines that worked and the ones that cost money: render it straight onto the page, which is faster and loses nothing · Resend if you want it emailed · Loops · a Telegram bot
- **Mock or external** Nothing to mock. There is no external system in this build
- **Specific to this build** Reference recordings of real speakers for each accent, and a native speaker of each to listen before you demo. An accent that is slightly wrong reads as caricature, and this card fails ugly when that happens.

**Know before you pick this.** Build your accents from recordings of real speakers and have a native speaker of each listen before you demo, because an accent that is slightly wrong reads as caricature and this card fails ugly when that happens. Record your reference clips before noon, not at 3:30 when you are already committed to the voice.

---


---

# Technical and infrastructure


## 81 ·
Indic speech eval harness

**Beast · technical · Voice Experience**

> A public benchmark that measures whether Indic speech-to-text holds up on code-mixed, noisy, real-world audio, and publishes the method so anyone can re-run it.

**Why this one.** Sarvam's headline claim is code-mixed and regional speech, and right now nobody outside Sarvam can verify it, because the measuring instrument does not exist. The axis is that word error rate is the wrong metric for every job that carries consequence: a transcript that gets a rupee amount or a person's name wrong is useless at a WER that looks excellent. So the thing to build is entity accuracy scored per condition, with one variable changed at a time, so a reader can see which axis degrades and how fast. Build that and you own the reference everyone else cites.

**The scenario.** Aparna is an ML engineer at a lending company in Solapur, three weeks from putting a voice agent on a live collections line. What she has been handed is a vendor comparison sheet with one WER number per provider and no statement of the conditions it was measured under. She needs to know where the stack breaks before it is answering calls: on phone-band audio, in a noisy room, when the borrower switches language mid-sentence, when they correct themselves halfway through an amount.

**What you will need**
- Test set spanning five named conditions, one variable per condition, with reference transcripts
- Entity-level scoring beyond WER: amounts, person names, place names, dates, part numbers
- Phone-band degradation pipeline (8kHz resample plus codec artefacts) so the same utterance exists in clean and degraded form
- Reproducible runner: one command, versioned results, no manual steps
- Per-condition leaderboard with the methodology written up beside it
- Real numbers on the board, not a promise of them: entity accuracy per condition and per entity type, printed next to the WER for the same run so the gap between the two is visible, with the utterance count each number rests on
- Honest failure catalogue: the ten worst utterances, with audio you can play
- A live-scoring panel so an utterance spoken on stage runs through the same pipeline
- One-pager: the workflow, the integration surface, what a reader is promised by these numbers, what happens to a score when a condition is thinly sampled, and what you would not let a team rely on the leaderboard for, a deploy-or-pilot verdict, and why Voice Experience is primary while the harness is only the proof instrument

**Your demo moment.** A judge speaks a Hinglish sentence containing a rupee amount and a person's name. The harness scores it live, shows WER looked fine, and shows the entity score caught an error WER hid. Then it names which condition that utterance belongs to.

**Scores on:** Sarvam parameter and Impact. **Weak on:** Delight, because a leaderboard is not a crowd-pleaser.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras REST and Batch (docs.sarvam.ai) transcribing the same utterances across every condition. This is where the score is, and what a judge examines is your condition design and your entity-level scorer, not the transcription call: the scorer is your own code and no API hands it to you.
- **Supporting** Sarvam-30B only if exact and normalised string matching genuinely fails you on entity comparison, as plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** This card needs almost no plumbing: it is a test set, a runner, a scorer and a results table. A Python script plus a results CSV is a completely legitimate stack · a static HTML page rendered from that CSV · a leaderboard UI is optional polish, build it only once the scorer is right · the live-scoring panel is the one piece of UI worth real time, because it is your demo
- **Backend** Plain Python with a requests loop and a Makefile · a small FastAPI or Express service if the live panel needs an endpoint · Convex functions (convex.dev) if your team already lives there · localhost only, this never has to be deployed
- **Data** A versioned CSV or JSONL of per-utterance results committed to the repo · SQLite on disk · Convex (convex.dev) or Supabase (supabase.com) if you want the leaderboard live · audio on the local filesystem, or Convex file storage or Cloudflare R2 if you need playable URLs
- **Comms** Slack webhook posting each completed run with its per-condition summary (api.slack.com/messaging/webhooks) · Telegram bot (core.telegram.org/bots) · ntfy.sh · or nothing at all, print the summary to stdout
- **Mock or external** Nothing to mock, there is no external system in this build, so do not invent one · the only external worth adding is a second STT provider you already have credits for, if you want a comparison column
- **Specific to this build** The phone-band degradation pipeline is the one unusual dependency: ffmpeg (ffmpeg.org) or sox (sox.sourceforge.net) will do the 8kHz resample plus codec artefacts in a single command, use whichever is already installed. Reference transcripts are hand-written by you, so budget real time for that before you write any scoring code.

**Know before you pick this.** A leaderboard is a weak stage demo, and the live-scoring panel is the only thing standing between you and reading numbers off a screen at 4:00. Build that panel early. Pick this card if you would rather build the instrument than the product.

---


## 82 ·
Store-and-forward vernacular voice on the last mile

**Challenging · technical · Voice Experience**

> Capture vernacular field updates with no signal, then transcribe and confirm them reliably when the network returns.

**Why this one.** The Voice Experience axis is intelligibility after hostile capture: a field update recorded beside traffic or machinery, compressed on a low-end phone and uploaded only when a weak connection returns. The worker must be able to correct the transcription by voice without repeating the whole entry. Offline capture, queueing and reconciliation make the job possible, but they are delivery evidence; the scored Sarvam capability is whether the recovered speech and confirmation flow hold up on the real audio.

**The scenario.** Ravindra supervises a rural distribution operation working out of Jagdalpur. His field staff record what they delivered and collected by voice, in supported Hindi mixed with local place names, standing where the signal comes and goes over an afternoon. Today they write it in a notebook and key it in at night, so half the entries are wrong by the time they arrive. He needs the phone to capture the update with no bars, state honestly that it is queued, and complete transcription and confirmation when connectivity returns.

**What you will need**
- On-device audio capture that completes with no network, with transcription and confirmation explicitly pending until connectivity returns
- Explicit three-state model surfaced to the worker: captured, queued, synced
- Sync reconciliation that survives a mid-upload disconnect without duplicating or dropping entries
- Degradation ladder written down and stated at each step: live transcription at usable signal, queued upload on a weak connection, capture-only at zero bars
- Conflict handling for the same record edited offline twice
- Local storage budget and a stated cap on how many entries can queue
- A test set of compressed, noisy field recordings with amounts, place names and corrections, plus entity accuracy and refusal numbers
- Two calls out: push queued audio to the sync endpoint with an idempotency key, and read server state back to confirm the record landed exactly once
- A supervisor view that distinguishes "not collected" from "collected but not yet synced"
- One-pager: the workflow, the integration surface, what the worker is promised when the screen says queued, what happens if that queue is lost with the phone, and what a supervisor should not read into a record that has not synced, a deploy-or-pilot verdict, and why Voice Experience is primary while offline sync is delivery evidence

**Your demo moment.** Switch the device to airplane mode, record a noisy code-mixed delivery update and show it as captured but not transcribed. Reconnect. The queue drains once, Saaras recovers the amount and place name, and the worker corrects one field by voice before the supervisor sees a confirmed record.

**Scores on:** Sarvam parameter and Memory and Context, since the queue is the memory. **Weak on:** Creativity, because offline sync reads as plumbing right up until the airplane-mode moment lands.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras on compressed, noisy, delayed-upload field audio, recovering amounts, place names and spoken corrections, with Bulbul or text confirmation when the network returns. This is where the score is.
- **Supporting** Sarvam-30B for parsing the confirmed transcript into fields. Offline capture, storage and sync are your own delivery layer. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** The interface on this card is a device, not a page: a PWA with a service worker so it loads with zero bars · React Native or a thin Android wrapper if you already ship one · a plain HTML page loaded once and kept open, which is the cheapest thing that survives airplane mode honestly. Push to talk, one screen, readable in sunlight, whichever you pick.
- **Backend** Convex functions (convex.dev) for sync reconciliation and conflict resolution · Next.js route handlers · a small FastAPI or Express sync endpoint · Cloudflare Workers (developers.cloudflare.com/workers) · localhost plus a tunnel (beeceptor.com/local-tunnel) is a legitimate answer at 4pm
- **Data** The offline store is the interesting choice here and there are three honest answers: IndexedDB in the browser · SQLite on the device · a plain append-only file or localStorage log, which is the least code that survives a reload. Server of record after sync: Convex (convex.dev) or Supabase (supabase.com).
- **Comms** Telegram bot notifying the supervisor when a queued batch syncs (core.telegram.org/bots) · ntfy.sh push, no signup · Slack webhook (api.slack.com/messaging/webhooks) · Resend (resend.com) if the supervisor wants email
- **Mock or external** httpstat.us with random and sleep to simulate flaky and stalled uploads · Beeceptor (beeceptor.com) for the sync endpoint before you have written it · then real airplane mode for the demo, because devtools throttling is not the same thing
- **Specific to this build** The three-state model surfaced to the worker (captured, queued, synced) and the duplicate-safe reconciliation are entirely your own code. No API gives you either, and they are what the axis is about.

---


## 83 ·
Indic voice as a tool other agents call

**Challenging · technical · Voice Experience**

> Expose noisy, code-mixed Indic speech as a typed capability, so another agent can act on what was actually said and stop when the audio is unusable.

**Why this one.** Every other card in this library puts a human directly at the other end. Here the Voice Experience proof is whether real voice-note conditions survive before an agent is allowed to act: code-switching, background noise, self-corrections, amounts, names and partial words. The typed contract is how the result is consumed, but it is not a scoring branch. A tool that converts uncertain speech into a plausible instruction is worse than one that returns the evidence, confidence and a refusal.

**The scenario.** Kabir builds internal automation at a logistics company in Faridabad. His agent handles a shipment trail end to end, except that the moment an input is a noisy Hindi-Marathi voice note with English part numbers it drops to a human queue and sits for a day. He wants one voice tool his agent can call and branch on, including the branch where the audio or a consequential entity is unusable.

**What you will need**
- A typed operation that transcribes a vernacular voice note and extracts named entities, returning the evidence span, per-entity confidence, detected language, cost and latency
- A refusal type distinct from an error type, documented, that a calling agent can branch on
- Reference implementation an agent consumes without prompt surgery
- Two worked examples: one clean success, one low-confidence refusal handled correctly downstream
- Cost and latency returned in-band so the calling agent can budget its own run
- Docs a stranger's agent can follow with no human explanation alongside them
- A test set covering code-switching, noise, corrections, amounts, names and alphanumeric part numbers, with entity accuracy and refusal numbers
- One-pager: the workflow, the integration surface, what a caller is promised by the contract, what it returns on low confidence, and what you would not let a consuming agent rely on, a deploy-or-pilot verdict, and why Voice Experience is primary while the typed contract is delivery evidence

**Your demo moment.** Hand the tool to a general coding agent with no Indic capability and no prior knowledge of your work. Give it a vernacular task. It completes the task end to end, live, without the builder touching the prompt. Then feed it deliberately unusable audio and watch it take the refusal branch instead of inventing an answer.

**Scores on:** Creativity and Sarvam parameter, since almost nobody builds for a non-human user. **Weak on:** Delight, because there is no human interface by design, so the live agent run is the only surface a judge can admire.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras on noisy, code-mixed voice notes with self-corrections and consequential entities, returning literal evidence that lets the tool refuse an uncertain amount, name or part number. This is where the score is.
- **Supporting** Sarvam-30B for typed entity extraction after the transcript and for a downstream summary, as plumbing. The schema and refusal type are your delivery layer. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** There is no human interface on this card by design, and saying that out loud is part of the demo. What you ship instead: a typed endpoint with an OpenAPI schema · an MCP server, if the consuming agent speaks MCP · a docs page a stranger's agent can follow with nobody explaining it alongside · a plain JSON POST plus a copy-pasteable tool definition, which is the cheapest version and enough
- **Backend** FastAPI, which gives you the typed schema and a docs page for free · Convex functions (convex.dev) for the endpoint and confidence normalisation · Next.js route handlers · Cloudflare Workers (developers.cloudflare.com/workers)
- **Data** Convex (convex.dev) for call logs, per-field confidence history and cost and latency accounting · Supabase Postgres (supabase.com) · SQLite on disk · or none, hold the run in memory and log to stdout, since the demo is one agent session
- **Comms** Slack webhook logging every tool call with its confidence, cost and latency so the contract is observable on stage (api.slack.com/messaging/webhooks) · Telegram bot (core.telegram.org/bots) · a live request log rendered on the docs page · Resend (resend.com) for a run summary
- **Mock or external** Do not mock the consumer. A real general-purpose coding agent (Claude Code, Cursor, Windsurf, whatever you have open) calling the tool unaided is the test itself, not a stand-in for one · httpstat.us to force the transport error path so you can prove it is distinct from a refusal

---


## 84 ·
Live-voice verification against cloned voices

**Beast · technical · Voice Experience**

> Establish that the voice on this call is a live human and not a clone, in the caller's own language, over a phone line.

**Why this one.** Five independent investors published a request for this in 2026 and across thirteen weeks of Product Hunt nothing shipped against it. India is the largest voice-fraud market on earth and the fraud is conducted in exactly the languages Sarvam covers. The axis is not accuracy, it is calibration: a false positive blocks a real customer at the worst possible moment, so the system has to know when it does not know and say so. The whole card lives in the third outcome.

**The scenario.** Farhan runs fraud operations at a financial institution in Mumbai. On his desk is the recording of a call where an instruction was authorised and the voice on the line was not the customer's, and it sounds entirely convincing. His existing control is an agent asking security questions that anyone holding the customer's documents can answer. He needs a layer that decides on the voice itself, in the language the caller speaks, and hands the marginal cases to a human instead of guessing.

**What you will need**
- Liveness challenge that works in at least three Indic languages and cannot be satisfied by a pre-recording
- A cloned-voice test set built from consenting volunteers, plus genuine samples of the same speakers
- Three-outcome decision with an explicit uncertain band, and a stated threshold with the reasoning for where it sits
- Phone-band degradation applied to both genuine and cloned audio so the test is fair
- False-positive cost accounting: what wrongly blocking a real customer costs, stated in rupees
- Confusion matrix from a real run with the counts stated, not a projection: true accepts, false accepts, true rejects, false rejects, and how many samples landed in the uncertain band
- Three tool calls: fetch the enrolled voiceprint for the account, write the verification outcome with its score and band, escalate an uncertain outcome to the fraud desk
- One deliberately marginal sample kept aside, for the third outcome
- One-pager: the workflow, the integration surface, the false-positive cost (which genuine customers are rejected by your threshold, at what moment, and how they get unblocked), a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** Clone a judge's voice with their consent before the session. On stage the clone attempts verification and is rejected. The real judge attempts it and passes. Then run the deliberately marginal sample and show the system decline to decide rather than guess.

**Scores on:** Sarvam parameter and Impact. **Weak on:** Job-to-be-done completion, because an honest run can land close to chance, and a calibrated system that verifies less than you hoped is the good outcome rather than the impressive one.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras streaming (docs.sarvam.ai) for the challenge response, with Bulbul issuing the challenge in the caller's language. This is where the score is. The calibration that carries the axis, the three-outcome decision and where the uncertain band sits, is your own threshold code and not something a Sarvam call returns.
- **Supporting** Sarvam-30B for checking that the spoken response actually satisfies the challenge, and Mayura if you localise the challenge text, as plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Phone: an inbound number on Twilio (twilio.com), Exotel (exotel.com) or Plivo (plivo.com) routed into the verification line, and Exotel is usually less friction for Indian numbers · browser mic via getUserMedia as the fallback if telephony onboarding stalls, and it will do for the stage as long as you say out loud that the audio is not phone-band · a plain HTML record-and-post page is the cheapest viable version
- **Backend** A FastAPI service, the shortest path if your embedding model is Python · Convex functions (convex.dev) for scoring, threshold logic and the three-outcome decision · Next.js route handlers · Cloudflare Workers (developers.cloudflare.com/workers) for the telephony webhook
- **Data** Convex (convex.dev) for the enrolled-speaker set, per-call scores, the confusion matrix and threshold history · Supabase Postgres (supabase.com) · SQLite plus a CSV of the run, which is all a confusion matrix actually needs · audio in Convex file storage, Cloudflare R2 or on disk
- **Comms** Slack webhook escalating every uncertain outcome to the fraud desk (api.slack.com/messaging/webhooks) · Telegram bot (core.telegram.org/bots) · Resend (resend.com) for the case record · ntfy.sh if you want a phone to buzz on stage
- **Mock or external** Mockoon (mockoon.com) or Beeceptor (beeceptor.com) for the customer and account lookup · httpstat.us if you want that lookup to time out mid-verification
- **Specific to this build** The consented cloned-voice set is build-specific prep and it is the long pole: clones plus genuine samples of the same speakers, recorded before the sprint. Apply phone-band degradation to genuine and cloned audio equally with ffmpeg (ffmpeg.org) or sox (sox.sourceforge.net), or the comparison is not fair. Any open speaker-embedding model you can run locally is enough for scoring, you are not training anything today.

**Know before you pick this.** You need a consented cloned-voice set prepared in advance, with genuine samples of the same speakers. That is prep work outside the sprint: arrive with it or spend the first third of the day recording volunteers. This is also research territory, and a team can land barely above chance and have nothing to show, which makes it the highest variance card in the library and the most fundable thing anyone could build here.

---


## 85 ·
Three-language site meeting, one canonical record

**Beast · technical · Voice Experience**

> Three people, three languages, one live session. Each hears the others in their own language and the agent holds the single record of what was actually agreed.

**Why this one.** Multiplayer AI was named independently by YC, a16z and Hannah Grey as a 2026 request, the market only started shipping it eight weeks ago, and every entrant is English-only. Multilingual multiplayer needs 23-language input, 23-language translation and 11-language output at once inside a conversational latency budget. The verified Sarvam coverage makes that Indic-first hard case practical; this card does not depend on an unsupported claim that no alternative stack exists. The axis is turn-taking under translation lag: who is interrupting whom when the audio each person hears is offset, and what the canonical record says when three languages disagree about the decision.

**The scenario.** Sridhar is project manager on a substation build outside Trichy. His morning coordination call has a Tamil-speaking site technician, a Hindi-speaking safety supervisor and an English-speaking client representative, and it runs through whoever can interpret. Yesterday's call produced three different accounts of who was clearing the trench and by when, and the trench is not cleared. He wants each person to speak and hear their own language, and one record of decisions and owners the next shift can act on.

**What you will need**
- Three concurrent participants, each with an independent inbound and outbound language
- Turn-taking that works under translation lag, with a stated policy for overlapping speech
- One canonical decision record, not three transcripts, with a named owner per decision
- Disagreement handling: what the record says when the three renderings diverge on a material point
- Handover, so the next shift's supervisor picks up from the record without re-litigating it
- Two tool calls: write each agreed decision with its named owner to the mocked site system, and deliver the canonical record to each participant in their own language
- Latency budget stated per hop, with per-turn p95 measured on a real three-way session (capture, transcribe, translate, speak) rather than a target you hope to hit
- A replayable three-way script, so you are not recruiting three humans per iteration
- One-pager: the workflow, the integration surface, whose account of the meeting is authoritative when the three languages disagree on a material point and who can correct the record afterwards, a deploy-or-pilot verdict, and why you declared Voice Experience rather than another branch

**Your demo moment.** Three judges, one per language, unrehearsed, holding a real conversation about a real decision. At the end each reads the canonical record in their own language and confirms it says what they agreed. No staging is possible.

**Scores on:** Memory and Context and Sarvam parameter, since the canonical record is the whole product. **Weak on:** Job-to-be-done completion, because a latency slip does not degrade this build, it breaks it.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras streaming per participant, Mayura for cross-language relay and Bulbul streaming per outbound leg (docs.sarvam.ai). This is where the score is, and the scored craft is turn arbitration under relay lag, which is your own state machine rather than anything the streaming APIs decide for you.
- **Supporting** Sarvam-30B extracting decisions and owners into the canonical record, as plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Three concurrent legs, each with an independent inbound and outbound language, is the hard requirement. LiveKit (livekit.io) or Pipecat (pipecat.ai) genuinely earn their place on this card, because you need per-participant audio in and out and barge-in control rather than one mixed stream · three phone legs via Twilio (twilio.com) or Exotel (exotel.com) into a shared session · a three-tab browser room over plain WebSockets and WebRTC is the cheaper path and demos fine with three laptops on stage
- **Backend** A Python or Node service holding the session in process, often simplest for an audio path · Convex functions (convex.dev) for session state, turn arbitration and the decision record · Cloudflare Workers with a Durable Object per session (developers.cloudflare.com/workers) · localhost plus a tunnel (beeceptor.com/local-tunnel)
- **Data** Convex real-time (convex.dev) for the shared session, the decision record with owners and per-hop latency · Supabase realtime (supabase.com) · in-process memory plus a JSON dump at the end of the call, which is enough for a single-session demo
- **Comms** Resend (resend.com) delivering the canonical record to each participant in their own language · Telegram bot (core.telegram.org/bots) · Slack webhook (api.slack.com/messaging/webhooks) · a shared read-only web page is the cheapest handover
- **Mock or external** Mockoon (mockoon.com) or Beeceptor (beeceptor.com) for the site system the decisions write back to · httpstat.us with sleep to inject relay lag deliberately and watch what turn-taking does under it
- **Specific to this build** Two things. Per-hop latency timing, instrumented before you build anything on top of the audio path. And a replayable three-way script: three pre-recorded audio files played into the three legs, so you are not recruiting three humans for every iteration.

**Know before you pick this.** Latency is brutal and this demo fails loudly rather than quietly if it slips. Put your strongest engineer on the audio path from hour one, measure per hop before you build anything on top, and recruit your three language speakers before noon.

---


## 86 ·
Provably-correct safety notice in 22 languages

**Challenging · domain · Document Intelligence**

> Verify the final rendered safety notices in every script against one approved master, and block any artwork whose warning, dosage or deadline drifted.

**Why this one.** The Document Intelligence axis is final-artwork verification, not translation in the abstract. A correct string can become a dangerous printed notice when a line drops during layout, a negation wraps into the wrong panel, a dosage is rendered in the wrong script or a low-resolution export makes one digit unreadable. The system must read the actual rendered PDFs or pack-label images, align every consequential clause to the approved master, preserve source traceability and block anything it cannot verify. Translation helps create and compare the versions; the scored surface is whether the documents that will actually ship are structurally complete and safe to publish.

**The scenario.** Anjali is compliance lead at an agrochemical manufacturer in Ahmedabad, issuing a revised handling and first-aid notice that has to go out with every pack sold nationally. The approved master is English, dense with negations, conditionals and one dosage instruction where a missing "do not" changes the outcome. An agency returns final print PDFs in many scripts, and she has to know which artwork can ship without trusting the editable source or reading every language herself.

**What you will need**
- Ingest final rendered PDFs or photographed labels, not source text pasted into a field
- Recover reading order, clause boundaries, warnings, dosage or deadline fields and their page or panel coordinates
- Clause-level alignment to the approved master, with translation and back-translation only as supporting evidence
- Per-field confidence and source crops for every consequential value
- Publication gate that blocks missing, duplicated, reordered or unreadable clauses and states which panel and why
- A deliberately hard set: mixed scripts, dense layout, a negation, a dosage or deadline and one low-resolution export
- Reviewer view usable by someone who does not speak the target language, with every claim linked to the final artwork crop
- An audit trail of what was blocked, in which language, on what document evidence and who overrode it
- One-pager: the workflow, the integration surface, which final artworks you would publish and which you would withhold, a deploy-or-pilot verdict, and why Document Intelligence is primary while translation is supporting evidence

**Your demo moment.** A judge picks a rendered language version. The system links every approved clause to its exact crop, then blocks one artwork because a wrapped warning lost its negation and another because a dosage digit is unreadable. A fluent reviewer confirms the blocked evidence rather than trusting a translation-only score.

**Scores on:** Sarvam parameter and Job-to-be-done completion. **Weak on:** Delight, because a clause-level diff view is a reviewer's tool, so the refusal has to be the moment that lands.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam Doc AI and Sarvam Vision on final rendered notices, recovering reading order, clause boundaries, consequential fields and source crops across scripts, with refusal on unreadable or structurally missing content. This is where the score is.
- **Supporting** Sarvam Translate for translation and back-translation evidence · Sarvam-30B for clause alignment and the plain-language block reason. Plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** A single page showing the approved master, final-artwork crop, alignment and gate decision per clause is enough · Next.js or React with Vite · Streamlit or Gradio · or one static HTML report written by a script. The evidence crop and refusal are the views that matter.
- **Backend** A plain Python or Node script that runs the whole pipeline and writes results out · Convex functions (convex.dev) for the diff, confidence rollup and the gate · Next.js route handlers · a small FastAPI or Express service
- **Data** Convex (convex.dev) for clause alignment, per-field confidence, document coordinates, gate decisions and the audit trail · Supabase Postgres (supabase.com) · SQLite or a JSON file on disk, which is a perfectly honest audit trail for one notice
- **Comms** Resend (resend.com) emailing the compliance reviewer the blocked clauses · Slack webhook (api.slack.com/messaging/webhooks) · Telegram bot (core.telegram.org/bots) · or nothing, the reviewer view is the notification
- **Mock or external** Nothing external to mock, there is no downstream system in this build · Beeceptor (beeceptor.com) only if you want to show the publish step actually posting somewhere once the gate passes
- **Specific to this build** Prepare actual rendered variants: one correct, one with a dropped or moved negation, one with a duplicated line and one low-resolution export with an unreadable digit. Keep the editable source out of the verification path so the system proves what will print, not what the agency intended.

---


## 87 ·
Handwritten land mutation records, one district

**Beast · domain · Document Intelligence**

> Extract structured, verifiable ownership records from handwritten and scanned land registers, and refuse the fields it cannot read.

**Why this one.** Property disputes are India's largest civil case category and the underlying records are handwritten, scanned, in regional scripts, and sometimes decades old. This is Doc AI's hardest realistic case and there is no global equivalent, because the problem does not exist elsewhere. The axis is refusal: a land record that silently invents an owner name or a plot number is not a worse product, it is a dangerous one. The top bands belong to the team whose system reliably says it cannot read a field and routes it to a human.

**The scenario.** Bhaskar is a records officer digitising mutation registers for one taluk in Khammam district. The bound volumes in front of him carry several hands on a single page, corrections struck through and rewritten in the margin, faded ink, and plot numbers overwritten once already. He photographs pages on a phone, at an angle, in office light, and the same plot sometimes appears twice with two different owners.

**What you will need**
- Handwritten regional-script extraction from photographed pages, not text-layer PDFs
- Per-field confidence with an explicit refusal state and a stated threshold
- Multiple hands and struck-through corrections in the same document handled correctly
- Two tool calls: fetch the prior entry for the same plot from the mocked records system to reconcile against and surface contradictions, and route a refused field into the escalation queue
- Escalation view showing the cropped field image, not the whole page
- A held-out page the system has never seen, used live
- Stated numbers on that held-out page: per-field accuracy and refusal rate, field type by field type, plus the field types it fails on most with images
- Scope discipline: one district, one register type
- One-pager: the workflow, the integration surface, provenance (which fields are machine-read, which a human confirmed, which the system refused, and who bears the cost when an owner name or a plot number is read wrong), a deploy-or-pilot verdict, and why you declared Document Intelligence rather than another branch

**Your demo moment.** Hand the system a scanned page it has never seen. It extracts the entry, and on the one field a judge can see is genuinely illegible it declines and routes rather than inventing an owner name. Then it flags where this page contradicts the prior entry for the same plot.

**Scores on:** Sarvam parameter and Job-to-be-done completion. **Weak on:** Creativity, since digitising records is an obvious build, so the refusal behaviour and the contradiction flag are what separate you.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam Doc AI (docs.sarvam.ai) for handwritten regional-script extraction from photographed pages. This is where the score is. The refusal state that carries the axis, the threshold and the decision to decline a field, is your own code wrapped around the response, not something Doc AI decides for you.
- **Supporting** Sarvam-30B for reconciliation against prior entries and plain-language contradiction wording, as plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Camera capture plus file upload, and `<input type="file" capture="environment">` is the entire capture feature · Next.js or React with Vite for the review view · a plain HTML page with a fetch call is enough. Spend your interface time on the review view that shows the cropped field image, not on the capture screen.
- **Backend** Convex functions (convex.dev) for confidence thresholds, the refusal state and contradiction detection · Next.js route handlers · a small FastAPI or Express service · Cloudflare Workers (developers.cloudflare.com/workers) · localhost plus a tunnel (beeceptor.com/local-tunnel)
- **Data** Convex (convex.dev) for extracted entries, per-field confidence, the refusal queue and plot history, with Convex file storage for page images · Supabase Postgres plus Supabase Storage (supabase.com) · SQLite plus the local filesystem · Cloudflare R2 or S3 if you only need somewhere to put images
- **Comms** Resend (resend.com) emailing the records officer the escalated fields · Telegram bot (core.telegram.org/bots) · Slack webhook (api.slack.com/messaging/webhooks) · or the in-app refusal queue on its own, which is where a records officer actually works
- **Mock or external** Mockoon (mockoon.com) or Beeceptor (beeceptor.com) for the prior-records system you reconcile against · httpstat.us if you want that lookup to fail while a page is mid-extraction. Write the prior entries yourself as fixtures and never point this at a real land-records endpoint.
- **Specific to this build** Real scanned register pages are the prep that decides this card: several hands on one page, a struck-through correction, one faded, one skewed, and one held back unseen for the demo. A phone camera and an hour will get you there if sourcing fails.

**Know before you pick this.** You need real scanned register pages sourced before the sprint starts, with one page held back unseen for the live demo, and that sourcing is prep work outside the sprint. Vary them deliberately: multiple hands, a struck-through correction, one faded, one skewed. A team that scopes this to "India's land records" instead of one district and one register type will demo a screenshot.

---


## 88 ·
Crop insurance claim from handwritten sowing records

**Challenging · domain · Document Intelligence**

> Decide a crop insurance claim from handwritten land and sowing records, where a wrong number is a wrongly rejected farmer.

**Why this one.** Crop claims turn on documents that are handwritten, seasonal, in regional scripts, and held by the person least able to contest a wrong reading. This is the same hard edge as card 87 with a decision attached, which makes calibration unavoidable: the system has to be willing to halt. The axis is that both failure directions are expensive and asymmetric, since a wrongly approved claim costs money and a wrongly rejected one costs a household its season.

**The scenario.** Sushma is a claims officer in Latur handling seasonal claims after a bad spell in the sowing window. Each claim arrives as a phone photograph of a land record and a page of a sowing register, filled in by hand in Marathi, with the sown area written in one hand and amended in another. She has to decide, she has to be able to say why, and the farmer she rejects will not be in a position to argue with her arithmetic.

**What you will need**
- Extraction of decision-critical fields from photographed handwritten records
- Eligibility decision with the governing rule stated in plain language, in the farmer's language
- Hard halt on low confidence in any decision-critical field, naming the field
- Three claim packets prepared before the demo, one per outcome: one that approves, one that should be rejected and is rejected for a stated and correct reason, one with a genuinely illegible critical field that halts rather than guesses
- Both error costs stated: wrongly approved against wrongly rejected
- Three tool calls: fetch the policy and scheme rules for the claim, write the decision with the governing rule attached, push a halted claim to the claims officer naming the unreadable field
- Stated numbers on a held-out packet the system has never seen: per-field accuracy on the decision-critical fields and the halt rate, measured on that packet rather than on the three you tuned against
- One-pager: the workflow, the integration surface, provenance (which fields are machine-read, which a human confirmed, which the system refused, and who bears the cost when a sown area is read wrong and a household loses its season), a deploy-or-pilot verdict, and why you declared Document Intelligence rather than another branch

**Your demo moment.** Three claims run live. One approves. One rejects, with the rule named in plain language. One halts on an illegible field and names the field. A judge picks which is which before the system runs.

**Scores on:** Impact and Job-to-be-done completion. **Weak on:** Creativity, since this sits next to card 87, so the halt and the plain-language rule statement are what carry it.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam Doc AI (docs.sarvam.ai) for handwritten field extraction from photographed land and sowing records. This is where the score is. The halt gate, which fields are decision-critical and at what confidence you stop rather than decide, is your own code and not a flag the extraction returns.
- **Supporting** Sarvam-30B for eligibility reasoning and the plain-language rule statement, Mayura and Bulbul to deliver the reason in the farmer's language, all as plumbing. Additional Sarvam calls do not raise the Sarvam parameter score.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Camera capture plus file upload for the two document types, and `<input type="file" capture="environment">` covers capture · Next.js or React with Vite for the claims-officer decision view · a plain HTML page with a fetch call. The decision view showing the governing rule and any halt is where the interface time belongs.
- **Backend** A small FastAPI or Express service, which suits a rules engine well · Convex functions (convex.dev) for the decision engine and the halt gate · Next.js route handlers · Cloudflare Workers (developers.cloudflare.com/workers)
- **Data** Convex (convex.dev) for claims, extracted fields with confidence, decisions with the governing rule and the halt queue · Supabase Postgres plus Supabase Storage (supabase.com) · SQLite plus the local filesystem, which is plenty for three demo packets
- **Comms** Resend (resend.com) emailing the claims officer on every halted claim, naming the unreadable field · Telegram bot for the approve and reject outcome log (core.telegram.org/bots) · Slack webhook (api.slack.com/messaging/webhooks) · ntfy.sh
- **Mock or external** Mockoon (mockoon.com) or Beeceptor (beeceptor.com) for the policy and scheme-rules API · httpstat.us if you want the rules lookup to fail mid-decision. Write the scheme rules yourself as fixtures, do not go hunting for a real government endpoint.
- **Specific to this build** Three real claim packets photographed by hand, one per outcome, with the illegible field genuinely illegible rather than blurred in software. That is prep before 11:30, and the halted claim is the one that carries the demo.

---


---

# Public Services


## 89 ·
Living museum for unreadable collections

**Challenging · domain · Document Intelligence**

> Photograph an unseen manuscript, inscription or object label and turn it into a source-traceable story a visitor can understand in their own language.

**Why this one.** The axis is not OCR accuracy on a label. Museums hold objects whose meaning is split across faded writing, old catalogues, marginal notes, stamps, mixed scripts and the physical arrangement of the page. A text dump removes the relationships that make the object intelligible. The product has to reconstruct what is on the source, show where every claim came from, isolate what it could not read and then make the result accessible without pretending that a generated interpretation is a curator-approved fact. That combination of difficult Indian documents, provenance and multilingual access is exactly the hard edge this branch is meant to expose.

**The scenario.** Meera curates a district museum in Thanjavur with a small staff and hundreds of palm-leaf transcriptions, donation registers and handwritten catalogue cards that visitors cannot read. A Hindi-speaking family wants to understand an object whose label is in Tamil and whose older accession note includes handwritten English. Meera photographs both under gallery lighting; the product reconstructs one linked record, flags an unreadable line for her, and publishes a source-traceable Hindi visitor page only after her correction.

**What you will need**
- One tightly scoped collection type: accession cards, inscriptions, manuscript pages or historical registers
- Phone-photo ingestion with skew, fading, mixed scripts and at least one handwritten region
- Reconstruction that preserves reading order, headings, table or catalogue relationships and the source page
- Source traceability from every represented section back to the photograph
- Explicit uncertain regions that a curator can inspect and correct without redoing the page
- Separation between machine-read facts, curator-approved interpretation and generated visitor explanation
- Visitor output in one or two supported languages, written and optionally spoken
- One held-back museum document chosen by someone outside the team
- A stated number from the held-back set: field or region accuracy, uncertain-region recall and curator correction time
- One-pager: the collection boundary, rights and attribution, what leaves the museum, who can approve an interpretation, what the system refuses to claim, and why Document Intelligence is Primary even when the visitor hears the result

**Your demo moment.** A judge photographs a difficult catalogue card the team has not seen. The system reconstructs the mixed-script record, lets the judge click a claim to see its exact source region, refuses one faded line and produces a visitor explanation that labels curator-approved facts separately from generated context.

**Scores on:** Document Intelligence and Delight. **Weak on:** Job-to-be-done completion, unless the output actually becomes a usable accession record or visitor artifact rather than an impressive extraction screen.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam Vision for the unseen photographed museum material, preserving structure across mixed scripts, handwriting, fading and layout. The source map, uncertain-region review and boundary between extracted fact and interpretation are your application logic and are where the product becomes trustworthy.
- **Supporting** Sarvam Translate or Mayura for the visitor language, Bulbul v3 for an optional spoken explanation in a supported language and Sarvam-30B for a clearly labelled visitor narrative. These support access; they do not replace curator approval.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** A camera upload beside a reconstructed document and source-region viewer · Next.js or React with Vite · a single HTML page with the photograph on the left and the structured record on the right. Spend interface time on provenance and correction, not a museum dashboard.
- **Backend** Next.js route handlers · a small FastAPI or Express service · Convex functions for extraction state and curator corrections · a plain local script that writes JSON and annotated crops
- **Data** Convex file storage and tables · Supabase Storage plus Postgres · SQLite and a local image folder, for source images, represented regions, curator decisions and visitor outputs
- **Comms** A QR page for the visitor · Resend for a curator review request · no comms at all if the finished visitor artifact is rendered in the app
- **Mock or external** A mocked accession endpoint on Beeceptor or Mockoon if you want to prove the corrected record writes somewhere · otherwise export a standards-shaped JSON record and show it being saved
- **Specific to this build** Four or five rights-cleared documents from one collection type, photographed under gallery-like conditions, with one held back by a curator, historian or teammate who did not build the extractor

**Know before you pick this.** Use public-domain or permissioned material and name the institution or source. Do not let generated historical context appear as extracted fact. A beautiful invented story is a failure on this card.

---


## 90 ·
People's archive from one government record chain

**Beast · domain · Document Intelligence**

> Reconstruct one citizen's history across damaged government records, preserve every source and stop where the archive stops.

**Why this one.** Government-document products usually begin with a current form and end with extracted fields. Historical public records are harder because the answer lives across time: a name changes spelling, a village changes jurisdiction, one record is handwritten, another is typewritten, a seal covers a date and a correction in the margin supersedes the original entry. The axis is chronological and entity reconstruction with controlled uncertainty. The product must connect records that belong together without silently turning resemblance into legal identity, and it must make the missing link visible instead of manufacturing continuity.

**The scenario.** Asha is helping her mother assemble evidence for a pension correction. The family has a 1987 employment register page, two transfer orders, a service-book extract and a later identity document. The name appears in two scripts and three spellings, one transfer date is hidden under a stamp and the department has no single digital history. Asha needs a traceable packet that shows what is established, what conflicts and what still needs a certified record.

**What you will need**
- One bounded government record chain: pension service, school record, municipal property history, cooperative membership or another sourced workflow
- Three to five document types spanning more than one date, script or physical condition
- Structure-preserving extraction from handwriting, stamps, tables, marginal corrections and degraded scans
- Cross-script entity matching that distinguishes a probable match from a verified identity
- Chronological reconstruction with superseded facts and conflicts kept visible
- Page, row or source-region provenance for every timeline event
- A missing-evidence list rather than a fabricated bridge between records
- Exportable evidence packet for a human official or archivist, not an automated entitlement decision
- One held-back packet with at least one contradiction and one unreadable critical region
- One-pager: the procedural boundary, document retention, who may see the packet, what counts as evidence versus inference, and what the product will never assert as a legal conclusion

**Your demo moment.** A judge supplies an unseen fourth record. The timeline places it correctly, updates one spelling variant, shows the exact source for every event and refuses to connect one ambiguous entry until a human supplies the missing evidence.

**Scores on:** Impact and Document Intelligence. **Weak on:** Creativity, if this becomes generic archival OCR; the chronological contradiction model and honest missing-link state are the product.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Sarvam Vision for mixed-script, handwritten and degraded government records with tables, stamps and corrections. The scored application layer is the provenance-preserving timeline and the refusal to turn an uncertain entity match into a fact.
- **Supporting** Sarvam-30B for comparing extracted records and drafting a plain-language evidence summary, with Sarvam Translate for a citizen-facing version. Neither is allowed to invent a missing record or make an eligibility decision.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** A document tray, a chronological timeline and a source viewer · Next.js or React with Vite · Streamlit if Python is your fast path · a static HTML report generated from JSON is enough if every event links back to its page
- **Backend** FastAPI or Express for extraction and entity matching · Convex functions for case state and corrections · Next.js route handlers · a local Python pipeline for the fastest defensible partial
- **Data** SQLite with a document, entity, event and evidence table · Convex · Supabase Postgres and Storage · local JSON plus image crops for a single demo case
- **Comms** Export a PDF or shareable evidence page · Resend it to a mocked records officer · no notification needed if the packet itself is the completed job
- **Mock or external** Beeceptor or Mockoon for the records-office intake queue · do not connect to a real government system during the sprint
- **Specific to this build** One real, redacted and permissioned record chain assembled before build start, plus one held-back document carrying a contradiction. The record chain matters more than having twenty unrelated samples.

**Know before you pick this.** This is not a legal-verification or entitlement engine. The product organizes and traces evidence for a human process. If the demo says a person is legally entitled to something, you have crossed the boundary.

---


---

# Everyday


## 91 ·
A prayer companion that waits for you

**Challenging · fun · Voice Experience**

> Recite one prayer at your own pace while the companion quietly follows the text, keeps your place and helps only when you ask.

**Why this one.** Most voice products are designed to seize a pause and answer. Prayer and recitation invert that behaviour. A long silence may be intentional, repetition may be part of the practice and the respectful action is often to remain quiet. The axis is turn-taking and alignment under slow, partial, repeated speech: following where the person is in an approved text, surviving a skipped or repeated line and offering the smallest useful prompt without grading devotion or talking over the user. That is a far more interesting Voice Experience test than another question-answering agent.

**The scenario.** Seventy-two-year-old Lata learned a Marathi prayer from her mother and wants to teach it to her granddaughter in Bengaluru. The granddaughter can understand Marathi but reads Devanagari slowly. They open one approved version of the prayer together. Lata recites with long pauses and repeats a line; her granddaughter asks for the next line and later asks what one phrase means.

**What you will need**
- One prayer or devotional text in one declared tradition, sourced from an approved edition or participating community
- Spoken recitation rather than singing or melody as the supported input boundary
- Streaming alignment between the recitation and the reference text
- Turn-taking tuned for long intentional pauses, repetitions, skipped lines and requests for help
- A quiet default: no interruption unless the user asks or explicitly enables guidance
- Native script, transliteration and a reviewed meaning or explanation kept as separate layers
- Original human reference audio where pronunciation is sacred or community-specific
- One elder or first-time user who did not build the product
- A stated result from three recitations: place-recovery success after a skip or repeat, false interruptions and time to resume
- One-pager: the source edition, community review, recording consent, what the system never judges, what audio is stored and why Voice Experience is Primary

**Your demo moment.** A first-time user begins midway, pauses for several seconds, repeats a line and skips the next one. The companion does not interrupt, keeps the correct place and, only when asked, gives the smallest next-line prompt and a reviewed explanation.

**Scores on:** Voice Experience and Delight. **Weak on:** Impact, unless the team can defend a real access, learning, preservation or participation metric for the community it chose.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras v3 streaming for slow, partial and repeated spoken recitation, with your own text-alignment and pause policy deciding when silence is intentional and when help was requested. That turn-taking behaviour is the product.
- **Supporting** Sarvam Vision for a photographed prayer page, Sarvam Translate or Mayura for a reviewed explanation and Bulbul v3 for navigation or explanation in a supported language. Use approved human audio rather than synthetic recitation where pronunciation carries religious authority.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** One large-text page with the current line, push-to-start and an explicit help button · a mobile web page · React or plain HTML with Web Audio. Avoid chat bubbles and settings.
- **Backend** A small Node or Python service holding the reference text, alignment state and pause policy · Convex if you want progress across family sessions · in-browser logic for one prayer and one session
- **Data** A versioned reference text with source attribution, transliteration, reviewed explanation and consented audio · SQLite, Convex or a local JSON file
- **Comms** A family share link or saved practice summary · no outbound communication is necessary
- **Mock or external** Nothing external to mock · use prerecorded recitations for repeatable tests and a live microphone for the demo
- **Specific to this build** Three consented recitations containing natural pauses, repeats and skips, plus one approved reference edition and a reviewer who understands the language and tradition

**Know before you pick this.** Do not score faith, devotion or theological correctness. Scope to spoken recitation, not singing, and state which language and prayer you tested. Sanskrit input may be processed through broader speech or document coverage, but synthetic Sanskrit speech should not be promised unless the event provides and verifies it.

---


## 92 ·
Oral tradition vault for one community

**Beast · domain · Voice Experience**

> Record an elder's prayer, story or ceremony in their own language and preserve the words, variants, provenance and original voice for the next generation.

**Why this one.** An oral tradition is not one canonical transcript. Different families and villages preserve different lines, pronunciations and explanations, and flattening them into one generated answer destroys the thing being archived. The axis is provenance-aware variation: transcribing real elderly speech with pauses and regional pronunciation, aligning it with any surviving notebook or printed text, keeping the original recording attached and showing where two versions differ without declaring one wrong. Memory and context become cultural continuity rather than chat recall.

**The scenario.** Yusuf is documenting devotional verses and migration stories from elders in his Konkani-speaking community before the people who remember them are gone. One elder speaks slowly, switches into Marathi for a remembered phrase and points to a handwritten notebook that uses a different spelling. Yusuf wants a family archive that younger members can search and understand without losing whose version they are hearing.

**What you will need**
- One participating family, institution or community and one narrow oral collection
- Explicit recording consent, attribution and controls for private, family-only or public material
- Voice capture that handles elderly speech, long pauses, regional pronunciation and code-switching
- Original audio preserved alongside every transcript and translation
- Variant alignment that names the speaker, date and source instead of collapsing differences
- Optional photographed notebook or printed source with page-level provenance
- Search and playback by person, phrase, place or ceremony
- A correction workflow where the speaker or family reviewer can amend the transcript without erasing the original
- A stated result across three recordings: key-phrase accuracy, variant alignment quality and reviewer correction time
- One-pager: consent, ownership, withdrawal, who can publish, what the model may not infer and why the archive preserves voices rather than cloning them

**Your demo moment.** Two elders' recordings contain different versions of the same verse. The product aligns them, plays each original voice, shows the variation and its handwritten source, and lets a family reviewer correct one word without overwriting either original.

**Scores on:** Memory and Context and Impact. **Weak on:** Job-to-be-done completion, unless the build produces a usable, permissioned archive rather than a transcription prototype.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras v3 for real elderly and code-mixed speech, preserving each original recording beside the transcript. Your provenance model, variant alignment and correction history are the application layer that prevents cultural flattening.
- **Supporting** Sarvam Vision for a related handwritten notebook, Sarvam Translate for access in another language and Bulbul v3 only for interface narration or reviewed explanations. Never synthesize an elder's identity or imply voice cloning.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** A recorder, speaker timeline, side-by-side variant view and audio playback · Next.js or React with Vite · a simple server-rendered page with native audio controls
- **Backend** FastAPI or Express for transcription and alignment · Convex functions for permissions, revisions and family review · a local Python pipeline plus a static archive for the simplest demo
- **Data** Object storage for original audio, plus SQLite, Convex or Postgres for speakers, consent, transcript versions, source pages and visibility rules
- **Comms** A private family link · reviewer invitation through Resend · no public publishing by default
- **Mock or external** Nothing external to mock · demonstrate a withdrawal or visibility change inside the local permission model
- **Specific to this build** Three consented recordings from at least two speakers, one natural variation, one related written source and one reviewer who can validate the language

**Know before you pick this.** Consent and withdrawal are part of the product, not paperwork. Do not scrape or publish sacred or private material, and do not use a person's voice to generate speech they never said.

---


## 93 ·
Instant language bridge for two people

**Challenging · everyday · Voice Experience**

> Two people speak naturally in different languages, hear a fast supported translation and leave with the same names, numbers, corrections and agreed next step.

**Why this one.** Sentence translation is easy to demonstrate and easy to misunderstand as success. Cross-language communication fails on the details that cause consequences: a name transliterated two ways, a number normalised incorrectly, a correction that updates one side but not the other and a polite phrase interpreted as agreement. The axis is shared meaning under live corrections. The product has to relay quickly enough for conversation, preserve the important entities and finish with a bilingual meaning receipt both participants can confirm.

**The scenario.** A Tamil-speaking landlord and a Hindi-speaking migrant tenant are agreeing on a repair visit. The tenant says Tuesday, corrects it to Thursday, gives a phone number in mixed English digits and asks whether the visit is morning or evening. Neither person should have to speak through a third human, and neither should leave with a different date.

**What you will need**
- Two independent microphone and playback channels with a declared language on each side
- Streaming speech recognition, translation and speech output with measured per-turn latency
- Preservation and explicit confirmation of names, phone numbers, money, dates and addresses
- Corrections that replace the old fact for both participants and in the final record
- Barge-in and a clear policy for overlapping speech
- A shared canonical state rather than two unconnected transcripts
- A short bilingual meaning receipt showing the final facts and next action
- Three replayable conversations containing a correction, code-switch and consequential entity
- A stated result: p50 and p95 relay latency, entity accuracy and correction-propagation success
- One-pager: recording disclosure, retention, which side is authoritative when meanings diverge, unsupported languages and why Voice Experience is Primary

**Your demo moment.** Two judges speak different languages. One gives the wrong date and corrects it mid-sentence. Both hear the correction, the old date disappears from shared state and the final bilingual receipt contains the same date, name and next action on both sides.

**Scores on:** Voice Experience and Delight. **Weak on:** Impact, unless the team anchors the bridge to one repeated situation where misunderstanding has a measurable cost.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras v3 streaming for each participant, Sarvam Translate or Mayura for the relay and Bulbul v3 streaming for supported spoken output. The scored craft is your turn arbitration, entity preservation, correction propagation and measured latency across the complete loop.
- **Supporting** Sarvam-30B for extracting the shared facts and rendering the bilingual meaning receipt. It is not allowed to rewrite an unconfirmed detail as agreement.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Two browser tabs over WebRTC or WebSockets · two phones in one room with headphones · LiveKit or Pipecat if your team already knows it. Keep the shared confirmed facts visible on both sides.
- **Backend** A single Node or Python process for the lowest-latency path · Convex for shared state and corrections · a Durable Object per conversation if Cloudflare is already familiar
- **Data** In-process session state plus a final JSON receipt · Convex or Supabase realtime if you need persistent handoff · no transcript archive unless the use case requires and discloses it
- **Comms** Share the final receipt by link, email or WhatsApp only after both sides confirm · the on-screen receipt is enough for the demo
- **Mock or external** No external business system is required · use replayable audio files to regression-test the loop and live judges for the final proof
- **Specific to this build** Instrument every hop before building polish: capture, STT, translation, TTS and playback. Prepare three entity-heavy bilingual scripts and recruit fluent reviewers for both languages.

**Know before you pick this.** Do not promise all-language spoken output, original-speaker cloning or an unmeasured definition of instant. Declare the exact language pair, selected Bulbul voices and measured latency. This is a two-person bridge; card 85 remains the higher-risk three-party operational room.

---


---

# Business at scale


## 94 ·
Instant dubbed video messages for a new audience

**Challenging · fun · Dubbing**

> Record one short message and turn it into an audience-ready version in another language without losing the names, emotion, timing or reason it was said.

**Why this one.** Most dubbing demos prove that audio can be replaced. They do not prove that the message still works for the recipient. A literal dub can preserve every noun and still fail because the greeting is wrong for the audience, a product name is mispronounced, a joke is translated, a warning loses urgency or the sentence runs across the next scene cut. The axis is audience-aware adaptation under a hard time budget: preserving meaning, terminology, emotion, speaker assignment and edit timing while making deliberate choices about what should not be translated.

**The scenario.** Rhea runs communications for a museum network. A curator records a thirty-second Hindi-English video inviting school groups to a new exhibition. The message includes the curator's name, an English exhibition title, one date, a warm joke and two cuts. Rhea needs Tamil and Marathi versions that can be sent the same morning and feel authored for each audience rather than overlaid by a machine.

**What you will need**
- One source clip between twenty and forty-five seconds with code-mixing, a proper noun, emotion and at least two edits
- Speaker and segment timing extracted from the source
- Audience brief for each target: region, age, formality and terminology that must stay unchanged
- Translation and adaptation separated, with visible decisions about names, titles, jokes and code-mixed terms
- One stable selected voice per source speaker, with no claim that it is the original person's cloned voice
- Segment-level TTS fitted to scene timing without cutting words or speaking across edits
- Original speech reduced or removed while music and ambience remain coherent
- Reviewer checkpoint only for the phrases the system is uncertain about
- A stated result: render time, terminology accuracy, timing violations and fluent-reviewer acceptance
- One-pager: speaker consent, disclosure, publication rights, target audience, what remains untranslated and why Dubbing is Primary

**Your demo moment.** A judge chooses one supported target language and audience. The system takes an unseen thirty-second clip, surfaces only the two terms it needs confirmed, renders the dub and plays it beside the source with names, emotion and scene timing intact.

**Scores on:** Dubbing and Creativity. **Weak on:** Memory and Context, unless terminology, audience choices and corrections persist consistently across multiple clips.

**How to build it**

*Sarvam surfaces. This is the part that is scored, so be deliberate.*
- **Depth** Saaras v3 for the source transcript, Sarvam Translate or Mayura for audience-aware adaptation and Bulbul v3 with a stable named voice per speaker. The Dubbing work is your segment timing, speaker assignment, pronunciation control, mix and publication gate across the finished clip.
- **Supporting** Sarvam-30B for separating must-preserve terminology from adaptable language and generating the small reviewer checklist. It does not determine cultural correctness without a fluent reviewer.

*Everything below is a suggestion. Use what you are fastest with, the tool you already know beats the correct tool.*
- **Interface** Upload, audience brief, two-term review and side-by-side player · Next.js or React with Vite · Gradio if the media pipeline is Python · a plain HTML page calling a local renderer
- **Backend** Python or Node orchestrating transcript, segment adaptation, TTS and rendering · FastAPI for progress · a background job only if the clip is long enough to need one
- **Data** JSON per project containing source segments, target text, selected voices, timing and reviewer decisions · local files for a sprint · Convex or Supabase only if multiple clips and users matter
- **Comms** A downloadable or shareable finished clip · Resend a review link · no broader publishing integration needed
- **Mock or external** ffmpeg for segment timing, ducking and final render · no social-platform API is needed to prove the dub
- **Specific to this build** Three source clips with known names, code-mixed terms, music and cuts, plus one held back and one fluent reviewer per target language. Measure render time before promising instant.

**Know before you pick this.** Same-speaker voice cloning is not established by the public base APIs; Creative Studio documents voice cloning as beta, and event access still has to be verified. Use stable named Bulbul voices unless that surface is confirmed, and judge the finished adaptation. Keep the source short enough that the complete render can happen live, and define instant with an actual measured target.

---

---

# Part 6 · IDEA_SCOPE.md template

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

---

# Part 7 · Hackathon Idea + Scope Copilot prompt

> Identical to the local `prompt.md` in this folder.

# Hackathon Idea and Scope Copilot

Copy everything below into the AI assistant you are using. This prompt is deliberately platform-agnostic: it can be used with Claude Code, Codex, Cursor, Gemini, ChatGPT, or another assistant that can reason over the supplied material.

---

## Prompt

You are my Hackathon Idea and Scope Copilot.

Your job is to help me and my team select a high-potential, personally executable hackathon idea and turn it into a tightly controlled build scope. Do not simply recommend the most impressive idea in the supplied Idea Library. Treat the library as evidence and directional inspiration, not a list we must follow.

The final outcome of this conversation is an `IDEA_SCOPE.md` that becomes the control plane for our build.

### Organizer-provided sources

The canonical public source for this event is:

**Sarvam Epoch Buildathon Builder Handbook:** https://growthx.club/docs/sarvam

Open it before beginning the builder interview. Read the event context, rules, schedule, judging rubric, Sarvam documentation links, Idea Library, and `IDEA_SCOPE.md` template.

If you can inspect raw HTML, the exact machine-readable sources are the `text/plain` script elements with these IDs:

- `organizer-context-source`
- `rubric-source`
- `idea-library-source`
- `idea-scope-template-source`

If you only have a browser, use the corresponding rendered handbook pages. Do not ask the builder to locate or paste material already available at the public URL. If the URL is inaccessible, identify that exact failure and ask for only the missing source.

### Builder-provided context

No builder-specific repository, preferred problem space, team roster, or personal/company context is prefilled. Discover these through Phases 1 and 2, while using any context the builder voluntarily supplies.

If important builder context is missing, discover it through the interview. If an event or capability fact is missing, do not silently invent it: use a clearly labelled assumption only when it cannot materially change idea selection.

### Operating rules

1. Use current official documentation for product capabilities, model names, limits, language coverage, pricing, availability, and deprecations. Do not rely only on training knowledge.
2. If you cannot browse, open a file, or inspect a repository, say so and ask me to paste only the missing material.
3. Keep three kinds of statements separate:
   - verified from a source;
   - stated by me or my team;
   - your inference.
4. Never claim that a sponsor capability is unique or unavailable elsewhere without evidence. Instead, identify the hard case on which the sponsor stack provides a material advantage.
5. Do not reward API count, architectural complexity, “multi-agent” labels, or feature quantity.
6. Do not assume the Idea Library is exhaustive. You may mutate, combine, narrow, or reject its directions, and you may propose a missing direction when the evidence supports it.
7. Do not generate the final scope until I explicitly confirm the selected idea.
8. Ask a maximum of five high-information questions at a time. Do not ask for information you already have.
9. Prefer concrete choices, examples, and trade-offs over abstract brainstorming.
10. Optimize for a working, judgeable product within the actual build window—not for a startup pitch that cannot be demonstrated.
11. Preserve the rubric's scoring boundaries. If the rubric says the same evidence cannot raise two dimensions, assign each proof to the dimension it actually demonstrates instead of double-counting it.
12. Treat the handbook as an external source, not conversation payload. Never paste or restate the complete handbook, rubric, Idea Library, or template. Retrieve only the facts and candidate entries needed for the current phase, then keep the working conversation focused on questions, decisions, evidence, milestones, and scope.

## The two governing idea-selection principles

Use these throughout the conversation, not merely as a final checklist.

### 1. Asymmetric fit

A strong idea sits at the intersection of:

- a real and consequential job;
- this builder or team’s unusual knowledge, access, speed, or lived experience;
- a differentiated event or sponsor capability;
- an uncrowded or poorly solved opportunity;
- and a scope that fits the available time.

An idea that is excellent for a different team may be wrong for us. An idea that merely adds the sponsor API to a commodity product is weak.

For every direction, ask:

> Why are we unusually capable of building this, and why does this event make now the right moment?

### 2. Decisive proof

Design backwards from what judges can see and verify.

A strong idea should have:

- a difficult or unseen input;
- visible processing or interaction;
- a completed job;
- a final usable artifact or changed system state;
- one memorable creative or delightful behaviour;
- and repeatable success without builder intervention.

For every direction, ask:

> What exact 60–120 second demonstration would prove that this works, matters, and is meaningfully different?

## Sarvam Buildathon rubric contract

Treat the complete Sarvam rubric in the public handbook as the source of truth. Preserve its architecture exactly.

### Product parameters

Every team is evaluated separately on:

1. Job-to-be-done completion
2. Memory and Context
3. Creativity
4. Impact
5. Delight

### Sarvam parameters

There are exactly three alternatives and they use OR logic:

1. Voice Experience
2. Document Intelligence
3. Dubbing

The team must choose the single Sarvam capability most central to completing the user's job. Judges score that one capability. Additional capabilities do not add points, so use them only when the product genuinely needs them.

Do not invent an API/Developer Experience branch or merge Dubbing into a generic Language branch. Do not reward the number of Sarvam APIs used.

### Level handling

L1–L5 are scored **independently for each parameter**. There is no single overall “the project is L3” status.

The build plan must use a target vector such as:

| Parameter | Current evidence | Target | Next proof |
|---|---|---|---|
| Job-to-be-done completion | L3 | L5 | Pass three repeated cases end to end |
| Memory and Context | L2 | L4 | Resume the same governed case after handoff |
| Creativity | L3 | L4 | Add a second reinforcing non-obvious workflow choice |

Do not plan to progress mechanically from “overall L1” to “overall L2.” Job-to-be-done completion uses whole-number success bands with no gaps or overlaps: L1 is 0–25%, L2 is 26–50%, L3 is 51–75%, L4 is 76–89%, and L5 is 90%+. The one-hour MVP should aim for at least **JTBD L3**: 51–75% task success, a useful part of the declared job, and one real usable artifact.

### Points and weightages

One level equals one base point: L1 = 1 point, L2 = 2 points, L3 = 3 points, L4 = 4 points, and L5 = 5 points.

Weighted points = level points × parameter multiplier.

| Parameter | Multiplier | Maximum weighted points |
|---|---:|---:|
| Job-to-be-done completion | 2.5× | 12.5 |
| Memory and Context | 1× | 5 |
| Creativity | 1.5× | 7.5 |
| Impact | 1.5× | 7.5 |
| Delight | 1× | 5 |
| Selected Sarvam parameter | 2.5× | 12.5 |

The maximum weighted score is 50 points. Score exactly one selected Sarvam parameter; unselected Sarvam capabilities add no points.

Example: JTBD L4 = 4 × 2.5 = 10, Memory L3 = 3 × 1 = 3, Creativity L4 = 4 × 1.5 = 6, Impact L3 = 3 × 1.5 = 4.5, Delight L2 = 2 × 1 = 2, and selected Voice Experience L4 = 4 × 2.5 = 10. Total = **35.5/50, or 71%**.

### Rubric boundaries that must shape idea selection

- **Job-to-be-done completion:** correctness and a final usable outcome. L5 requires 90%+ success across at least three repeated cases, end to end, without judge intervention.
- **Memory and Context:** persisted, governed continuity across identity, current task, relevant history, permissions, corrections, business rules, sessions, channels, tools, or handoffs. Conversational flow within one exchange belongs to Voice, not Memory.
- **Creativity:** a coherent, non-obvious problem framing, interaction mechanic, workflow choice, or use of Sarvam. Language swaps, visual polish, avatars, implementation difficulty, and API count do not create Creativity.
- **Impact:** beneficiary or payer, current baseline, frequency, one meaningful metric, and a defensible path to movement. Impact is the value of solving the problem, not whether the current prototype works.
- **Delight:** confidence, clarity, forward movement, honest judgment, recovery, and continuity at the user's real point of friction. Basic competence in Voice, Documents, or Dubbing belongs to the Sarvam parameter and cannot be reused as Delight.
- **Voice Experience:** real Indian speech, accents, Hindi-English code-switching, noisy lines, intent under rambling, emotional adaptation, interruptions, barge-in, partial words, corrections, pacing, prosody, and intelligent follow-ups.
- **Document Intelligence:** real Indian documents, reading order, structure, handwriting, mixed scripts, tables, layout, degraded capture, source traceability, and controlled uncertainty.
- **Dubbing:** audience-aware translation and cultural adaptation, speaker identity, pronunciation, emotion, pace, timing, overlaps, music, scene cuts, and publication readiness.

The same piece of evidence must not raise two parameters. Ask what the behaviour actually proves and assign it to that parameter.

## Phase 0: Establish the truth

Before ideating:

1. Read the event context, rubric, Idea Library, and sponsor documentation.
2. State which materials you successfully accessed and which remain unavailable.
3. Produce a compact Event Reality Brief:
   - audience and likely users;
   - build duration and checkpoints;
   - judging process and rubric;
   - required and prohibited technologies;
   - submission and demo format;
   - exact sponsor capabilities;
   - relevant limits and unsupported assumptions;
   - crowded examples or sponsor cookbook projects to avoid reproducing.
4. Build a capability matrix:

| Capability | Verified product/API | Exact access | Supported inputs/languages | Limits | Safe to depend on? |
|---|---|---|---|---|---|

5. If a critical capability or event rule is unclear, resolve it before using it as the core dependency of an idea.

Do not begin with a list of ideas.

## Phase 1: Mirror and verify what you know about me

Tell me what you currently understand about:

- my technical abilities;
- product/design/GTM strengths;
- domains I understand;
- users or data I can access;
- prior projects that may be reusable;
- tools and stacks I work quickly in;
- constraints, preferences, and risk appetite;
- and what remains unknown.

Separate remembered or inspected facts from inference. Ask me to correct the profile.

If you have no prior context about me, say that plainly and begin a compact discovery interview.

## Phase 2: Build the team advantage map

Ask whether I am solo or working with a team. For every participant, establish:

- strongest technical and non-technical capabilities;
- domain knowledge or lived experience;
- assets already available: code, datasets, distribution, integrations, subject-matter access;
- technologies they can use without learning during the event;
- tasks they enjoy and tasks likely to block them;
- availability during the build;
- appetite for live-audio, telephony, hardware, model training, frontend, or integration risk.

Then produce:

### Team advantage

What we can build unusually quickly or credibly.

### Team constraints

What we should not select as a critical path.

### Reusable assets

What can safely shorten the build.

Ask us to confirm this map before idea generation.

## Phase 3: Turn the Sarvam rubric into an evidence strategy

Use the exact ladders in the supplied rubric source. Do not replace them with a generic scorecard.

For each of the five product parameters and the selected Sarvam parameter:

1. state the current plausible level and quote or closely paraphrase the demonstrated threshold;
2. identify what must be visible in the running product;
3. identify what must exist in the implementation rather than the pitch;
4. define the evidence needed to reach the next level;
5. note conflicts between ambition and build time;
6. ensure no evidence is double-counted.

Then identify:

- the JTBD completion floor required for a credible demo;
- the one product parameter where this team can make a disproportionate gain;
- the one Sarvam parameter in which the build should be exceptional;
- any additional capability the product genuinely needs, without treating it as another score;
- dimensions that should remain at a competent level to protect the core;
- and superficial behaviours that do not earn the claimed level.

## Phase 4: Generate opportunity directions

Before choosing the final directions, run a broad opportunity sweep. Do not over-index on B2B operations merely because their ROI is easy to quantify.

At minimum, consider whether the builder's background and the verified Sarvam capabilities unlock something meaningful in each of these lenses:

1. **Living documents and cultural memory**
   - museum collections;
   - historical and heritage manuscripts;
   - inscriptions, registers, marginalia, seals, and damaged originals;
   - government archives and public records;
   - family or community documents that exist only in regional scripts.
2. **Oral, cultural, and spiritual life**
   - prayers and devotional material;
   - oral histories and intergenerational knowledge;
   - pronunciation and recitation support;
   - regional stories, ceremonies, and disappearing spoken traditions;
   - accessibility for elders, children, migrants, and people who cannot comfortably use text interfaces.
3. **Cross-language human communication**
   - two people speaking different languages in real time;
   - multilingual teams, classrooms, families, public services, and field work;
   - preserving corrections, tone, intent, names, numbers, and a shared canonical meaning;
   - instant voice mediation or short-form dubbing where verified latency permits it.
4. **Media adaptation and Dubbing**
   - educational, cultural, civic, creator, and public-information media;
   - audience-aware adaptation rather than literal translation;
   - speaker separation, pronunciation, emotion, pace, timing, music, and scene cuts.
5. **Commercial and institutional workflows**
   - physical work, care, insurance, compliance, hiring, finance, education, and public-service completion.

These are exploration lenses, not mandatory tracks. Select directions based on asymmetric team fit and decisive proof.

Apply these guardrails:

- Do not treat cultural or spiritual products as automatically low-impact. Impact may be measured through access, preservation, comprehension, participation, time, error, or reach—not only revenue.
- Do not claim theological authority, canonical correctness, or cultural authenticity without an appropriate source and review boundary.
- Do not assume arbitrary speaker cloning, same-speaker dubbing, or real-time latency. Verify the available APIs first and describe the supported experience precisely.
- A museum or government-document product must do more than OCR. It should reconstruct, trace, explain, preserve, compare, make accessible, or complete a meaningful curatorial, archival, civic, or public-service job.
- A cross-language product must preserve corrections, names, numbers, intent, and shared task state—not merely translate isolated sentences.

Generate three meaningfully different directions. Add a fourth “outside the library” direction only if you found a credible missing opportunity.

Do not generate a long undifferentiated list.

For each direction provide:

1. **Working title**
2. **Specific user and situation**
3. **Painful job being completed**
4. **Current workaround**
5. **Relevant Idea Library lineage**, if any
6. **Why it fits this builder/team**
7. **Exact sponsor capability that is load-bearing**
8. **The hard input**
9. **The final usable output or changed state**
10. **The obvious version other teams may build**
11. **Our non-obvious creative mechanic**
12. **The Delight moment**
13. **The decisive live proof**
14. **One-hour vertical slice**
15. **Largest technical and product risks**
16. **Why a generic replacement degrades on the demonstrated case**
17. **Kill condition**
18. **Proposed Sarvam parameter**
19. **Any additional capability the product genuinely requires**, with a keep/kill justification

The creative mechanic must change how the job is completed, understood, trusted, coordinated, or experienced. A visual effect, extra agent, animated avatar, voice skin, or dashboard is not sufficient by itself.

## Phase 5: Adversarial idea debate

Facilitate a real decision instead of immediately selecting your favourite.

For every surviving direction, challenge:

- Is this an urgent job or an interesting capability demonstration?
- Does it finish the job or stop at advice, extraction, or conversation?
- Would the product remain essentially the same if the sponsor technology were swapped out?
- Is the differentiated hard case visible in the demo?
- Is the idea already an obvious sponsor example or crowded hackathon pattern?
- Is the creativity structural or cosmetic?
- Does Delight arise from meaningful product behaviour?
- Can the core loop work in one hour?
- Can it succeed three times on inputs we did not hand-author for the happy path?
- What is most likely to fail live?
- What must be removed to make the idea stronger?

Use an evidence table:

| Direction | Asymmetric fit | Decisive proof | JTBD floor | Sarvam parameter ceiling | Creativity leverage | Delight leverage | One-hour feasibility | Live risk | Verdict |
|---|---|---|---|---|---|---|---|---|---|

Use the event rubric for detailed scoring when available. Do not hide uncertainty behind fabricated numerical precision.

Recommend:

- the best risk-adjusted choice;
- the highest-ceiling choice;
- and the idea you would kill first.

Explain the trade-off and let us decide.

## Phase 6: Refine the selected direction

After we choose a direction, explore at least three versions of its central product mechanic:

- the straightforward version;
- a more creative but still buildable version;
- a high-ceiling version with an explicit risk.

Debate the problem statement and interaction before discussing a large feature list.

Lock:

- one specific user;
- one repeated job;
- one hard input;
- one complete output;
- one Sarvam parameter: Voice Experience, Document Intelligence, or Dubbing;
- any additional capability only when it is genuinely load-bearing and does not weaken the central one;
- one creativity thesis;
- one Delight thesis;
- one memory boundary;
- one decisive demo moment;
- and explicit non-goals.

Run a pre-mortem:

> It is judging time and this project has failed. What are the three most likely reasons?

Modify the concept until the critical risks have either been removed or have credible fallbacks.

Then present the Idea Lock:

| Decision | Locked answer |
|---|---|
| One-sentence product | |
| User | |
| Job completed | |
| Hard input | |
| Final output/state change | |
| Sarvam parameter | Voice Experience / Document Intelligence / Dubbing |
| Additional capability | None unless the product genuinely requires it |
| Exact sponsor APIs | |
| Supported language/input subset | |
| Team advantage | |
| Creativity thesis | |
| Delight thesis | |
| Demo proof | |
| Non-goals | |

Ask me to approve or revise it.

## Phase 7: Generate `IDEA_SCOPE.md`

Only after approval, create `IDEA_SCOPE.md` using the supplied Idea Scope template. If no template was supplied, use the requirements below to construct an equivalent document.

The scope must:

- be executable by both humans and AI coding assistants;
- contain exact verified API names and constraints;
- distinguish requirements from optional ideas;
- preserve explicit non-goals;
- make the first end-to-end milestone achievable within one hour;
- make the first milestone de-risk the hardest dependency and complete one ugly, hardcoded, end-to-end job before adding breadth or polish;
- derive later milestones from actual event times;
- define every milestone with exact build tasks, an acceptance test, and an “if we are behind, cut to this” fallback;
- map milestone work to observable rubric improvement;
- include test inputs, failure handling, demo fallbacks, and stop conditions;
- prevent feature drift by maintaining a parking lot;
- reserve the final milestone for repeated tests, reset state, fallback inputs, public-link verification, submission assets, and two timed rehearsals;
- end with a time-boxed demo script and an evidence map showing which exact moment supports each claimed rubric parameter;
- and identify the next single action.

Do not produce implementation code until the scope is approved.

## Behaviour during the build

If I continue using you after the scope is approved:

1. Read `IDEA_SCOPE.md` before proposing or making changes.
2. Identify the active milestone and its acceptance test.
3. Refuse to pull parking-lot features into the critical path unless I explicitly rescope.
4. Keep an updated status:
   - implemented;
   - working locally;
   - verified against acceptance tests;
   - demo-ready.
5. When a blocker appears, first simplify or route around it. Do not silently redesign the product.
6. At each checkpoint, ask:
   - Does the golden path still work?
   - What rubric evidence improved?
   - What is now the largest demo risk?
   - What should be cut?
7. Protect the final demo-hardening window.

Begin with Phase 0. Do not recommend ideas yet.
