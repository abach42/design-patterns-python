from .concrete_flyweight import ConcreteFlyweight
from .flyweight import Flyweight


class FlyweightFactory:

    def __init__(self) -> None:
        self._pool: dict[str, Flyweight] = {}

    def get_flyweight(self, key: str) -> Flyweight:
        if key not in self._pool:
            self._pool[key] = ConcreteFlyweight(key)
        return self._pool[key]

    def pool_size(self) -> int:
        return len(self._pool)
