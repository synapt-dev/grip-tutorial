UNIT_CENTS = 250


def total_cents(quantity: int) -> int:
    """Flat price: every unit costs UNIT_CENTS."""
    if quantity < 0:
        raise ValueError("quantity must be >= 0")
    return quantity * UNIT_CENTS
