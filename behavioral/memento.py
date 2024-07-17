"""
Memento lets you save and restore the previous state of an object without revealing the details of
its implementation.
"""
import string
from abc import abstractmethod, ABC
from dataclasses import dataclass
from datetime import datetime
import random

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S%z"


def generate_random_string(num: int = 10) -> str:
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(num))


@dataclass
class State:
    text: str


class Memento(ABC):

    @abstractmethod
    def get_name(self) -> str:
        ...

    @abstractmethod
    def get_datetime(self) -> str:
        ...


class Snapshot(Memento):

    def __init__(self, state: State) -> None:
        self._state = state
        self._created = datetime.now()

    @property
    def state(self) -> State:
        return self._state

    def get_name(self) -> str:
        return self._state.text

    def get_datetime(self) -> str:
        return self._created.strftime(DATETIME_FORMAT)


class Editor:

    def __init__(self) -> None:
        self._state = None

    def make_change(self) -> None:
        self._state = State(generate_random_string())

    def create_snapshot(self) -> Memento:
        return Snapshot(self._state)

    def restore(self, momento: Snapshot) -> None:
        print(f"Editor state changed to: {momento.get_name()}")
        self._state = momento.state


class Application:

    def __init__(self, editor: Editor) -> None:
        self._history = []
        self._editor = editor

    def save(self) -> None:
        print("Changes saved!")
        self._history.append(self._editor.create_snapshot())

    def undo(self) -> None:
        if not len(self._history):
            return

        snapshot = self._history.pop()
        try:
            self._editor.restore(snapshot)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("History:")
        for idx, snapshot in reversed(list(enumerate(self._history))):
            print(f"{idx + 1}::{snapshot.get_name()}::{snapshot.get_datetime()}")


if __name__ == "__main__":
    editor = Editor()
    app = Application(editor)
    editor.make_change()
    app.save()
    editor.make_change()
    app.save()
    editor.make_change()
    app.save()

    app.show_history()

    editor.make_change()  # uncommited changes
    app.undo()
    app.undo()

    app.show_history()
