#!/usr/bin/env python3
from pathlib import Path


with open(Path(__file__).parent / 'data' / 'day5.txt') as f:
    ranges: list[tuple[int, int]] = []
    ids = []
    for line in f.readlines():
        if '-' in line:
            low, high = line.rstrip().split('-')
            ranges.append((int(low), int(high)))
        elif line.rstrip():
            ids.append(int(line.rstrip()))


def merge_ranges() -> list[tuple[int, int]]:
    sorted_ranges = list(sorted(ranges))

    new_ranges = [sorted_ranges[0]]
    for r in sorted_ranges[1:]:
        prev = new_ranges[-1]
        if r[0] <= prev[1]:
            new_ranges[-1] = (prev[0], max(r[1], prev[1]))
        else:
            new_ranges.append(r)

    return new_ranges


def part1() -> int:
    def in_ranges(ingredient: int) -> bool:
        for r in ranges:
            if ingredient in range(r[0], r[1] + 1):
                return True
        return False

    fresh_ingredients = [
        ingredient for ingredient in ids if in_ranges(ingredient)]
    return len(fresh_ingredients)


def part2() -> int:
    return sum([r[1] - r[0] + 1 for r in merge_ranges()])


print(part1())
print(part2())
