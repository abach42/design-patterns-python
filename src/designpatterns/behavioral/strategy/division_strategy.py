from .strategy import Strategy


class DivisionStrategy(Strategy):

    def perform_operation(self, first_operand: int, second_operand: int) -> int:
        if second_operand == 0:
            raise ZeroDivisionError("Division by zero")
        return first_operand // second_operand
