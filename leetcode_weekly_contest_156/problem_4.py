from queue import Queue

class Solution:
    def minimumMoves(self, grid) -> int:
        self.n = len(grid)
        self.grid = grid
        self.checked = set()
        pos = [(0, 0), (0, 1)]
        end = [(self.n-1, self.n-2), (self.n-1, self.n-1)]
        q = Queue()
        q.put((pos, 0))
        self.checked.add(tuple(pos))
        while not q.empty():
            pos, dist = q.get()
            if pos == end:
                return dist

            for neighbor, dist2 in self.neighbors(pos, dist):
                if neighbor == end:
                    return dist2
                if tuple(neighbor) not in self.checked:
                    q.put((neighbor, dist2))
                    self.checked.add(tuple(neighbor))

        return -1

    def neighbors(self, pos, dist):
        (y1, x1), (y2, x2) = pos

        # try moving right
        if self.is_open(y1, x1+1) and self.is_open(y2, x2+1):
            yield [(y1, x1+1), (y2, x2+1)], dist + 1

        # try moving down
        if self.is_open(y1+1, x1) and self.is_open(y2+1, x2):
            yield [(y1+1, x1), (y2+1, x2)], dist+1

        # try rotating clockwise
        if y2 == y1:
            if self.is_open(y2+1, x2) and self.is_open(y2+1, x1):
                yield [(y1, x1), (y2+1, x1)], dist+1

        # try rotating counterclockwise
        if y2 > y1:
            if self.is_open(y2, x2+1) and self.is_open(y1, x2+1):
                yield [(y1, x1), (y1, x1+1)], dist+1

    def is_open(self, y, x):
        return (0 <= y < self.n and 0 <= x < self.n and not self.grid[y][x])

        



f = Solution().minimumMoves

inputs = [
    [[[0,0,0,0,0,1],
    [1,1,0,0,1,0],
    [0,0,0,0,1,1],
    [0,0,1,0,1,0],
    [0,1,1,0,0,0],
    [0,1,1,0,0,0]]],
    [[[0,0,1,1,1,1],
    [0,0,0,0,1,1],
    [1,1,0,0,0,1],
    [1,1,1,0,0,1],
    [1,1,1,0,0,1],
    [1,1,1,0,0,0]]]
]
expected_outputs = [
    11,
    9
]

for inp, outp in zip(inputs, expected_outputs):
    print(f(*inp), outp)
