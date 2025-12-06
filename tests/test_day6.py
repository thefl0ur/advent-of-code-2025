import unittest
from pathlib import Path

from aoc.day6 import part1, part2, read, read_cephalopod_way


class TestDay6(unittest.TestCase):
    filename = "test_input.md"

    def setUp(self):
        current_dir = Path(__file__).resolve()
        self.path = current_dir.parent.parent / "aoc" / "day6" / self.filename

    def test_part_1(self):
        result = part1(read(self.path))
        assert result == 4277556, f"expect 4277556, got {result}"

    def test_part_2(self):
        result = part2(read_cephalopod_way(self.path))
        assert result == 3263827, f"expect 3263827, got {result}"


if __name__ == "__main__":
    unittest.main()
