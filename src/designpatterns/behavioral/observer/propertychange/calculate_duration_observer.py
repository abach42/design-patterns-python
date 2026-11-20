from .abstract_observer import AbstractObserver
from .concrete_routing_subject import ConcreteRoutingSubject
from .route_entity import RouteEntity


class CalculateDurationObserver(AbstractObserver):

    SPEED = 5

    def __init__(self, subject: ConcreteRoutingSubject) -> None:
        super().__init__(subject)

        def visit(route_entity: RouteEntity) -> None:
            route_entity.duration = self._calculate_duration(route_entity)

        self.visitor = visit

    # does not read the distance another observer wrote: the order of observers must not matter
    def _calculate_duration(self, entity: RouteEntity) -> float:
        return entity.calculate_distance() / self.SPEED
