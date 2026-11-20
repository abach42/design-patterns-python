from dataclasses import dataclass


@dataclass(frozen=True)
class ProductData:
    name: str
    price: float
