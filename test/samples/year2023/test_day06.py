from aoc.year2023.day06_wait_for_it.wait_for_it import Day06WaitForIt

SAMPLE_INPUT = """Time:      7  15   30
Distance:  9  40  200"""


def test_part_one_sample():
    solution = Day06WaitForIt(content=SAMPLE_INPUT)
    solution.parse()
    assert solution.part_one() == "288"


def test_part_two_sample():
    solution = Day06WaitForIt(content=SAMPLE_INPUT)
    solution.parse()
    assert solution.part_two() == "71503"
