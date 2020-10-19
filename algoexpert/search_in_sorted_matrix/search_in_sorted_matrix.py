def searchInSortedMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return [-1, -1]

    rmid, cmid = len(matrix) // 2, len(matrix[0]) // 2
    if matrix[rmid][cmid] == target:
        return [rmid, cmid]
    elif target < matrix[rmid][cmid]:
        sub_mats = [
            [row[:cmid] for row in matrix[:rmid]],
            [row[:cmid] for row in matrix[rmid:]],
            [row[cmid:] for row in matrix[:rmid]]
        ]
        offsets = [
            [0, 0],
            [rmid, 0],
            [0, cmid]
        ]
    else:   # matrix[rmid][cmid] < target
        sub_mats = [
            [row[cmid+1:] for row in matrix[rmid+1:]],
            [row[:cmid+1] for row in matrix[rmid+1:]],
            [row[cmid+1:] for row in matrix[:rmid+1]]
        ]
        offsets = [
            [rmid+1, cmid+1],
            [rmid+1, 0],
            [0, cmid+1]
        ]

    for sub_mat, offset in zip(sub_mats, offsets):
        coords = searchInSortedMatrix(sub_mat, target)
        if coords != [-1, -1]:
            return [coords[0] + offset[0], coords[1] + offset[1]]

    return [-1, -1]
