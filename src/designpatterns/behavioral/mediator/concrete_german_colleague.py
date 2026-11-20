from .colleague import Colleague


class ConcreteGermanColleague(Colleague):

    def receive(self, message: str) -> None:
        self.last_received_message = f"Hallo Welt: {message}"
