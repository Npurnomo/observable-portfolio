# Local and hosted cascade

A free local review is still escalation. Missing it keeps answer accuracy at 100% while escalation recall falls from 100% to 50%.

All five cases and costs are synthetic. `evaluate` is a lookup fixture, not
a working model integration or a human review service.

From the kit root:

```sh
routeval run --config examples/local-hosted-cascade/routeval.json
```

Expected: five correct answers, complete known cost, escalation recall 1.
To inspect the deliberate route regression:

```sh
routeval run --config examples/local-hosted-cascade/routeval.json --pipeline examples/local-hosted-cascade/pipeline.py:missed_escalation
```

Expected: answer accuracy remains 1, escalation recall becomes 0.5, exit 1.

For a real trial, replace `evaluate` and the five golden examples. Decide route
labels before viewing the outputs. Report the total cost under the declared
cost basis. Use one run command on your chosen configuration.
