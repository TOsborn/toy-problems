from .array_of_products import arrayOfProducts

import pytest

tests = [
    ([1, 2], [2, 1]),
    ([1, 2, 3], [6, 3, 2]),
    ([5, 1, 4, 2], [8, 40, 10, 20]),
    ([0, 1], [1, 0]),
    ([0, 2, 3], [6, 0, 0]),
    ([0, 0, 2, 3], [0, 0, 0, 0]),
]

@pytest.mark.parametrize('array,product_array', tests)
def test_arrayOfProducts(array, product_array):
    assert arrayOfProducts(array) == product_array
