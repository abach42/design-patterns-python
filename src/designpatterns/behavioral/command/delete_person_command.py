from .command import Command
from .person_receiver import PersonReceiver


class DeletePersonCommand(Command):

    def __init__(self, receiver: PersonReceiver, id: int) -> None:
        self._receiver = receiver
        self._id = id

    def execute(self) -> None:
        self._receiver.delete_person(self._id)
