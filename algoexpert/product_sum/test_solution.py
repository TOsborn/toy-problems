import solution
import pytest


test_cases = [
    (
        [5, 2, [7, -1], 3, [6, [-13, 8], 4]], 
        12
    ), (
        [],
        0
    ), (
        [[]],
        0
    ), (
        [5],
        5
    ), (
        [[5]],
        10
    )
]

@pytest.mark.parametrize("test_input,expected", test_cases)
def test_productSum(test_input, expected):
    assert solution.productSum(test_input) == expected