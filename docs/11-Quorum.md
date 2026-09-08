---
title: Quorum — Cost per Correct Decision
---

# Quorum: Cost per Correct Decision

*A five-phase build of an eval-governed control plane for visual AI decisions — routing easy calls to a cheap detector, ambiguous ones to a vision-language model, and the genuinely uncertain to a human queue, with every decision priced and recorded. Built with an AI agent pair, documented in Confluence ADRs throughout, and completed for **£0 of external spend** against a £10 cap.*

<video src="./components/quorum-story.mp4" controls style="width: 100%; border-radius: 8px;" preload="metadata"></video>

---

## The premise

I built an AI system on the worst detector I could find. Deliberately.

The vertical is recycling-stream contamination: a materials recovery facility runs thousands of items past a camera every hour, and a single battery in a paper bale is a fire risk. The obvious pitch is "train a better model." I did the opposite — I took a free, hosted, visibly weak object detector and spent all five build phases on **the system around it**: a confidence gate, an escalation queue, an eval harness, a drift monitor, and a cost ledger.

The bet: for most operational AI, the model is not the product. The product is knowing **when to trust the model, what each decision costs, and who should decide instead.** By the end, the system had measured its own components failing — and routed around them. That's the whole story, and every number below comes out of the system's own records.

---

## The shape of the system

Every image becomes a **decision row** that walks a state machine. A four-rule gate reads the detector's output and picks one of three lanes:

<figure style="max-width: 100%; overflow-x: auto;">
<svg viewBox="0 0 880 300" style="width:100%; max-width:880px; font-family: var(--sans-serif); display:block; margin:auto;">
  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--theme-foreground-muted)"/>
    </marker>
  </defs>
  <!-- stream -->
  <rect x="8" y="120" width="112" height="56" rx="8" fill="none" stroke="var(--theme-foreground-muted)" stroke-width="1.5"/>
  <text x="64" y="144" text-anchor="middle" fill="var(--theme-foreground)" font-size="14" font-weight="600">image</text>
  <text x="64" y="162" text-anchor="middle" fill="var(--theme-foreground-muted)" font-size="11">replay stream</text>
  <line x1="120" y1="148" x2="164" y2="148" stroke="var(--theme-foreground-muted)" stroke-width="1.5" marker-end="url(#arr)"/>
  <!-- cache -->
  <rect x="166" y="120" width="112" height="56" rx="8" fill="none" stroke="var(--theme-foreground-muted)" stroke-width="1.5"/>
  <text x="222" y="144" text-anchor="middle" fill="var(--theme-foreground)" font-size="14" font-weight="600">cache</text>
  <text x="222" y="162" text-anchor="middle" fill="var(--theme-foreground-muted)" font-size="11">one call per key, ever</text>
  <line x1="278" y1="148" x2="322" y2="148" stroke="var(--theme-foreground-muted)" stroke-width="1.5" marker-end="url(#arr)"/>
  <!-- detector -->
  <rect x="324" y="120" width="112" height="56" rx="8" fill="none" stroke="var(--theme-foreground-muted)" stroke-width="1.5"/>
  <text x="380" y="144" text-anchor="middle" fill="var(--theme-foreground)" font-size="14" font-weight="600">detector</text>
  <text x="380" y="162" text-anchor="middle" fill="var(--theme-foreground-muted)" font-size="11">cheap &amp; wrong a lot</text>
  <line x1="436" y1="148" x2="480" y2="148" stroke="var(--theme-foreground-muted)" stroke-width="1.5" marker-end="url(#arr)"/>
  <!-- gate -->
  <rect x="482" y="116" width="96" height="64" rx="10" fill="none" stroke="var(--theme-foreground-focus)" stroke-width="2"/>
  <text x="530" y="143" text-anchor="middle" fill="var(--theme-foreground)" font-size="14" font-weight="600">gate</text>
  <text x="530" y="161" text-anchor="middle" fill="var(--theme-foreground-muted)" font-size="11">4 rules, versioned</text>
  <!-- three lanes -->
  <line x1="578" y1="132" x2="648" y2="56"  stroke="var(--theme-foreground-muted)" stroke-width="1.5" marker-end="url(#arr)"/>
  <line x1="578" y1="148" x2="648" y2="148" stroke="var(--theme-foreground-muted)" stroke-width="1.5" marker-end="url(#arr)"/>
  <line x1="578" y1="164" x2="648" y2="240" stroke="var(--theme-foreground-muted)" stroke-width="1.5" marker-end="url(#arr)"/>
  <rect x="652" y="28"  width="150" height="56" rx="8" fill="#2E7D32"/>
  <text x="727" y="52"  text-anchor="middle" fill="#fff" font-size="13" font-weight="600">auto-decide</text>
  <text x="727" y="70"  text-anchor="middle" fill="#fff" font-size="11" opacity="0.85">87% · ~0.5 s · pennies</text>
  <rect x="652" y="120" width="150" height="56" rx="8" fill="#B36B05"/>
  <text x="727" y="144" text-anchor="middle" fill="#fff" font-size="13" font-weight="600">VLM, asked twice</text>
  <text x="727" y="162" text-anchor="middle" fill="#fff" font-size="11" opacity="0.85">13% · ~55 s · tokens</text>
  <rect x="652" y="212" width="150" height="56" rx="8" fill="#C2413A"/>
  <text x="727" y="236" text-anchor="middle" fill="#fff" font-size="13" font-weight="600">human queue</text>
  <text x="727" y="254" text-anchor="middle" fill="#fff" font-size="11" opacity="0.85">only on disagreement</text>
  <!-- ledger -->
  <line x1="802" y1="56"  x2="838" y2="130" stroke="var(--theme-foreground-muted)" stroke-width="1.5"/>
  <line x1="802" y1="148" x2="838" y2="148" stroke="var(--theme-foreground-muted)" stroke-width="1.5"/>
  <line x1="802" y1="240" x2="838" y2="166" stroke="var(--theme-foreground-muted)" stroke-width="1.5"/>
  <text x="858" y="144" text-anchor="middle" fill="var(--theme-foreground)" font-size="13" font-weight="600" transform="rotate(90 858 148)">ledger</text>
</svg>
<figcaption>Every external model call passes through a permanent cache keyed on the exact input bytes plus every generation parameter — so a re-run of any experiment is byte-identical and free. The percentages are measured, not aspirational.</figcaption>
</figure>

Three design rules did most of the work:

1. **Thresholds are data, never code.** Every gate parameter lives in a versioned database row; every decision pins the version that made it. Tuning writes a new row. When routing behaviour changes, the audit trail says exactly when and why.
2. **The escalation model never gets to guess.** The VLM answers each question twice, independently. Agreement decides; disagreement goes to a person, and no machine verdict is recorded at all.
3. **Silent drops are forbidden.** Anything that fails permanently lands in a dead-letter state and gets counted. Accuracy is computed over *attempted* decisions, not convenient ones.

---

## The eval that called my bluff

Phase 3 built a 184-item golden set from the TACO litter dataset, hand-verified every one of them, and replayed the set through the full pipeline. The headline numbers were bad — accuracy 0.67, F1 0.57, routing recall 0.22 — and the interesting part was *why*. The detector's mAP@0.5 came out at effectively **zero**, which smelled like a bug in my metric code. It wasn't:

```js
const detections = [
  {measure: "boxes that overlap a real object (IoU ≥ 0.5)", count: 423, share: 423 / 514},
  {measure: "boxes with the correct class label", count: 3, share: 3 / 514}
];
```

```js
Plot.plot({
  marginLeft: 10,
  height: 170,
  x: {domain: [0, 514], label: "of 514 predicted boxes", grid: true},
  y: {label: null, axis: null},
  marks: [
    Plot.barX(detections, {
      y: "measure", x: "count", fill: "var(--theme-foreground-focus)",
      rx: 4, insetTop: 10, insetBottom: 10,
      tip: true, title: d => `${d.measure}\n${d.count} of 514 (${(d.share * 100).toFixed(1)}%)`
    }),
    Plot.text(detections, {y: "measure", x: "count", dx: 8, text: d => `${d.count}`, textAnchor: "start", fontWeight: 600, fill: "var(--theme-foreground)"}),
    Plot.text(detections, {y: "measure", x: 0, dy: -28, dx: 0, text: "measure", textAnchor: "start", fill: "var(--theme-foreground-muted)", fontSize: 11}),
    Plot.ruleX([0])
  ]
})
```

**The detector finds objects almost perfectly and names them almost randomly.** 423 of 514 predicted boxes sat on a real object; 3 carried the right label out of 59 classes. That single measurement explains everything downstream: a gate keyed on class labels under-escalates because the labels are noise, and 44 real contaminants sailed through marked clean — including a battery pile confidently labelled *"Other plastic, 0.96"*.

A composite accuracy score would have hidden this completely. Splitting *localization* from *classification* — and splitting *routing* correctness from *verdict* correctness — is what turned a bad number into a diagnosis.

The golden labels themselves were machine-drafted from the dataset's annotations, and the harness refused to treat them as truth: every report carried a **DRAFT** banner and every headline metric was computed over hand-verified items only, of which there were initially none. Clearing that banner meant sitting down with all 184 images. One label flipped — a "contaminated / aluminium foil" that was, on inspection, a drink can. A one-item correction is a boring result; being unable to quote a number until someone had looked is the point.

---

## Watching the world shift

Phase 4 added the monitoring layer: CLIP embeddings for every replayed image, per-class centroids from a "training era" window, and a drift alarm on the mean distance of recent decisions from those centroids. Then I deliberately broke the world — sixty familiar TACO images, followed by forty from a different dataset shot under different conditions, salted with photos of the one class held out of everything: batteries.

```js
const drift = [
  {window: "baseline 1", mean: 0.134, fired: false},
  {window: "baseline 2", mean: 0.134, fired: false},
  {window: "shifted 1", mean: 0.516, fired: true},
  {window: "shifted 2", mean: 0.510, fired: true}
];
```

```js
Plot.plot({
  height: 240,
  x: {domain: drift.map(d => d.window), label: null},
  y: {domain: [0, 0.6], label: "mean distance from known-class centroids", grid: true},
  marks: [
    Plot.ruleY([0.35], {stroke: "var(--theme-foreground-muted)", strokeDasharray: "4,4"}),
    Plot.text([{x: "baseline 1", y: 0.35}], {x: "x", y: "y", text: ["alarm threshold 0.35"], dy: -8, dx: 4, textAnchor: "start", fill: "var(--theme-foreground-muted)", fontSize: 11}),
    Plot.line(drift, {x: "window", y: "mean", stroke: "var(--theme-foreground-faint)"}),
    Plot.dot(drift, {
      x: "window", y: "mean", r: 7,
      fill: d => d.fired ? "#C2413A" : "var(--theme-foreground-focus)",
      tip: true, title: d => `${d.window}\nmean distance ${d.mean}\n${d.fired ? "ALARM FIRED" : "quiet"}`
    }),
    Plot.text(drift, {x: "window", y: "mean", dy: -14, text: d => d.fired ? `${d.mean} — fired` : `${d.mean}`, fontWeight: 600, fill: "var(--theme-foreground)"})
  ]
})
```

The alarm fired cleanly — baseline windows sat at 0.134, shifted windows jumped to ~0.51 against a 0.35 threshold. And on one battery seed, the zero-shot fallback did exactly what it was built for: detector blind, embedding far from every known class, CLIP text-match says **"battery"** — a class the system had never been configured to detect, flagged with no retraining.

The honest miss: three other battery photos never triggered the fallback, because the detector *confidently misidentified* them, and the trigger rule requires the detector to be unsure. Confident-but-wrong is the one gap the current rule can't see — every replayed decision now records its embedding distance so that "confident but far from anything known" is one dashboard filter away.

---

## The dial that turned out to be flat

Phase 5 built the operator dashboard: a threshold dial, economics inputs (£ per rejected bale, £ per reviewer-hour, £ per thousand VLM calls), and a cost-quality frontier simulated by re-gating the entire golden set — from cache, so sweeping 30 candidate configurations costs zero external calls. Here is that sweep, on real data:

```js
const frontier = [
  {gate_low: 0.15, clean_floor: 0.2, escalation: 0.13, accuracy: 0.714, cost_per_1k: 38.35, missed: 36.8},
  {gate_low: 0.15, clean_floor: 0.3, escalation: 0.13, accuracy: 0.714, cost_per_1k: 38.35, missed: 36.8},
  {gate_low: 0.15, clean_floor: 0.45, escalation: 0.13, accuracy: 0.714, cost_per_1k: 38.35, missed: 36.8},
  {gate_low: 0.15, clean_floor: 0.6, escalation: 0.13, accuracy: 0.714, cost_per_1k: 38.35, missed: 36.8},
  {gate_low: 0.15, clean_floor: 0.75, escalation: 0.136, accuracy: 0.712, cost_per_1k: 38.7, missed: 36.8},
  {gate_low: 0.15, clean_floor: 0.9, escalation: 0.136, accuracy: 0.712, cost_per_1k: 38.7, missed: 36.8},
  {gate_low: 0.25, clean_floor: 0.2, escalation: 0.13, accuracy: 0.714, cost_per_1k: 38.35, missed: 36.8},
  {gate_low: 0.25, clean_floor: 0.3, escalation: 0.13, accuracy: 0.714, cost_per_1k: 38.35, missed: 36.8},
  {gate_low: 0.25, clean_floor: 0.45, escalation: 0.13, accuracy: 0.714, cost_per_1k: 38.35, missed: 36.8},
  {gate_low: 0.25, clean_floor: 0.6, escalation: 0.13, accuracy: 0.714, cost_per_1k: 38.35, missed: 36.8},
  {gate_low: 0.25, clean_floor: 0.75, escalation: 0.136, accuracy: 0.712, cost_per_1k: 38.7, missed: 36.8},
  {gate_low: 0.25, clean_floor: 0.9, escalation: 0.136, accuracy: 0.712, cost_per_1k: 38.7, missed: 36.8},
  {gate_low: 0.35, clean_floor: 0.2, escalation: 0.13, accuracy: 0.714, cost_per_1k: 38.35, missed: 36.8},
  {gate_low: 0.35, clean_floor: 0.3, escalation: 0.13, accuracy: 0.714, cost_per_1k: 38.35, missed: 36.8},
  {gate_low: 0.35, clean_floor: 0.45, escalation: 0.13, accuracy: 0.714, cost_per_1k: 38.35, missed: 36.8},
  {gate_low: 0.35, clean_floor: 0.6, escalation: 0.13, accuracy: 0.714, cost_per_1k: 38.35, missed: 36.8},
  {gate_low: 0.35, clean_floor: 0.75, escalation: 0.136, accuracy: 0.712, cost_per_1k: 38.7, missed: 36.8},
  {gate_low: 0.35, clean_floor: 0.9, escalation: 0.136, accuracy: 0.712, cost_per_1k: 38.7, missed: 36.8},
  {gate_low: 0.45, clean_floor: 0.2, escalation: 0.125, accuracy: 0.711, cost_per_1k: 38.49, missed: 37.4},
  {gate_low: 0.45, clean_floor: 0.3, escalation: 0.125, accuracy: 0.711, cost_per_1k: 38.49, missed: 37.4},
  {gate_low: 0.45, clean_floor: 0.45, escalation: 0.125, accuracy: 0.711, cost_per_1k: 38.49, missed: 37.4},
  {gate_low: 0.45, clean_floor: 0.6, escalation: 0.125, accuracy: 0.711, cost_per_1k: 38.49, missed: 37.4},
  {gate_low: 0.45, clean_floor: 0.75, escalation: 0.13, accuracy: 0.709, cost_per_1k: 38.84, missed: 37.4},
  {gate_low: 0.45, clean_floor: 0.9, escalation: 0.13, accuracy: 0.709, cost_per_1k: 38.84, missed: 37.4},
  {gate_low: 0.55, clean_floor: 0.2, escalation: 0.114, accuracy: 0.704, cost_per_1k: 38.77, missed: 38.6},
  {gate_low: 0.55, clean_floor: 0.3, escalation: 0.114, accuracy: 0.704, cost_per_1k: 38.77, missed: 38.6},
  {gate_low: 0.55, clean_floor: 0.45, escalation: 0.114, accuracy: 0.704, cost_per_1k: 38.77, missed: 38.6},
  {gate_low: 0.55, clean_floor: 0.6, escalation: 0.114, accuracy: 0.704, cost_per_1k: 38.77, missed: 38.6},
  {gate_low: 0.55, clean_floor: 0.75, escalation: 0.12, accuracy: 0.702, cost_per_1k: 39.12, missed: 38.6},
  {gate_low: 0.55, clean_floor: 0.9, escalation: 0.12, accuracy: 0.702, cost_per_1k: 39.12, missed: 38.6}
];
```

```js
Plot.plot({
  height: 300,
  grid: true,
  x: {domain: [37, 40], label: "£ per 1,000 decisions (incl. missed-contaminant risk)"},
  y: {domain: [0.60, 0.80], label: "expected accuracy", tickFormat: ".0%"},
  marks: [
    Plot.dot(frontier, {
      x: "cost_per_1k", y: "accuracy", r: 6,
      fill: "var(--theme-foreground-focus)", fillOpacity: 0.55,
      tip: true,
      title: d => `gate_low ${d.gate_low} · clean_floor ${d.clean_floor}\naccuracy ${(d.accuracy * 100).toFixed(1)}%\n£${d.cost_per_1k}/1k · escalation ${(d.escalation * 100).toFixed(0)}%`
    })
  ]
})
```

Thirty threshold configurations, and they all land in a smudge two points wide. **The dial was flat — and that flatness was the most valuable output of the whole project.** The frontier simulation prices escalation using the *measured* quality of the escalation path, and the local 7B vision model I was escalating to had scored 0.44 on adjudications — worse than a coin flip. Escalating more items to a coin flip buys nothing, at any threshold. The instrument didn't just fail to find a better setting; it proved *where the next unit of investment had to go* — a better adjudicator, not better thresholds. That's the go/no-go evidence for the paid-model upgrade, produced by the harness instead of by opinion.

---

## Failure paths, exercised for real

The parts of the system I'm most attached to are the ones that fired without permission:

- **A decision dead-lettered live** during the first full adjudication run. Root cause: the local model server rejects large images — a 1.5 MB photo alone consumed more context than the default window. The decision retried twice with backoff, landed in the dead-letter state, stayed countable, and the fix (a bigger context window, recorded as a cache-key parameter so old outputs can't silently replay) is one line of config history.
- **The judge got audited, and failed.** An LLM scores the adjudicator's written rationales, and its scores stay labelled *uncalibrated* until they agree with human scoring at κ ≥ 0.6 on a blind sample. So I scored thirty of them blind. Agreement came back at **κ = 0.032** — worse than chance. A rewritten rubric got it to **κ = 0.259, 60% raw agreement**: better, still nowhere near trustworthy. The report now says **NOT TRUSTED** in as many words, with the number next to it. The diagnosis is the interesting half: my judge is text-only, so it *cannot see the image it is grading against*. A rationale that names a real visible object and one that hallucinates a plausible-sounding fake are, in text, indistinguishable — both read as specific and grounded. The two worst disagreements were exactly that: fluent, confident descriptions of things that were not in the photograph. No amount of rubric wording fixes a blind judge; it needs eyes. A judge you haven't calibrated is a vibes generator — and mine turned out to be one.
- **The adjudicator contradicted itself in writing.** One rationale described cigarette butts in detail and then concluded "clean." It's stored verbatim in the ledger — that sentence is now a test case for the next rubric revision.

---

## What I'd tell another PM

1. **Buy measurement before capability.** The £10 model budget went unspent because the eval harness kept proving the bottleneck wasn't where I assumed. Every pound you spend before you can measure is a guess.
2. **Split your metrics until they confess.** Accuracy hid everything. Localization vs classification, routing vs verdict, measured vs modelled — each split converted a grade into a cause.
3. **Config is data with a history.** Versioned thresholds cost one join and bought a complete answer to "why did the system decide that, that day?" — which is also roughly what incoming AI regulation asks for.
4. **Design the failure paths first.** Dead letters, retry budgets, stale-claim reaping, and no-guessing rules were all built before they were needed. All of them fired.
5. **An honest bad number beats a flattering composite.** The flat frontier, the 0.44 adjudicator, and a judge that failed its own audit at κ = 0.26 are the most persuasive artifacts this project produced. Nothing sells a measurement system like watching it catch your own assumptions — including the assumption that the thing doing the measuring is fit to.

---

*Stack: Python, FastAPI, SQLAlchemy/SQLite (WAL), LangGraph, Roboflow-hosted TACO detector, Qwen2.5-VL via Ollama, CLIP ViT-B/32, Llama 3.1 as judge, Streamlit. 271 tests. Total external spend: £0.00 of a £10 cap. The explainer video above was rendered programmatically — Pillow frames, ffmpeg, and a local neural-TTS voiceover, with scene timing derived from the narration audio.*
