from dataclasses import dataclass


# Helper does not belong to the pattern
@dataclass
class Point3DHelper:
    x: float
    y: float
    z: float

    def __str__(self) -> str:
        return f"Point3D{{x={self.x}, y={self.y}, z={self.z}}}"
