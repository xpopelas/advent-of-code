import time


class AdventOfCodeSolution:
    """Base class for the Advent of Code solutions.

    Attributes:
        name (str | None): The name of the solution - used for logging as a prefix, if None, no prefix is used.
        input_file (str): The input file to read from - your puzzle input.
        lines (list[str]): The lines of the input file - each line is stripped of whitespace.
    """

    def __init__(self, name: str | None = None, input_file: str = "input.txt"):
        self.name: str | None = name
        self.input_file: str = input_file
        self.lines: list[str] = self.__load_lines()

    def __load_lines(self) -> list[str]:
        with open(self.input_file, "r") as file:
            return [line.strip() for line in file.readlines()]

    def part_one(self) -> str:
        """Method used for overriding the first part of the solution.

        :return: Solution for the first part of the puzzle.
        """
        raise NotImplementedError

    def part_two(self) -> str:
        """Method used for overriding the second part of the solution.

        :return: Solution for the second part of the puzzle.
        """
        raise NotImplementedError

    def _log_run(self, part: int, perf_time: float, solution_result: str):
        """Logs the run of the solution.

        :param part: Which part of the solution is being logged
        :param perf_time: The performance time of the solution
        :param solution_result: The solution of the solution
        :return:
        """
        if self.name:
            print(f"{self.name} - ", end="")
        print(f"Part {part}: {perf_time:.6f} seconds - Solution: {solution_result}")

    def run(self) -> None:
        """
        Runs the solution and logs the results.

        :return: Nothing
        """
        try:
            start_time = time.perf_counter()
            solution_result = self.part_one()
            end_time = time.perf_counter()
            perf_time = end_time - start_time
            self._log_run(1, perf_time, solution_result)
        except NotImplementedError:
            print("Part one not implemented")

        try:
            start_time = time.perf_counter()
            solution_result = self.part_two()
            end_time = time.perf_counter()
            perf_time = end_time - start_time
            self._log_run(2, perf_time, solution_result)
        except NotImplementedError:
            print("Part two not implemented")
