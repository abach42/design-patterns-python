from designpatterns.geometry import Point

from .renderer import Renderer
from .shape import Shape


# "Refined Abstraction"
class Rectangle(Shape):

    def __init__(self, renderer: Renderer, width: float, height: float, top_left: Point) -> None:
        super().__init__(renderer)
        self.width = width
        self.height = height
        self.top_left = top_left

    def draw(self) -> object:
        return self.renderer.render_rectangle(self.width, self.height, self.top_left)
