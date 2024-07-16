"""
Abstract factory allows produce families of related objects without specifying their concrete
classes.
"""
from abc import ABC, abstractmethod


class AnimalFactory(ABC):

    @abstractmethod
    def create_bird(self) -> "Bird":
        ...

    @abstractmethod
    def create_fish(self) -> "Fish":
        ...


class Bird(ABC):

    @abstractmethod
    def fly(self) -> None:
        ...

    @abstractmethod
    def can_attack_fish(self, fish: "Fish") -> bool:
        ...


class Fish(ABC):

    @abstractmethod
    def swim(self) -> None:
        ...

    @abstractmethod
    def is_vulnerable(self) -> bool:
        ...


class Pterodactyl(Bird):

    def can_attack_fish(self, fish: "Fish") -> bool:
        can_attack = fish.is_vulnerable()
        return can_attack

    def fly(self) -> None:
        print("pterodactyl can fly.")


class Megalodon(Fish):

    def is_vulnerable(self) -> bool:
        return False

    def swim(self) -> None:
        print("Megalodon can swim.")


class Seagull(Bird):

    def can_attack_fish(self, fish: "Fish") -> bool:
        can_attack = fish.is_vulnerable()
        return can_attack

    def fly(self) -> None:
        print("even chicken can fly")


class Salmon(Fish):

    def is_vulnerable(self) -> bool:
        return True

    def swim(self) -> None:
        print("Salmon can swim")


class DinosaurFactory(AnimalFactory):
    def create_fish(self) -> "Fish":
        return Megalodon()

    def create_bird(self) -> "Bird":
        return Pterodactyl()


class ModernAnimalFactory(AnimalFactory):

    def create_bird(self) -> "Bird":
        return Seagull()

    def create_fish(self) -> "Fish":
        return Salmon()


if __name__ == "__main__":
    dino_factory = DinosaurFactory()
    dino_bird = dino_factory.create_bird()
    dino_fish = dino_factory.create_fish()
    print(f"Dinosaurs bird can attack fish? {dino_bird.can_attack_fish(dino_fish)}")

    modern_animals_factory = ModernAnimalFactory()
    mod_bird = modern_animals_factory.create_bird()
    mod_fish = modern_animals_factory.create_fish()
    print(f"Modern bird can attack fish? {mod_bird.can_attack_fish(mod_fish)}")

