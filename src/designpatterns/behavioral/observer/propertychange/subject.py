from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from .property_change_event import PropertyChangeListener

if TYPE_CHECKING:
    from .route_entity import RouteEntity


class Subject(Protocol):

    def set_route_entity(self, route_entity: RouteEntity) -> None: ...

    def get_route_entity(self) -> RouteEntity | None: ...

    def attach_observer(self, listener: PropertyChangeListener) -> None: ...

    def detach_observer(self, listener: PropertyChangeListener) -> None: ...
