from .chain import MemberList
from .handable import Handable


class FilterHandler(Handable):

    def __init__(self, min_age: int = 40) -> None:
        self.min_age = min_age

    def handle(self, member_list: MemberList) -> MemberList:
        if not member_list:
            return member_list

        # removes the members younger than min_age
        member_list[:] = [member for member in member_list if member.age >= self.min_age]

        return member_list
