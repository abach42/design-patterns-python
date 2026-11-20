from .memento import Memento


class Caretaker:

    def __init__(self) -> None:
        self._mementos: list[Memento] = []

    def add_memento(self, memento: Memento) -> None:
        self._mementos.append(memento)

    def get_memento(self, index: int) -> Memento:
        return self._mementos[index]
