from dataclasses import dataclass

from .context import Context
from .expression import Expression


# NonTerminalExpression
@dataclass(frozen=True)
class AndExpression(Expression):
    first: Expression
    second: Expression

    def interpret(self, context: Context) -> bool:
        return self.first.interpret(context) and self.second.interpret(context)
