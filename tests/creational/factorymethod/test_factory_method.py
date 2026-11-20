from designpatterns.creational.factorymethod.circle_creator import CircleCreator
from designpatterns.creational.factorymethod.square_creator import SquareCreator
from designpatterns.geometry import Ellipse, Point, Rectangle


def test_should_return_circle() -> None:
    creator = CircleCreator()
    product = creator.create_product(Point(1, 1))
    shape = product.get_shape()

    assert isinstance(shape, Ellipse)
    assert shape.width == 40


def test_should_return_square() -> None:
    creator = SquareCreator()
    product = creator.create_product(Point(1, 1))
    shape = product.get_shape()

    assert isinstance(shape, Rectangle)
    assert shape.width == 50
