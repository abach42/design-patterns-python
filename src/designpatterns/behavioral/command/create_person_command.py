from .command import Command
from .person_receiver import PersonReceiver


class CreatePersonCommand(Command):

    def __init__(self, receiver: PersonReceiver, name: str, age: int | None) -> None:
        self._receiver = receiver
        self._name = name
        self._age = age

    def execute(self) -> None:
        self._receiver.create_person(self._name, self._age)
