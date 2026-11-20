from .strategy import Strategy


class MultiplicationStrategy(Strategy):

    def perform_operation(self, first_operand: int, second_operand: int) -> int:
        return first_operand * second_operand
