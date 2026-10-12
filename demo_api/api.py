from demo_core.pricing import total_cents


def price(request: dict) -> dict:
    """{'qty': 4} -> {'qty': 4, 'cents': 1000}; a missing or bad qty is {'error': ...}."""
    qty = request.get("qty")
    if not isinstance(qty, int) or isinstance(qty, bool) or qty < 0:
        return {"error": "qty must be a non-negative integer"}
    return {"qty": qty, "cents": total_cents(qty)}
