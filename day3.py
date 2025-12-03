#!/usr/bin/env python3
from pathlib import Path


with open(Path(__file__).parent / 'data' / 'day3.txt') as f:
    banks = [[int(x) for x in line.rstrip()] for line in f.readlines()]


def find_batteries(bank: list[int], max_len: int) -> int:
    if max_len == 1:
        return max(bank)
    else:
        largest = max(bank[0:-(max_len-1)])

    remainder = find_batteries(bank[bank.index(largest)+1:],
                               max_len-1)
    return (largest * (10 ** (max_len-1))) + remainder


def part1() -> int:
    return sum([find_batteries(b, 2) for b in banks])


def part2() -> int:
    return sum([find_batteries(b, 12) for b in banks])


print(part1())
print(part2())
