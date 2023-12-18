from aoc.year2023.day12_hot_springs.hot_springs import Day12HotSprings

SAMPLE_INPUT = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def test_part_one_sample():
    solution = Day12HotSprings(content=SAMPLE_INPUT)
    solution.parse()
    assert solution.part_one() == "21"


def test_part_two_sample():
    solution = Day12HotSprings(content=SAMPLE_INPUT)
    solution.parse()
    assert solution.part_two() == "525152"
