def removeIslands(matrix):
    ocean = Ocean(matrix)
    for point in ocean.iter_edges():
        if point.value == 1:
            ocean.traverse_from_and_mark(point)

    return ocean.new_matrix


class Point:
    def __init__(self, i, j, matrix):
        self.i = i
        self.j = j
        self.matrix = matrix
        self.value = matrix[self.i][self.j]

    def iter_neighbors(self):
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (0 <= self.i+di < len(self.matrix) 
                and 0 <= self.j+dj < len(self.matrix[0])):
                neighbor = Point(self.i+di, self.j+dj, self.matrix)
                if neighbor.value == 1:
                    yield neighbor

    def __repr__(self):
        return f"Point({self.i}{self.j}{self.value})"

class Ocean:
    def __init__(self, matrix):
        self.matrix = matrix
        self.new_matrix = [[0]*len(row) for row in matrix]

    def iter_edges(self):
        for i in range(len(self.matrix)):
            yield Point(i, 0, self.matrix)
            yield Point(i, len(self.matrix[0])-1, self.matrix)
    
        for j in range(len(self.matrix[0])):
            yield Point(0, j, self.matrix)
            yield Point(len(self.matrix)-1, j, self.matrix)

    def traverse_from_and_mark(self, point):
        if self.new_matrix[point.i][point.j]:
            return

        self.new_matrix[point.i][point.j] = 1
        for neighbor in point.iter_neighbors():
            self.traverse_from_and_mark(neighbor)

    def iter_matrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                yield Point(i, j, self.matrix)
