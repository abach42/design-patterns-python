from decimal import Decimal
from typing import Protocol


class Component(Protocol):

    def calculate_price(self) -> Decimal: ...
