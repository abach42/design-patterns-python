from dataclasses import dataclass

from .prototype import Prototype


@dataclass
class CirclePrototype(Prototype):

    radius: int = 0

    def clone(self) -> "CirclePrototype":
        return CirclePrototype(self.x, self.y, self.color, self.radius)
