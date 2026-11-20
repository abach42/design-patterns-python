from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Prototype(ABC):
    """A mutable point with a color; clone() creates a copy of it."""

    x: float = 0
    y: float = 0
    color: str = ""

    @abstractmethod
    def clone(self) -> "Prototype": ...
