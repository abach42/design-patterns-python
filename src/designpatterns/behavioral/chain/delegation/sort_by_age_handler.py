from .chain import MemberList
from .handable import Handable


class SortByAgeHandler(Handable):

    def handle(self, member_list: MemberList) -> MemberList:
        if not member_list:
            return member_list

        member_list.sort(key=lambda member: member.age)

        return member_list
