from typing import Protocol

from designpatterns.geometry import Point

from .product import Product


class Creator(Protocol):

    def create_product(self, position: Point) -> Product: ...
