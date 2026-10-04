# routeval

**Compare routing policies by answer quality, escalation correctness, and cost.**

For a Python pipeline with several paths — a model cascade, a cache, an abstain,
or a human handoff — Routeval replays labelled examples through your callable.
It reports which paths produced correct answers, which cases missed escalation,
and what each correct answer cost.

The core uses only the Python standard library. Python 3.10+; MIT licensed.

## Release status

**0.1.0 is published on [PyPI](https://pypi.org/project/routeval/0.1.0/).**
Both published distributions match the verified local files. A fresh public
installation, the offline demo, and all three five-case trial fixtures passed
verification on October 4, 2026.

```sh
python -m pip install routeval==0.1.0
```

For development, install this checkout with `python -m pip install .`.

## Try it without an API key

```sh
routeval init
routeval run
```

This scaffolds `routeval_example/{pipeline.py,golden.jsonl,routeval.json}`.
The offline support-bot example deliberately includes one failed request;
its config explicitly allows that error. The report should show:

| Measurement | Expected result |
|---|---|
| Attempted / correct / failed | 20 / 16 / 1 |
| Accuracy over attempted | 80% |
| Total synthetic cost | $0.0613 |
| Cost per correct answer | $0.00383125 |
| Successful automatic decisions / attempted | 65% |
| Escalation recall | 6/7 |
| Correct answer with a different route label | 1/20 |

Each run writes a unique, complete JSON artifact to `runs/`. Running the demo
again with `routeval run --baseline runs/<first-run>.json` should pass.
For a different destination, use `routeval init my-demo` and
`routeval run --config my-demo/routeval.json`. Paths in config are relative to
that config; paths passed on the command line are relative to your current directory.

## Evaluate your own pipeline

Wrap your existing code in a callable returning `Decision`. Report the
**whole decision's cost**, including cheap calls made before escalation.
Here is a runnable five-case example using synthetic outputs and prices:

```python
# pipeline.py
from routeval import Decision

ANSWERS = {
    "hours": "9–5",
    "address": "London",
    "refund": "review",
    "billing": "review",
    "hello": "hello",
}


def evaluate(text: str) -> Decision:
    route = "review" if text in {"refund", "billing"} else "fast"
    return Decision(
        answer=ANSWERS[text], route=route, cost_usd=0.011 if route == "review" else 0.001
    )
```

```jsonl
{"id":"1","input":"hours","expected":"9–5","expected_route":"fast"}
{"id":"2","input":"address","expected":"London","expected_route":"fast"}
{"id":"3","input":"refund","expected":"review","expected_route":"review"}
{"id":"4","input":"billing","expected":"review","expected_route":"review"}
{"id":"5","input":"hello","expected":"hello","expected_route":"fast"}
```

Save these as `pipeline.py` and `golden.jsonl`, then run:

```sh
routeval run --pipeline pipeline.py:evaluate --golden golden.jsonl \
  --auto-route fast --escalation-route review --cost-basis api-only \
  --min-accuracy 0.9 --min-escalation-recall 1
```

It reports five correct answers, $0.025 total cost, and $0.005 per correct
answer. Replace `evaluate` with your real call. Route names can be anything;
**declare their roles explicitly**. A free local model can be an escalation,
and a paid cache hit can be automatic. Prices never determine policy roles.
`expected_route` is optional: without it you still get answer quality, per-route
cost and latency, cost per correct answer, and declared automatic completion rate.

## Python, async, and custom scoring

```python
from routeval import Harness
from pipeline import evaluate

run = Harness(
    evaluate, auto_routes=["fast"], escalation_routes=["review"], cost_basis="api-only"
).run("golden.jsonl")
# Later, with the same data, scorer, route roles, and cost basis:
run = Harness(
    evaluate, auto_routes=["fast"], escalation_routes=["review"], cost_basis="api-only"
).run("golden.jsonl", baseline="runs/<previous>.json")
```

For async pipelines or scorers, use `await harness.arun(...)`. The CLI detects
async pipelines. Replay is sequential and does not add retries or concurrency. Reported cost covers
the pipeline; scorer/judge charges are excluded unless your wrapper accounts
for them explicitly.
Bring your own judge as a scorer `(expected, answer) -> bool`; numeric scores
need an explicit threshold. Set `scorer_id="team.rubric"` and
`scorer_version="1"` for a custom scorer before baseline comparison. Built-in
`exact`, `normalized` (case and whitespace), and `contains` scorers are versioned.

## Costs and failures

- Supply `cost_usd=0` for a genuinely zero cost under your declared cost basis.
  Missing cost is **unknown**, never zero. A local model's zero API bill does
  not include compute, energy, or reviewer time.
- Alternatively, return `model`, `tokens_in`, and `tokens_out`, and supply a
  pricing JSON file: `{"my-model":{"in_per_1m":1.0,"out_per_1m":3.0}}`.
  Use `--pricing prices.json` or `Harness(pricing_path="prices.json")`.
  This estimates one model call; report a total explicitly for multi-call cascades.
  Bundled rates are synthetic examples plus zero-API-spend local aliases.
- A failed call with known spend can return
  `Decision(None, route="review", cost_usd=0.011, error="timeout after charge")`.
  An ordinary exception records unknown spend. Both remain attempted items.
- Scorer errors preserve the pipeline's answer, route, cost, and latency and
  fail measurement. Invalid decisions and nonfinite/negative costs also fail
  measurement. Errors never disappear from the denominator.

## CI and baseline comparison

```sh
routeval compare runs/<current>.json runs/<baseline>.json
routeval run --config routeval.json --baseline runs/<baseline>.json
```

| Exit | Meaning |
|---|---|
| 0 | Evaluation completed; requested gates passed |
| 1 | Regression, failed quality limit, or pipeline errors (default) |
| 2 | Invalid config, input, or incompatible baseline before execution |
| 3 | Invalid/incomplete measurement or artifact comparison |

Without a baseline or quality limits, exit 0 means a completed evaluation;
it does not certify acceptable answer quality. `--allow-errors` permits
execution failures, but never scorer/validation failures. Cost gates and
baseline comparisons require complete cost coverage. Baselines also require
matching golden-set and pricing hashes, versioned scorer, route roles, and
cost basis. A different code commit is allowed. Zero-to-paid cost increases
are checked with an absolute tolerance; missing required metrics fail closed.
See [the artifact contract](docs/run-schema.md) for denominators and tolerances.

## Sharing results

Full artifacts contain expected answers, model outputs, error messages, stage
content, IDs, and hashes even when raw inputs are omitted. Treat them as private.
For an aggregate export:

```sh
routeval summary runs/<run>.json --output summary.json
```

Review route and stage names before sharing. Summaries omit item content and
identifiers and cannot serve as baselines.

## Scope and next step

Routeval supplies an opinionated routing report and comparable run artifact.
It composes with pytest and existing evaluation tools; it does not supply a
judge, a dashboard, model execution adapters, or response caching. Route labels
measure agreement with your policy, not proof that a route was optimal or an
answer was accidental.

The next adoption test is to onboard three independent cascades and check
whether users can get a useful report with five examples. Results-file import
and more integrations should follow observed friction in those trials.

[Quorum audit](https://nicopurnomo.me/12-Quorum-Audit) ·
[Origin story](content/launch-essay.md) · [Contributing](CONTRIBUTING.md)
