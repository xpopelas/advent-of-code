import dataclasses

from sol.utils import AdventOfCodeSolution


@dataclasses.dataclass
class CubeSet:
    red_count: int = 0
    blue_count: int = 0
    green_count: int = 0

    def __str__(self) -> str:
        return (
            f"Red: {self.red_count}, Blue: {self.blue_count}, Green: {self.green_count}"
        )

    @property
    def power(self) -> int:
        return self.red_count * self.blue_count * self.green_count


@dataclasses.dataclass
class GameResult:
    game_id: int
    cube_sets: list[CubeSet]

    def __str__(self) -> str:
        return f"Game {self.game_id}: {self.cube_sets}"

    def is_possible_with(self, target_cube_set: CubeSet) -> bool:
        return all(
            cube_set.red_count <= target_cube_set.red_count
            and cube_set.blue_count <= target_cube_set.blue_count
            and cube_set.green_count <= target_cube_set.green_count
            for cube_set in self.cube_sets
        )

    @property
    def lowest_needed_cubeset(self) -> CubeSet:
        return CubeSet(
            red_count=max(cube_set.red_count for cube_set in self.cube_sets),
            blue_count=max(cube_set.blue_count for cube_set in self.cube_sets),
            green_count=max(cube_set.green_count for cube_set in self.cube_sets),
        )


class CubeConundrum(AdventOfCodeSolution):
    def __init__(self):
        super().__init__(name="Day 2: Cube Conundrum")
        self.game_results: dict[int, GameResult] = {}
        self._load_game_results()

    def _load_game_results(self) -> None:
        for line in self.lines:
            game_line, cube_sets_line = line.split(": ")
            game_id = int(game_line[len("Game ") :])
            self.game_results[game_id] = GameResult(game_id, [])
            for cube_set_line in cube_sets_line.split("; "):
                cube_set = CubeSet()
                for cube_line in cube_set_line.split(", "):
                    match cube_line.split(" "):
                        case [count, "red"]:
                            cube_set.red_count = int(count)
                        case [count, "blue"]:
                            cube_set.blue_count = int(count)
                        case [count, "green"]:
                            cube_set.green_count = int(count)
                        case _:
                            raise ValueError(
                                f"Invalid cube line: {cube_line} on line {line}"
                            )
                self.game_results[game_id].cube_sets.append(cube_set)

    def part_one(self) -> str:
        result = 0
        target_cube_set = CubeSet(red_count=12, green_count=13, blue_count=14)
        for game_id, game_result in self.game_results.items():
            if game_result.is_possible_with(target_cube_set):
                result += game_id
        return str(result)

    def part_two(self) -> str:
        result = 0
        for game_result in self.game_results.values():
            result += game_result.lowest_needed_cubeset.power
        return str(result)


def main():
    CubeConundrum().run()


if __name__ == "__main__":
    main()
