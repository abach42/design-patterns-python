from dataclasses import dataclass

from .point_3d_helper import Point3DHelper


# Helper does not belong to the pattern
@dataclass
class Circle3DHelper:
    center: Point3DHelper
    radius: float
