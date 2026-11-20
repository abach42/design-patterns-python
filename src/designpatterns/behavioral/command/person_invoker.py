from collections import deque

from .command import Command


class PersonInvoker:

    def __init__(self) -> None:
        self._commands: deque[Command] = deque()

    def add_command(self, command: Command) -> None:
        self._commands.append(command)

    def run_commands(self) -> None:
        while self._commands:
            self._commands.popleft().execute()

    # todo implement undo of command
    # todo log errors
