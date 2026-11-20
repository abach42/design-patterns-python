from collections.abc import Iterator

from .aggregate import Aggregate
from .concrete_iterator import ConcreteIterator


class ConcreteAggregate[T](Aggregate[T]):

    def __init__(self, items: list[T]) -> None:
        self._items = items

    def create_iterator(self) -> Iterator[T]:
        return ConcreteIterator(self._items)
