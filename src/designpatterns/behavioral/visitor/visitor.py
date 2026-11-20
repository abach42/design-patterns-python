from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from .elephant_element import ElephantElement
    from .lion_element import LionElement


class Visitor(Protocol):
    # Python has no method overloading: each visit method is named after its element type

    def visit_lion(self, lion: LionElement) -> None: ...

    def visit_elephant(self, elephant: ElephantElement) -> None: ...
