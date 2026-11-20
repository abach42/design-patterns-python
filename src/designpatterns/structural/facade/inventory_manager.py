class InventoryManager:

    def check_stock(self, product: str | None, quantity: int) -> bool:
        return quantity > 0 and product is not None
