from designpatterns.behavioral.memento.caretaker import Caretaker
from designpatterns.behavioral.memento.originator import Originator


def test_memento_change_and_restore_history() -> None:
    originator = Originator("foo")

    caretaker = Caretaker()
    originator.change_state("bar")
    caretaker.add_memento(originator.create_snapshot())
    originator.restore_snapshot(caretaker.get_memento(0))
    actual_foo_bar = originator.state

    originator.change_state("baz")
    caretaker.add_memento(originator.create_snapshot())
    originator.restore_snapshot(caretaker.get_memento(1))
    actual_foo_bar_baz = originator.state

    assert actual_foo_bar == "foo, bar"
    assert actual_foo_bar_baz == "foo, bar, baz"
