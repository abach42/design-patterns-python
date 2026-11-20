from abc import ABC


class AbstractProductA(ABC):

    name: str

    def __str__(self) -> str:
        return f"Name:{self.name}"
