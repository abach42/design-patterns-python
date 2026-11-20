from dataclasses import dataclass

from .prototype import Prototype


@dataclass
class SquarePrototype(Prototype):

    side: int = 0

    def clone(self) -> "SquarePrototype":
        return SquarePrototype(self.x, self.y, self.color, self.side)
