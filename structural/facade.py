"""
Facade provides a simplified interface to a library, a framework, or any other complex set of classes.
"""


class Multiply:
    def calculate(self, a: float, b: float) -> float:
        return a * b


class Square:
    def calculate(self, a: float, b: float) -> float:
        return a ** b


class Facade:

    def __init__(self, multiply: Multiply, square: Square) -> None:
        self.multiply = multiply
        self.square = square

    def _get_pi(self) -> float:
        return 3.14

    def process(self, number: int | float) -> str:
        # here we have some complex processing that could include many subsystems
        # i.e. calculate area of square: pi * r ^ 2
        radius_squared = self.square.calculate(number, 2)
        # facade lets us hide this logic and provide simple interface for clients
        pi = self._get_pi()
        result = self.multiply.calculate(pi, radius_squared)
        return f"The area of square is {result}"


if __name__ == "__main__":
    facade = Facade(Multiply(), Square())
    print(facade.process(10))
