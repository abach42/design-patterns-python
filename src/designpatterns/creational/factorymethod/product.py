from typing import Protocol

from designpatterns.geometry import Shape


class Product(Protocol):

    def get_shape(self) -> Shape: ...
