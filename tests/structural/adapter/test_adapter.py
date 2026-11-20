from collections.abc import Iterable

from designpatterns.structural.adapter.api_adapter import ApiAdapter
from designpatterns.structural.adapter.api_adaptee import ApiAdaptee
from designpatterns.structural.adapter.stream_adapter import StreamAdapter
from designpatterns.structural.adapter.stream_adaptee import StreamAdaptee
from designpatterns.structural.adapter.target import Record, Target


def test_api_adapter() -> None:
    fake_api_adaptee: ApiAdaptee[str] = lambda: '{"id": 42, "name": "John Doe"}'
    target: Target[Record] = ApiAdapter(fake_api_adaptee)
    actual_record = target.fetch_data()

    expected_record = Record(42, "John Doe")

    assert actual_record == expected_record


def test_stream_adapter() -> None:
    fake_stream_adaptee: StreamAdaptee[Iterable[str]] = lambda: iter(["42,John Doe"])
    target: Target[Record] = StreamAdapter(fake_stream_adaptee)
    actual_record = target.fetch_data()

    expected_record = Record(42, "John Doe")

    assert actual_record == expected_record
