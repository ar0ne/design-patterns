"""
Proxy lets you provide a substitute or placeholder for another object. A proxy controls access to
the original object, allowing you to perform something either before or after the request gets
through to the original object.
"""
from typing import Optional


class TextFile:
    def __init__(self, path: str) -> None:
        self.path: str = path
        self.data: Optional[str] = None
        # heavy operation which we want to avoid
        self._load_from_disk()

    def _load_from_disk(self) -> None:
        # could be any heavy operations
        print("Reading from the file system!")
        with open(self.path, "r") as file:
            self.data = file.read()

    def display(self) -> None:
        print(self.data)


class Proxy(TextFile):

    def __init__(self, path: str) -> None:
        self.path = path
        self._subject = None

    def display(self) -> None:
        if self._subject is None:
            # lazy loading
            self._subject = TextFile(self.path)
        self._subject.display()


if __name__ == "__main__":
    proxy = Proxy("/etc/os-release")
    print(proxy.path)
    # read only once
    proxy.display()
    proxy.display()
