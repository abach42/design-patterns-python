from designpatterns.behavioral.iterator.simple.concrete_aggregate import ConcreteAggregate


def test_iterator_pattern() -> None:
    numbers = [1, 2, 3, 4, 5]

    aggregate = ConcreteAggregate(numbers)
    iterator = aggregate.create_iterator()

    result = []
    for item in iterator:
        result.append(item)

    assert result == [1, 2, 3, 4, 5]
