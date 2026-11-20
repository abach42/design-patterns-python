from designpatterns.behavioral.mediator.concrete_german_colleague import ConcreteGermanColleague
from designpatterns.behavioral.mediator.concrete_polish_colleague import ConcretePolishColleague
from designpatterns.behavioral.mediator.mediator import Mediator


def test_mediator() -> None:
    mediator = Mediator()

    german_colleague = ConcreteGermanColleague(mediator)
    polish_colleague = ConcretePolishColleague(mediator)

    mediator.add_colleague(german_colleague)
    mediator.add_colleague(polish_colleague)

    german_colleague.send("Schönes Wetter!")
    polish_colleague.send("ładna pogoda!")

    assert polish_colleague.last_received_message == "Witaj świecie: Schönes Wetter!"
    assert german_colleague.last_received_message == "Hallo Welt: ładna pogoda!"
