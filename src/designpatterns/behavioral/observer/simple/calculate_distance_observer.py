from .abstract_observer import AbstractObserver


class CalculateDistanceObserver(AbstractObserver):

    def update(self) -> None:
        entity = self.subject.get_state_entity()
        entity.distance = entity.calculate_distance()
