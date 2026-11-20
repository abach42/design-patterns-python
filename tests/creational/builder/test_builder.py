import pytest

from designpatterns.creational.builder.barebone_concrete_builder import BareboneConcreteBuilder
from designpatterns.creational.builder.director import Director
from designpatterns.creational.builder.tower_concrete_builder import TowerConcreteBuilder


@pytest.fixture
def director() -> Director:
    return Director()


def test_barebone_builder_basic_computer(director: Director) -> None:
    barebone_builder = BareboneConcreteBuilder()
    director.construct_basic_computer(barebone_builder)
    barebone_product = barebone_builder.build()

    expected_product = (
        "BareboneProduct[cpu=Intel Core i3,ram_size=16,hard_disk_size=500,cooler=SMALL]"
    )

    assert str(barebone_product) == expected_product


def test_barebone_builder_gaming_computer(director: Director) -> None:
    barebone_builder = BareboneConcreteBuilder()
    director.construct_gaming_computer(barebone_builder)
    barebone_product = barebone_builder.build()

    expected_product = (
        "BareboneProduct[cpu=Intel Core i9,ram_size=64,hard_disk_size=2000,cooler=SMALL]"
    )

    assert str(barebone_product) == expected_product


def test_tower_builder_basic_computer(director: Director) -> None:
    tower_builder = TowerConcreteBuilder()
    director.construct_basic_computer(tower_builder)
    tower_product = tower_builder.build()

    expected_product = (
        "TowerProduct[cpu=Intel Core i3,ram_size=16,hard_disk_size=500,cooler=LARGE]"
    )

    assert str(tower_product) == expected_product


def test_tower_builder_gaming_computer(director: Director) -> None:
    tower_builder = TowerConcreteBuilder()
    director.construct_gaming_computer(tower_builder)
    tower_product = tower_builder.build()

    expected_product = (
        "TowerProduct[cpu=Intel Core i9,ram_size=64,hard_disk_size=2000,cooler=LARGE]"
    )

    assert str(tower_product) == expected_product
