import pytest

from designpatterns.behavioral.strategy.addition_strategy import AdditionStrategy
from designpatterns.behavioral.strategy.calculator_context import CalculatorContext
from designpatterns.behavioral.strategy.division_strategy import DivisionStrategy
from designpatterns.behavioral.strategy.multiplication_strategy import MultiplicationStrategy
from designpatterns.behavioral.strategy.strategy import Strategy
from designpatterns.behavioral.strategy.subtraction_strategy import SubtractionStrategy


def _context(strategy: Strategy) -> CalculatorContext:
    context = CalculatorContext()
    context.set_behavior(strategy)
    return context


@pytest.mark.parametrize(
    "name, context, operands, expected_result",
    [
        ("1+1", _context(AdditionStrategy()), (1, 1), 2),
        ("1-1", _context(SubtractionStrategy()), (1, 1), 0),
        ("2*3", _context(MultiplicationStrategy()), (2, 3), 6),
        ("4/2", _context(DivisionStrategy()), (4, 2), 2),
    ],
    ids=["1+1", "1-1", "2*3", "4/2"],
)
def test_strategy_calculates(
    name: str,
    context: CalculatorContext,
    operands: tuple[int, int],
    expected_result: int,
) -> None:
    actual_result = context.calculate(*operands)
    assert actual_result == expected_result


def test_division_by_zero_throws() -> None:
    calculator = CalculatorContext()
    calculator.set_behavior(DivisionStrategy())

    with pytest.raises(ZeroDivisionError, match="Division by zero"):
        calculator.calculate(1, 0)
