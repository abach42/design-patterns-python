from .elephant_element import ElephantElement
from .lion_element import LionElement
from .visitor import Visitor


class VeterinarianVisitor(Visitor):

    def visit_lion(self, lion: LionElement) -> None:
        lion.care_lion()

    def visit_elephant(self, elephant: ElephantElement) -> None:
        elephant.care_elephant()
