from collections.abc import Callable

# functional interface: a callable that fetches data from a stream
type StreamAdaptee[T] = Callable[[], T]
