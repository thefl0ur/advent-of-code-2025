def read(filename) -> list[int]:
    result = []
    with open(filename) as f:
        for line in f.readlines():
            direction, value = line[0], int(line[1:])
            if direction == "L":
                value = value * -1
            result.append(value)

    return result


def part1(data) -> int:
    current = 50
    zeros = 0

    for value in data:
        current = (current - value % 100) % 100

        if current == 0:
            zeros += 1

    return zeros
