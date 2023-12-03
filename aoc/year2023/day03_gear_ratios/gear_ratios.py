import dataclasses
from typing import NamedTuple

from aoc.utilities.solution import AdventOfCodeSolution

Position = NamedTuple("Position", [("x", int), ("y", int)])


@dataclasses.dataclass
class PositionalNumber:
    number: int = 0
    start: Position = Position(0, 0)

    def __post_init__(self):
        self._current_position = self.start
        self._end_position = Position(
            self.start.x + len(str(self.number)), self.start.y
        )

    def __iter__(self):
        self._current_position = self.start
        return self

    def __next__(self):
        if self._current_position.x - self.start.x >= len(str(self.number)):
            raise StopIteration
        result = self._current_position
        self._current_position = Position(
            self._current_position.x + 1, self._current_position.y
        )
        return result

    def __eq__(self, other):
        return self.number == other.number and self.start == other.start


class Day03GearRatios(AdventOfCodeSolution):
    def __init__(self):
        self.symbols: dict[Position, str] = {}
        self.number_positions: dict[Position, PositionalNumber] = {}
        self.numbers: list[PositionalNumber] = []
        super().__init__(name="Day 3: Gear Ratios")

    def parse(self) -> None:
        was_on_digit = False
        current_number = PositionalNumber()

        for y, line in enumerate(self.lines):
            if was_on_digit:
                was_on_digit = False
                current_number = PositionalNumber()

            for x, char in enumerate(line):
                if char.isdigit():
                    if not was_on_digit:
                        was_on_digit = True
                        current_number.start = Position(x, y)
                        self.numbers.append(current_number)
                    current_number.number = 10 * current_number.number + int(char)
                    self.number_positions[Position(x, y)] = current_number
                elif was_on_digit:
                    was_on_digit = False
                    current_number = PositionalNumber()

                if not char.isdigit() and char != ".":
                    self.symbols[Position(x, y)] = char

    def has_adjacent_symbol(self, position: Position) -> bool:
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == dy == 0:
                    continue
                if self.symbols.get(Position(position.x + dx, position.y + dy)):
                    return True
        return False

    def get_unique_adjacent_numbers(self, position: Position) -> list[PositionalNumber]:
        result = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == dy == 0:
                    continue
                number = self.number_positions.get(
                    Position(position.x + dx, position.y + dy)
                )
                if number and number not in result:
                    result.append(number)
        return result

    def part_one(self) -> str:
        result = 0
        for number in self.numbers:
            for position in number:
                if self.has_adjacent_symbol(position):
                    result += number.number
                    break
        return str(result)

    def part_two(self) -> str:
        result = 0
        for position, symbol in self.symbols.items():
            if symbol != "*":
                continue
            adjacent_numbers = self.get_unique_adjacent_numbers(position)
            if len(adjacent_numbers) == 2:
                result += adjacent_numbers[0].number * adjacent_numbers[1].number
        return str(result)


def main():
    Day03GearRatios().run()


if __name__ == "__main__":
    main()
