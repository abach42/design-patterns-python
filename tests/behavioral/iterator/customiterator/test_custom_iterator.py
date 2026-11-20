import pytest

from designpatterns.behavioral.iterator.customiterator.concrete_aggregate import ConcreteAggregate


def test_iterator_pattern() -> None:
    numbers = [1, 2, 3, 4, 5]

    aggregate = ConcreteAggregate(numbers)
    iterator = aggregate.create_iterator()

    result = []
    for item in iterator:
        result.append(item)

    assert result == [1, 2, 3, 4, 5]


def test_iterator_exception() -> None:
    aggregate = ConcreteAggregate([])
    iterator = aggregate.create_iterator()

    assert not iterator.has_next()
    with pytest.raises(StopIteration, match="No more elements"):
        next(iterator)
