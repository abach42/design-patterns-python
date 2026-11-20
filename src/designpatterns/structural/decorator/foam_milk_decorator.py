from decimal import Decimal

from .decorator import Decorator


class FoamMilkDecorator(Decorator):

    def calculate_price(self) -> Decimal:
        return self.component.calculate_price() + Decimal("2.39")
