"""Offline synthetic fixture. Replace evaluate with your own five-case wrapper."""

from routeval import Decision

RESPONSES = {
    "greeting": ("Hello", "local", 0.0),
    "hours": ("9–5", "local", 0.0),
    "address": ("London", "local", 0.0),
    "citation": ("Checked source", "hosted", 0.011),
    "ambiguous": ("Reviewed locally", "local_review", 0.0),
}


def evaluate(request: str) -> Decision:
    """Report the full decision cost, including work before escalation."""
    answer, route, cost = RESPONSES[request]
    return Decision(answer=answer, route=route, cost_usd=cost)


def missed_escalation(request: str) -> Decision:
    """Deliberately violate one route label while retaining the correct answer."""
    decision = evaluate(request)
    if request == "ambiguous":
        return Decision(decision.answer, "local", decision.cost_usd)
    return decision
