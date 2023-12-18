from aoc.year2023.day08_haunted_wasteland.haunted_wasteland import Day08HauntedWasteland


SAMPLE_INPUT_PART_ONE = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""


def test_part_one_sample():
    solution = Day08HauntedWasteland(content=SAMPLE_INPUT_PART_ONE)
    solution.parse()
    assert solution.part_one() == "6"


SAMPLE_INPUT_PART_TWO = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


def test_part_two_sample():
    solution = Day08HauntedWasteland(content=SAMPLE_INPUT_PART_TWO)
    solution.parse()
    assert solution.part_two() == "6"
