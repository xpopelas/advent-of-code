from aoc.year2023.day18_lavaduct_lagoon.lavaduct_lagoon import Day18LavaductLagoon

SAMPLE_INPUT = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""


def test_part_one_sample():
    solution = Day18LavaductLagoon(content=SAMPLE_INPUT)
    solution.parse()
    assert solution.part_one() == "62"


def test_part_two_sample():
    solution = Day18LavaductLagoon(content=SAMPLE_INPUT)
    solution.parse()
    assert solution.part_two() == "952408144115"
