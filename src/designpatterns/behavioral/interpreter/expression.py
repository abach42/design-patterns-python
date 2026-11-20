from typing import Protocol

from .context import Context


class Expression(Protocol):

    def interpret(self, context: Context) -> bool: ...
