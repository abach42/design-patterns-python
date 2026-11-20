from dataclasses import dataclass

from .point_3d_helper import Point3DHelper


# Helper does not belong to the pattern
@dataclass
class Rectangle3DHelper:
    top_left: Point3DHelper
    width: float
    height: float
