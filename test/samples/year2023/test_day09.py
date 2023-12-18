from aoc.year2023.day09_mirage_maintenance.mirage_maintenance import (
    Day09MirageMaintenance,
)


SAMPLE_INPUT = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def test_part_one_sample():
    solution = Day09MirageMaintenance(content=SAMPLE_INPUT)
    solution.parse()
    assert solution.part_one() == "114"


def test_part_two_sample():
    solution = Day09MirageMaintenance(content=SAMPLE_INPUT)
    solution.parse()
    assert solution.part_two() == "2"
