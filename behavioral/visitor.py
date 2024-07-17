"""
Visitor lets you separate algorithms from the objects on which they operate.
"""
from abc import abstractmethod, ABC
from typing import List


class Shape(ABC):

    @abstractmethod
    def accept(self, visitor: "Visitor") -> str:
        ...


class Circle(Shape):

    def __init__(self, x: int, y: int, radius: float) -> None:
        self.x = x
        self.y = y
        self.radius = radius

    def accept(self, visitor: "Visitor") -> str:
        return visitor.visit_circle(self)


class Rectangle(Shape):

    def __init__(self, x1, y1, x2, y2) -> None:
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def accept(self, visitor: "Visitor") -> str:
        return visitor.visit_rectangle(self)


class Visitor(ABC):

    @abstractmethod
    def visit_circle(self, circle: Circle) -> str:
        ...

    @abstractmethod
    def visit_rectangle(self, rectangle: Rectangle) -> str:
        ...


class XMLExporter(Visitor):

    def export(self, shapes: List[Shape]) -> str:
        result = "<?xml version=\"1.0\" encoding=\"utf-8\"?>" + "\n"
        for shape in shapes:
            result += shape.accept(self)
        result += "</xml>"
        return result

    def visit_rectangle(self, rectangle: Rectangle) -> str:
        xml = "<rectangle>\n"
        xml += f"\t<x1>{rectangle.x1}</x1>\n"
        xml += f"\t<y1>{rectangle.y1}</y1>\n"
        xml += f"\t<x2>{rectangle.x2}</x2>\n"
        xml += f"\t<y2>{rectangle.x2}</y2>\n"
        xml += "</rectangle>\n"
        return xml

    def visit_circle(self, circle: Circle) -> str:
        xml = "<circle>\n"
        xml += f"\t<x>{circle.x}</x>\n"
        xml += f"\t<y>{circle.y}</y>\n"
        xml += f"\t<radius>{circle.radius}</radius>\n"
        xml += "</circle>\n"
        return xml


if __name__ == "__main__":
    exporter = XMLExporter()

    circle = Circle(1, 5, 2.1)
    rectangle = Rectangle(10, 20, 15, 40)

    xml = exporter.export([circle, rectangle])
    print(xml)
