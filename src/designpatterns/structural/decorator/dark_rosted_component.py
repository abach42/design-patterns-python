from decimal import Decimal

from .component import Component


class DarkRostedComponent(Component):

    def calculate_price(self) -> Decimal:
        return Decimal("4.49")
