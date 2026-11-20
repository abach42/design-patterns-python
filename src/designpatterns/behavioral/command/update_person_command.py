from .command import Command
from .person import Person
from .person_receiver import PersonReceiver


class UpdatePersonCommand(Command):

    def __init__(self, receiver: PersonReceiver, person: Person) -> None:
        self._receiver = receiver
        self._person = person

    def execute(self) -> None:
        self._receiver.update_person(self._person)
