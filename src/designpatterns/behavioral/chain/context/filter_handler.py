from .abstract_handler import AbstractHandler, MemberList


class FilterHandler(AbstractHandler):

    def __init__(self, data: MemberList, min_age: int = 40) -> None:
        super().__init__(data)
        self.min_age = min_age

    def handle(self) -> None:
        if not self.data:
            self.handle_next()
            return

        # removes the members younger than min_age
        self.data[:] = [member for member in self.data if member.age >= self.min_age]

        self.handle_next()
