from . import spiral_traverse
import pytest

test_cases = [
    (       # test 1
        [
            [1,   2,  3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10,  9,  8, 7]
        ],
        list(range(1, 17))
    )
]

@pytest.mark.parametrize("test_input,expected", test_cases)
def test_solution(test_input, expected):
    assert spiral_traverse.spiralTraverse(test_input) == expected