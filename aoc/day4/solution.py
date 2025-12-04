def read(filename):
    field = []
    with open(filename) as f:
        for line in f:
            field.append([x for x in line.strip()])

    return field


def _get_adjacent(data, row, col):
    width = len(data[0]) - 1
    height = len(data) - 1
    adjacents = []
    for row_inc in [-1, 0, 1]:
        for col_inc in [-1, 0, 1]:
            new_pos = (row + row_inc, col + col_inc)
            if new_pos[0] == row and new_pos[1] == col:
                continue
            if new_pos[0] < 0 or new_pos[0] > width:
                continue
            if new_pos[1] < 0 or new_pos[1] > height:
                continue

            adjacents.append(data[new_pos[0]][new_pos[1]])

    return adjacents


def part1(data):
    count = 0
    for row, _ in enumerate(data):
        for col, _ in enumerate(data[row]):
            if data[row][col] != "@":
                continue
            adjacents = _get_adjacent(data, row, col)

            if len(list(filter(lambda x: x == "@", adjacents))) < 4:
                count += 1

    return count


def part2(data):
    raise NotImplementedError()
