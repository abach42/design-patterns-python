from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from .chain import MemberList


class Handable(Protocol):

    def handle(self, member_list: MemberList) -> MemberList: ...
