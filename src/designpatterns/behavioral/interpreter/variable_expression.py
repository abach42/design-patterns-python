from dataclasses import dataclass

from .context import Context
from .expression import Expression


# TerminalExpression
@dataclass(frozen=True)
class VariableExpression(Expression):
    name: str

    def interpret(self, context: Context) -> bool:
        return context.lookup(self.name)
