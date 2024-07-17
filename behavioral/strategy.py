"""
Strategy lets you define a family of algorithms, put each of them into a separate class, and make
their objects interchangeable.
"""
from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def calculate_fee(self, amount: float) -> float:
        ...


class CreditCard(PaymentMethod):
    def calculate_fee(self, amount: float) -> float:
        return 0.01 * amount


class DebitCard(PaymentMethod):

    def calculate_fee(self, amount: float) -> float:
        return 0.05 * amount


class PaymentGateway:
    payment_method: PaymentMethod = None

    def process_payment(self, amount: float) -> float:
        return amount + self.payment_method.calculate_fee(amount)


class PaymentService:

    def __init__(self, gateway: PaymentGateway) -> None:
        self.payment_gateway = gateway

    def process_payment(self, payment_method: str, amount: float) -> None:
        match payment_method:
            case "CreditCard":
                self.payment_gateway.payment_method = CreditCard()
            case "DebitCard":
                self.payment_gateway.payment_method = DebitCard()
            case _:
                raise Exception()
        result = self.payment_gateway.process_payment(amount)
        print(f"{result=}")


if __name__ == "__main__":
    payment_service = PaymentService(PaymentGateway())
    payment_service.process_payment("CreditCard", 100)
    payment_service.process_payment("DebitCard", 100)
