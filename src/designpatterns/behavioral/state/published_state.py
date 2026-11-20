from __future__ import annotations

from typing import TYPE_CHECKING

from .archive_state import ArchiveState
from .state import State

if TYPE_CHECKING:
    from .document import Document


class PublishedState(State):

    def publish(self, document: Document) -> None:
        raise RuntimeError("Document already is published")

    def archive(self, context: Document) -> None:
        context.state = ArchiveState()

    @property
    def name(self) -> str:
        return "Published"
