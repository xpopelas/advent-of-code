from collections import defaultdict

from matplotlib.path import Path

from aoc.utilities.solution import AdventOfCodeSolution


Coordinate = tuple[int, int]


class Day10PipeMaze(AdventOfCodeSolution):
    def __init__(self, content: str | None = None):
        self.graph: dict[Coordinate, list[Coordinate]] = defaultdict(list)
        self.start: Coordinate = (0, 0)
        super().__init__(name="Day 10: Pipe Maze", content=content)

    def parse(self) -> None:
        for y, line in enumerate(self.lines):
            for x, char in enumerate(line):
                match char:
                    case "|":
                        self.graph[(x, y)].append((x, y - 1))
                        self.graph[(x, y)].append((x, y + 1))
                    case "-":
                        self.graph[(x, y)].append((x - 1, y))
                        self.graph[(x, y)].append((x + 1, y))
                    case "L":
                        self.graph[(x, y)].append((x + 1, y))
                        self.graph[(x, y)].append((x, y - 1))
                    case "J":
                        self.graph[(x, y)].append((x - 1, y))
                        self.graph[(x, y)].append((x, y - 1))
                    case "7":
                        self.graph[(x, y)].append((x - 1, y))
                        self.graph[(x, y)].append((x, y + 1))
                    case "F":
                        self.graph[(x, y)].append((x + 1, y))
                        self.graph[(x, y)].append((x, y + 1))
                    case ".":
                        continue
                    case "S":
                        self.start = (x, y)
        start_x, start_y = self.start
        if self.lines[start_y][start_x + 1] in ("-", "J", "7"):
            self.graph[self.start].append((start_x + 1, start_y))
        if self.lines[start_y][start_x - 1] in ("-", "L", "F"):
            self.graph[self.start].append((start_x - 1, start_y))
        if self.lines[start_y + 1][start_x] in ("|", "7", "F"):
            self.graph[self.start].append((start_x, start_y + 1))
        if self.lines[start_y - 1][start_x] in ("|", "J", "L"):
            self.graph[self.start].append((start_x, start_y - 1))

    def get_loop_coordinates(self) -> list[Coordinate]:
        result: list[Coordinate] = [self.start, self.graph[self.start][0]]
        visited_set = set(result)
        current_queue: list[Coordinate] = [self.graph[self.start][0]]
        while current_queue:
            coordinate = current_queue.pop()
            for next_coordinate in self.graph[coordinate]:
                if next_coordinate in visited_set:
                    continue
                result.append(next_coordinate)
                visited_set.add(next_coordinate)
                current_queue.append(next_coordinate)
        return result

    def part_one(self) -> str:
        loop_coordinates = self.get_loop_coordinates()
        return str(len(loop_coordinates) // 2)

    def part_two(self) -> str:
        loop_coordinates = self.get_loop_coordinates()
        result = 0

        min_x = min(x for x, _ in loop_coordinates)
        max_x = max(x for x, _ in loop_coordinates)
        min_y = min(y for _, y in loop_coordinates)
        max_y = max(y for _, y in loop_coordinates)

        polygon = Path(loop_coordinates)
        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                if (x, y) in loop_coordinates:
                    continue
                if polygon.contains_point((x, y)):
                    result += 1

        return str(result)


def main():
    Day10PipeMaze().run()


if __name__ == "__main__":
    main()
