import unittest
from pathlib import Path

from aoc.day11 import part1, part2, read


class TestDay11(unittest.TestCase):
    filename = "test_input.md"

    def setUp(self):
        current_dir = Path(__file__).resolve()
        self.data = read(current_dir.parent.parent / "aoc" / "day11" / self.filename)

    def test_part_1(self):
        result = part1(self.data)
        assert result == 5, f"expect 5, got {result}"

    def test_part_2(self):
        result = part2(self.data)

if __name__ == "__main__":
    unittest.main()
