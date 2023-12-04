import dataclasses

from aoc.utilities.solution import AdventOfCodeSolution


@dataclasses.dataclass
class ScratchCard:
    card_number: int
    winning_numbers: list[int]
    scratch_numbers: list[int]

    @staticmethod
    def from_line(line: str) -> "ScratchCard":
        card_number, numbers = line.split(": ")
        final_card_number = int(card_number[len("Card ") :])
        winning_numbers, scratch_numbers = numbers.split("|")
        final_winning_numbers = [
            int(number) for number in winning_numbers.split(" ") if number
        ]
        final_scratch_numbers = [
            int(number) for number in scratch_numbers.split(" ") if number
        ]
        return ScratchCard(
            final_card_number, final_winning_numbers, final_scratch_numbers
        )

    @property
    def overlapping_numbers_count(self) -> int:
        return len(set(self.winning_numbers).intersection(set(self.scratch_numbers)))

    @property
    def points(self) -> int:
        if self.overlapping_numbers_count == 0:
            return 0

        final_points = 2 ** (self.overlapping_numbers_count - 1)
        return final_points

    def __iter__(self):
        return iter(
            range(
                self.card_number + 1,
                self.card_number + 1 + self.overlapping_numbers_count,
            )
        )


class Day04Scratchcards(AdventOfCodeSolution):
    def __init__(self):
        self.cards: dict[int, ScratchCard] = {}
        super().__init__(name="Day 4: Scratchcards")

    def parse(self) -> None:
        for line in self.lines:
            card = ScratchCard.from_line(line)
            self.cards[card.card_number] = card

    def part_one(self) -> str:
        result = 0
        for card in self.cards.values():
            result += card.points
        return str(result)

    def part_two(self) -> str:
        copies = {card.card_number: 1 for card in self.cards.values()}
        for card_number, number_of_copies in copies.items():
            card = self.cards[card_number]
            for new_card_number in card:
                if new_card_number in copies:
                    copies[new_card_number] += number_of_copies
        return str(sum(copies.values()))


def main():
    Day04Scratchcards().run()


if __name__ == "__main__":
    main()
