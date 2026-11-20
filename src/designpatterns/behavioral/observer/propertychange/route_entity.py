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

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, RouteEntity):
            return NotImplemented
        return (
            self.distance == other.distance
            and self.duration == other.duration
            and self.name == other.name
            and self.location == other.location
            and self.destination == other.destination
        )

    def __hash__(self) -> int:
        return hash((self.name, self.location, self.destination, self.distance, self.duration))
