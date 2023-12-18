from aoc.year2023.day03_gear_ratios.gear_ratios import Day03GearRatios

SAMPLE_INPUT = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def test_part_one_sample():
    gear_ratios = Day03GearRatios(content=SAMPLE_INPUT)
    gear_ratios.parse()
    assert gear_ratios.part_one() == "4361"


def test_part_two_sample():
    gear_ratios = Day03GearRatios(content=SAMPLE_INPUT)
    gear_ratios.parse()
    assert gear_ratios.part_two() == "467835"
