from .inventory_manager import InventoryManager
from .payment_processor import PaymentProcessor
from .shipping_service import ShippingService


class OrderFacade:

    def __init__(self) -> None:
        self.payment_processor = PaymentProcessor()
        self.inventory_manager = InventoryManager()
        self.shipping_service = ShippingService()

    def place_order(self, product: str, quantity: int, amount: float) -> str:
        if not self.inventory_manager.check_stock(product, quantity):
            return "Order failed: not enough stock"
        if not self.payment_processor.process_payment(amount):
            return "Order failed: payment declined"
        return self.shipping_service.ship_product(product, quantity)
