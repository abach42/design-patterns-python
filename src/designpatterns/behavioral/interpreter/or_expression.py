from dataclasses import dataclass

from .context import Context
from .expression import Expression


# NonTerminalExpression
@dataclass(frozen=True)
class OrExpression(Expression):
    first: Expression
    second: Expression

    def interpret(self, context: Context) -> bool:
        return self.first.interpret(context) or self.second.interpret(context)
