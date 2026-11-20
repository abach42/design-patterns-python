from dataclasses import dataclass
from typing import Protocol, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class Record:
    id: int | None
    name: str | None


class Target(Protocol[T]):

    def fetch_data(self) -> T: ...
