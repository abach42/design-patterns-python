from .abstract_product_a import AbstractProductA


class ConcreteProductA1(AbstractProductA):

    def __init__(self) -> None:
        self.name = "ProductA1"
