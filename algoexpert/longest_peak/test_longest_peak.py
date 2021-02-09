from . import longest_peak
import pytest

test_cases = [
    (   # test 1
        [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3],
        6
    )
]

@pytest.mark.parametrize("test_input,expected", test_cases)
def test_solution(test_input, expected):
    assert longest_peak.longestPeak(test_input) == expected
