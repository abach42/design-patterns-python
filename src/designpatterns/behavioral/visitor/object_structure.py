from .element import Element
from .visitor import Visitor


class ObjectStructure:

    def __init__(self) -> None:
        self._animals: list[Element] = []

    def add_animal(self, element: Element) -> None:
        self._animals.append(element)

    def visit_animals(self, visitor: Visitor) -> None:
        for animal in self._animals:
            animal.accept(visitor)

    @property
    def animals(self) -> list[Element]:
        return self._animals
