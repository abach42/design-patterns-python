import pytest

from designpatterns.behavioral.visitor.elephant_element import ElephantElement
from designpatterns.behavioral.visitor.feeding_visitor import FeedingVisitor
from designpatterns.behavioral.visitor.lion_element import LionElement
from designpatterns.behavioral.visitor.object_structure import ObjectStructure
from designpatterns.behavioral.visitor.veterinarian_visitor import VeterinarianVisitor


@pytest.fixture
def zoo() -> ObjectStructure:
    zoo = ObjectStructure()
    zoo.add_animal(LionElement())
    zoo.add_animal(ElephantElement())
    return zoo


def test_feed_animals(zoo: ObjectStructure) -> None:
    zoo.visit_animals(FeedingVisitor())

    for animal in zoo.animals:
        assert animal.fed_up


def test_care_animals(zoo: ObjectStructure) -> None:
    zoo.visit_animals(VeterinarianVisitor())

    for animal in zoo.animals:
        assert animal.health_checked
