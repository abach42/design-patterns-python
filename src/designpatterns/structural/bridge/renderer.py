from typing import Protocol

from designpatterns.geometry import Point


# "Implementator"
class Renderer(Protocol):

    def render_circle(self, radius: float, center: Point) -> object: ...

    def render_rectangle(self, width: float, height: float, top_left: Point) -> object: ...
