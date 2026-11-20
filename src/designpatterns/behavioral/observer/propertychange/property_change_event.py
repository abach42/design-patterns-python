from dataclasses import dataclass
from typing import Protocol


# stand-in for java.beans.PropertyChangeEvent / PropertyChangeListener
@dataclass(frozen=True)
class PropertyChangeEvent[T]:
    property_name: str
    old_value: T | None
    new_value: T


class PropertyChangeListener(Protocol):

    def property_change(self, event: PropertyChangeEvent) -> None: ...
