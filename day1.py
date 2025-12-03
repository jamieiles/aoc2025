#!/usr/bin/env python3
from pathlib import Path


with open(Path(__file__).parent / 'data' / 'day1.txt') as f:
    sequence = [-int(l[1:]) if l[0] == 'L' else int(l[1:])
                for l in f.readlines()]


def part1() -> int:
    position = 50
    zero_count = 0
    for step in sequence:
        position = (position + step) % 100
        if position == 0:
            zero_count += 1

    return zero_count


def part2() -> int:
    position = 50
    zero_count = 0
    for step in sequence:
        zero_count += abs(step) // 100

        delta = abs(step) % 100
        if step < 0:
            delta *= -1

        new_position = (position + delta) % 100
        if position != 0 and (position + delta != new_position or new_position == 0):
            zero_count += 1
        position = new_position

    return zero_count


print(part1())
print(part2())
