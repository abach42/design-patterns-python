from .abstract_handler import AbstractHandler, MemberList


class SortByAgeHandler(AbstractHandler):

    def __init__(self, data: MemberList) -> None:
        super().__init__(data)

    def handle(self) -> None:
        if not self.data:
            self.handle_next()
            return

        self.data.sort(key=lambda member: member.age)

        self.handle_next()
