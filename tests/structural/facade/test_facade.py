from designpatterns.structural.facade.order_facade import OrderFacade


def test_order_facade_success() -> None:
    facade = OrderFacade()

    result = facade.place_order("Laptop", 2, 2000.0)

    assert result == "Shipping 2 units of Laptop"


def test_order_facade_stock_failure() -> None:
    facade = OrderFacade()

    result = facade.place_order("Laptop", 0, 2000.0)

    assert result == "Order failed: not enough stock"


def test_order_facade_payment_failure() -> None:
    facade = OrderFacade()

    result = facade.place_order("Laptop", 2, 0.0)

    assert result == "Order failed: payment declined"
