import pytest

from demo_worker.batch import run


def test_one_row_per_order_in_order():
    assert run([4, 1]) == [{"qty": 4, "cents": 1000}, {"qty": 1, "cents": 250}]


def test_a_negative_quantity_fails_the_batch():
    with pytest.raises(ValueError):
        run([1, -1])
