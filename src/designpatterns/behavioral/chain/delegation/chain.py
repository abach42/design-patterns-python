from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .handable import Handable


@dataclass(frozen=True)
class Member:
    name: str
    age: int


class MemberList(list[Member]):
    pass


class Chain:

    def __init__(self) -> None:
        self._handlers: list[Handable] = []

    def add(self, handler: Handable) -> Chain:
        self._handlers.append(handler)
        return self

    def process(self, member_list: MemberList) -> MemberList:
        for handler in self._handlers:
            member_list = handler.handle(member_list)

        return member_list
