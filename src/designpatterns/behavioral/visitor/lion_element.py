from .element import Element
from .visitor import Visitor


class LionElement(Element):

    def __init__(self) -> None:
        self._lion_fed = False
        self._lion_teeth_healthy = False

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_lion(self)

    @property
    def fed_up(self) -> bool:
        return self._lion_fed

    def feed_lion(self) -> None:
        self._lion_fed = True

    @property
    def health_checked(self) -> bool:
        return self._lion_teeth_healthy

    def care_lion(self) -> None:
        self._lion_teeth_healthy = True
