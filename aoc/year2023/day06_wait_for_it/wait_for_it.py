import dataclasses

from aoc.utilities.solution import AdventOfCodeSolution


@dataclasses.dataclass
class Race:
    time: int
    distance: int

    @property
    def minimum_holding_time(self) -> int:
        for speed in range(1, self.time):
            travelled_distance = speed * (self.time - speed)
            if travelled_distance > self.distance:
                return speed
        raise ValueError("No minimum holding time found")

    @property
    def count_of_variations_to_beat_the_race(self) -> int:
        return self.time + 1 - 2 * self.minimum_holding_time


class Day06WaitForIt(AdventOfCodeSolution):
    def __init__(self):
        self.races: list[Race] = []
        self.final_race: Race = Race(0, 0)
        super().__init__(name="Day 6: Wait For It")

    def parse(self) -> None:
        times = [int(time) for time in self.lines[0].split(" ")[1:] if time]
        distances = [
            int(distance) for distance in self.lines[1].split(" ")[1:] if distance
        ]
        for time, distance in zip(times, distances):
            self.races.append(Race(time=time, distance=distance))

        final_race_time = int("".join(char for char in self.lines[0] if char.isdigit()))
        final_race_distance = int(
            "".join(char for char in self.lines[1] if char.isdigit())
        )
        self.final_race = Race(time=final_race_time, distance=final_race_distance)

    def part_one(self) -> str:
        result = 1
        for race in self.races:
            result *= race.count_of_variations_to_beat_the_race
        return str(result)

    def part_two(self) -> str:
        return str(self.final_race.count_of_variations_to_beat_the_race)


def main():
    Day06WaitForIt().run()


if __name__ == "__main__":
    main()
