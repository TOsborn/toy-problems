import pytest

from .first_duplicate_value import firstDuplicateValue

input_output = [
    ([2, 2], 2),
    ([1, 2], -1),
    ([1, 1, 2, 2], 1),
    ([1, 2, 2, 3, 3], 2),
    ([2, 1, 5, 2, 3, 3, 4], 2)
]

@pytest.mark.parametrize("array,first_duplicate", input_output)
def test_firstDuplicateValue(array, first_duplicate):
    assert firstDuplicateValue(array) == first_duplicate
