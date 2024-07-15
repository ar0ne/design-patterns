"""
Builder lets you construct complex objects step by step. The pattern allows you to produce different
 types and representations of an object using the same construction code.
"""
from typing import Self, Optional


class Pizza:

    def __init__(self, name: str, dough: Optional[str], cheese: Optional[str], sauce: Optional[str], oil: Optional[str]) -> None:
        self.name = name
        self.dough = dough
        self.cheese = cheese
        self.sauce = sauce
        self.oil = oil

    def __str__(self) -> str:
        """Cook a pizza"""
        res = f"Enjoy your pizza {self.name}. That features a bubbly crust"
        if self.dough:
            res += f", {self.dough} dough"
        if self.sauce:
            res += f", crushed {self.sauce} sauce"
        if self.cheese:
            res += f", fresh {self.cheese}"
        if self.oil:
            res += f", a drizzle of {self.oil} oil"
        return res + "."


class PizzaBuilder:

    def __init__(self, name: str) -> None:
        self._name = name
        self._cheese: Optional[str] = None
        self._sauce: Optional[str] = None
        self._oil: Optional[str] = None
        self._dough: Optional[str] = None

    def add_cheese(self, cheese: str) -> Self:
        self._cheese = cheese
        return self

    def add_sauce(self, sauce: str) -> Self:
        self._sauce = sauce
        return self

    def add_oil(self, oil: str) -> Self:
        self._oil = oil
        return self

    def add_dough(self, dough: str) -> Self:
        self._dough = dough
        return self

    def build(self) -> Pizza:
        return Pizza(
            name=self._name,
            dough=None,
            cheese=self._cheese,
            sauce=self._sauce,
            oil=self._oil
        )


if __name__ == "__main__":
    margherita = (PizzaBuilder("margherita")
                  .add_cheese("mozzarella")
                  .add_sauce("tomato")
                  .add_oil("olive")
                  .build())
    print(margherita)
