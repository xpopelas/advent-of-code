from typing import Final

from sol.utils import AdventOfCodeSolution


class Trebuchet(AdventOfCodeSolution):
    WORDS: Final[dict[str, int]] = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    def __init__(self):
        super().__init__(name="Day 1: Trebuchet?!")

    @classmethod
    def get_first_digit(
        cls,
        line: str,
        use_words: bool = False,
    ) -> int | None:
        for index, char in enumerate(line):
            if char.isdigit():
                return int(char)
            if use_words:
                for word, digit in cls.WORDS.items():
                    if line[index:].startswith(word):
                        return digit
        return None

    @classmethod
    def get_last_digit(
        cls,
        line: str,
        use_words: bool = False,
    ) -> int:
        for index in reversed(range(len(line))):
            if (
                digit := cls.get_first_digit(line[index:], use_words=use_words)
            ) is not None:
                return digit
        raise ValueError("No digit found")

    def part_one(self) -> str:
        result = 0
        for line in self.lines:
            first_digit = self.get_first_digit(line, use_words=False)
            assert first_digit is not None
            last_digit = self.get_last_digit(line, use_words=False)
            result += 10 * first_digit + last_digit
        return str(result)

    def part_two(self) -> str:
        result = 0
        for line in self.lines:
            first_digit = self.get_first_digit(line, use_words=True)
            assert first_digit is not None
            last_digit = self.get_last_digit(line, use_words=True)
            result += 10 * first_digit + last_digit
        return str(result)


def main():
    solution = Trebuchet()
    solution.run()


if __name__ == "__main__":
    main()
