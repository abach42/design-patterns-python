from typing import Protocol


class Flyweight(Protocol):

    def operation(self, extrinsic_state: str) -> str: ...
