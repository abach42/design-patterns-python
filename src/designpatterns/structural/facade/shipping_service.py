class ShippingService:

    def ship_product(self, product: str, quantity: int) -> str:
        return f"Shipping {quantity} units of {product}"
