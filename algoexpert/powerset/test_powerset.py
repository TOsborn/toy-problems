import powerset
import pytest

test_cases = [
    (
        [],
        [[]]
    ), (
        [0],
        [[], [0]]
    ), (
        [0, 1],
        [[], [0], [1], [0, 1]]
    ), (
        [0, 1, 2],
        [[], [0], [1], [0, 1], [2], [0, 2], [1, 2], [0, 1, 2]]
    )
]

@pytest.mark.parametrize('test_input,expected', test_cases)
def test_powerset(test_input, expected):
    result = powerset.powerset(test_input)

    assert sorted(result) == sorted(expected)