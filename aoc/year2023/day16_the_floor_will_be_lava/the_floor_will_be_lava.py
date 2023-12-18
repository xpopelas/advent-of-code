from collections import defaultdict
from typing import NamedTuple

from aoc.utilities.solution import AdventOfCodeSolution


class Position(NamedTuple):
    x: int
    y: int


class Direction(NamedTuple):
    x: int
    y: int


class PositionWithDirection(NamedTuple):
    position: Position
    direction: Direction

    def move(self) -> "PositionWithDirection":
        return PositionWithDirection(
            Position(
                self.position.x + self.direction.x, self.position.y + self.direction.y
            ),
            self.direction,
        )


class Contraption:
    def __init__(self, lines: list[str]):
        self.lines = lines
        self.energized: set[Position] = set()
        self.mirrors: dict[
            PositionWithDirection, list[PositionWithDirection]
        ] = defaultdict(list)
        self._calculate_mirrors()

    def _outside_of_range(self, position: Position) -> bool:
        return (
            position.x < 0
            or position.x >= len(self.lines[0])
            or position.y < 0
            or position.y >= len(self.lines)
        )

    def _add_mirror(self, position: Position):
        mirror_type = self.lines[position.y][position.x]
        new_mirrors: dict[Direction, list[PositionWithDirection]] = defaultdict(list)
        match mirror_type:
            case "|":
                splits = [
                    PositionWithDirection(
                        Position(position.x, position.y - 1), Direction(0, -1)
                    ),
                    PositionWithDirection(
                        Position(position.x, position.y + 1), Direction(0, 1)
                    ),
                ]
                new_mirrors[Direction(0, -1)].append(splits[0])
                new_mirrors[Direction(0, 1)].append(splits[1])
                new_mirrors[Direction(-1, 0)].extend(splits)
                new_mirrors[Direction(1, 0)].extend(splits)
            case "-":
                splits = [
                    PositionWithDirection(
                        Position(position.x - 1, position.y), Direction(-1, 0)
                    ),
                    PositionWithDirection(
                        Position(position.x + 1, position.y), Direction(1, 0)
                    ),
                ]
                new_mirrors[Direction(0, 1)].extend(splits)
                new_mirrors[Direction(0, -1)].extend(splits)
                new_mirrors[Direction(-1, 0)].append(splits[0])
                new_mirrors[Direction(1, 0)].append(splits[1])
            case "/":
                new_mirrors[Direction(1, 0)].append(
                    PositionWithDirection(
                        Position(position.x, position.y - 1), Direction(0, -1)
                    )
                )
                new_mirrors[Direction(-1, 0)].append(
                    PositionWithDirection(
                        Position(position.x, position.y + 1), Direction(0, 1)
                    )
                )
                new_mirrors[Direction(0, 1)].append(
                    PositionWithDirection(
                        Position(position.x - 1, position.y), Direction(-1, 0)
                    )
                )
                new_mirrors[Direction(0, -1)].append(
                    PositionWithDirection(
                        Position(position.x + 1, position.y), Direction(1, 0)
                    )
                )
            case "\\":
                new_mirrors[Direction(0, 1)].append(
                    PositionWithDirection(
                        Position(position.x + 1, position.y), Direction(1, 0)
                    )
                )
                new_mirrors[Direction(0, -1)].append(
                    PositionWithDirection(
                        Position(position.x - 1, position.y), Direction(-1, 0)
                    )
                )
                new_mirrors[Direction(1, 0)].append(
                    PositionWithDirection(
                        Position(position.x, position.y + 1), Direction(0, 1)
                    )
                )
                new_mirrors[Direction(-1, 0)].append(
                    PositionWithDirection(
                        Position(position.x, position.y - 1), Direction(0, -1)
                    )
                )
        for direction, splits in new_mirrors.items():
            self.mirrors[PositionWithDirection(position, direction)].extend(splits)

    def _calculate_mirrors(self):
        for y, line in enumerate(self.lines):
            for x, char in enumerate(line):
                if char in "|/-\\":
                    self._add_mirror(Position(x, y))

    def point(self, position_with_direction: PositionWithDirection) -> None:
        seen_positional_directions: set[PositionWithDirection] = set()
        queue = [position_with_direction]
        while queue:
            current = queue.pop(0)
            if current in seen_positional_directions or self._outside_of_range(
                current.position
            ):
                continue
            self.energized.add(current.position)
            seen_positional_directions.add(current)
            next_mirrors = self.mirrors.get(current)
            if next_mirrors:
                queue.extend(next_mirrors)
            else:
                queue.append(current.move())

    def print_energized(self) -> None:
        for y in range(len(self.lines)):
            print(
                "".join(
                    [
                        "#" if Position(x, y) in self.energized else "."
                        for x in range(len(self.lines[0]))
                    ]
                )
            )


class Day16TheFloorWillBeLava(AdventOfCodeSolution):
    def __init__(self, content: str | None = None):
        self.contraption: Contraption = Contraption([])
        super().__init__(name="Day 16: The Floor Will Be Lava", content=content)

    def parse(self) -> None:
        self.contraption = Contraption(self.lines)

    def part_one(self) -> str:
        self.contraption.energized = set()
        self.contraption.point(PositionWithDirection(Position(0, 0), Direction(1, 0)))
        return str(len(self.contraption.energized))

    def part_two(self) -> str:
        result = 0
        for x in range(len(self.lines[0])):
            self.contraption.energized = set()
            self.contraption.point(
                PositionWithDirection(Position(x, 0), Direction(0, 1))
            )
            result = max(result, len(self.contraption.energized))

            self.contraption.energized = set()
            self.contraption.point(
                PositionWithDirection(
                    Position(x, len(self.lines) - 1), Direction(0, -1)
                )
            )
            result = max(result, len(self.contraption.energized))

        for y in range(len(self.lines)):
            self.contraption.energized = set()
            self.contraption.point(
                PositionWithDirection(Position(0, y), Direction(1, 0))
            )
            result = max(result, len(self.contraption.energized))

            self.contraption.energized = set()
            self.contraption.point(
                PositionWithDirection(
                    Position(len(self.lines[0]) - 1, y), Direction(-1, 0)
                )
            )
            result = max(result, len(self.contraption.energized))

        return str(result)


def main():
    Day16TheFloorWillBeLava().run()


if __name__ == "__main__":
    main()
