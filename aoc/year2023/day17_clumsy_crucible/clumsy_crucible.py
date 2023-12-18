import dataclasses
import heapq
from collections import namedtuple
from functools import cached_property

from aoc.utilities.solution import AdventOfCodeSolution


Position = namedtuple("Position", ["x", "y"])


@dataclasses.dataclass(frozen=True)
class SetElement:
    position: Position
    direction: Position
    steps: int


@dataclasses.dataclass(frozen=True)
class QueueElement:
    heat: int
    position: Position
    direction: Position
    steps: int

    def __lt__(self, other: "QueueElement") -> bool:
        return self.heat < other.heat

    @cached_property
    def set_element(self) -> SetElement:
        return SetElement(self.position, self.direction, self.steps)

    @cached_property
    def moved_position(self) -> Position:
        return Position(
            self.position.x + self.direction.x,
            self.position.y + self.direction.y,
        )

    def __iter__(self):
        positions = [
            Position(
                self.position.x + self.direction.y, self.position.y + -self.direction.x
            ),
            Position(
                self.position.x + -self.direction.y, self.position.y + self.direction.x
            ),
        ]
        directions = (
            Position(x, y)
            for x, y in zip(
                (self.direction.y, -self.direction.y),
                (-self.direction.x, self.direction.x),
            )
        )
        return iter(zip(positions, directions))


class Day17ClumsyCrucible(AdventOfCodeSolution):
    def __init__(self, content: str | None = None):
        self.grid: dict[Position, int] = {}
        super().__init__(name="Day 17: Clumsy Crucible", content=content)

    def parse(self) -> None:
        for y, line in enumerate(self.lines):
            for x, number in enumerate(line):
                self.grid[Position(x, y)] = int(number)

    def traverse(self, min_steps: int, max_steps: int) -> int:
        queue = [
            QueueElement(
                heat=self.grid[Position(1, 0)],
                position=Position(1, 0),
                direction=Position(1, 0),
                steps=0,
            ),
            QueueElement(
                heat=self.grid[Position(0, 1)],
                position=Position(0, 1),
                direction=Position(0, 1),
                steps=0,
            ),
        ]

        seen: set[SetElement] = set()
        end = max(self.grid)

        while queue:
            queue_element = heapq.heappop(queue)

            if queue_element.position == end and min_steps <= queue_element.steps:
                return queue_element.heat

            if queue_element.set_element in seen:
                continue

            seen.add(queue_element.set_element)

            if (
                queue_element.steps < (max_steps - 1)
                and queue_element.moved_position in self.grid
            ):
                heapq.heappush(
                    queue,
                    QueueElement(
                        queue_element.heat + self.grid[queue_element.moved_position],
                        queue_element.moved_position,
                        queue_element.direction,
                        queue_element.steps + 1,
                    ),
                )

            if min_steps > queue_element.steps:
                continue

            for position, direction in queue_element:
                if position not in self.grid:
                    continue

                heapq.heappush(
                    queue,
                    QueueElement(
                        queue_element.heat + self.grid[position],
                        position,
                        direction,
                        0,
                    ),
                )

        raise ValueError("No path found")

    def part_one(self) -> str:
        return str(self.traverse(0, 3))

    def part_two(self) -> str:
        return str(self.traverse(3, 10))


def main():
    Day17ClumsyCrucible().run()


if __name__ == "__main__":
    main()
