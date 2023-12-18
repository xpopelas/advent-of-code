from aoc.year2023.day02_cube_conundrum.cube_conundrum import CubeConundrum

SAMPLE_INPUT_PART_ONE = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def test_part_one_sample():
    cube_conundrum = CubeConundrum(content=SAMPLE_INPUT_PART_ONE)
    cube_conundrum.parse()
    assert cube_conundrum.part_one() == "8"


SAMPLE_INPUT_PART_TWO = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def test_part_two_sample():
    cube_conundrum = CubeConundrum(content=SAMPLE_INPUT_PART_TWO)
    cube_conundrum.parse()
    assert cube_conundrum.part_two() == "2286"
