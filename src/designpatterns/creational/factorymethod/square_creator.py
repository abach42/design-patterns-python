from designpatterns.geometry import Point

from .creator import Creator
from .product import Product
from .square_product import SquareProduct


class SquareCreator(Creator):

    def create_product(self, position: Point) -> Product:
        return SquareProduct(position, 50)
