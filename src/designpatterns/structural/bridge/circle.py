from designpatterns.geometry import Point

from .renderer import Renderer
from .shape import Shape


# "Refined Abstraction"
class Circle(Shape):

    def __init__(self, renderer: Renderer, radius: float, center: Point) -> None:
        super().__init__(renderer)
        self.radius = radius
        self.center = center

    def draw(self) -> object:
        return self.renderer.render_circle(self.radius, self.center)
