from pathlib import Path
from functools import cache


class Point:
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col

    def manhattan(self, rhs) -> int:
        delta = self - rhs
        return abs(delta.row) + abs(delta.col)

    def __add__(self, rhs):
        if isinstance(rhs, Point):
            return Point(self.row + rhs.row, self.col + rhs.col)
        else:
            return Point(self.row + rhs[0], self.col + rhs[1])

    def __mul__(self, rhs):
        assert isinstance(rhs, int)
        return Point(self.row * rhs, self.col * rhs)

    def __sub__(self, rhs):
        if isinstance(rhs, Point):
            return Point(self.row - rhs.row, self.col - rhs.col)
        else:
            return Point(self.row - rhs[0], self.col - rhs[1])

    def __str__(self):
        return f'({self.row}, {self.col})'

    def __repr__(self):
        return f'Point({self.row}, {self.col})'

    def __eq__(self, rhs):
        return rhs is not None and self.row == rhs.row and self.col == rhs.col

    def __lt__(self, rhs):
        return (self.row, self.col) < (rhs.row, rhs.col)

    def __hash__(self):
        return hash((self.row, self.col))

    @property
    def neighbours(self):
        vectors = [Point(x, y) for x in range(-1, 2)
                   for y in range(-1, 2) if not (x == 0 and y == 0)]
        for v in vectors:
            yield self + v

    def __getitem__(self, key):
        if key == 0:
            return self.row
        elif key == 1:
            return self.col
        else:
            raise KeyError('invalid index')


class Direction:
    UP = Point(-1, 0)
    RIGHT = Point(0, 1)
    DOWN = Point(1, 0)
    LEFT = Point(0, -1)


all_directions = [Direction.UP, Direction.RIGHT,
                  Direction.DOWN, Direction.LEFT]


class Grid:
    def __init__(self, filename: Path | None = None, celltype=str,
                 lines: list | None = None):
        if filename and not lines:
            with open(filename) as f:
                lines = f.readlines()

        self.grid = [[celltype(p) for p in line.strip()]
                     for line in lines]
        self.num_rows = len(self.grid)
        self.num_cols = len(self.grid[0])

    @property
    def rows(self):
        return self.grid

    @property
    def cols(self):
        cols = []
        for col in range(self.num_cols):
            cols.append([self.grid[row][col] for row in range(self.num_rows)])
        return cols

    def __str__(self):
        return '\n'.join([''.join([str(x) for x in row]) for row in self.grid])

    @cache
    def find(self, val):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self[Point(row, col)] == val:
                    return Point(row, col)
        raise KeyError(f'{val} not in grid')

    @cache
    def findall(self, val):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self[Point(row, col)] == val:
                    yield Point(row, col)

    def __contains__(self, n):
        return (n.row >= 0 and n.row < self.num_rows and
                n.col >= 0 and n.col < self.num_cols)

    def __getitem__(self, key):
        return self.grid[key.row][key.col]

    def __setitem__(self, key, val):
        assert key in self
        self.grid[key.row][key.col] = val

    def __iter__(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                yield Point(row, col)

    def pprint(self):
        col_header_len = len(str(self.num_cols))
        row_header_len = len(str(self.num_rows))

        col_headers = [f'{i:0{col_header_len}d}' for i in range(self.num_cols)]
        row_headers = [f'{i:0{row_header_len}d}' for i in range(self.num_rows)]

        for i in range(col_header_len):
            line = (row_header_len + 1) * ' ' + \
                ''.join(h[i] for h in col_headers)
            print(line)
        print()

        for row in range(self.num_rows):
            print(row_headers[row] + ' ' + ''.join(str(x)
                                                   for x in self.grid[row]))


def shoelace(points: list[Point]) -> float:
    x = [p.col for p in points]
    y = [p.row for p in points]

    v = (sum(map(lambda p: p[0] * p[1], zip(x, y[1:] + [y[0]]))) -
         sum(map(lambda p: p[0] * p[1], zip(x[1:] + [x[0]], y)))) / 2

    return abs(v)
