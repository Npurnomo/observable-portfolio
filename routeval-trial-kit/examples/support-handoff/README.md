# Support and human handoff

A plausible answer can bypass a handoff required by policy. Label the path independently of the final answer. Human charges here are illustrative USD totals, not measured reviewer spend.

All five cases and costs are synthetic. `evaluate` is a lookup fixture, not
a working model integration or a human review service.

From the kit root:

```sh
routeval run --config examples/support-handoff/routeval.json
```

Expected: five correct answers, complete known cost, escalation recall 1.
To inspect the deliberate route regression:

```sh
routeval run --config examples/support-handoff/routeval.json --pipeline examples/support-handoff/pipeline.py:missed_escalation
```

Expected: answer accuracy remains 1, escalation recall becomes 0.5, exit 1.

For a real trial, replace `evaluate` and the five golden examples. Decide route
labels before viewing the outputs. Report the total cost under the declared
cost basis. Use one run command on your chosen configuration.
