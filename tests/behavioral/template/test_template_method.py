from designpatterns.behavioral.template.product_data import ProductData
from designpatterns.behavioral.template.product_processor import ProductProcessor
from designpatterns.behavioral.template.user_data import UserData
from designpatterns.behavioral.template.user_processor import UserProcessor


def test_user_processor_overrides_hook() -> None:
    processor = UserProcessor()
    processor.process_data()

    assert processor.saved_data == [UserData("Alice"), UserData("John")]


def test_product_processor_uses_default_hook() -> None:
    processor = ProductProcessor()
    processor.process_data()

    assert processor.saved_data == [ProductData("Laptop", 999.0), ProductData("Phone", 599.0)]
