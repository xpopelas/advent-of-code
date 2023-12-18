from aoc.year2023.day10_pipe_maze.pipe_maze import Day10PipeMaze

SAMPLE_INPUT_PART_ONE = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""


def test_part_one_sample():
    solution = Day10PipeMaze(content=SAMPLE_INPUT_PART_ONE)
    solution.parse()
    assert solution.part_one() == "8"


SAMPLE_INPUT_PART_TWO = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""


def test_part_two_sample():
    solution = Day10PipeMaze(content=SAMPLE_INPUT_PART_TWO)
    solution.parse()
    assert solution.part_two() == "10"
