"""
Chain of responsibility lets you pass requests along a chain of handlers. Upon receiving a request,
each handler decides either to process the request or to pass it to the next handler in the chain.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Self

Data = int


@dataclass
class ValidationResult:
    is_valid: bool
    error: str | None = None


class ValidationChain(ABC):

    def __init__(self) -> None:
        self.next = None

    @abstractmethod
    def validate(self, data: Data) -> ValidationResult:
        ...

    def set_next(self, next_action: "ValidationChain") -> Self:
        self.next = next_action
        return self

    def execute(self, data: Data) -> ValidationResult:
        validation_result = self.validate(data)
        if not validation_result.is_valid or not self.next:
            print("stop validation chain")
            return validation_result
        return self.next.execute(data)


class LessThan100(ValidationChain):

    def validate(self, data: Data) -> ValidationResult:
        print("LessThan100::validate")
        if data < 100:
            return ValidationResult(True)
        return ValidationResult(False, "should be less than 100")


class NotEqualTo5(ValidationChain):

    def validate(self, data: Data) -> ValidationResult:
        print("NotEqualTo5::validate")
        if data != 5:
            return ValidationResult(True)
        return ValidationResult(False, "should be not equal to 5")


class BiggerOrEqualTo20(ValidationChain):

    def validate(self, data: Data) -> ValidationResult:
        print("BiggerOrEqualTo20::validate")
        if data >= 20:
            return ValidationResult(True)
        return ValidationResult(False, "should be more or equal to 20")


if __name__ == "__main__":
    chain = LessThan100().set_next(NotEqualTo5().set_next((BiggerOrEqualTo20())))
    print(chain.execute(19))
