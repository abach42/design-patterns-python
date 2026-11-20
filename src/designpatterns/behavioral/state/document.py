from .draft_state import DraftState
from .state import State


class Document:

    def __init__(self) -> None:
        self.state: State = DraftState()

    def publish(self) -> None:
        self.state.publish(self)

    def archive(self) -> None:
        self.state.archive(self)

    @property
    def state_name(self) -> str:
        return self.state.name
