import dataclasses

from aoc.utilities.solution import AdventOfCodeSolution


@dataclasses.dataclass
class SpringRow:
    field: str
    groups: list[int]

    @staticmethod
    def from_line(line: str) -> "SpringRow":
        field, groups_string = line.split(" ")
        groups = [int(group) for group in groups_string.split(",")]
        return SpringRow(field, groups)

    @property
    def extended(self) -> "SpringRow":
        new_field = "?".join(self.field for _ in range(5))
        new_groups = self.groups * 5
        return SpringRow(new_field, new_groups)

    def _can_place_group(self, position: int, group_length: int):
        if position + group_length > len(self.field):
            return False

        if any(self.field[position + index] == "." for index in range(group_length)):
            return False

        if (
            position + group_length < len(self.field)
            and self.field[position + group_length] == "#"
        ):
            return False

        return True

    def _count_ways(
        self,
        position: int = 0,
        group_index: int = 0,
        memory: dict[tuple[int, int], int] | None = None,
    ) -> int:
        if memory is None:
            memory = {}
        if group_index == len(self.groups):
            if all(c != "#" for c in self.field[position:]):
                return 1
            return 0

        if position >= len(self.field):
            return 0

        key = (position, group_index)
        if key in memory:
            return memory[key]

        possible_ways = 0
        if self._can_place_group(position, self.groups[group_index]):
            new_position = position + self.groups[group_index] + 1
            possible_ways += self._count_ways(new_position, group_index + 1, memory)

        if self.field[position] != "#":
            possible_ways += self._count_ways(position + 1, group_index, memory)

        memory[key] = possible_ways
        return possible_ways

    @property
    def valid_combinations_count(self) -> int:
        return self._count_ways()


class Day12HotSprings(AdventOfCodeSolution):
    def __init__(self):
        self.spring_rows: list[SpringRow] = []
        super().__init__(name="Day 12: Hot Springs")

    def parse(self) -> None:
        for line in self.lines:
            self.spring_rows.append(SpringRow.from_line(line))

    def part_one(self) -> str:
        result = sum(row.valid_combinations_count for row in self.spring_rows)
        return f"{result}"

    def part_two(self) -> str:
        result = sum(row.extended.valid_combinations_count for row in self.spring_rows)
        return f"{result}"


def main():
    Day12HotSprings().run()


if __name__ == "__main__":
    main()
