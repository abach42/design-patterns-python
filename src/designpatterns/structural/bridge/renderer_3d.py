from designpatterns.geometry import Point

from .geom.circle_3d_helper import Circle3DHelper
from .geom.point_3d_helper import Point3DHelper
from .geom.rectangle_3d_helper import Rectangle3DHelper
from .renderer import Renderer


# "Concrete Implementator"
class Renderer3D(Renderer):

    def render_circle(self, radius: float, center: Point) -> Circle3DHelper:
        # assume z = 0 for simplicity
        return Circle3DHelper(Point3DHelper(center.x, center.y, 0), radius)

    def render_rectangle(self, width: float, height: float, top_left: Point) -> Rectangle3DHelper:
        # assume z = 0 for simplicity
        return Rectangle3DHelper(Point3DHelper(top_left.x, top_left.y, 0), width, height)
