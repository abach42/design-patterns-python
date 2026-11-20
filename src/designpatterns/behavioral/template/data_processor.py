from abc import ABC, abstractmethod
from typing import final


class DataProcessor[T](ABC):
    """Abstract class: owns the template method and the invariant steps."""

    def __init__(self) -> None:
        self._saved_data: list[T] = []

    # template method; @final, so subclasses cannot change the order of the steps
    @final
    def process_data(self) -> None:
        data_list = self.fetch_data()
        processed = self.process(data_list)
        self._save_data(processed)

    @property
    def saved_data(self) -> list[T]:
        return self._saved_data

    # primitive operation: every subclass must provide it
    @abstractmethod
    def fetch_data(self) -> list[T]: ...

    # hook: default keeps the data unchanged, subclasses may override
    def process(self, data_list: list[T]) -> list[T]:
        return data_list

    # invariant step: the same for every subclass
    def _save_data(self, data_list: list[T]) -> None:
        # simulates writing the data back to a database
        self._saved_data = list(data_list)
