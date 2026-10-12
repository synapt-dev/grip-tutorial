from demo_api.api import price


def test_price():
    assert price({"qty": 4}) == {"qty": 4, "cents": 1000}


def test_a_bad_quantity_is_an_error():
    assert "error" in price({"qty": -1})
    assert "error" in price({"qty": "4"})
    assert "error" in price({})
