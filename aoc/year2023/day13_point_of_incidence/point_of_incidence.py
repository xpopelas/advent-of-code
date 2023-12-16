import dataclasses

from aoc.utilities.solution import AdventOfCodeSolution


@dataclasses.dataclass
class Board:
    rows: list[str]

    def __post_init__(self):
        self.columns: list[str] = [
            "".join(col[index] for col in self.rows)
            for index in range(len(self.rows[0]))
        ]

    @staticmethod
    def calculate_difference(line_a: str, line_b: str) -> int:
        return sum(a != b for a, b in zip(line_a, line_b))

    def get_symetry(self, lines: list[str], target_distance: int = 0) -> int:
        for line_index in range(1, len(lines)):
            if (
                sum(
                    self.calculate_difference(left, right)
                    for left, right in zip(
                        reversed(lines[:line_index]), lines[line_index:]
                    )
                )
                == target_distance
            ):
                return line_index

        return 0

    @property
    def symetry_value(self) -> int:
        if row_symetry := self.get_symetry(self.rows):
            return 100 * row_symetry

        if column_symetry := self.get_symetry(self.columns):
            return column_symetry

        raise ValueError("No symetry found")

    @property
    def symetry_distance_value(self) -> int:
        if row_symetry := self.get_symetry(self.rows, target_distance=1):
            return 100 * row_symetry

        if column_symetry := self.get_symetry(self.columns, target_distance=1):
            return column_symetry

        raise ValueError("No symetry found")


class Day13PointOfIncidence(AdventOfCodeSolution):
    def __init__(self):
        self.board: list[Board] = []
        super().__init__(name="Day 13: Point of Incidence")

    def parse(self) -> None:
        current_rows = []
        for line in self.lines:
            if line:
                current_rows.append(line)
            else:
                self.board.append(Board(current_rows))
                current_rows = []
        if current_rows:
            self.board.append(Board(current_rows))

    def part_one(self) -> str:
        result = 0
        for board in self.board:
            result += board.symetry_value
        return str(result)

    def part_two(self) -> str:
        result = 0
        for board in self.board:
            result += board.symetry_distance_value
        return str(result)


def main():
    Day13PointOfIncidence().run()


if __name__ == "__main__":
    main()
