from aoc.year2023.day16_the_floor_will_be_lava.the_floor_will_be_lava import (
    Day16TheFloorWillBeLava,
)

SAMPLE_INPUT = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""


def test_part_one_sample():
    solution = Day16TheFloorWillBeLava(content=SAMPLE_INPUT)
    solution.parse()
    assert solution.part_one() == "46"


def test_part_two_sample():
    solution = Day16TheFloorWillBeLava(content=SAMPLE_INPUT)
    solution.parse()
    assert solution.part_two() == "51"
