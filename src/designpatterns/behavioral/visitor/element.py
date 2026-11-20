from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from .visitor import Visitor


class Element(Protocol):

    def accept(self, visitor: Visitor) -> None: ...

    @property
    def fed_up(self) -> bool: ...

    @property
    def health_checked(self) -> bool: ...
