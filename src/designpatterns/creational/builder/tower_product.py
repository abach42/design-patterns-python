from dataclasses import dataclass


@dataclass(frozen=True)
class TowerProduct:
    cpu: str
    ram_size: int
    hard_disk_size: int
    cooler: str

    def __str__(self) -> str:
        return (
            f"TowerProduct[cpu={self.cpu},ram_size={self.ram_size},"
            f"hard_disk_size={self.hard_disk_size},cooler={self.cooler}]"
        )
