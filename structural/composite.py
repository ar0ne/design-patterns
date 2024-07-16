"""
Composite lets you compose objects into tree structures and then work with these structures as if
they were individual objects.
"""
from abc import ABC, abstractmethod
from typing import List


def space(level: int) -> str:
    result = ""
    if level:
        result = "  " * (level - 1) + "|--"
    return result


class Component(ABC):

    def __init__(self, name: str) -> None:
        self.name = name

    def is_composite(self) -> bool:
        return False

    def add(self, component: "Component") -> None:
        pass

    def remove(self, component: "Component") -> None:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass

    def printify(self, tabs: int = 0) -> str:
        return space(tabs) + self.name + "\n"


class File(Component):

    def get_size(self) -> int:
        return len(self.name)


class Folder(Component):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._children: List[Component] = []

    def is_composite(self) -> bool:
        return True

    def get_size(self) -> int:
        sum_size = sum(children.get_size() for children in self._children)
        return sum_size + 1

    def add(self, component: "Component") -> None:
        self._children.append(component)

    def remove(self, component: "Component") -> None:
        self._children.remove(component)

    def printify(self, tabs: int = 0) -> str:
        res = space(tabs) + self.name + "\n"
        for child in self._children:
            res += child.printify(tabs + 1)
        return res


if __name__ == "__main__":
    root = Folder("/")
    root.add(File("hello.txt"))
    var = Folder("var")
    log = Folder("log")
    log_file = File("pacman.log")
    log.add(log_file)
    log.add(File(".env"))
    var.add(log)
    root.add(var)

    print(root.printify())
    """
    /
    |--hello.txt
    |--var
      |--log
        |--pacman.log
        |--.env
    """
    print(f"Size of root {root.get_size()}")
    log.remove(log_file)
    print(f"Updated size of root {root.get_size()}")
