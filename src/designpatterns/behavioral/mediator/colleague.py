from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .mediator import Mediator


class Colleague(ABC):

    def __init__(self, mediator: Mediator) -> None:
        self.mediator = mediator
        self.last_received_message: str | None = None

    @abstractmethod
    def receive(self, message: str) -> None: ...

    def send(self, message: str) -> None:
        self.mediator.send_message(message, self)
