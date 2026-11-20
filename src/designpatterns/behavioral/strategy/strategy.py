from typing import Protocol


class Strategy(Protocol):

    def perform_operation(self, first_operand: int, second_operand: int) -> int: ...
