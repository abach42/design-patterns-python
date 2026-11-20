from decimal import Decimal

from .decorator import Decorator


class ChocolateDecorator(Decorator):

    def calculate_price(self) -> Decimal:
        return self.component.calculate_price() + Decimal("1.99")
