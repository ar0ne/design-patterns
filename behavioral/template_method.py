"""
Template method defines the skeleton of an algorithm in the superclass but lets subclasses override
specific steps of the algorithm without changing its structure.
"""
from abc import ABC, abstractmethod


class DocumentGenerator(ABC):

    def __init__(self) -> None:
        self._content = ""

    def generate(self) -> str:
        self.build_header()
        self.build_body()
        self.build_outer()
        return self._content

    @abstractmethod
    def build_header(self) -> None:
        ...

    @abstractmethod
    def build_body(self) -> None:
        ...

    def build_outer(self) -> None:
        pass


class MarkdownDocumentGenerator(DocumentGenerator):

    def build_header(self) -> None:
        self._content += "## This is my title\n"

    def build_body(self) -> None:
        self._content += "Here is the body"


class HTMLDocumentGenerator(DocumentGenerator):
    def build_header(self) -> None:
        self._content += "<html>"
        self._content += "<header>"
        self._content += "<title>This is my title</title>"
        self._content += "</header>"

    def build_body(self) -> None:
        self._content += "<p>Here is the body</p>"

    def build_outer(self) -> None:
        self._content += "</html>"


def generate_document(gen: DocumentGenerator) -> None:
    print("Generating document...")
    print(gen.generate())


if __name__ == "__main__":
    html = HTMLDocumentGenerator()
    markdown = MarkdownDocumentGenerator()

    generate_document(html)
    generate_document(markdown)
