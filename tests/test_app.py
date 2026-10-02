from demo_web.app import handle


def test_price_endpoint():
    assert handle("/price?qty=4") == (200, {"qty": 4, "cents": 1000})


def test_bad_quantity_is_a_400():
    assert handle("/price?qty=-1")[0] == 400


def test_unknown_path_is_a_404():
    assert handle("/nope")[0] == 404
