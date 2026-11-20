from designpatterns.structural.flyweight.concrete_flyweight import ConcreteFlyweight  # noqa: F401
from designpatterns.structural.flyweight.flyweight_factory import FlyweightFactory
from designpatterns.structural.flyweight.unshared_concrete_flyweight import UnsharedConcreteFlyweight


def test_shared_flyweights() -> None:
    factory = FlyweightFactory()

    shared_a1 = factory.get_flyweight("A")
    shared_a2 = factory.get_flyweight("A")
    shared_b = factory.get_flyweight("B")

    assert shared_a1 is shared_a2
    assert shared_a1 is not shared_b

    assert shared_a1.operation("first") == "Intrinsic: A, Extrinsic: first"
    assert shared_a2.operation("second") == "Intrinsic: A, Extrinsic: second"
    assert shared_b.operation("context") == "Intrinsic: B, Extrinsic: context"

    assert factory.pool_size() == 2


def test_unshared_flyweight() -> None:
    unshared = UnsharedConcreteFlyweight("CustomState")

    result = unshared.operation("external context")

    assert result == "Unshared: CustomState, Extrinsic: external context"
