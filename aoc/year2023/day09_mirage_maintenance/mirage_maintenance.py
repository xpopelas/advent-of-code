import dataclasses
from typing import Optional

from aoc.utilities.solution import AdventOfCodeSolution


@dataclasses.dataclass
class Sequence:
    values: list[int]
    differences: Optional["Sequence"] = None

    def _calculate_differences(self) -> None:
        differences = [a - b for a, b in zip(self.values[1:], self.values[:-1])]
        self.differences = Sequence(values=differences)

    def __post_init__(self):
        if all(value == 0 for value in self.values):
            return

        self._calculate_differences()

    def get_next_value(self) -> int:
        if self.differences is None:
            return 0

        return self.values[-1] + self.differences.get_next_value()

    def get_previous_value(self) -> int:
        if self.differences is None:
            return 0

        return self.values[0] - self.differences.get_previous_value()


class Day09MirageMaintenance(AdventOfCodeSolution):
    def __init__(self, content: str | None = None):
        self.sequences: list[Sequence] = []
        super().__init__(name="Day 9: Mirage Maintenance", content=content)

    def parse(self) -> None:
        for line in self.lines:
            self.sequences.append(
                Sequence(values=[int(value) for value in line.split(" ")])
            )

    def part_one(self) -> str:
        result = 0
        for sequence in self.sequences:
            result += sequence.get_next_value()
        return str(result)

    def part_two(self) -> str:
        result = 0
        for sequence in self.sequences:
            result += sequence.get_previous_value()
        return str(result)


def main():
    Day09MirageMaintenance().run()


if __name__ == "__main__":
    main()
