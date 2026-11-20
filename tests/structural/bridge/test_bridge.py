import pytest

from designpatterns.geometry import Ellipse, Point
from designpatterns.structural.bridge.circle import Circle
from designpatterns.structural.bridge.geom.circle_3d_helper import Circle3DHelper
from designpatterns.structural.bridge.geom.rectangle_3d_helper import Rectangle3DHelper
from designpatterns.structural.bridge.rectangle import Rectangle
from designpatterns.structural.bridge.renderer_2d import Renderer2D
from designpatterns.structural.bridge.renderer_3d import Renderer3D


def test_circle_with_2d_renderer() -> None:
    renderer2d = Renderer2D()
    circle = Circle(renderer2d, 5.0, Point(10, 10))

    result = circle.draw()

    assert isinstance(result, Ellipse)
    assert result.width / 2 == pytest.approx(5.0, abs=0.01)  # circle radius (width)
    assert result.height / 2 == pytest.approx(5.0, abs=0.01)  # circle radius (height)
    # top-left corner is adjusted for the radius
    assert result.x == pytest.approx(10 - 5, abs=0.01)
    assert result.y == pytest.approx(10 - 5, abs=0.01)


def test_rectangle_with_3d_renderer() -> None:
    renderer3d = Renderer3D()
    rectangle = Rectangle(renderer3d, 10.0, 5.0, Point(0, 0))

    result = rectangle.draw()

    assert isinstance(result, Rectangle3DHelper)
    assert result.width == 10.0
    assert result.height == 5.0
    assert result.top_left.x == 0.0
    assert result.top_left.y == 0.0
    assert result.top_left.z == 0.0  # z defaults to 0 in 3D rendering


def test_circle_with_3d_renderer() -> None:
    renderer3d = Renderer3D()
    circle = Circle(renderer3d, 7.5, Point(5, 5))

    result = circle.draw()

    assert isinstance(result, Circle3DHelper)
    assert result.radius == pytest.approx(7.5, abs=0.01)
    assert result.center.x == pytest.approx(5.0, abs=0.01)
    assert result.center.y == pytest.approx(5.0, abs=0.01)
    assert result.center.z == 0.0  # z defaults to 0 in 3D rendering
