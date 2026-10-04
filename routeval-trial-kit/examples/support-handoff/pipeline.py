"""Offline synthetic fixture. Replace evaluate with your own five-case wrapper."""

from routeval import Decision

RESPONSES = {
    "hours": ("9–5", "self_service", 0.001),
    "address": ("London", "self_service", 0.001),
    "password": ("Reset link", "self_service", 0.001),
    "refund": ("Refund approved", "human", 0.201),
    "account_dispute": ("Account reviewed", "human", 0.201),
}


def evaluate(request: str) -> Decision:
    """Report the full decision cost, including work before escalation."""
    answer, route, cost = RESPONSES[request]
    return Decision(answer=answer, route=route, cost_usd=cost)


def missed_escalation(request: str) -> Decision:
    """Deliberately violate one route label while retaining the correct answer."""
    decision = evaluate(request)
    if request == "account_dispute":
        return Decision(decision.answer, "self_service", decision.cost_usd)
    return decision
