from aoc.year2023.day11_cosmic_expansion.cosmic_expansion import Day11CosmicExpansion

SAMPLE_INPUT = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


def test_part_one_sample():
    solution = Day11CosmicExpansion(content=SAMPLE_INPUT)
    solution.parse()
    assert solution.part_one() == "374"


def test_part_two_sample():
    solution = Day11CosmicExpansion(content=SAMPLE_INPUT)
    solution.parse()
    assert solution.part_two() == "82000210"
