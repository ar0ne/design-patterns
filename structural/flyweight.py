"""
Flyweight lets you fit more objects into the available amount of RAM by sharing common parts of
state between multiple objects instead of keeping all the data in each object.
"""
from dataclasses import dataclass
from typing import Dict, List

Data = dict


@dataclass
class City:
    name: str
    # ...
    # image, map or anything that take a lot of RAM


class CityFactory:
    _cities: Dict[str, City] = {}

    def __init__(self, initial_cities: List[City]) -> None:
        for city in initial_cities:
            self._cities[city.name] = city

    @classmethod
    def get_city(cls, name: str) -> City:
        city = cls._cities.get(name)
        if city is None:
            city = City(name)
            cls._cities[name] = city
        return city

    def list_cache(self) -> None:
        print(self._cities)


@dataclass
class User:
    full_name: str
    city: City


class Citizens:
    def __init__(self) -> None:
        self.users: List[User] = []

    def add_resident(self, username: str, city: str) -> None:
        city = CityFactory.get_city(city)
        user = User(username, city)
        self.users.append(user)


if __name__ == "__main__":
    factory = CityFactory([City("New York"), City("Atlanta"), City("Los Angeles")])
    usa_citizens = Citizens()
    usa_citizens.add_resident("John Doe", "Atlanta")
    usa_citizens.add_resident("Kevin Brown", "Washington")
    usa_citizens.add_resident("Isaak Newton", "Washington")
    print(usa_citizens.__dict__)
    factory.list_cache()
