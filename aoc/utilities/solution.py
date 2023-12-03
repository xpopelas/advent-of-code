import time
from typing import Callable, Any


class AdventOfCodeSolution:
    """Base class for the Advent of Code solutions.

    Attributes:
        name (str | None): The name of the solution
            used for logging as a prefix, if None, no prefix is used.
        input_file (str): The input file to read from - your puzzle input.
        lines (list[str]): The lines of the input file - each line is stripped of whitespace.
    """

    def __init__(self, name: str | None = None, input_file: str = "input.txt"):
        self.name: str | None = name
        self.input_file: str = input_file
        self.lines: list[str] = self.__load_lines()

    def __load_lines(self) -> list[str]:
        with open(self.input_file, "r", encoding="UTF-8") as file:
            return [line.strip() for line in file.readlines()]

    def parse(self) -> None:
        """Method used for parsing the lines into a more usable format.

        :return: Nothing
        """
        raise NotImplementedError

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

    def _log_run(
        self, prefix: str, perf_time: float, solution_result: str | None = None
    ):
        """Logs the run of the solution.

        :param prefix: Prefix of the part being logged
        :param perf_time: The performance time of the solution
        :param solution_result: The solution of the solution
        :return:
        """
        if self.name:
            print(f"{self.name} - ", end="")
        print(f"{prefix}: {perf_time:.6f} seconds", end="")
        if solution_result is not None:
            print(f" - Solution: {solution_result}", end="")
        print()

    @staticmethod
    def _timed_run(function: Callable[[], Any]) -> tuple[float, Any]:
        """Runs the given function and logs the time taken.

        :param function: The function to run
        :return: The time of the run and the result of the function
        """
        start_time = time.perf_counter()
        solution_result = function()
        end_time = time.perf_counter()
        perf_time = end_time - start_time
        return perf_time, solution_result

    def run(self) -> None:
        """
        Runs the solution and logs the results.

        :return: Nothing
        """

        try:
            perf_time, _ = self._timed_run(self.parse)
            self._log_run("Parser", perf_time)
        except NotImplementedError:
            print("Parser not used")

        try:
            perf_time, solution_result = self._timed_run(self.part_one)
            self._log_run("Part 1", perf_time, solution_result)
        except NotImplementedError:
            print("Part 1 not implemented")

        try:
            perf_time, solution_result = self._timed_run(self.part_two)
            self._log_run("Part 2", perf_time, solution_result)
        except NotImplementedError:
            print("Part 2 not implemented")
