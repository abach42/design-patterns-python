from typing import Protocol


class Subject(Protocol):

    def get_data(self) -> str: ...
