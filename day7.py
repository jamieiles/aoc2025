#!/usr/bin/env python3
from pathlib import Path
from utils import Grid, Point, Direction
from functools import cache


grid = Grid(Path(__file__).parent / 'data' / 'day7.txt')


def part1() -> int:
    start = grid.find('S')
    beams = set([start])
    splitters = set()

    while beams:
        new_beams = set()
        for beam in beams:
            if beam not in grid:
                continue
            if grid[beam] == '^':
                splitters.add(beam)
                new_beams |= set(
                    [beam + Direction.LEFT, beam + Direction.RIGHT])
            else:
                new_beams.add(beam + Direction.DOWN)
        beams = new_beams

    return len(splitters)


def part2() -> int:
    @cache
    def follow(pos: Point) -> int:
        if pos not in grid:
            return 1
        if grid[pos] == '^':
            return follow(pos + Direction.LEFT) + follow(pos + Direction.RIGHT)
        return follow(pos + Direction.DOWN)

    return follow(grid.find('S'))


print(part1())
print(part2())
