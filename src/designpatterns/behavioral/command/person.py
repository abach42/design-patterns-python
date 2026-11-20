from dataclasses import dataclass


@dataclass(frozen=True)
class Person:
    id: int | None
    name: str
    age: int | None
