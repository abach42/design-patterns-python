from designpatterns.behavioral.interpreter.and_expression import AndExpression
from designpatterns.behavioral.interpreter.context import Context
from designpatterns.behavioral.interpreter.not_expression import NotExpression
from designpatterns.behavioral.interpreter.or_expression import OrExpression
from designpatterns.behavioral.interpreter.variable_expression import VariableExpression


def test_expression_tree_with_not() -> None:
    context = Context({"a": True, "b": False, "c": True})

    expression = AndExpression(
        VariableExpression("a"),
        NotExpression(
            OrExpression(
                VariableExpression("b"),
                VariableExpression("c"),
            )
        ),
    )

    assert expression.interpret(context) is False


def test_only_not_expression() -> None:
    context = Context({"a": False})

    expression = NotExpression(VariableExpression("a"))

    assert expression.interpret(context) is True
