from queue import Queue

def removeIslands(matrix):
    ones_to_keep = set()
    for point in iter_edges(matrix):
        if point.value == 1:
            traverse_from_and_mark(point, matrix, ones_to_keep)

    new_matrix = [[0]*len(matrix[0]) for row in matrix]
    for point in iter_matrix(matrix):
        if point in ones_to_keep:
            new_matrix[point.i][point.j] = 1

    return new_matrix


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

    def __hash__(self):
        return hash((self.i, self.j))

    def __eq__(self, other):
        return self.i == other.i and self.j == other.j

    def __repr__(self):
        return f"Point({self.i}{self.j}{self.value})"


def iter_edges(matrix):
    for i in range(len(matrix)):
        yield Point(i, 0, matrix)
        yield Point(i, len(matrix[0])-1, matrix)
    
    for j in range(len(matrix[0])):
        yield Point(0, j, matrix)
        yield Point(len(matrix)-1, j, matrix)

def traverse_from_and_mark(start, matrix, visited):
    if start in visited:
        return

    q = Queue()
    q.put(start)
    visited.add(start)
    while not q.empty():
        point = q.get()
        for neighbor in point.iter_neighbors():
            if neighbor not in visited:
                visited.add(neighbor)
                q.put(neighbor)
        
def iter_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            yield Point(i, j, matrix)
