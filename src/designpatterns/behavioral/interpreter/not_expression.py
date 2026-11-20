from dataclasses import dataclass

from .context import Context
from .expression import Expression


# NonTerminalExpression
@dataclass(frozen=True)
class NotExpression(Expression):
    expression: Expression

    def interpret(self, context: Context) -> bool:
        return not self.expression.interpret(context)
