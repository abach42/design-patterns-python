from abc import ABC, abstractmethod

from .renderer import Renderer


# "Abstraction"
class Shape(ABC):

    # dependency on Renderer makes the bridge
    def __init__(self, renderer: Renderer) -> None:
        self.renderer = renderer

    @abstractmethod
    def draw(self) -> object: ...
