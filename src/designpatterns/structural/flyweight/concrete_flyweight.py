from .flyweight import Flyweight


class ConcreteFlyweight(Flyweight):

    def __init__(self, intrinsic_state: str) -> None:
        self._intrinsic_state = intrinsic_state

    def operation(self, extrinsic_state: str) -> str:
        return f"Intrinsic: {self._intrinsic_state}, Extrinsic: {extrinsic_state}"
