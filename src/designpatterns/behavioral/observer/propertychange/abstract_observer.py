from __future__ import annotations

from abc import ABC
from collections.abc import Callable
from typing import TYPE_CHECKING, TypeVar

from .property_change_event import PropertyChangeEvent, PropertyChangeListener
from .route_entity import RouteEntity

if TYPE_CHECKING:
    from .subject import Subject

O = TypeVar("O", bound="AbstractObserver")


class AbstractObserver(ABC, PropertyChangeListener):

    def __init__(self, subject: Subject) -> None:
        self.subject = subject
        self.entity = subject.get_route_entity()
        self.visitor: Callable[[RouteEntity], None]

    @classmethod
    def create_and_attach(cls, observer: O) -> O:
        observer.subject.attach_observer(observer)
        return observer

    def property_change(self, event: PropertyChangeEvent[RouteEntity]) -> None:
        subject_name = type(self.subject).__name__

        if subject_name == event.property_name:
            self.visitor(event.new_value)
