from collections.abc import Iterator


class ConcreteIterator[T](Iterator[T]):

    def __init__(self, items: list[T]) -> None:
        self._items = items
        self._position = 0

    def has_next(self) -> bool:
        return self._position < len(self._items)

    def __iter__(self) -> ConcreteIterator[T]:
        return self

    def __next__(self) -> T:
        if not self.has_next():
            raise StopIteration("No more elements")
        item = self._items[self._position]
        self._position += 1
        return item
