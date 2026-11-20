from designpatterns.geometry import Point, Rectangle

from .product import Product


class SquareProduct(Product):

    def __init__(self, top_left: Point, side: int) -> None:
        self.top_left = top_left
        self.side = side

    def get_shape(self) -> Rectangle:
        return Rectangle(self.top_left.x, self.top_left.y, self.side, self.side)
