import math

from designpatterns.geometry import Point


class RouteEntity:

    def __init__(self, name: str, location: Point, destination: Point) -> None:
        self.name = name
        self.location = location
        self.destination = destination
        self.distance = 0.0
        self.duration = 0.0

    # derived from location and destination only, so observers do not depend on each other
    def calculate_distance(self) -> float:
        delta_x = self.destination.x - self.location.x
        delta_y = self.destination.y - self.location.y
        return math.sqrt(delta_x * delta_x + delta_y * delta_y)

    def __hash__(self) -> int:
        return hash((self.location, self.destination))
