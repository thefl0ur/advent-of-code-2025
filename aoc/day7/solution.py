from pathlib import Path

type PathLike = str | Path


def read(filename: PathLike) -> list[list[str]]:
    data = []
    with open(filename) as f:
        for line in f:
            data.append([x for x in line.strip()])

    return data


def part1(data) -> int:
    width = len(data[0]) - 1
    height = len(data)

    beams = [(1, data[0].index("S"))]
    visited = set()
    splitters = set()

    while beams:
        current_beam = beams.pop(0)

        if current_beam in visited:
            continue
        visited.add(current_beam)

        for line in range(current_beam[0], height):
            if data[line][current_beam[1]] != "^":
                continue

            splitters.add((line, current_beam[1]))

            if current_beam[1] - 1 >= 0:
                pos = (line, current_beam[1] - 1)
                beams.append(pos)
            if current_beam[1] + 1 <= width:
                pos = (line, current_beam[1] + 1)
                beams.append(pos)
            break

    return len(splitters)


def part2(data):
    raise NotImplementedError()
