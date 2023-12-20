import dataclasses
import enum
import math
from collections import defaultdict

from aoc.utilities.solution import AdventOfCodeSolution


class PulseType(enum.StrEnum):
    HIGH = enum.auto()
    LOW = enum.auto()


@dataclasses.dataclass(frozen=True)
class Pulse:
    source: str
    target: str
    type: PulseType


@dataclasses.dataclass
class Module:
    name: str
    targets: list[str]
    source_modules: set[str] = dataclasses.field(default_factory=set)

    def reset(self) -> None:
        pass

    @staticmethod
    def from_line(line: str) -> "Module":
        name, target = line.split(" -> ")
        first_letter = line[0]
        targets = target.split(", ")
        match first_letter:
            case "%":
                return FlipFlopModule(name=name[1:], targets=targets)
            case "&":
                return ConjunctionModule(name=name[1:], targets=targets)
            case _:
                return BroadcasterModule(name=name, targets=targets)

    def receive_pulse(self, pulse: Pulse) -> list[Pulse]:
        raise NotImplementedError


@dataclasses.dataclass
class FlipFlopModule(Module):
    is_enabled: bool = False

    def reset(self) -> None:
        self.is_enabled = False

    @property
    def sending_pulse(self):
        if self.is_enabled:
            return PulseType.HIGH
        return PulseType.LOW

    def receive_pulse(self, pulse: Pulse) -> list[Pulse]:
        if pulse.type == PulseType.HIGH:
            return []

        self.is_enabled = not self.is_enabled
        return [
            Pulse(source=self.name, target=target, type=self.sending_pulse)
            for target in self.targets
        ]


@dataclasses.dataclass
class ConjunctionModule(Module):
    _received_pulses_from_source: dict[str, PulseType] = dataclasses.field(
        default_factory=lambda: defaultdict(lambda: PulseType.LOW)
    )

    def reset(self) -> None:
        self._received_pulses_from_source = defaultdict(lambda: PulseType.LOW)

    @property
    def sending_pulse(self):
        if all(
            self._received_pulses_from_source[source_module] == PulseType.HIGH
            for source_module in self.source_modules
        ):
            return PulseType.LOW
        return PulseType.HIGH

    def receive_pulse(self, pulse: Pulse) -> list[Pulse]:
        self._received_pulses_from_source[pulse.source] = pulse.type

        return [
            Pulse(source=self.name, target=target, type=self.sending_pulse)
            for target in self.targets
        ]


@dataclasses.dataclass
class BroadcasterModule(Module):
    def receive_pulse(self, pulse: Pulse) -> list[Pulse]:
        return [
            Pulse(source=self.name, target=target, type=pulse.type)
            for target in self.targets
        ]


class Day20PulsePropagation(AdventOfCodeSolution):
    def __init__(self, content: str | None = None):
        self.modules: dict[str, Module] = {}
        super().__init__(name="Day 20: Pulse Propagation", content=content)

    def parse(self) -> None:
        for line in self.lines:
            module = Module.from_line(line)
            self.modules[module.name] = module

        for module_source, module in self.modules.items():
            module.source_modules = {
                input_module.name
                for input_module in self.modules.values()
                if module_source in input_module.targets
            }

    def reset_all(self) -> None:
        for module in self.modules.values():
            module.reset()

    def press_button(self) -> dict[PulseType, list[Pulse]]:
        pulses = [Pulse(source="button", target="broadcaster", type=PulseType.LOW)]
        seen_pulses: dict[PulseType, list[Pulse]] = defaultdict(list)
        for pulse in pulses:
            seen_pulses[pulse.type].append(pulse)

            if pulse.target not in self.modules:
                continue

            pulses.extend(self.modules[pulse.target].receive_pulse(pulse))
        return seen_pulses

    def part_one(self) -> str:
        self.reset_all()

        high_pulses = 0
        low_pulses = 0

        for _ in range(1000):
            seen_pulses = self.press_button()
            high_pulses += len(seen_pulses[PulseType.HIGH])
            low_pulses += len(seen_pulses[PulseType.LOW])

        return str(low_pulses * high_pulses)

    def part_two(self) -> str:
        self.reset_all()

        conjunction = next(m for m in self.modules.values() if "rx" in m.targets)
        conjunction_high_pulses: dict[str, int] = {}
        button_presses = 0

        while not all(
            source in conjunction_high_pulses for source in conjunction.source_modules
        ):
            seen_pulses = self.press_button()
            button_presses += 1
            for pulse in [
                seen_pulse
                for seen_pulse in seen_pulses[PulseType.HIGH]
                if seen_pulse.target == conjunction.name
            ]:
                if pulse.source not in conjunction_high_pulses:
                    conjunction_high_pulses[pulse.source] = button_presses

        return str(math.lcm(*conjunction_high_pulses.values()))


def main():
    Day20PulsePropagation().run()


if __name__ == "__main__":
    main()
