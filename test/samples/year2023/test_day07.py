from aoc.year2023.day07_camel_cards.camel_cards import Day07CamelCards

SAMPLE_INPUT = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def test_part_one_sample():
    solution = Day07CamelCards(content=SAMPLE_INPUT)
    solution.parse()
    assert solution.part_one() == "6440"


def test_part_two_sample():
    solution = Day07CamelCards(content=SAMPLE_INPUT)
    solution.parse()
    assert solution.part_two() == "5905"
