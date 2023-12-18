import math
from typing import Callable

from aoc.utilities.solution import AdventOfCodeSolution


class Day08HauntedWasteland(AdventOfCodeSolution):
    def __init__(self, content: str | None = None):
        self.instructions: str = ""
        self.map: dict[str, tuple[str, str]] = {}
        super().__init__(name="Day 8: Haunted Wasteland", content=content)

    def parse(self) -> None:
        self.instructions = self.lines[0]

        for line in self.lines[2:]:
            source = line[:3]
            destination_left = line[7:10]
            destination_right = line[12:15]
            self.map[source] = (destination_left, destination_right)

    def find_number_of_steps(self, start: str, is_at_end: Callable[[str], bool]) -> int:
        result = 0
        while not is_at_end(start):
            result += 1
            match self.instructions[(result - 1) % len(self.instructions)]:
                case "L":
                    start = self.map[start][0]
                case "R":
                    start = self.map[start][1]
        return result

    def part_one(self) -> str:
        return str(self.find_number_of_steps("AAA", lambda node: node == "ZZZ"))

    def part_two(self) -> str:
        least_steps = {
            k: self.find_number_of_steps(k, lambda node: node.endswith("Z"))
            for k in self.map
            if k.endswith("A")
        }
        return str(math.lcm(*least_steps.values()))


def main():
    Day08HauntedWasteland().run()


if __name__ == "__main__":
    main()
