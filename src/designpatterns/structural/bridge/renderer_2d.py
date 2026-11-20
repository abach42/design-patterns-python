from designpatterns import geometry
from designpatterns.geometry import Point

from .renderer import Renderer


# "Concrete Implementator"
class Renderer2D(Renderer):

    def render_circle(self, radius: float, center: Point) -> geometry.Ellipse:
        return geometry.Ellipse(
            center.x - radius,  # x-coordinate of the top-left corner
            center.y - radius,  # y-coordinate of the top-left corner
            2 * radius,  # width
            2 * radius,  # height
        )

    def render_rectangle(self, width: float, height: float, top_left: Point) -> geometry.Rectangle:
        return geometry.Rectangle(top_left.x, top_left.y, width, height)
