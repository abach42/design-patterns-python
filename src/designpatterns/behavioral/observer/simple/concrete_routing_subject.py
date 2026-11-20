from __future__ import annotations

from .abstract_observer import AbstractObserver
from .route_entity import RouteEntity
from .subject import Subject


class ConcreteRoutingSubject(Subject):

    def __init__(self) -> None:
        self._observers: list[AbstractObserver] = []
        self._entity: RouteEntity | None = None
        self._entity_hash_code = 0

    def attach_observer(self, observer: AbstractObserver) -> None:
        self._observers.append(observer)

    def detach_observer(self, observer: AbstractObserver) -> None:
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()

    def set_state_entity(self, entity: RouteEntity) -> None:
        self._entity = entity

        if self._entity_hash_code != hash(entity):
            self.notify_observers()
            self._entity_hash_code = hash(entity)

    def get_state_entity(self) -> RouteEntity | None:
        return self._entity
