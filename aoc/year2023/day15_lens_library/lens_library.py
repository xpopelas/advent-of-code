import dataclasses
from collections import defaultdict

from aoc.utilities.solution import AdventOfCodeSolution


@dataclasses.dataclass
class Box:
    text: str

    def __post_init__(self):
        self.subtracting = "-" in self.text
        self.prefix = "".join(char for char in self.text if char.isalpha())
        self.value = None
        if not self.subtracting:
            self.value = int(self.text.split("=")[1])

    @staticmethod
    def _hash(text: str) -> int:
        current_value = 0
        for char in text:
            current_value = ((current_value + ord(char)) * 17) % 256
        return current_value

    @property
    def text_hash(self) -> int:
        return self._hash(self.text)

    @property
    def prefix_hash(self) -> int:
        return self._hash(self.prefix)


@dataclasses.dataclass
class BoxSet:
    boxes: dict[int, list[Box]] = dataclasses.field(
        default_factory=lambda: defaultdict(list)
    )

    def add(self, box: Box) -> None:
        prefix_hash = box.prefix_hash
        for index, list_box in enumerate(self.boxes[prefix_hash]):
            if list_box.prefix == box.prefix:
                self.boxes[prefix_hash][index] = box
                return
        self.boxes[prefix_hash].append(box)

    def remove(self, box: Box) -> None:
        prefix_hash = box.prefix_hash
        for index, list_box in enumerate(self.boxes[prefix_hash]):
            if list_box.prefix == box.prefix:
                self.boxes[prefix_hash].pop(index)
                return

    @property
    def focusing_power(self) -> int:
        result = 0
        for box_number, box_list in self.boxes.items():
            for index, box in enumerate(box_list, start=1):
                assert box.value is not None
                result += (box_number + 1) * index * box.value
        return result


class Day15LensLibrary(AdventOfCodeSolution):
    def __init__(self):
        self.values: list[Box] = []
        super().__init__(name="Day 15: Lens Library")

    def parse(self) -> None:
        for box_text in self.lines[0].split(","):
            self.values.append(Box(box_text))

    def part_one(self) -> str:
        return str(sum(value.text_hash for value in self.values))

    def part_two(self) -> str:
        box_set = BoxSet()
        for value in self.values:
            if value.subtracting:
                box_set.remove(value)
            else:
                box_set.add(value)
        return str(box_set.focusing_power)


def main():
    Day15LensLibrary().run()


if __name__ == "__main__":
    main()
