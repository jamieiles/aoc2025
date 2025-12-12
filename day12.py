#!/usr/bin/env python3
from pathlib import Path
from functools import cache


with open(Path(__file__).parent / 'data' / 'day12.txt') as f:
    areas = [
        (tuple(map(int, line.split(':')[0].split('x'))),
         list(map(int, line.split(':')[1].strip().split())))
        for line in f.readlines() if 'x' in line
    ]


def solve() -> int:
    count = 0
    for a in areas:
        scaled = (a[0][0] // 3, a[0][1] // 3)
        area_size = scaled[0] * scaled[1]
        if area_size >= sum(a[1]):
            count += 1
    return count


print(solve())
