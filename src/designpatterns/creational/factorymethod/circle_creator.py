from designpatterns.geometry import Point

from .creator import Creator
from .circle_product import CircleProduct
from .product import Product


class CircleCreator(Creator):

    def create_product(self, position: Point) -> Product:
        return CircleProduct(position, 20)
