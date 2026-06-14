---
title: World Cup Pub, Part 2 — Steering the Agent
---

# World Cup Pub, Part 2: Steering the Agent

*A follow-up to the [World Cup Pub build post-mortem](/09-World-Cup-Pub). The first piece covered architecture and bugs. This one is about the human in the loop — me — and what I caught, missed, and would do differently next time.*

---

I shipped a working app in 48 hours with an AI agent doing most of the typing. That sentence is true, and it is also the most misleading way to describe what actually happened.

The honest version: **the agent produced a first draft of almost everything, and I spent the build catching the parts that were wrong before they shipped.** Sometimes I caught them in seconds. Sometimes a milestone slipped through a review I skipped, and the bug landed in production.

This piece is about that review process — what it looked like, where it failed, and what a repeatable version would be next time.

---

## Where the agent's first attempt was wrong

Three moments stood out during the build. Each was caught a different way.

### 1. The wrong World Cup

The first `teams.json` the agent produced listed Venezuela, Indonesia, Nigeria, Hungary, and Slovakia as 2026 World Cup qualifiers. None of them qualified. England was placed in Group G — actually Group L. I caught it because I'd been watching the qualifiers, and the first team I scrolled to was the one I cared about.

**How I caught it:** domain knowledge. Pure luck that the wrong fact was about a topic I knew.

### 2. A library class that no longer exists

The agent imported `Loader` from `@googlemaps/js-api-loader` and built the entire Maps integration around it. The class was dropped in v2. The build failed at compile, not runtime, so it was loud — but the agent then tried to "fix" it by downgrading the package rather than switching to the supported approach.

**How I caught it:** the package's GitHub README. The agent's training data predates the v2 release.

### 3. A DRY violation hiding a broken URL

The worst one, because it shipped. `places.ts` set `pub.mapsUrl` using an unofficial URL format. Then `booking.ts` ignored `pub.mapsUrl` entirely and rebuilt a near-identical broken URL from scratch. Two bugs cancelled into one symptom: "Book a table" opened a broken Maps link for any pub without a website.

**How I caught it:** I didn't, during the build. A user tap on launch day surfaced it.

---

## Prompts and specs: before/after

The pattern that emerged: vague prompts produced over-engineered, hallucinated, or scope-creeping output. Specs with constraints produced clean output on the first try.

Before (vague) | After (constrained) | What changed
--- | --- | ---
"Add a booking feature." | "On each PubCard, render a 'Book a table' CTA. Link to `pub.website` if present, else `pub.mapsUrl`. No third-party branding. No new state." | Agent stopped inventing OpenTable integrations.
"Load Google Maps." | "Load Maps JS API via `<Script>` from `next/script`, `strategy=afterInteractive`. Do not use `@googlemaps/js-api-loader`; the Loader class was removed in v2." | Agent stopped reaching for a deprecated API.
"Build the schedule view." | "Render only the selected team's matches. Times in the user's detected timezone. No knockout rounds in this milestone — out of scope." | Agent stopped inventing a bracket visualisation no one asked for.

The shift that mattered: **writing the out-of-scope list before the in-scope list**. An agent without an out-of-scope list will always fill the space.

---

## A taxonomy of failure modes

Categorising what went wrong is the part that interested me most, because it's the foundation of an eval framework. Five categories covered everything I saw:

Category | What it looks like | Example from this build
--- | --- | ---
**Stale training data** | Confident answers about facts that changed after the model's cutoff. | 2026 World Cup groups; `@googlemaps/js-api-loader` v2.
**Hallucinated APIs** | Imports or method calls that don't exist, presented with conviction. | The `Loader` class. A non-existent flag on Vercel CLI.
**Over-engineering** | Inventing requirements the spec didn't ask for. | Rebuilding `mapsUrl` from scratch in `booking.ts` instead of reading the field.
**Silent scope creep** | Quietly adding state, dependencies, or layers not in the spec. | An early draft of the team picker introduced a Zustand store for a four-step flow with no persistence.
**Confidently wrong edge cases** | The happy path works. The fallback is broken in a subtle way. | Tap targets at `py-2.5` (~34px, below the 44px minimum). Maps URL format unofficial and brittle.

This is the connection to evals: **each category is a test class**. "Does this function reference a method that exists?" is a static check. "Does the fallback path produce a working URL?" is a behavioural one. "Did the agent add state we didn't ask for?" is a diff check on the component tree.

You can't write evals for failures you haven't named. The taxonomy is the prerequisite.

---

## Cost and speed honesty

Where the agent genuinely saved time, and where reviewing its output cost more than writing it myself:

Saved time | Cost time
--- | ---
Component scaffolding (Tailwind classes, prop types, state hooks). Probably 4–6 hours. | Verifying every factual claim about the 2026 tournament. ~1 hour against Sky Sports and Wikipedia.
TypeScript interface generation from the data shape. | The Maps loader detour. Two failed attempts before I read the changelog myself.
Boilerplate (the favicon SVG, the analytics wiring, the error states). | The booking URL bug. Two commits to fix what should have been one.
The discriminated union refactor for `MatchContext`. Cleanly executed across five files. | The skipped M3 review. Five minutes saved, two production bugs gained.

On net, the agent shaved roughly a day off a three-day build. Not the "48 hours, fully automated" line you see on LinkedIn — closer to "48 hours instead of 72, with active steering throughout".

The honest claim isn't that AI built the app. It's that **AI made it feasible to spend 48 hours reviewing rather than typing**. That's a different skill, and arguably the one worth getting good at.

---

## A repeatable eval checklist

If I were to formalise the review process from this build into an eval checklist for the next one, it would be these:

1. **Fact-check anything time-sensitive against a live source.** Tournaments, library versions, API surfaces, pricing. Never trust the model's recall on these.
2. **Grep every import against the package's current docs.** One `npm view` per third-party import catches deprecated APIs before they compile.
3. **Write the out-of-scope list before the in-scope list.** Agents fill empty space. Constrain the space first.
4. **Diff the dependency tree after each milestone.** If the agent added a state library, a router, or a UI framework you didn't ask for, that's silent scope creep — catch it at the package.json level.
5. **For every utility that returns a URL, ID, or formatted string: hand-test the fallback.** The happy path will work. The fallback is where the confidence-without-knowledge lives.
6. **Run the agent review at every milestone boundary.** Not just M1. Especially under deadline pressure — the bug in production cost more than the review would have.
7. **Smoke test on a real device before sharing the URL.** "TypeScript compiles" is not a smoke test. "I tapped every button on my phone" is.

None of this is novel. It's the same discipline you'd apply to a junior engineer's first PR — written down, made explicit, and applied consistently regardless of how clean the diff looks.

The next post in this series will turn this checklist into an actual evaluation harness — programmatic, repeatable, runnable on every agent-generated diff. That's the Retrieval Lab project. This piece is the prerequisite: **you can't automate a review you haven't articulated**.

---

*The first piece in this series — the World Cup Pub build post-mortem — is at [World Cup Pub — 0→1 in 48hrs](/09-World-Cup-Pub). Live app: [world-cup-pub.vercel.app](https://world-cup-pub.vercel.app).*
