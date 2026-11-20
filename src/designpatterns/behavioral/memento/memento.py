from dataclasses import dataclass


@dataclass(frozen=True)
class Memento:
    state: str
