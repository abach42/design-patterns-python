from abc import ABC, abstractmethod
from enum import StrEnum


class CoolerType(StrEnum):
    SMALL = "SMALL"
    LARGE = "LARGE"


class Builder(ABC):

    cpu: str = ""
    ram_size: int = 0
    hard_disk_size: int = 0
    cooler: CoolerType | None = None

    @abstractmethod
    def add_cooler(self) -> "Builder": ...

    def set_cpu(self, cpu: str) -> "Builder":
        self.cpu = cpu
        return self

    def set_ram_size(self, ram_size: int) -> "Builder":
        self.ram_size = ram_size
        return self

    def set_hard_disk_size(self, hard_disk_size: int) -> "Builder":
        self.hard_disk_size = hard_disk_size
        return self
