from os import PathLike

type Grid = list[list[str]]
type Point = tuple[int, int]
type PathLikeStr = str | PathLike[str]

def read(filename: PathLikeStr) -> Grid:
    field = []
    with open(filename) as f:
        for line in f:
            field.append([x for x in line.strip()])

    return field


def _get_adjacent(data: Grid, point: Point) -> list[Point]:
    width = len(data[0]) - 1
    height = len(data) - 1
    adjacents = []
    for row_inc in [-1, 0, 1]:
        for col_inc in [-1, 0, 1]:
            new_pos = (point[0] + row_inc, point[1] + col_inc)
            if new_pos[0] == point[0] and new_pos[1] == point[1]:
                continue
            if new_pos[0] < 0 or new_pos[0] > width:
                continue
            if new_pos[1] < 0 or new_pos[1] > height:
                continue

            adjacents.append(data[new_pos[0]][new_pos[1]])

    return adjacents


def _scan_map(data: Grid) -> tuple[int, list[Point]]:
    count = 0
    removable = []
    for row, _ in enumerate(data):
        for col, _ in enumerate(data[row]):
            if data[row][col] != "@":
                continue
            adjacents = _get_adjacent(data, (row, col))

            if len(list(filter(lambda x: x == "@", adjacents))) < 4:
                count += 1
                removable.append((row, col))

    return count, removable


def _replace_removable(data: Grid, removables: list[Point]) -> Grid:
    new_data = data
    for removable in removables:
        new_data[removable[0]][removable[1]] = "."
    return new_data


def part1(data: Grid) -> int:
    return _scan_map(data)[0]


def part2(data: Grid) -> int:
    total = 0
    while True:
        result = _scan_map(data)

        if result[0] == 0:
            break

        total += result[0]
        data = _replace_removable(data, result[1])

    return total
