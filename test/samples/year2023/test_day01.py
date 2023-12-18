from aoc.year2023.day01_trebuchet.trebuchet import Trebuchet

SAMPLE_INPUT_PART_ONE = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


def test_part_one_sample():
    trebuchet = Trebuchet(content=SAMPLE_INPUT_PART_ONE)
    assert trebuchet.part_one() == "142"


SAMPLE_INPUT_PART_TWO = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


def test_part_two_sample():
    trebuchet = Trebuchet(content=SAMPLE_INPUT_PART_TWO)
    assert trebuchet.part_two() == "281"
