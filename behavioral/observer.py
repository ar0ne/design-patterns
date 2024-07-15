"""
Observer defines a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.
"""
from typing import Set

Data = dict


class Subscriber:

    def update(self, data: Data) -> None:
        ...


class Publisher:
    subscribers: Set[Subscriber] = set()

    def add_subscriber(self, subscriber: Subscriber) -> None:
        self.subscribers.add(subscriber)

    def remove_subscriber(self, subscriber: Subscriber) -> None:
        self.subscribers.remove(subscriber)

    def notify_all(self, data: Data) -> None:
        print("New event triggered! Notify all!")
        for sub in self.subscribers:
            sub.update(data)


class ConcreteSubscriberA(Subscriber):
    def update(self, data: Data) -> None:
        print("Update in concreate component A")


class ConcreteSubscriberB(Subscriber):
    def update(self, data: Data) -> None:
        print("Update in concreate component B")


if __name__ == "__main__":
    event = {"foo": "bar"}
    subA = ConcreteSubscriberA()
    subB = ConcreteSubscriberB()

    publisher = Publisher()
    publisher.add_subscriber(subA)
    publisher.notify_all(event)

    publisher.add_subscriber(subB)
    publisher.notify_all(event)
    publisher.remove_subscriber(subB)
    publisher.notify_all(event)
