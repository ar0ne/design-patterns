"""
Adapter allows objects with incompatible interfaces to collaborate.
"""


class FullName:
    def __init__(self, name: str) -> None:
        self.first_name, self.last_name = name.split(" ")


class LegacyService:

    def extract_name(self, full_name: FullName) -> str:
        return full_name.first_name


class ModernService:

    def print_name(self, name: str) -> None:
        print(name)


class Adapter(LegacyService, ModernService):
    def print_name(self, data: str) -> None:
        name = self.extract_name(FullName(data))
        super().print_name(name)


if __name__ == "__main__":
    adapter = Adapter()
    adapter.print_name("Kevin O'Neal")
