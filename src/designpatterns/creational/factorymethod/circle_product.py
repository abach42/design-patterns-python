from designpatterns.geometry import Ellipse, Point

from .product import Product


class CircleProduct(Product):

    def __init__(self, center: Point, radius: int) -> None:
        self.center = center
        self.radius = radius

    def get_shape(self) -> Ellipse:
        return Ellipse(
            self.center.x - self.radius,  # x-coordinate of the top-left corner
            self.center.y - self.radius,  # y-coordinate of the top-left corner
            2 * self.radius,  # width
            2 * self.radius,  # height
        )
