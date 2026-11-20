from collections.abc import Mapping
from dataclasses import dataclass


@dataclass(frozen=True)
class Context:
    variables: Mapping[str, bool]

    def lookup(self, name: str) -> bool:
        return self.variables.get(name, False)
