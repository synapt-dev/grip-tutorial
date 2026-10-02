import pytest

from demo_core.pricing import total_cents


def test_flat_price():
    assert total_cents(4) == 1000


def test_negative_quantity_is_refused():
    with pytest.raises(ValueError):
        total_cents(-1)
