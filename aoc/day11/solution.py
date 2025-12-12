from pathlib import Path

type PathLike = str | Path


def read(filename: PathLike):
    out = {}
    with open(filename) as f:
        for line in f.readlines():
            out[line[0:3]] = line.strip()[5:].split(' ')

    return out

def part1(data) -> int:
    explore_nodes = data['you']
    outs = 0
    while explore_nodes:
        current_point = explore_nodes.pop()
        current_node = data[current_point]
        for connection in current_node:
            if connection == 'out':
                outs += 1
            else:
                explore_nodes.append(connection)

    return outs


def part2(data):
    raise NotImplementedError()
