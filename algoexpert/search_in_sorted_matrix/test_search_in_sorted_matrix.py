from .search_in_sorted_matrix import searchInSortedMatrix

def test_searchInSortedMatrix_1():
    matrix = [
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004],
    ]
    target = 44

    assert searchInSortedMatrix(matrix, target) == [3, 3]

def test_searchInSortedMatrix_top_left():
    matrix = [
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004],
    ]
    target = 1

    assert searchInSortedMatrix(matrix, target) == [0, 0]

def test_searchInSortedMatrix_all_present():
    matrix = [
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004],
    ]
    for ridx in range(len(matrix)):
        for cidx in range(len(matrix[0])):
            target = matrix[ridx][cidx]
            assert searchInSortedMatrix(matrix, target) == [ridx, cidx]

def test_searchInSortedMatrix_all_not_present():
    matrix = [
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004],
    ]
    present = set.union(*(set(row) for row in matrix))
    for target in range(1006):
        if target not in present:
            assert searchInSortedMatrix(matrix, target) == [-1, -1]

def test_searchInSortedMatrix_empty():
    assert searchInSortedMatrix([], 0) == [-1, -1]


def test_searchInSortedMatrix_empty_rows():
    assert searchInSortedMatrix([[], []], 0) == [-1, -1]
