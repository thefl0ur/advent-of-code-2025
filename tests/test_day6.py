import unittest
from pathlib import Path

from aoc.day6 import part1, part2, read


class TestDay6(unittest.TestCase):
    filename = "test_input.md"

    def setUp(self):
        current_dir = Path(__file__).resolve()
        self.data = read(current_dir.parent.parent / "aoc" / "day6" / self.filename)

    def test_part_1(self):
        result = part1(self.data)
        assert result == 4277556, f"expect 4277556, got {result}"

    def test_part_2(self):
        result = part2(self.data)


if __name__ == "__main__":
    unittest.main()
