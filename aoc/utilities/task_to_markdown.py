import markdownify
import pyperclip


class AdventOfCodeHtmlToMarkdown:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.content: str = ""
        self._load_content()

    def _load_content(self) -> None:
        with open(self.file_path, "r", encoding="UTF-8") as file:
            self.content = file.read().strip()

    @property
    def markdown(self) -> str:
        return markdownify.markdownify(
            self.content, heading_style="ATX", strip=["script", "style", "link"]
        )

    @property
    def sanitized_markdown(self) -> str:
        lines = self.markdown.split("\n")
        result_lines = []
        past_title = False
        puzzle_answers = 0

        for line in lines:
            if not past_title:
                if not line.startswith("## ---"):
                    continue
                past_title = True

            if line.startswith("Your puzzle answer was"):
                puzzle_answers += 1
                if puzzle_answers == 2:
                    break
                continue

            if "Both parts of this puzzle are complete" in line:
                break

            result_lines.append(line)

        result = "\n".join(result_lines)
        while "\n\n\n" in result:
            result = result.replace("\n\n\n", "\n\n")

        result.strip()
        return result


def main():
    converter = AdventOfCodeHtmlToMarkdown("day.html")
    pyperclip.copy(converter.sanitized_markdown)
    print("Sanitized markdown copied to clipboard")


if __name__ == "__main__":
    main()
