"""
Command turns a request into a stand-alone object that contains all information about the request.
 This transformation lets you pass requests as a method arguments, delay or queue a request’s
 execution, and support undoable operations.
"""
import string
from abc import ABC, abstractmethod


class Command(ABC):

    def __init__(self, app: "Application") -> None:
        self._app = app

    @abstractmethod
    def execute(self) -> None:
        ...

    @property
    def editor(self) -> "Editor":
        return self.app.editor

    @property
    def app(self) -> "Application":
        return self._app


class CopyCommand(Command):
    def execute(self) -> None:
        print("Copy first 10")
        self.app.clipboard = self.editor.get_selection()


class CutCommand(Command):

    def execute(self) -> None:
        print("Cut first 10")
        text = self.editor.get_selection()
        self.editor.remove_selection()
        self.app.clipboard = text


class PasteCommand(Command):

    def execute(self) -> None:
        print("Paste")
        text = self.app.clipboard
        self.editor.replace_selection(text)


class Editor:
    def __init__(self) -> None:
        self._text = ""

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, text: str) -> None:
        self._text = text

    def get_selection(self) -> str:
        return self._text[:10]

    def remove_selection(self) -> None:
        self.text = self._text[10:]

    def replace_selection(self, text: str) -> None:
        # should replace selected text and insert text at current position
        self.text += text


class Application:

    def __init__(self):
        self._editor = Editor()
        self._clipboard = None

    @property
    def clipboard(self) -> str:
        return self._clipboard

    @clipboard.setter
    def clipboard(self, text: str) -> None:
        self._clipboard = text

    @property
    def editor(self) -> Editor:
        return self._editor

    def set_text(self, text: str) -> None:
        self.editor.text = text

    def execute_command(self, command: Command) -> None:
        command.execute()

    def show_text(self) -> None:
        print(self.editor.text)


def main():
    app = Application()
    app.set_text(string.ascii_letters)

    app.execute_command(CopyCommand(app))
    app.show_text()
    app.execute_command(PasteCommand(app))
    app.show_text()
    app.execute_command(CutCommand(app))
    app.show_text()
    app.execute_command(PasteCommand(app))
    app.show_text()


if __name__ == "__main__":
    main()
