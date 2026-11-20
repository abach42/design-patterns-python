from .builder import Builder


class Director:

    def construct_basic_computer(self, builder: Builder) -> None:
        builder.set_cpu("Intel Core i3") \
            .set_ram_size(16) \
            .set_hard_disk_size(500) \
            .add_cooler()

    def construct_gaming_computer(self, builder: Builder) -> None:
        builder.set_cpu("Intel Core i9") \
            .set_ram_size(64) \
            .set_hard_disk_size(2000) \
            .add_cooler()
