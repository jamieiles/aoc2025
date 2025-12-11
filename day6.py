#!/usr/bin/env python3
from pathlib import Path
from functools import reduce


def solve(operator: str, values: list[int]) -> int:
    match operator:
        case '+':
            return sum(values)
        case '*':
            return reduce(lambda a, b: a * b, values)
        case _:
            raise KeyError('bad operator')


def part1() -> int:
    with open(Path(__file__).parent / 'data' / 'day6.txt') as f:
        lines = [line.rstrip().split() for line in f.readlines()]

    total = 0
    for problem in list(zip(*lines)):
        values = [int(x) for x in problem[0:-1]]
        operator = problem[-1]
        total += solve(operator, values)

    return total


def part2() -> int:
    with open(Path(__file__).parent / 'data' / 'day6.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]
    max_len = max([len(line) for line in lines])
    lines = [line.ljust(max_len, ' ') for line in lines]
    transposed = [''.join(line) for line in zip(*list(lines))]

    problems = []
    buffer: list[str] = []
    for line in transposed:
        if not line.strip() and buffer:
            problems.append(buffer)
            buffer = []
        else:
            buffer.append(line)
    if buffer:
        problems.append(buffer)

    total = 0
    for p in problems:
        values = [int(x[0:-1]) for x in p]
        operator = p[0][-1]
        total += solve(operator, values)

    return total


print(part1())
print(part2())
