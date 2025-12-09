import math
from pathlib import Path

type PathLike = str | Path


def read(filename: PathLike):
    out = []
    with open(filename) as f:
        for line in f:
            parts = line.strip().split(",")
            out.append((int(parts[0]), int(parts[1])))
    return out


def part1(data) -> int:
    dists = {(x, y): math.sqrt((0 - x) ** 2 + (0 - y) ** 2) for x, y in data}
    sorted_points = [k for k, _ in sorted(dists.items(), key=lambda item: item[1])]
    l, r = 0, len(sorted_points) - 1
    max_ = 0

    while l < len(sorted_points):
        square = abs(
            max(sorted_points[l][0], sorted_points[r][0])
            + 1
            - min(sorted_points[r][0], sorted_points[r][0])
        ) * abs(
            max(sorted_points[l][1], sorted_points[r][1])
            + 1
            - min(sorted_points[r][1], sorted_points[r][1])
        )
        if max_ < square:
            max_ = square

        l += 1
        r -= 1
    return max_


def part2(data):
    raise NotImplementedError()
