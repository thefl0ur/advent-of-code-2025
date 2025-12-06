import operator
from functools import reduce
from os import PathLike
from typing import Callable

type PathLikeStr = str | PathLike[str]
type Input = tuple[list[int], list[Callable]]


def read(filename: PathLikeStr) -> Input:
    out = None
    ops = []
    with open(filename) as f:
        iterator = iter(f)
        out = list(map(lambda x: [x], map(int, next(iterator).strip().split())))
        next_line = next(iterator)

        while True:
            line = next_line.strip().split()
            try:
                next_line = next(iterator)
            except StopIteration:
                ops = [operator.add if x == "+" else operator.mul for x in line]
                break
            for i, v in enumerate(map(int, line)):
                out[i].append(v)

    return out, ops


def read_cephalopod_way(filename: PathLikeStr) -> Input:
    out = []
    ops = []

    with open(filename) as f:
        lines = f.readlines()

    sizes = []
    for idx, char in enumerate(lines[-1]):
        if char != " ":
            sizes.append(idx)
            ops.append(operator.add if char == "+" else operator.mul)
    sizes.append(-1)

    out = [[] for _ in range(len(ops))]
    for line in lines[:-1]:  # omit ops line
        p1 = sizes[0]
        idx = 0
        for p in sizes[1:-1]:
            out[idx].append(line[p1 : p - 1])
            p1 = p
            idx += 1
        out[idx].append(line[p1:-1])

    clean = []

    for i, v in enumerate(out):
        clean.append(
            list(
                map(
                    lambda x: int(x) if x != "" else 0,
                    map(lambda x: "".join(x).strip(), zip(*v)),
                )
            )
        )

    return clean, ops


def part1(data: Input) -> int:
    totals = []
    for i in range(len(data[0])):
        totals.append(reduce(data[1][i], data[0][i]))

    return sum(totals)


def part2(data: Input) -> int:
    totals = []
    for i in range(len(data[0])):
        totals.append(reduce(data[1][i], data[0][i]))

    return sum(totals)
