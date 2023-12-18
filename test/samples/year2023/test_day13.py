from aoc.year2023.day13_point_of_incidence.point_of_incidence import (
    Day13PointOfIncidence,
)

SAMPLE_INPUT = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


def test_part_one_sample():
    solution = Day13PointOfIncidence(content=SAMPLE_INPUT)
    solution.parse()
    assert solution.part_one() == "405"


def test_part_two_sample():
    solution = Day13PointOfIncidence(content=SAMPLE_INPUT)
    solution.parse()
    assert solution.part_two() == "400"
