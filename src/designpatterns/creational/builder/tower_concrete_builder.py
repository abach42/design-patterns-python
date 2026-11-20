from .builder import Builder, CoolerType
from .tower_product import TowerProduct


class TowerConcreteBuilder(Builder):

    def add_cooler(self) -> Builder:
        self.cooler = CoolerType.LARGE
        return self

    def build(self) -> TowerProduct:
        return TowerProduct(self.cpu, self.ram_size, self.hard_disk_size, str(self.cooler))
