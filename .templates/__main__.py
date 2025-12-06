from pathlib import Path

from . import part1, part2, read

DIR = Path(__file__).resolve().parent
FILENAME = "input.md"

if __name__ == "__main__":
    data = read(DIR / FILENAME)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
