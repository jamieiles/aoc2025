#!/usr/bin/env python3
from pathlib import Path
from utils import Grid, Point
from typing import Iterator


grid = Grid(Path(__file__).parent / 'data' / 'day4.txt')


def roll_accessible(roll: Point) -> bool:
    full_neighbours = 0
    for neighbour in roll.neighbours:
        if neighbour in grid and grid[neighbour] == '@':
            full_neighbours += 1
    return full_neighbours < 4


def accessible_rolls() -> Iterator[Point]:
    for cell in grid:
        if grid[cell] != '@':
            continue
        if roll_accessible(cell):
            yield cell


def part2() -> int:
    removed = []
    accessible = list(accessible_rolls())

    for roll in accessible:
        if grid[roll] != '@':
            continue
        removed.append(roll)
        grid[roll] = '.'
        for neighbour in roll.neighbours:
            if neighbour not in grid or grid[neighbour] != '@':
                continue
            if roll_accessible(neighbour):
                accessible.append(neighbour)

    return len(removed)


def part1() -> int:
    return len(list(accessible_rolls()))


print(part1())
print(part2())
