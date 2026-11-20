import pytest

from designpatterns.behavioral.chain.simple.first_handler import FirstHandler
from designpatterns.behavioral.chain.simple.second_handler import SecondHandler


def test_simple_chain_returns_console_output(capsys: pytest.CaptureFixture[str]) -> None:
    first_handler = FirstHandler()
    second_handler = SecondHandler()
    first_handler.set_next(second_handler)
    first_handler.handle()

    captured = capsys.readouterr()
    assert captured.out == "first handler\nsecond handler\n"
