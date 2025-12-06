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


def part1(data: Input):
    totals = []
    for i in range(len(data[0])):
        totals.append(reduce(data[1][i], data[0][i]))

    return sum(totals)


def part2(data):
    raise NotImplementedError()
