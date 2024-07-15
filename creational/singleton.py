"""
Ensure a class only has one instance, and provide a global point of access to it.
"""


class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance


class Example(Singleton):
    ...


if __name__ == "__main__":
    obj1 = Example()
    obj2 = Example()
    assert obj1 is obj2
