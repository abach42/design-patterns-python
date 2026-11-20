from abc import ABC


class AbstractProductB(ABC):

    id: str

    def __str__(self) -> str:
        return f"Id:{self.id}"
