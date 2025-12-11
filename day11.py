#!/usr/bin/env python3
from pathlib import Path
from functools import cache


with open(Path(__file__).parent / 'data' / 'day11.txt') as f:
    graph = {
        x.split(':')[0]: [to.strip() for to in x.split(':')[1].split(' ')
                          if to.strip()] for x in f.readlines()
    }


def part1() -> int:
    def solve(node: str) -> int:
        count = 0
        for next in graph[node]:
            if next == 'out':
                count += 1
            else:
                count += solve(next)
        return count

    return solve('you')


def part2() -> int:

    @cache
    def solve(node: str, fft_visited: bool, dac_visited: bool) -> int:
        if node == 'out':
            return 1 if fft_visited and dac_visited else 0

        if node == 'dac':
            dac_visited = True
        if node == 'fft':
            fft_visited = True

        count = 0
        for next in graph[node]:
            count += solve(next, fft_visited, dac_visited)

        return count

    return solve('svr', False, False)


print(part1())
print(part2())
