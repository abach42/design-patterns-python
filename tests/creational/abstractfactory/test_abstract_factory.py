import pytest

from designpatterns.creational.abstractfactory.concrete_factory1 import ConcreteFactory1
from designpatterns.creational.abstractfactory.concrete_factory2 import ConcreteFactory2


@pytest.mark.parametrize(
    "expected, actual",
    [
        ("Name:ProductA1", str(ConcreteFactory1().create_product_a())),
        ("Name:ProductA2", str(ConcreteFactory2().create_product_a())),
        ("Id:ProductB1", str(ConcreteFactory1().create_product_b())),
        ("Id:ProductB2", str(ConcreteFactory2().create_product_b())),
    ],
    ids=["ProductA1", "ProductA2", "ProductB1", "ProductB2"],
)
def test_abstract_factory_returns_product_string(expected: str, actual: str) -> None:
    assert expected == actual
