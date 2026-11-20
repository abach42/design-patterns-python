from .element import Element
from .visitor import Visitor


class ElephantElement(Element):

    def __init__(self) -> None:
        self._elephant_fed = False
        self._elephant_weight_ok = False

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_elephant(self)

    @property
    def fed_up(self) -> bool:
        return self._elephant_fed

    def feed_elephant(self) -> None:
        self._elephant_fed = True

    @property
    def health_checked(self) -> bool:
        return self._elephant_weight_ok

    def care_elephant(self) -> None:
        self._elephant_weight_ok = True
