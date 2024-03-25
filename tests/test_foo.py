from src.main import sum_, product, quotient, difference


def test_sum():
    assert sum_(1, 2) == 3


def test_product():
    assert product(1, 2) == 2


def test_quotient():
    assert quotient(4, 2) == 2


def test_difference():
    assert difference(4, 2) == 2


def test_sum_incorrect():
    assert sum_(1, 2) == 4