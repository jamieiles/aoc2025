#!/usr/bin/env python3
# /// script
# dependencies = [
#   "numpy",
#   "scipy",
# ]
# ///
from pathlib import Path
from heapq import heappop, heappush
import re
import numpy as np
from scipy.optimize import LinearConstraint, milp


with open(Path(__file__).parent / 'data' / 'day10.txt') as f:
    machines = []
    for line in f.readlines():
        match = re.match(
            r'(?P<lights>\[[.#]+\]) (?P<wiring>(\(.*\))) (?P<joltage>{.*})', line)
        assert match
        machines.append(
            {
                'lights': tuple([s == '#' for s in match.groupdict()['lights'].strip('[]')]),
                'wiring': tuple([tuple(map(int, v.strip('()').split(','))) for v in match.groupdict()['wiring'].split()]),
                'joltage': tuple(list(map(int, match.groupdict()['joltage'].strip('{}').split(','))))
            }
        )


def part1() -> int:
    def solve(wiring, target_state) -> int:
        queue = []
        visited = set()

        best = None
        heappush(queue, (0, [False for _ in target_state]))

        while queue:
            count, state = heappop(queue)
            if best and count >= best:
                continue
            if state == target_state:
                if not best:
                    best = count
                best = min(best, count)
                continue

            def toggle(wires):
                new_state = list(state)
                for w in wires:
                    new_state[w] = not new_state[w]
                return tuple(new_state)

            for wires in wiring:
                next_state = toggle(wires)
                if (count + 1, next_state) not in visited:
                    visited.add((count + 1, next_state))
                    heappush(queue, (count + 1, next_state))

        assert best
        return best

    return sum([solve(m['wiring'], m['lights']) for m in machines])


def part2() -> int:
    def solve(wiring, target_joltage) -> int:
        coeffs = np.array([1 for _ in wiring])

        def wires_to_vec(joltage_index):
            return [1 if joltage_index in wires else 0 for wires in wiring]

        A = np.array([
            wires_to_vec(i) for i in range(len(target_joltage))
        ])

        b_l = b_u = np.array(target_joltage)
        constraints = LinearConstraint(A, b_l, b_u)
        integrality = np.ones_like(coeffs)
        res = milp(c=coeffs, constraints=constraints, integrality=integrality)
        return int(res.fun)

    return sum([solve(m['wiring'], m['joltage']) for m in machines])


print(part1())
print(part2())
