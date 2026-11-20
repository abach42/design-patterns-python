from designpatterns.creational.prototype.circle_prototype import CirclePrototype
from designpatterns.creational.prototype.square_prototype import SquarePrototype


def test_circle_should_be_not_same_but_equal() -> None:
    circle_prototype = CirclePrototype()
    circle_prototype.x = 1
    circle_prototype.y = 1
    circle_prototype.radius = 10
    circle_prototype.color = "blue"

    actual_circle = circle_prototype.clone()

    assert actual_circle is not circle_prototype
    assert actual_circle == circle_prototype


def test_square_should_be_not_same_but_equal() -> None:
    square_prototype = SquarePrototype()
    square_prototype.x = 1
    square_prototype.y = 1
    square_prototype.side = 10
    square_prototype.color = "yellow"

    actual_square = square_prototype.clone()

    assert actual_square is not square_prototype
    assert actual_square == square_prototype
