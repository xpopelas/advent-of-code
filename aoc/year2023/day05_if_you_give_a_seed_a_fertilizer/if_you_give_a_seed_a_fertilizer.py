from aoc.utilities.solution import AdventOfCodeSolution


class SourceToTargetInstruction:
    def __init__(self, line: str):
        target, source, source_range = line.split(" ")
        self.target = int(target)
        self.source = int(source)
        self.range = int(source_range)

    @property
    def end(self) -> int:
        return self.source + self.range

    @property
    def move(self) -> int:
        return self.target - self.source

    def calculate_target(self, value: int) -> int | None:
        if value < self.source:
            return None

        if value >= self.source + self.range:
            return None

        return value - self.source + self.target


class SourceToTargetMap:
    def __init__(self, lines: list[str]):
        self.name = lines[0][: -len(" map:")]
        self.instructions = []
        for line in lines[1:]:
            self.instructions.append(SourceToTargetInstruction(line))

    def calculate_target(self, value: int) -> int:
        for instruction in self.instructions:
            target = instruction.calculate_target(value)
            if target is not None:
                return target

        return value

    def calculate_ranges(self, ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
        intersecting_ranges = []
        for instruction in self.instructions:
            new_ranges = []

            for start, end in ranges:
                before = (start, min(end, instruction.source))
                intersect = (max(start, instruction.source), min(end, instruction.end))
                after = (max(start, instruction.end), end)
                if before[0] < before[1]:
                    new_ranges.append(before)
                if intersect[0] < intersect[1]:
                    intersecting_ranges.append(
                        (
                            intersect[0] + instruction.move,
                            intersect[1] + instruction.move,
                        )
                    )
                if after[0] < after[1]:
                    new_ranges.append(after)

            ranges = new_ranges
        return intersecting_ranges + ranges


class Day05IfYouGiveASeedAFertilizer(AdventOfCodeSolution):
    def __init__(self, content: str | None = None):
        self.seeds: list[int] = []
        self.seed_ranges: list[tuple[int, int]] = []
        self.maps: list[SourceToTargetMap] = []
        super().__init__(name="Day 5: If You Give A Seed A Fertilizer", content=content)

    def _parse_seeds(self, line: str) -> None:
        self.seeds = [int(seed) for seed in line[len("seeds: ") :].split(" ")]
        self.seed_ranges = [
            (seed_from, seed_from + seed_range)
            for seed_from, seed_range in zip(self.seeds[::2], self.seeds[1::2])
        ]

    def parse(self) -> None:
        self._parse_seeds(self.lines[0])
        current_lines = []
        for line in self.lines[2:]:
            if line:
                current_lines.append(line)
            elif current_lines:
                self.maps.append(SourceToTargetMap(current_lines))
                current_lines = []

        if current_lines:
            self.maps.append(SourceToTargetMap(current_lines))

    def _calculate_position(self, seed: int) -> int:
        for source_to_target_map in self.maps:
            seed = source_to_target_map.calculate_target(seed)

        return seed

    def part_one(self) -> str:
        result = min(self._calculate_position(seed) for seed in self.seeds)
        return str(result)

    def part_two(self) -> str:
        result = []
        for seed_from, seed_to in self.seed_ranges:
            ranges = [(seed_from, seed_to)]
            for source_to_target_map in self.maps:
                ranges = source_to_target_map.calculate_ranges(ranges)
            result.append(min(ranges)[0])
        return str(min(result))


def main():
    Day05IfYouGiveASeedAFertilizer().run()


if __name__ == "__main__":
    main()
