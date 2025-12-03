def read(filename) -> list[list[int]]:
    data = []
    with open(filename) as f:
        for line in f:
            data.append(list(map(int, line.strip())))

    return data


def part1(data) -> int:
    summ = 0
    for battery in data:
        part = battery[:-1]

        f_max = max(part)
        f_max_index = part.index(f_max)

        s_max = max(battery[f_max_index + 1 :])
        summ += int(f"{f_max}{s_max}")

    return summ


def part2(data):
    raise NotImplementedError()
