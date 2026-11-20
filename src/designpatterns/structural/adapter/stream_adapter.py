from collections.abc import Iterable

from .stream_adaptee import StreamAdaptee
from .target import Record, Target


class StreamAdapter(Target[Record]):

    def __init__(self, stream_adaptee: StreamAdaptee[Iterable[str]]) -> None:
        self._stream_adaptee = stream_adaptee

    def fetch_data(self) -> Record:
        for line in self._stream_adaptee():
            parts = line.split(",")
            return Record(int(parts[0]), parts[1])

        return Record(None, None)
