#!/usr/bin/env python3
from itertools import combinations
from functools import cache
from pathlib import Path
from collections import namedtuple

Box = namedtuple('Box', ['x', 'y', 'z', 'id'])


with open(Path(__file__).parent / 'data' / 'day8.txt') as f:
    points = [Box(*[int(v) for v in line.rstrip().split(',')], i)
              for i, line in enumerate(f.readlines())]


def dist_sq(a: Box, b: Box) -> int:
    return sum([(a[0] - a[1]) ** 2 for a in zip(a[0:3], b[0:3])])


@cache
def calculate_distances() -> list[tuple[float, Box, Box]]:
    distances = []
    for pair in combinations(points, 2):
        distances.append((dist_sq(pair[0], pair[1]), min(pair), max(pair)))
    return sorted(distances, reverse=True)


class Graph:
    def __init__(self):
        self.network_ids = {p.id: i for i, p in enumerate(points)}
        self.networks = {i: set([i]) for i, p in enumerate(points)}
        self.distances = list(calculate_distances())
        self.connections = 0
        self.num_nets = len(self.networks)

    def connect(self) -> None:
        _, a, b = self.distances.pop()
        if self.network_ids[a.id] == self.network_ids[b.id]:
            self.connections += 1
            return

        dst = self.network_ids[a.id]
        src = self.network_ids[b.id]
        for p in self.networks[src]:
            self.network_ids[p] = dst
        self.networks[dst] |= self.networks[src]
        self.networks[src] = set()
        self.connections += 1
        self.num_nets -= 1


def part1() -> int:
    g = Graph()
    while g.connections != 1000:
        g.connect()

    networks = sorted(g.networks.values(), key=lambda k: len(k))

    return len(networks[-1]) * len(networks[-2]) * len(networks[-3])


def part2() -> int:
    g = Graph()
    while g.num_nets != 2:
        g.connect()

    while True:
        _, a, b = g.distances.pop()
        if g.network_ids[a.id] != g.network_ids[b.id]:
            return a[0] * b[0]


print(part1())
print(part2())