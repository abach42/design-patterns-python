from .barebone_product import BareboneProduct
from .builder import Builder, CoolerType


class BareboneConcreteBuilder(Builder):

    def add_cooler(self) -> Builder:
        self.cooler = CoolerType.SMALL
        return self

    def build(self) -> BareboneProduct:
        return BareboneProduct(self.cpu, self.ram_size, self.hard_disk_size, str(self.cooler))
