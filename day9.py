#!/usr/bin/env python3
from itertools import combinations
from multiprocessing import Value
from pathlib import Path
from utils import Point


with open(Path(__file__).parent / 'data' / 'day9.txt') as f:
    seats = [Point(*reversed(list(map(int, line.rstrip().split(',')))))
             for line in f.readlines()]


def part1() -> int:
    def area_pair(arg):
        a, b = arg
        return (1 + abs(a.col - b.col)) * (1 + abs(a.row - b.row)), a, b
    largest = max(map(area_pair, combinations(seats, 2)))
    return largest[0]


def part2() -> int:
    candidates = list(combinations(seats, 2))
    lines = [(s[0], s[1]) for s in zip(seats[1:] + [seats[0]], seats)]

    def area(a: Point, b: Point) -> int:
        return (1 + abs(a.col - b.col)) * (1 + abs(a.row - b.row))
    
    boxes = sorted([(area(b[0], b[1]), b[0], b[1]) for b in candidates],
                   reverse=True)

    for box_area, a, b in boxes:
        bl = Point(min(a.row, b.row), min(a.col, b.col))
        tr = Point(max(a.row, b.row), max(a.col, b.col))

        def misses_box(line: tuple[Point, Point]) -> bool:
            start, end = line
            line_min_row = min(start.row, end.row)
            line_max_row = max(start.row, end.row)
            line_min_col = min(start.col, end.col)
            line_max_col = max(start.col, end.col)

            return (line_max_col <= bl.col or
                    line_min_col >= tr.col or
                    line_max_row <= bl.row or
                    line_min_row >= tr.row)

        for line in lines:
            if not misses_box(line):
                break
        else:
            return box_area
        
    raise ValueError('No maximal box found')


print(part1())
print(part2())
