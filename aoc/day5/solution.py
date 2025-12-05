from os import PathLike

type PathLikeStr = str | PathLike[str]
type Range = tuple[int, int]
type Input = tuple[list[Range], list[int]]


def read(filename: PathLikeStr) -> Input:
    fresh_ingredient_id_ranges = []
    available_ingredient_ids = []
    with open(filename) as f:
        meet_delimeter = False
        for line in f:
            line = line.strip()
            if not line:
                meet_delimeter = True
                continue

            if not meet_delimeter:
                start, stop = line.split("-")
                fresh_ingredient_id_ranges.append((int(start), int(stop)))
            else:
                available_ingredient_ids.append(int(line))

    return fresh_ingredient_id_ranges, available_ingredient_ids


def part1(data: Input) -> int:
    breakpoint()
    ranges = []
    fresh_items = []
    for ids in data[0]:
        ranges.append(range(ids[0], ids[1] + 1))

    for item in data[1]:
        if any(item in s for s in ranges):
            fresh_items.append(item)

    return len(set(fresh_items))


def part2(data):
    raise NotImplementedError()
