"""Offline synthetic fixture. Replace evaluate with your own five-case wrapper."""

from routeval import Decision

RESPONSES = {
    "invoice_number": ("INV-100", "rules", 0.0),
    "currency": ("USD", "rules", 0.0),
    "due_date": ("2026-10-31", "rules", 0.0),
    "ambiguous_total": ("123.45", "llm", 0.011),
    "unusual_layout": ("ACME", "llm", 0.011),
}


def evaluate(request: str) -> Decision:
    """Report the full decision cost, including work before escalation."""
    answer, route, cost = RESPONSES[request]
    return Decision(answer=answer, route=route, cost_usd=cost)


def missed_escalation(request: str) -> Decision:
    """Deliberately violate one route label while retaining the correct answer."""
    decision = evaluate(request)
    if request == "unusual_layout":
        return Decision(decision.answer, "rules", decision.cost_usd)
    return decision
