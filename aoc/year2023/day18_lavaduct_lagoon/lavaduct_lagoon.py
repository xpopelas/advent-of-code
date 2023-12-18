import dataclasses
import enum
from collections import namedtuple

from shapely import Polygon
from shapely.geometry import JOIN_STYLE

from aoc.utilities.solution import AdventOfCodeSolution


Position = namedtuple("Position", ["x", "y"])


class Direction(enum.Enum):
    LEFT = Position(-1, 0)
    RIGHT = Position(1, 0)
    UP = Position(0, -1)
    DOWN = Position(0, 1)

    @staticmethod
    def from_letter(letter: str) -> "Direction":
        match letter:
            case "L":
                return Direction.LEFT
            case "R":
                return Direction.RIGHT
            case "U":
                return Direction.UP
            case "D":
                return Direction.DOWN
            case _:
                raise ValueError(f"Invalid direction letter {letter}")

    @staticmethod
    def from_number(number: int) -> "Direction":
        match number:
            case 0:
                return Direction.RIGHT
            case 1:
                return Direction.DOWN
            case 2:
                return Direction.LEFT
            case 3:
                return Direction.UP
            case _:
                raise ValueError(f"Invalid direction number {number}")


@dataclasses.dataclass
class Instruction:
    direction: Direction
    distance: int
    hex_direction: Direction
    hex_distance: int

    @staticmethod
    def from_line(line: str) -> "Instruction":
        direction_letter, distance, color = line.split(" ")
        return Instruction(
            direction=Direction.from_letter(direction_letter),
            distance=int(distance),
            hex_direction=Direction.from_number(int(color[-2])),
            hex_distance=int(color[2:-2], 16),
        )

    def next_point(self, current_point: Position) -> Position:
        return Position(
            current_point.x + self.direction.value.x * self.distance,
            current_point.y + self.direction.value.y * self.distance,
        )

    def next_hex_point(self, current_point: Position) -> Position:
        return Position(
            current_point.x + self.hex_direction.value.x * self.hex_distance,
            current_point.y + self.hex_direction.value.y * self.hex_distance,
        )


class Day18LavaductLagoon(AdventOfCodeSolution):
    def __init__(self, content: str | None = None):
        self.instructions: list[Instruction] = []
        super().__init__(name="Day 18: Lavaduct Lagoon", content=content)

    def parse(self) -> None:
        for line in self.lines:
            self.instructions.append(Instruction.from_line(line))

    @staticmethod
    def polygon_area(vertices: list[Position]) -> int:
        polygon = Polygon(vertices).buffer(0.5, join_style=JOIN_STYLE.mitre)
        return int(polygon.area)

    def part_one(self) -> str:
        vertices = [Position(0, 0)]
        for instruction in self.instructions:
            vertices.append(instruction.next_point(vertices[-1]))

        return str(self.polygon_area(vertices))

    def part_two(self) -> str:
        vertices = [Position(0, 0)]
        for instruction in self.instructions:
            vertices.append(instruction.next_hex_point(vertices[-1]))

        return str(self.polygon_area(vertices))


def main():
    Day18LavaductLagoon().run()


if __name__ == "__main__":
    main()
