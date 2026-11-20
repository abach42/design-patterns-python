from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from .document import Document


class State(Protocol):

    def publish(self, context: Document) -> None: ...

    def archive(self, context: Document) -> None: ...

    @property
    def name(self) -> str: ...
