from .memento import Memento


class Originator:

    def __init__(self, state: str) -> None:
        self._state = state

    @property
    def state(self) -> str:
        return self._state

    def change_state(self, state: str) -> None:
        self._state += f", {state}"

    def create_snapshot(self) -> Memento:
        return Memento(self._state)

    def restore_snapshot(self, memento: Memento) -> None:
        self._state = memento.state
