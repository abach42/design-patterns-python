from .data_processor import DataProcessor
from .product_data import ProductData


# uses the default of the process hook: products are saved as fetched
class ProductProcessor(DataProcessor[ProductData]):

    def fetch_data(self) -> list[ProductData]:
        # simulates reading products from a database
        return [ProductData("Laptop", 999.0), ProductData("Phone", 599.0)]
