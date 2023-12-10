import markdownify


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


def main():
    converter = AdventOfCodeHtmlToMarkdown("day.html")
    print(converter.markdown)


if __name__ == "__main__":
    main()
