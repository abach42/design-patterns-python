from __future__ import annotations

from typing import TYPE_CHECKING

from .published_state import PublishedState
from .state import State

if TYPE_CHECKING:
    from .document import Document


class DraftState(State):

    def publish(self, context: Document) -> None:
        context.state = PublishedState()

    def archive(self, context: Document) -> None:
        raise RuntimeError("DraftState can't be archived directly")

    @property
    def name(self) -> str:
        return "Draft"
