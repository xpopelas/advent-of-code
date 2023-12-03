import dataclasses
import os.path
from pathlib import Path


@dataclasses.dataclass
class AdventOfCodeBuilder:
    day_name: str
    year: int

    @property
    def day(self) -> int:
        return int(self.day_name.split(": ")[0].split(" ")[1])

    @property
    def task_name(self) -> str:
        return "".join(
            letter
            for letter in self.day_name.split(": ")[1].strip()
            if letter.isalnum() or letter == " "
        )

    @property
    def class_name(self) -> str:
        camel_case_name = "".join(
            word.capitalize() for word in self.task_name.split(" ")
        )
        return f"Day{self.day:02d}{camel_case_name}"

    @property
    def snake_case_task_name(self) -> str:
        return f"{self.task_name.replace(' ', '_').lower()}"

    @property
    def folder_path(self) -> str:
        return f"../year{self.year}/day{self.day:02d}_{self.snake_case_task_name}"

    @property
    def file_name(self) -> str:
        return f"{self.snake_case_task_name}.py"

    @property
    def class_content(self) -> str:
        content = "from aoc.utilities.solution import AdventOfCodeSolution\n"
        content += "\n\n"
        content += f"class {self.class_name}(AdventOfCodeSolution):\n"
        content += "    def __init__(self):\n"
        content += (
            "        # If you need any additional variables, you can set them here\n"
        )
        content += f'        super().__init__(name="{self.day_name}")\n'
        content += "\n"
        content += "    def parse(self) -> None:\n"
        content += "        # If you need to parse the input, you can do it here\n"
        content += "        pass\n"
        content += "\n"
        content += "    def part_one(self) -> str:\n"
        content += "        raise NotImplementedError\n"
        content += "\n"
        content += "    def part_two(self) -> str:\n"
        content += "        raise NotImplementedError\n"
        content += "\n\n"
        content += "def main():\n"
        content += f"    {self.class_name}().run()\n"
        content += "\n\n"
        content += 'if __name__ == "__main__":\n'
        content += "    main()\n"
        return content


def write_to_file(builder: AdventOfCodeBuilder) -> None:
    path = Path(builder.folder_path)
    current_path = ""
    for part in path.parts:
        current_path += part
        if not os.path.exists(current_path):
            os.mkdir(current_path)
            if not os.path.exists(current_path + "/__init__.py"):
                with open(current_path + "/__init__.py", "w", encoding="UTF-8") as file:
                    file.write("\n")
        current_path += "/"

    if os.path.exists(current_path + builder.file_name):
        print("File already exists - either erase it, or change the name of the class")
        return

    with open(current_path + builder.file_name, "w", encoding="UTF-8") as file:
        file.write(builder.class_content)

    print(f"Created {current_path + builder.file_name}")


def main():
    print(
        "Hey, I'm going to prepare a class for you!, please add the following details:"
    )
    year = int(input("Year: "))
    day_name = input("Day name: ")
    builder = AdventOfCodeBuilder(day_name, year)
    print(
        f"Alright, I've generated a class {builder.class_name} for you in {builder.folder_path}/{builder.file_name}"
    )
    print(
        "Please check everything is correct and if so, press enter to continue, otherwise type anything and press enter"
    )
    if input():
        print("Exiting...")
        return
    write_to_file(builder)
    print("Done!")


if __name__ == "__main__":
    main()
