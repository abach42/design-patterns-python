from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .subject import Subject


class AbstractObserver(ABC):

    def __init__(self, subject: Subject) -> None:
        subject.attach_observer(self)
        self.subject = subject

    @abstractmethod
    def update(self) -> None: ...
