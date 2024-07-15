"""
Iterator lets you traverse elements of a collection without exposing its underlying representation
"""
from collections.abc import Iterator, Iterable
from typing import List, Any


class MyCollectionIterator(Iterator):

    def __init__(self, collection: "MyCollection") -> None:
        self.collection = collection
        self.current_position = 0

    def __next__(self) -> Any:
        try:
            next_element = self.collection[self.current_position]
            self.current_position += 1
        except IndexError:
            raise StopIteration()
        return next_element


class MyCollection(Iterable):

    def __init__(self, collection: List[Any] | None = None) -> None:
        self._list: List[Any] = collection or []

    def __iter__(self) -> Iterator:
        return MyCollectionIterator(self)

    def __getitem__(self, item) -> Any:
        return self._list[item]

    def add(self, element: Any) -> None:
        self._list.append(element)


if __name__ == "__main__":
    my_coll = MyCollection()
    my_coll.add(1)
    my_coll.add("foo")
    my_coll.add(None)
    for el in my_coll:
        print(el)
