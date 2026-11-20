from .abstract_observer import AbstractObserver
from .concrete_routing_subject import ConcreteRoutingSubject
from .route_entity import RouteEntity


class CalculateDistanceObserver(AbstractObserver):

    def __init__(self, subject: ConcreteRoutingSubject) -> None:
        super().__init__(subject)

        def visit(route_entity: RouteEntity) -> None:
            route_entity.distance = route_entity.calculate_distance()

        self.visitor = visit
