---
title: Routeval — What Did Your Escalations Buy?
toc: false
---

<style>
.rv-hero{max-width:850px;margin:2.7rem 0 1.8rem}
.rv-kicker{font:600 .9rem var(--monospace);letter-spacing:.09em;text-transform:uppercase;color:#c59546}
.rv-hero h1{font-size:clamp(2.3rem,5vw,4.3rem);line-height:1.08;letter-spacing:-.035em;margin:.7rem 0 1.2rem}
.rv-hero p{font-size:1.12rem;line-height:1.65;max-width:700px;color:var(--theme-foreground-muted)}
.rv-actions{display:flex;gap:1rem;align-items:center;flex-wrap:wrap;margin:1.3rem 0}
.rv-download{display:inline-block;background:#dab56a;color:#141923!important;padding:.8rem 1.15rem;border-radius:5px;font-weight:650;text-decoration:none;font-size:1rem}
.rv-download:hover{background:#c9a45a;text-decoration:underline}
.rv-actions a:focus-visible{outline:3px solid var(--theme-foreground-focus);outline-offset:4px}
.rv-note{font-size:.9rem;line-height:1.65;color:var(--theme-foreground-muted)}
.rv-status{border-left:3px solid #c59546;padding:.9rem 1.1rem;background:var(--theme-background-alt);line-height:1.6;margin:1.3rem 0 2.2rem;font-size:1rem}
.rv-stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:.8rem;margin:1.25rem 0}
.rv-stat{padding:1.1rem;border:1px solid var(--theme-foreground-faintest);border-radius:7px;background:var(--theme-background-alt)}
.rv-stat b{display:block;font-size:clamp(1.6rem,2.6vw,2.1rem);line-height:1.2;color:var(--theme-foreground-focus)}
.rv-stat>span{display:block;margin-top:.4rem;font-size:.9rem;line-height:1.4;color:var(--theme-foreground-muted)}
.rv-compare{padding:1rem 1.15rem;border-left:3px solid #c59546;background:var(--theme-background-alt);line-height:1.6;margin:1rem 0}
.rv-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:.8rem;margin:1.3rem 0 2rem}
.rv-grid article{border-top:2px solid #c59546;padding:1rem .1rem}.rv-grid h3{font-size:1.08rem;margin:.2rem 0 .7rem}.rv-grid p{font-size:1rem;line-height:1.6}
.rv-matrix{width:100%;border-collapse:separate;border-spacing:.5rem;margin:1rem 0}.rv-matrix th{text-align:left;font-size:.9rem;padding:.4rem}.rv-matrix td{width:40%;padding:.9rem;border:1px solid var(--theme-foreground-faintest);border-radius:5px;background:var(--theme-background-alt)}
.rv-matrix b{font-size:1.7rem;display:block}.rv-matrix td>span{font-size:.9rem}.rv-matrix .watch{border-color:#c59546}
.rv-table{overflow-x:auto}.rv-table table{min-width:460px}
@media(max-width:650px){.rv-stats,.rv-grid{grid-template-columns:1fr}.rv-hero{margin-top:1.7rem}.rv-hero h1{font-size:2.6rem}.rv-matrix th,.rv-matrix td>span{font-size:.875rem}.rv-matrix td{padding:.65rem}}
</style>

```js
const reports = await FileAttachment("data/routeval/demo-reports.json").json();
const kitUrl = await FileAttachment("downloads/routeval-trial-kit-0.1.0.zip").url();
const sourceUrl = await FileAttachment("downloads/routeval-0.1.0.tar.gz").url();
const pct = value => (100 * value).toFixed(0) + "%";
const usd = value => value === null ? "Unknown" : "$" + value.toFixed(4);
```

<div class="rv-hero">
  <span class="rv-kicker">Routeval · Python evaluation tool · 0.1.0 candidate</span>
  <h1>What did your escalations buy?</h1>
  <p>Replay examples through your AI pipeline. Compare answer quality, routing decisions, and cost in one report — for a model cascade, a human handoff, or a rules-and-LLM flow.</p>
  <p class="rv-note">Python 3.10+ · no required package dependencies · three offline examples · no API key needed</p>
</div>

```js
display(html`<div class="rv-actions">
  <a class="rv-download" href="${kitUrl}" download="routeval-trial-kit-0.1.0.zip">Download trial kit</a>
  <a href="#try-it-with-five-cases">Run five cases</a>
  <a href="${sourceUrl}" download="routeval-0.1.0.tar.gz">Package source · MIT</a>
</div>`);
```

<div class="rv-status"><strong>Ready to try:</strong> the kit includes the locally verified 0.1.0 wheel and source archive. The public PyPI 0.0.1 release reserves the name and does not contain this harness. Install the included wheel for this trial.</div>

## See what answer accuracy leaves out

These are five **synthetic** cases, evaluated by the installed Routeval package. The second policy skips a required local review. Its final answer stays correct and its API cost stays the same — the review is free. Its escalation recall still falls.

```js
const scenario = view(Inputs.radio(["baseline", "missed"], {
  label: "Compare a routing policy",
  value: "baseline",
  format: key => reports.scenarios[key].title
}));
```

```js
const chosen = reports.scenarios[scenario];
const a = chosen.summary.aggregates;
const r = a.routing;
const e = a.economics;
```

<div class="rv-stats">
  <div class="rv-stat"><b>${pct(a.accuracy_attempted)}</b><span>correct answers / all five attempts</span></div>
  <div class="rv-stat"><b>${pct(r.escalation_recall)}</b><span>required escalations actually taken</span></div>
  <div class="rv-stat"><b>${usd(e.cost_per_correct_usd)}</b><span>synthetic API spend per correct answer</span></div>
</div>

<div class="rv-compare">${scenario === "missed" ? "Baseline comparison: FAIL (exit 1). Answer accuracy is still 100%, but escalation recall fell from 100% to 50%. A free escalation remains an escalation." : "Reference policy: all five answers match and both required escalations are taken. Total synthetic API spend is $0.011. Declare route roles independently of price."}</div>

<table class="rv-matrix">
  <thead><tr><th></th><th>Answer correct</th><th>Answer wrong / failed</th></tr></thead>
  <tbody>
    <tr><th>Route matches label</th><td><b>${r.grid.route_right_verdict_right}</b><span>Both checks passed</span></td><td><b>${r.grid.route_right_verdict_wrong}</b><span>Chosen path failed</span></td></tr>
    <tr><th>Route differs</th><td class="watch"><b>${r.grid.route_wrong_verdict_right}</b><span>Correct answer, policy mismatch</span></td><td><b>${r.grid.route_wrong_verdict_wrong}</b><span>Both checks failed</span></td></tr>
  </tbody>
</table>

```js
const rows = chosen.cases.map(item => ({
  "Case": item.case,
  "Expected route": item.expected_route,
  "Actual route": item.route,
  "Answer correct": item.correct ? "Yes" : "No",
  "Cost (USD)": item.cost_usd
}));
```

<div class="rv-table">${Inputs.table(rows, {format: {"Cost (USD)": value => "$" + value.toFixed(3)}})}</div>

<p class="rv-note">These route labels express a reference policy. A mismatch does not prove an answer was accidental or that another path would have produced a better answer. The costs are illustrative; zero API spend excludes local compute and energy.</p>

## Try it with five cases

Download and unzip the trial kit. Open a terminal in its <code>routeval-trial-kit</code> folder, then run:

```sh
python -m pip install routeval-0.1.0-py3-none-any.whl
routeval --version
routeval run --config examples/local-hosted-cascade/routeval.json
```

You should see version **0.1.0**, five correct answers, 100% escalation recall, $0.011 total synthetic cost, and $0.0022 per correct answer. The report also saves a complete JSON run artifact.

The kit includes three starting points. Each uses a lookup fixture; none calls a model or claims to implement a production integration.

<div class="rv-grid">
  <article><h3>Local / hosted cascade</h3><p>A local fast path, a hosted escalation, and a free local review. Check that price never determines a route's role.</p></article>
  <article><h3>Support handoff</h3><p>Self-service answers and cases that require a human. Keep policy labels separate from whether the final answer sounds right.</p></article>
  <article><h3>Rules / LLM extraction</h3><p>Rules handle ordinary fields; an LLM handles ambiguous layouts. Check whether a policy change skips required fallbacks.</p></article>
</div>

To reproduce all three fixtures and their deliberate routing regressions:

```sh
python run_trials.py
```

For your own pipeline, change one function and replace the five golden examples. Return the answer, actual route, and **whole-decision cost**, including calls made before escalation:

```python
from routeval import Decision

def evaluate(request) -> Decision:
    result = your_pipeline(request)
    return Decision(
        answer=result.answer,
        route=result.route,
        cost_usd=result.total_cost_usd,
    )
```

Name the automatic and escalation routes in the supplied config. Add <code>expected_route</code> labels if you want routing metrics. Without those labels, answer quality, per-route cost and latency, and cost per correct answer still work. Missing cost stays unknown; cost gates require complete coverage.

Save a baseline, change one policy, and compare on the same five examples. An unavailable required metric, a changed measurement contract, or a routing regression returns a nonzero exit code.

## Where this came from

In [Quorum's verified routing audit](./12-Quorum-Audit), 40 of 184 attempts had correct verdicts with different route labels: **34 missed escalations and six unnecessary escalations**. That is 21.7% of all attempts; it is a different quantity from the share of correct verdicts.

The result led me to separate answer quality, policy agreement, and economics. It did not establish that those answers were luck. The Quorum evaluation set is diagnostic evidence, not a verified independent estimate of production performance.

Routeval packages that separation as a small report and versioned artifact. Bring your own scoring function or judge. Existing evaluation tools can also accept custom scoring; Routeval is a focused reporting contract that can sit alongside them.

## Help shape the next release

I'm looking for three independent trials: a cascade, a support handoff, and an extraction flow. The useful result is a repeatable report that changes a decision. Five cases are an onboarding test, not a production-quality estimate.

The kit includes <code>FEEDBACK.md</code>. Record time to your first useful report, wrapper effort, confusing labels, missing costs, and the decision the report changed. If you get stuck, that is useful feedback too.

[Email me about a trial](mailto:purnomonico@gmail.com?subject=Routeval%20trial).
Full artifacts can contain private answers and errors. The <code>routeval summary</code> command removes item contents and identifiers; review route and stage names before sharing. Nothing in this page or kit sends your results automatically.
