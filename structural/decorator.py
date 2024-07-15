"""
Decorator allows adding new behaviors to objects dynamically by placing them inside special wrapper objects, called decorators.

"""
from typing import Protocol


class Speechable(Protocol):

    def say(self) -> str:
        ...


class Cat:
    def say(self) -> str:
        return "Meow!"


class SpeechableDecorator:

    def __init__(self, sayer: Speechable):
        self.sayer = sayer

    def say(self) -> str:
        return f"Mega {self.sayer.say()}"


def say_word(sayer: Speechable) -> None:
    print(f"Word is '{sayer.say()}'")


if __name__ == "__main__":
    cat = Cat()
    say_word(cat)

    decorator = SpeechableDecorator(cat)
    say_word(decorator)

    decoratorForDecorator = SpeechableDecorator(decorator)
    say_word(decoratorForDecorator)
