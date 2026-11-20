from .strategy import Strategy


class CalculatorContext:

    def __init__(self) -> None:
        self._strategy: Strategy | None = None

    def set_behavior(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def calculate(self, first_operand: int, second_operand: int) -> int:
        return self._strategy.perform_operation(first_operand, second_operand)
