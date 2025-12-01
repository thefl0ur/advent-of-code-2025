import unittest
from pathlib import Path

from aoc.day1 import part1, read


class TestDay1(unittest.TestCase):
    filename = "test_input.md"

    def setUp(self):
        current_dir = Path(__file__).resolve()
        self.data = read(current_dir.parent.parent / "aoc" / "day1" / self.filename)

    def test_part_1(self):
        result = part1(self.data)
        assert result == 3, f"expected to be 3, got {result}"


if __name__ == "__main__":
    unittest.main()
