"""
Null object encapsulates the absence of an object by providing a substitutable
alternative that offers suitable default do nothing behavior.
"""
from abc import ABC, abstractmethod


class Graphic(ABC):

    @abstractmethod
    def draw(self):
        ...


class Button(Graphic):

    def draw(self):
        print("[OK]")


class NullObject(Graphic):

    def draw(self):
        pass


if __name__ == "__main__":
    elements = [Button(), Button(), NullObject()]
    for el in elements:
        el.draw()
