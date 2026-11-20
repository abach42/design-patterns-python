from collections.abc import Callable

# functional interface: a callable that fetches data from an external API
type ApiAdaptee[T] = Callable[[], T]
