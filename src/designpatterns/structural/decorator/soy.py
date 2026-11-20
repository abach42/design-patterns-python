from decimal import Decimal

from .decorator import Decorator


class Soy(Decorator):

    def calculate_price(self) -> Decimal:
        return self.component.calculate_price() + Decimal("3.29")
