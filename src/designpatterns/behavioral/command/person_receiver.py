from .person import Person


class PersonReceiver:
    """Receiver: knows how to carry out the operations behind a request.
    It knows nothing about commands."""

    def __init__(self) -> None:
        self._persons: dict[int, Person] = {}
        self._last_id = 0

    def create_person(self, name: str, age: int | None) -> Person:
        self._last_id += 1
        person = Person(self._last_id, name, age)
        self._persons[self._last_id] = person
        return person

    def update_person(self, person: Person) -> None:
        if person.id is None:
            raise ValueError("Person needs an Id to be updated")
        self._require_existing(person.id)
        self._persons[person.id] = person

    def delete_person(self, id: int) -> None:
        self._require_existing(id)
        del self._persons[id]

    def get_persons(self) -> list[Person]:
        return list(self._persons.values())

    def _require_existing(self, id: int) -> None:
        if id not in self._persons:
            raise LookupError(f"No person with Id {id}")
