from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .colleague import Colleague


class Mediator:

    def __init__(self) -> None:
        self._colleagues: list[Colleague] = []

    def add_colleague(self, colleague: Colleague) -> None:
        self._colleagues.append(colleague)

    def send_message(self, message: str, colleague: Colleague) -> None:
        for col in self._colleagues:
            if col is not colleague:
                col.receive(message)
