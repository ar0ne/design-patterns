"""
Factory method provides an interface for creating objects in a superclass, but allows subclasses to
alter the type of objects that will be created.
"""
from abc import ABC, abstractmethod
from typing import Dict


class Game(ABC):
    @abstractmethod
    def make_turn(self) -> None:
        ...

    @staticmethod
    @abstractmethod
    def create_game() -> "Game":
        ...


class Go(Game):

    @staticmethod
    def create_game() -> "Game":
        print("Create game board for Go")
        return Go()

    def make_turn(self) -> None:
        print("Go game turn")


class Chess(Game):
    @staticmethod
    def create_game() -> "Game":
        print("Create game board for Chess")
        return Chess()

    def make_turn(self) -> None:
        print("Chess game turn")


class GameFactory(ABC):
    @abstractmethod
    def get_game(self, name: str) -> Game:
        ...


class BoardGameFactory(GameFactory):

    def __init__(self, games: Dict[str, Game]) -> None:
        self.games = games

    def get_game(self, name: str) -> Game:
        game = self.games.get(name)
        return game


if __name__ == "__main__":
    factory = BoardGameFactory({
        "chess": Chess(),
        "go": Go()}
    )
    chess = factory.get_game("chess")
    chess.create_game()
    chess.make_turn()
