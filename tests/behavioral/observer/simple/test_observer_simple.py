import pytest

from designpatterns.behavioral.observer.simple.calculate_distance_observer import (
    CalculateDistanceObserver,
)
from designpatterns.behavioral.observer.simple.calculate_duration_observer import (
    CalculateDurationObserver,
)
from designpatterns.behavioral.observer.simple.concrete_routing_subject import ConcreteRoutingSubject
from designpatterns.behavioral.observer.simple.route_entity import RouteEntity
from designpatterns.geometry import Point


def test_observers_listen_and_change_routing_information() -> None:
    subject = ConcreteRoutingSubject()
    CalculateDistanceObserver(subject)
    CalculateDurationObserver(subject)

    route = RouteEntity("way home", Point(0, 0), Point(20, 20))
    subject.set_state_entity(route)

    assert route.distance == pytest.approx(28.284271, abs=0.000001)
    assert route.duration == pytest.approx(5.656854, abs=0.000001)


def test_observer_order_does_not_matter() -> None:
    subject = ConcreteRoutingSubject()
    CalculateDurationObserver(subject)
    CalculateDistanceObserver(subject)

    route = RouteEntity("way home", Point(0, 0), Point(20, 20))
    subject.set_state_entity(route)

    assert route.distance == pytest.approx(28.284271, abs=0.000001)
    assert route.duration == pytest.approx(5.656854, abs=0.000001)


def test_observers_listen_and_change_partly() -> None:
    subject = ConcreteRoutingSubject()
    CalculateDistanceObserver(subject)
    duration_observer = CalculateDurationObserver(subject)
    subject.detach_observer(duration_observer)

    route = RouteEntity("way home", Point(0, 0), Point(20, 20))
    subject.set_state_entity(route)

    assert route.distance == pytest.approx(28.284271, abs=0.000001)
    assert route.duration == 0.0
