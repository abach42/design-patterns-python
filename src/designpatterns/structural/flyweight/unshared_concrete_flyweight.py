from .flyweight import Flyweight


class UnsharedConcreteFlyweight(Flyweight):

    def __init__(self, all_state: str) -> None:
        self._all_state = all_state

    def operation(self, extrinsic_state: str) -> str:
        return f"Unshared: {self._all_state}, Extrinsic: {extrinsic_state}"
