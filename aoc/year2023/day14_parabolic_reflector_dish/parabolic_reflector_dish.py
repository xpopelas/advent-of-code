import dataclasses
from functools import cached_property

from aoc.utilities.solution import AdventOfCodeSolution


Position = tuple[int, int]

NORTH = (0, -1)
EAST = (1, 0)
SOUTH = (0, 1)
WEST = (-1, 0)


@dataclasses.dataclass
class ParabolicReflectorDish:
    round_rocks: set[Position]
    cube_rocks: set[Position]

    @property
    def rocks(self) -> set[Position]:
        return self.round_rocks.union(self.cube_rocks)

    @cached_property
    def height(self) -> int:
        return max(rock[1] for rock in self.rocks)

    @cached_property
    def width(self) -> int:
        return max(rock[0] for rock in self.rocks)

    def is_at_border(self, position: Position, direction: Position) -> bool:
        if direction == NORTH:
            return position[1] <= 0
        if direction == WEST:
            return position[0] <= 0
        if direction == SOUTH:
            return position[1] >= self.height
        if direction == EAST:
            return position[0] >= self.width

        raise ValueError(f"Invalid direction {direction}")

    def copy(self) -> "ParabolicReflectorDish":
        return ParabolicReflectorDish(
            round_rocks=self.round_rocks.copy(),
            cube_rocks=self.cube_rocks.copy(),
        )

    def next_available_in_direction(
        self, start: Position, direction: Position
    ) -> Position:
        next_position = (start[0] + direction[0], start[1] + direction[1])
        while next_position not in self.rocks and not self.is_at_border(
            start, direction
        ):
            start = next_position
            next_position = (
                start[0] + direction[0],
                start[1] + direction[1],
            )
        return start

    def tilt(self, direction: Position) -> None:
        reverse = direction[0] > 0 or direction[1] > 0
        index = 1 if direction[1] != 0 else 0
        sorted_round_rocks = sorted(
            self.round_rocks, key=lambda rock: rock[index], reverse=reverse
        )
        for round_rock in sorted_round_rocks:
            self.round_rocks.remove(round_rock)
            new_round_rock = self.next_available_in_direction(round_rock, direction)
            self.round_rocks.add(new_round_rock)

    def cycle(self) -> None:
        self.tilt(NORTH)
        self.tilt(WEST)
        self.tilt(SOUTH)
        self.tilt(EAST)

    def __str__(self) -> str:
        result = ""
        for y in range(self.height + 1):
            for x in range(self.width + 1):
                if (x, y) in self.round_rocks:
                    result += "O"
                elif (x, y) in self.cube_rocks:
                    result += "#"
                else:
                    result += "."
        return result

    @property
    def total_load(self) -> int:
        return sum(self.height - round_rock[1] + 1 for round_rock in self.round_rocks)


class Day14ParabolicReflectorDish(AdventOfCodeSolution):
    def __init__(self):
        self.parabolic_reflector_dish: ParabolicReflectorDish = ParabolicReflectorDish(
            set(), set()
        )
        super().__init__(name="Day 14: Parabolic Reflector Dish")

    def parse(self) -> None:
        for y, line in enumerate(self.lines):
            for x, char in enumerate(line):
                match char:
                    case "O":
                        self.parabolic_reflector_dish.round_rocks.add((x, y))
                    case "#":
                        self.parabolic_reflector_dish.cube_rocks.add((x, y))
                    case ".":
                        pass
                    case _:
                        raise ValueError(f"Invalid character {char}")

    def part_one(self) -> str:
        parabolic_dish = self.parabolic_reflector_dish.copy()
        parabolic_dish.tilt(NORTH)
        return str(parabolic_dish.total_load)

    def part_two(self) -> str:
        cycles: dict[str, int] = {}
        cycle_index = 0
        found_cycle = False
        goal = 1_000_000_000
        parabolic_dish = self.parabolic_reflector_dish.copy()
        while cycle_index < goal:
            parabolic_dish.cycle()
            cycle_index += 1

            if not found_cycle and (found_cycle := str(parabolic_dish) in cycles):
                cycle_length = cycle_index - cycles[str(parabolic_dish)]
                cycle_index += cycle_length * ((goal - cycle_index) // cycle_length)
            else:
                cycles[str(parabolic_dish)] = cycle_index
        return str(parabolic_dish.total_load)


def main():
    Day14ParabolicReflectorDish().run()


if __name__ == "__main__":
    main()
