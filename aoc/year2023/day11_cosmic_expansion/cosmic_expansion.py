from itertools import combinations

from aoc.utilities.solution import AdventOfCodeSolution


Position = tuple[int, int]


class Day11CosmicExpansion(AdventOfCodeSolution):
    def __init__(self, content: str | None = None):
        self.galaxies: set[Position] = set()
        super().__init__(name="Day 11: Cosmic Expansion", content=content)

    def parse(self) -> None:
        for y, line in enumerate(self.lines, start=1):
            for x, char in enumerate(line, start=1):
                if char == "#":
                    self.galaxies.add((x, y))

    def cosmic_expansion(self, expansion_coefficient: int = 2) -> set[Position]:
        result = set(self.galaxies)
        columns_to_be_added = []
        for x in range(len(self.lines[0]), 1, -1):
            galaxies_in_row = sum(1 for galaxy in result if galaxy[0] == x)
            if galaxies_in_row != 0:
                continue

            columns_to_be_added.append(x)

        rows_to_be_added = []
        for y in range(len(self.lines), 1, -1):
            galaxies_in_column = sum(1 for galaxy in result if galaxy[1] == y)
            if galaxies_in_column != 0:
                continue

            rows_to_be_added.append(y)

        for x in columns_to_be_added:
            moved_galaxies = [galaxy for galaxy in result if galaxy[0] > x]
            for galaxy in moved_galaxies:
                result.remove(galaxy)
                result.add((galaxy[0] + expansion_coefficient - 1, galaxy[1]))

        for y in rows_to_be_added:
            moved_galaxies = [galaxy for galaxy in result if galaxy[1] > y]
            for galaxy in moved_galaxies:
                result.remove(galaxy)
                result.add((galaxy[0], galaxy[1] + expansion_coefficient - 1))

        return result

    @staticmethod
    def galaxy_distance(galaxy_a: Position, galaxy_b: Position) -> int:
        return abs(galaxy_a[0] - galaxy_b[0]) + abs(galaxy_a[1] - galaxy_b[1])

    @classmethod
    def all_pair_min_distance(cls, galaxies: set[Position]) -> int:
        result = 0
        all_pairs = list(combinations(galaxies, 2))
        for galaxy_a, galaxy_b in all_pairs:
            result += cls.galaxy_distance(galaxy_a, galaxy_b)
        return result

    def part_one(self) -> str:
        expanded_cosmic_map = self.cosmic_expansion()
        result = self.all_pair_min_distance(expanded_cosmic_map)
        return str(result)

    def part_two(self) -> str:
        very_expanded_cosmic_map = self.cosmic_expansion(
            expansion_coefficient=1_000_000
        )
        result = self.all_pair_min_distance(very_expanded_cosmic_map)
        return str(result)


def main():
    Day11CosmicExpansion().run()


if __name__ == "__main__":
    main()
