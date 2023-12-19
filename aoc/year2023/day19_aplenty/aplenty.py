import dataclasses

from aoc.utilities.solution import AdventOfCodeSolution


@dataclasses.dataclass(frozen=True)
class Part:
    x: tuple[int, int]
    m: tuple[int, int]
    a: tuple[int, int]
    s: tuple[int, int]
    target: str = "in"

    def change(
        self,
        x: tuple[int, int] | None = None,
        m: tuple[int, int] | None = None,
        a: tuple[int, int] | None = None,
        s: tuple[int, int] | None = None,
        target: str | None = None,
    ) -> "Part":
        return Part(
            x=x if x is not None else self.x,
            m=m if m is not None else self.m,
            a=a if a is not None else self.a,
            s=s if s is not None else self.s,
            target=target if target is not None else self.target,
        )

    def change_by_key(self, key: str, value: tuple[int, int]) -> "Part":
        match key:
            case "x":
                return self.change(x=value)
            case "m":
                return self.change(m=value)
            case "a":
                return self.change(a=value)
            case "s":
                return self.change(s=value)
            case _:
                raise ValueError(f"Invalid key {key}")

    def __getitem__(self, item: str) -> tuple[int, int]:
        return getattr(self, item)

    @property
    def sum(self) -> int:
        return self.x[0] + self.m[0] + self.a[0] + self.s[0]

    @property
    def combinations_count(self) -> int:
        return (
            (self.x[1] - self.x[0] + 1)
            * (self.m[1] - self.m[0] + 1)
            * (self.a[1] - self.a[0] + 1)
            * (self.s[1] - self.s[0] + 1)
        )


@dataclasses.dataclass
class Rule:
    key: str
    operation: str
    value: int
    target: str

    @staticmethod
    def from_string(string: str) -> "Rule":
        condition, target = string.split(":")

        if ">" in condition:
            key, value = condition.split(">")
            return Rule(key, ">", int(value), target)

        if "<" in condition:
            key, value = condition.split("<")
            return Rule(key, "<", int(value), target)

        raise ValueError

    def is_satisfied(self, values: Part) -> bool:
        match self.operation:
            case ">":
                return values[self.key][0] > self.value
            case "<":
                return values[self.key][0] < self.value
            case _:
                raise ValueError

    def split_part(self, part: Part) -> list[Part]:
        lower_bound, upper_bound = part[self.key]
        if not lower_bound <= self.value <= upper_bound:
            if (self.operation == "<" and upper_bound < self.value) or (
                self.operation == ">" and lower_bound > self.value
            ):
                return [part.change(target=self.target)]
            return [part]

        outwards_part = part.change(target=self.target)
        inwards_part = part.change()

        match self.operation:
            case ">":
                outwards_part = outwards_part.change_by_key(
                    self.key, (self.value + 1, upper_bound)
                )
                inwards_part = inwards_part.change_by_key(
                    self.key, (lower_bound, self.value)
                )
            case "<":
                outwards_part = outwards_part.change_by_key(
                    self.key, (lower_bound, self.value - 1)
                )
                inwards_part = inwards_part.change_by_key(
                    self.key, (self.value, upper_bound)
                )
            case _:
                raise ValueError(f"Invalid operation {self.operation}")

        return [outwards_part, inwards_part]


@dataclasses.dataclass
class Workflow:
    name: str
    rules: list[Rule]
    fallback: str

    @staticmethod
    def from_line(line: str) -> "Workflow":
        name, rules_string = line.split("{")
        rules = rules_string[:-1].split(",")
        options = []
        fallback = rules[-1]
        for rule in rules[:-1]:
            options.append(Rule.from_string(rule))
        return Workflow(name, options, fallback)

    def next_target(self, values: Part) -> str:
        for option in self.rules:
            if option.is_satisfied(values):
                return option.target

        return self.fallback

    def split_part(self, part: Part) -> list[Part]:
        to_process = [part]
        result = []

        for option in self.rules:
            split_parts = []
            for process_part in to_process:
                split_parts.extend(option.split_part(process_part))

            result.extend([p for p in split_parts if p.target != self.name])
            to_process = [p for p in split_parts if p.target == self.name]

        for fallback_part in to_process:
            result.append(fallback_part.change(target=self.fallback))

        return result


class Day19Aplenty(AdventOfCodeSolution):
    def __init__(self, content: str | None = None):
        self.workflows: dict[str, Workflow] = {}
        self.parts: list[Part] = []
        super().__init__(name="Day 19: Aplenty", content=content)

    @staticmethod
    def _parse_values(line) -> Part:
        values = {}
        for value in line[1:-1].split(","):
            key, value = value.split("=")
            values[key] = int(value), int(value)
        return Part(x=values["x"], m=values["m"], a=values["a"], s=values["s"])

    def parse(self) -> None:
        parsing_workflows = True
        for line in self.lines:
            if line == "":
                parsing_workflows = False
                continue

            if parsing_workflows:
                rule = Workflow.from_line(line)
                self.workflows[rule.name] = rule
            else:
                self.parts.append(self._parse_values(line))

    def part_one(self) -> str:
        result = 0

        for part in self.parts:
            current_target = part.target

            while current_target not in ["R", "A"]:
                current_target = self.workflows[current_target].next_target(part)

            if current_target == "A":
                result += part.sum

        return str(result)

    def part_two(self) -> str:
        parts = [Part(x=(1, 4000), m=(1, 4000), a=(1, 4000), s=(1, 4000))]
        accepting_values = []

        while parts:
            current_parts = [*parts]
            parts = []

            for part in current_parts:
                split_parts = self.workflows[part.target].split_part(part)

                accepting_values.extend([p for p in split_parts if p.target == "A"])
                parts.extend([p for p in split_parts if p.target not in ["A", "R"]])

        result = 0
        for part in accepting_values:
            result += part.combinations_count

        return str(result)


def main():
    Day19Aplenty().run()


if __name__ == "__main__":
    main()
