"""
Bridge  lets you split a large class or a set of closely related classes into two separate
hierarchies — abstraction and implementation — which can be developed independently of each other.
"""
from abc import ABC, abstractmethod


class Furniture(ABC):

    def __init__(self, material: "Material") -> None:
        self.material = material

    @abstractmethod
    def process(self) -> str:
        ...


class Chair(Furniture):

    def process(self) -> str:
        return f"It's nice chair from {self.material.get_material_name()}."


class Table(Furniture):

    def process(self) -> str:
        return f"Awesome table from {self.material.get_material_name()}."


class Material:

    @abstractmethod
    def get_material_name(self) -> str:
        ...


class Metal(Material):

    def get_material_name(self) -> str:
        return "metal"


class Wood(Material):
    def get_material_name(self) -> str:
        return "wood"


if __name__ == "__main__":
    metal_table = Table(Metal())
    print(metal_table.process())
    wood_chair = Chair(Wood())
    print(wood_chair.process())
