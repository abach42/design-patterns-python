from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from .abstract_observer import AbstractObserver
    from .route_entity import RouteEntity


class Subject(Protocol):

    def attach_observer(self, observer: AbstractObserver) -> None: ...

    def detach_observer(self, observer: AbstractObserver) -> None: ...

    def notify_observers(self) -> None: ...

    def set_state_entity(self, entity: RouteEntity) -> None: ...

    def get_state_entity(self) -> RouteEntity | None: ...
