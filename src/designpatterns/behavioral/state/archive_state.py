from __future__ import annotations

from typing import TYPE_CHECKING

from .state import State

if TYPE_CHECKING:
    from .document import Document


class ArchiveState(State):

    def publish(self, context: Document) -> None:
        raise RuntimeError("Archived documents cannot be published again.")

    def archive(self, context: Document) -> None:
        raise RuntimeError("Document already is archived.")

    @property
    def name(self) -> str:
        return "Archived"
