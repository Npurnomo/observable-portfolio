# Routeval — first useful report

This kit contains the published Routeval 0.1.0 package, its MIT-licensed
source, three runnable five-case examples, and a feedback form. The included
wheel and source archive match the files published on PyPI.

## 1. Install Routeval

Python 3.10 or later is required. Unzip the kit and open a terminal in
its `routeval-trial-kit` folder.

```sh
python -m pip install routeval==0.1.0
routeval --version
```

Expected version: 0.1.0. The package has no required dependencies.
For installation without network access, use the included wheel instead:
`python -m pip install routeval-0.1.0-py3-none-any.whl`.

## 2. Get a first report

```sh
routeval run --config examples/local-hosted-cascade/routeval.json
```

Expected: 100% answer accuracy, 100% escalation recall, $0.011 total
synthetic cost and $0.0022 per correct answer. A run artifact is saved in
`examples/local-hosted-cascade/runs/`. No API keys or model calls are needed.

Alternatively choose `support-handoff` or `rules-llm-extraction`. Every
example uses five synthetic cases and declares route roles explicitly.

```sh
python run_trials.py
```

This checks all three bundled fixtures and their deliberate route regressions.
It does not test any real external users or model integration.

## 3. Connect one real pipeline

Copy the example closest to your pipeline. Replace `evaluate` with a wrapper
returning `Decision(answer, route, cost_usd)`; report the whole decision
cost. Replace the five golden rows with your examples and expected answers.
Route labels are optional for answer/cost reporting, but required to measure
escalation precision and recall. Decide them from your policy before running.

- Declare automatic and escalation paths independently of price.
- Specify your cost basis: API-only, API and human, or another clearly named basis.
- Use zero for known zero spend, and None for unknown spend.
- Keep failed attempts. A failed call with known charges can return
  `Decision(None, route="hosted", cost_usd=0.01, error="timeout after charge")`.
- A custom scorer must return bool and have an explicit ID/version for comparisons.

Use the single run command for your chosen config. After one useful report,
save its artifact as your baseline, change one policy, and rerun against it:

```sh
routeval run --config examples/local-hosted-cascade/routeval.json --baseline examples/local-hosted-cascade/runs/<previous-run>.json
```

Keep the dataset, scorer, route roles, pricing, and cost basis fixed.
Comparisons require complete cost; missing required measurements fail.
Exit 0 = requested gates passed, 1 = regression or quality failure,
2 = input/config failure, 3 = invalid or incomplete measurement.

## 4. Tell us what changed

Complete FEEDBACK.md after your first report. Record time spent and any
confusing steps, even if you could not finish. A useful trial produces a
repeatable report and a concrete decision; five cases do not establish
production performance.

To share aggregate results:

```sh
routeval summary examples/local-hosted-cascade/runs/<run>.json --output summary.json
```

Full artifacts contain expected answers, model outputs, stage contents, and
error text. The summary removes item contents and identifiers; review route
and stage names before sharing. Use synthetic reproductions for private bugs.

Questions and feedback: purnomonico@gmail.com. Nothing is sent automatically.
See PACKAGE-README.md for the full contract and APIs.
