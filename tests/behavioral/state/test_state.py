import pytest

from designpatterns.behavioral.state.document import Document


def test_valid_transitions() -> None:
    document = Document()
    assert document.state_name == "Draft"

    document.publish()
    assert document.state_name == "Published"

    document.archive()
    assert document.state_name == "Archived"


def test_invalid_transitions() -> None:
    document = Document()

    with pytest.raises(RuntimeError):
        document.archive()
    document.publish()

    with pytest.raises(RuntimeError):
        document.publish()
    document.archive()

    with pytest.raises(RuntimeError):
        document.publish()
    with pytest.raises(RuntimeError):
        document.archive()
