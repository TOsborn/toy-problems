from . import permutations
import pytest

from collections import Counter

test_cases = [
    (
        [1, 2],
        [[1, 2], [2, 1]]
    ), (
        [1],
        [[1]]
    ), (
        [1, 2, 3],
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [3, 1, 2], [2, 3, 1], [3, 2, 1]]
    ), (
        [],
        []
    ), (
        [1, 2, 3, 4],
        [
            [1, 2, 3, 4],
            [1, 2, 4, 3],
            [1, 3, 2, 4],
            [1, 3, 4, 2],
            [1, 4, 2, 3],
            [1, 4, 3, 2],
            [2, 1, 3, 4],
            [2, 1, 4, 3],
            [2, 3, 1, 4],
            [2, 3, 4, 1],
            [2, 4, 1, 3],
            [2, 4, 3, 1],
            [3, 1, 2, 4],
            [3, 1, 4, 2],
            [3, 2, 1, 4],
            [3, 2, 4, 1],
            [3, 4, 1, 2],
            [3, 4, 2, 1],
            [4, 1, 2, 3],
            [4, 1, 3, 2],
            [4, 2, 1, 3],
            [4, 2, 3, 1],
            [4, 3, 1, 2],
            [4, 3, 2, 1]
        ],
    )
]

@pytest.mark.parametrize("test_input,expected", test_cases)
def test_getPermutations(test_input, expected):
    result = permutations.getPermutations(test_input)

    assert sorted(result) == sorted(expected)


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_getPermutations2(test_input, expected):
    result = permutations.getPermutations2(test_input)

    assert sorted(result) == sorted(expected)
