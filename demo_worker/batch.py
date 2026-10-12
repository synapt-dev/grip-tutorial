from demo_core.pricing import total_cents


def run(quantities):
    """Price a batch of orders: one {'qty', 'cents'} row per quantity, in order."""
    return [{"qty": q, "cents": total_cents(q)} for q in quantities]
