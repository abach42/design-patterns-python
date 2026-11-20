"""Small geometry value objects.

Stand-in for the java.awt / java.awt.geom classes the Java cheat sheet
uses (Point, Point2D, Ellipse2D, Rectangle, Rectangle2D).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: float
    y: float


@dataclass(frozen=True)
class Ellipse:
    x: float
    y: float
    width: float
    height: float


@dataclass(frozen=True)
class Rectangle:
    x: float
    y: float
    width: float
    height: float


Shape = Ellipse | Rectangle
