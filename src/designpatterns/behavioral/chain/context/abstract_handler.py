from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class Member:
    name: str
    age: int


class MemberList(list[Member]):
    pass


class AbstractHandler(ABC):

    def __init__(self, data: MemberList) -> None:
        self.next: AbstractHandler | None = None
        self.data = data

    def set_next(self, next: AbstractHandler) -> None:
        self.next = next

    @abstractmethod
    def handle(self) -> None: ...

    @staticmethod
    def initialize_chain(first_handler: AbstractHandler, *more_handlers: AbstractHandler) -> AbstractHandler:
        handler = first_handler
        for next_handler in more_handlers:
            handler.set_next(next_handler)
            handler = next_handler

        return first_handler

    def handle_next(self) -> None:
        if self.next is not None:
            self.next.handle()
