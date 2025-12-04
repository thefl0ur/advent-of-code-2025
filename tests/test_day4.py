import unittest
from pathlib import Path

from aoc.day4 import part1, part2, read


class TestDay4(unittest.TestCase):
    filename = "test_input.md"

    def setUp(self):
        current_dir = Path(__file__).resolve()
        self.data = read(current_dir.parent.parent / "aoc" / "day4" / self.filename)

    def test_part_1(self):
        result = part1(self.data)
        assert result == 13, f"expect 13, got {result}"

    def test_part_2(self):
        result = part2(self.data)
        assert result == 43, f"expect 43, got {result}"


if __name__ == "__main__":
    unittest.main()
