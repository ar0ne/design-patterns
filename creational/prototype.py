"""
Prototype lets you copy existing objects without making your code dependent on their classes.
"""
import copy
from abc import ABC
from dataclasses import dataclass
from typing import List, Any


@dataclass
class Coordinate:
    x: int
    y: int


class Shape(ABC):

    def __init__(self, coordinate: Coordinate, color: str, tags: List[Any]) -> None:
        self.coordinate = coordinate
        self.color = color
        self.tags = tags


class Circle(Shape):

    def __init__(self, coordinate: Coordinate, color: str, tags: List[Any], radius: int) -> None:
        super().__init__(coordinate, color, tags)
        self.radius = radius

    def __copy__(self) -> "Circle":
        tags = copy.copy(self.tags)
        coordinate = copy.copy(self.coordinate)
        new = self.__class__(coordinate, self.color, tags, self.radius)
        return new

    def __deepcopy__(self, memodict=None) -> "Shape":
        if memodict is None:
            memodict = {}
        tags = copy.deepcopy(self.tags)
        coordinate = copy.deepcopy(self.coordinate)
        new = self.__class__(coordinate, self.color, tags, self.radius)
        new.__dict__ = copy.deepcopy(self.__dict__, memodict)
        return new


def print_ids(shape: Shape):
    print(f"Id: {shape}")
    for key, value in shape.__dict__.items():
        print(f"{key}: {value}, id: {id(value)}")


if __name__ == "__main__":
    tags = [
        {
            "KeyName": "hello",
            "KeyValue": "world"
        }
    ]
    original_circle = Circle(Coordinate(10, 20), "red", tags, 2)
    swallow_clone_circle = copy.copy(original_circle)
    swallow_clone_circle.x = -100
    deep_clone_circle = copy.deepcopy(original_circle)

    print_ids(original_circle)
    print_ids(swallow_clone_circle)
    print_ids(deep_clone_circle)
