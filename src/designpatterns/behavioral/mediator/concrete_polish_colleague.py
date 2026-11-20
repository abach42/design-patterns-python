from .colleague import Colleague


class ConcretePolishColleague(Colleague):

    def receive(self, message: str) -> None:
        self.last_received_message = f"Witaj świecie: {message}"
