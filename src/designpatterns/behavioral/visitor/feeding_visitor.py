from .elephant_element import ElephantElement
from .lion_element import LionElement
from .visitor import Visitor


class FeedingVisitor(Visitor):

    def visit_lion(self, lion: LionElement) -> None:
        lion.feed_lion()

    def visit_elephant(self, elephant: ElephantElement) -> None:
        elephant.feed_elephant()
