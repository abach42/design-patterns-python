from .property_change_event import PropertyChangeEvent, PropertyChangeListener
from .route_entity import RouteEntity
from .subject import Subject


class ConcreteRoutingSubject(Subject):

    def __init__(self) -> None:
        self._route_entity: RouteEntity | None = None
        self._listeners: list[PropertyChangeListener] = []

    def set_route_entity(self, route_entity: RouteEntity) -> None:
        old_value = self._route_entity
        self._route_entity = route_entity
        subject_name = type(self).__name__

        event = PropertyChangeEvent(subject_name, old_value, route_entity)
        for listener in self._listeners:
            listener.property_change(event)

    def get_route_entity(self) -> RouteEntity | None:
        return self._route_entity

    def attach_observer(self, listener: PropertyChangeListener) -> None:
        self._listeners.append(listener)

    def detach_observer(self, listener: PropertyChangeListener) -> None:
        # like java.beans.PropertyChangeSupport: detaching an unknown listener is a no-op
        if listener in self._listeners:
            self._listeners.remove(listener)
