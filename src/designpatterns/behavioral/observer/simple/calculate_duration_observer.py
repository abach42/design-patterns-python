from .abstract_observer import AbstractObserver
from .route_entity import RouteEntity


class CalculateDurationObserver(AbstractObserver):

    SPEED = 5

    def update(self) -> None:
        entity = self.subject.get_state_entity()
        entity.duration = self._calculate_duration(entity)

    # does not read the distance another observer wrote: the order of observers must not matter
    def _calculate_duration(self, entity: RouteEntity) -> float:
        return entity.calculate_distance() / self.SPEED
