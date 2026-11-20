from .strategy import Strategy


class AdditionStrategy(Strategy):

    def perform_operation(self, first_operand: int, second_operand: int) -> int:
        return first_operand + second_operand
