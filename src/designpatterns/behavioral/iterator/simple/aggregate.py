from collections.abc import Iterator
from typing import Protocol


class Aggregate[T](Protocol):

    def create_iterator(self) -> Iterator[T]: ...
