import pytest

from designpatterns.behavioral.command.create_person_command import CreatePersonCommand
from designpatterns.behavioral.command.delete_person_command import DeletePersonCommand
from designpatterns.behavioral.command.person import Person
from designpatterns.behavioral.command.person_invoker import PersonInvoker
from designpatterns.behavioral.command.person_receiver import PersonReceiver
from designpatterns.behavioral.command.update_person_command import UpdatePersonCommand


@pytest.fixture
def invoker() -> PersonInvoker:
    return PersonInvoker()


@pytest.fixture
def receiver() -> PersonReceiver:
    return PersonReceiver()


def test_create_command(invoker: PersonInvoker, receiver: PersonReceiver) -> None:
    invoker.add_command(CreatePersonCommand(receiver, "John", 62))
    invoker.run_commands()

    assert receiver.get_persons() == [Person(1, "John", 62)]


def test_create_command_create_multiple_elements(invoker: PersonInvoker, receiver: PersonReceiver) -> None:
    invoker.add_command(CreatePersonCommand(receiver, "John", 62))
    invoker.add_command(CreatePersonCommand(receiver, "Peter", 43))
    invoker.add_command(CreatePersonCommand(receiver, "James", 21))
    invoker.run_commands()

    assert receiver.get_persons() == [
        Person(1, "John", 62),
        Person(2, "Peter", 43),
        Person(3, "James", 21),
    ]


def test_update_element(invoker: PersonInvoker, receiver: PersonReceiver) -> None:
    invoker.add_command(CreatePersonCommand(receiver, "Saul", 62))
    invoker.add_command(CreatePersonCommand(receiver, "Peter", 43))
    invoker.add_command(UpdatePersonCommand(receiver, Person(1, "Paul", 34)))
    invoker.run_commands()

    assert receiver.get_persons() == [Person(1, "Paul", 34), Person(2, "Peter", 43)]


def test_update_of_unknown_id_fails(invoker: PersonInvoker, receiver: PersonReceiver) -> None:
    invoker.add_command(UpdatePersonCommand(receiver, Person(1, "Paul", 34)))

    with pytest.raises(LookupError):
        invoker.run_commands()


def test_update_without_id_fails(invoker: PersonInvoker, receiver: PersonReceiver) -> None:
    invoker.add_command(UpdatePersonCommand(receiver, Person(None, "Paul", 34)))

    with pytest.raises(ValueError, match="Person needs an Id to be updated"):
        invoker.run_commands()


def test_ids_stay_unique_after_update_and_delete(invoker: PersonInvoker, receiver: PersonReceiver) -> None:
    invoker.add_command(CreatePersonCommand(receiver, "John", 62))
    invoker.add_command(CreatePersonCommand(receiver, "Peter", 43))
    invoker.add_command(UpdatePersonCommand(receiver, Person(1, "Paul", 34)))
    invoker.add_command(DeletePersonCommand(receiver, 2))
    invoker.add_command(CreatePersonCommand(receiver, "James", 21))
    invoker.run_commands()

    assert receiver.get_persons() == [Person(1, "Paul", 34), Person(3, "James", 21)]


def test_delete_element(invoker: PersonInvoker, receiver: PersonReceiver) -> None:
    invoker.add_command(CreatePersonCommand(receiver, "Peter", 62))
    invoker.add_command(DeletePersonCommand(receiver, 1))
    invoker.run_commands()

    assert receiver.get_persons() == []


def test_delete_of_unknown_id_fails(invoker: PersonInvoker, receiver: PersonReceiver) -> None:
    invoker.add_command(DeletePersonCommand(receiver, 1))

    with pytest.raises(LookupError):
        invoker.run_commands()


def test_commands_run_only_once(invoker: PersonInvoker, receiver: PersonReceiver) -> None:
    invoker.add_command(CreatePersonCommand(receiver, "John", 62))
    invoker.run_commands()
    invoker.run_commands()

    assert receiver.get_persons() == [Person(1, "John", 62)]
