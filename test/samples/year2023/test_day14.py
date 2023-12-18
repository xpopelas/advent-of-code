from aoc.year2023.day14_parabolic_reflector_dish.parabolic_reflector_dish import (
    Day14ParabolicReflectorDish,
)

SAMPLE_INPUT = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""


def test_part_one_sample():
    solution = Day14ParabolicReflectorDish(content=SAMPLE_INPUT)
    solution.parse()
    assert solution.part_one() == "136"


def test_part_two_sample():
    solution = Day14ParabolicReflectorDish(content=SAMPLE_INPUT)
    solution.parse()
    assert solution.part_two() == "64"
