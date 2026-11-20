from decimal import Decimal

from .component import Component


class EspressoComponent(Component):

    def calculate_price(self) -> Decimal:
        return Decimal("3.49")
