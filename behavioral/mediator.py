"""
Mediator (Middleware) lets you reduce chaotic dependencies between objects. The pattern restricts
direct communications between the objects and forces them to collaborate only via a mediator object.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, List


@dataclass
class Event:
    type: str
    context: str | None = None


class Participant(ABC):
    def __init__(self, name: str) -> None:
        self._name = name
        self._room = None

    @property
    def room(self) -> "ChatRoom":
        return self._room

    @room.setter
    def room(self, room: "ChatRoom") -> None:
        self._room = room

    @property
    def name(self) -> str:
        return self._name

    def leave_room(self) -> None:
        self.room.notify(self, Event("leave"))

    def send_message(self, message: str) -> None:
        self.room.notify(self, Event("message", message))


class User(Participant):
    ...


class Bot(Participant):

    def greetings_all(self) -> None:
        for user in self.room.get_users(self):
            self.send_message(f"Welcome {user.name}!")


class Mediator(ABC):

    @abstractmethod
    def notify(self, participant: "Participant", event: Event) -> None:
        ...


class ChatRoom(Mediator):

    def __init__(self) -> None:
        self._participants = {}

    def add_participant(self, participant: Participant) -> None:
        self._participants[participant.name] = participant
        participant.room = self

    def remove_participant(self, participant: Participant) -> None:
        del self._participants[participant.name]

    def notify(self, participant: Participant, event: Event) -> None:
        match event.type:
            case "message":
                print(f"{participant.name}::{event.context}")
            case "leave":
                print(f"{participant.name} left the room!")
                self.remove_participant(participant)

    def get_users(self, sender: Participant) -> List[Participant]:
        if not isinstance(sender, Bot):
            return []
        return list(filter(lambda p: isinstance(p, User), self._participants.values()))


def main():
    room = ChatRoom()
    ai_bot = Bot("AI Admin")
    bob = User("Bob")
    alex = User("Alex")

    room.add_participant(ai_bot)
    room.add_participant(bob)
    room.add_participant(alex)

    alex.send_message("Hi All!")
    bob.send_message("Hi Alex")
    ai_bot.greetings_all()

    bob.leave_room()


if __name__ == "__main__":
    main()
