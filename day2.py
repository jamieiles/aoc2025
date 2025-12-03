#!/usr/bin/env python3
from pathlib import Path


with open(Path(__file__).parent / 'data' / 'day2.txt') as f:
    ranges = [(int(x.split('-')[0]), int(x.split('-')[1]))
              for x in f.read().split(',')]


def part1() -> int:
    total = 0

    for r in ranges:
        for i in range(r[0], r[1] + 1):
            idstr = str(i)
            if len(idstr) % 2 == 1:
                continue
            if idstr[0:len(idstr) // 2] == idstr[len(idstr) // 2:]:
                total += i
    return total


def part2() -> int:
    total = 0

    def is_repeated(idstr: str) -> bool:
        for i in range(1, (len(idstr) // 2) + 1):
            if len(idstr) % i != 0:
                continue

            substr = idstr[0:i]
            count = len(idstr) // i
            if idstr == substr * count:
                return True

        return False

    for r in ranges:
        for i in range(r[0], r[1] + 1):
            idstr = str(i)
            if is_repeated(idstr):
                total += i
    return total


print(part1())
print(part2())
