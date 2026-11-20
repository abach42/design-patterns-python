from decimal import Decimal

from .component import Component


class HouseBlendComponent(Component):

    def calculate_price(self) -> Decimal:
        return Decimal("2.99")
