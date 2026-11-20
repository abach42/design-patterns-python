from abc import ABC, abstractmethod


class AbstractHandler(ABC):

    next: AbstractHandler | None = None

    def set_next(self, next: AbstractHandler) -> None:
        self.next = next

    @abstractmethod
    def handle(self) -> None: ...

    def handle_next(self) -> None:
        if self.next is not None:
            self.next.handle()
