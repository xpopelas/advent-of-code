import dataclasses
import enum
from collections import Counter
from functools import cache

from aoc.utilities.solution import AdventOfCodeSolution


@cache
def get_value_card(card: str) -> int:
    match card:
        case "T":
            return 10
        case "J":
            return 11
        case "Q":
            return 12
        case "K":
            return 13
        case "A":
            return 14
        case _:
            return int(card)


class CardsType(enum.IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIRS = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


@dataclasses.dataclass
class CardPlay:
    cards: str
    bid: int

    @staticmethod
    def _get_cards_type(cards: str) -> CardsType:
        jokerless_counter = Counter(card for card in cards if card != "1")
        joker_cards_count = Counter(cards).get("1", 0)

        if 5 in jokerless_counter.values():
            return CardsType.FIVE_OF_A_KIND

        if 4 in jokerless_counter.values():
            if joker_cards_count >= 1:
                return CardsType.FIVE_OF_A_KIND
            return CardsType.FOUR_OF_A_KIND

        if 3 in jokerless_counter.values():
            if joker_cards_count >= 2:
                return CardsType.FIVE_OF_A_KIND
            if joker_cards_count >= 1:
                return CardsType.FOUR_OF_A_KIND
            if 2 in jokerless_counter.values():
                return CardsType.FULL_HOUSE
            return CardsType.THREE_OF_A_KIND

        if 2 in jokerless_counter.values():
            if joker_cards_count >= 3:
                return CardsType.FIVE_OF_A_KIND
            if joker_cards_count >= 2:
                return CardsType.FOUR_OF_A_KIND
            if joker_cards_count >= 1:
                if Counter(jokerless_counter.values()).get(2, 0) == 2:
                    return CardsType.FULL_HOUSE
                return CardsType.THREE_OF_A_KIND
            if Counter(jokerless_counter.values()).get(2, 0) == 2:
                return CardsType.TWO_PAIRS
            return CardsType.ONE_PAIR

        if 1 in jokerless_counter.values():
            if joker_cards_count >= 4:
                return CardsType.FIVE_OF_A_KIND
            if joker_cards_count >= 3:
                return CardsType.FOUR_OF_A_KIND
            if joker_cards_count >= 2:
                return CardsType.THREE_OF_A_KIND
            if joker_cards_count >= 1:
                return CardsType.ONE_PAIR

        if joker_cards_count >= 5:
            return CardsType.FIVE_OF_A_KIND
        if joker_cards_count >= 4:
            return CardsType.FOUR_OF_A_KIND
        if joker_cards_count >= 3:
            return CardsType.THREE_OF_A_KIND
        if joker_cards_count >= 2:
            return CardsType.ONE_PAIR

        return CardsType.HIGH_CARD

    @staticmethod
    def _card_score(cards: str):
        result = CardPlay._get_cards_type(cards) * 0x100000
        for index, card in enumerate(reversed(cards)):
            result += get_value_card(card) * 0x10**index
        return result

    @property
    def joker_card_score(self) -> int:
        cards = "".join(card if card != "J" else "1" for card in self.cards)
        return self._card_score(cards)

    @property
    def card_score(self) -> int:
        return self._card_score(self.cards)


class Day07CamelCards(AdventOfCodeSolution):
    def __init__(self, content: str | None = None):
        self.card_plays: list[CardPlay] = []
        super().__init__(name="Day 7: Camel Cards", content=content)

    def parse(self) -> None:
        for line in self.lines:
            cards, bid = line.split(" ")
            self.card_plays.append(CardPlay(cards=cards, bid=int(bid)))

    def part_one(self) -> str:
        result = 0
        for rank, card_play in enumerate(
            sorted(self.card_plays, key=lambda x: x.card_score), start=1
        ):
            result += rank * card_play.bid
        return str(result)

    def part_two(self) -> str:
        result = 0
        for rank, card_play in enumerate(
            sorted(self.card_plays, key=lambda x: x.joker_card_score), start=1
        ):
            result += rank * card_play.bid
        return str(result)


def main():
    Day07CamelCards().run()


if __name__ == "__main__":
    main()
