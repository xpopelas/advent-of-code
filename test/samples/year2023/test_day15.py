from aoc.year2023.day15_lens_library.lens_library import Day15LensLibrary

SAMPLE_INPUT = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""


def test_part_one_sample():
    solution = Day15LensLibrary(content=SAMPLE_INPUT)
    solution.parse()
    assert solution.part_one() == "1320"


def test_part_two_sample():
    solution = Day15LensLibrary(content=SAMPLE_INPUT)
    solution.parse()
    assert solution.part_two() == "145"
