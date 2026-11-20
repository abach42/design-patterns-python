from decimal import Decimal

import pytest

from designpatterns.structural.decorator.chocolate_decorator import ChocolateDecorator
from designpatterns.structural.decorator.component import Component
from designpatterns.structural.decorator.dark_rosted_component import DarkRostedComponent
from designpatterns.structural.decorator.espresso_component import EspressoComponent
from designpatterns.structural.decorator.foam_milk_decorator import FoamMilkDecorator
from designpatterns.structural.decorator.house_blend_component import HouseBlendComponent
from designpatterns.structural.decorator.soy import Soy


@pytest.mark.parametrize(
    "name, component, expected_price",
    [
        (
            "Espresso+Chocolate+FoamMilk",
            FoamMilkDecorator(ChocolateDecorator(EspressoComponent())),
            Decimal("7.87"),
        ),
        (
            "Soy+DarkRosted",
            Soy(DarkRostedComponent()),
            Decimal("7.78"),
        ),
        (
            "FoamMilk+HouseBlend",
            FoamMilkDecorator(HouseBlendComponent()),
            Decimal("5.38"),
        ),
    ],
    ids=["Espresso+Chocolate+FoamMilk", "Soy+DarkRosted", "FoamMilk+HouseBlend"],
)
def test_decorator_calculates(name: str, component: Component, expected_price: Decimal) -> None:
    actual_price = component.calculate_price()
    assert actual_price == expected_price
