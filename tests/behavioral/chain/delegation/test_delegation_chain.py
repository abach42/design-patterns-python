from unittest.mock import MagicMock

from designpatterns.behavioral.chain.delegation.chain import Chain, Member, MemberList
from designpatterns.behavioral.chain.delegation.filter_handler import FilterHandler
from designpatterns.behavioral.chain.delegation.handable import Handable
from designpatterns.behavioral.chain.delegation.sort_by_age_handler import SortByAgeHandler


def test_chain_not_handles_if_empty() -> None:
    member_list = MemberList()
    handler_mock = MagicMock(spec=Handable)
    handler_mock.handle.assert_not_called()

    Chain().add(SortByAgeHandler()).process(member_list)

    assert member_list == []


def test_chain_sorts_data() -> None:
    member_list = MemberList([Member("John", 50), Member("Doe", 62), Member("Marilyn", 32)])

    Chain().add(SortByAgeHandler()).process(member_list)

    assert member_list[0] == Member("Marilyn", 32)


def test_chain_filters_data() -> None:
    member_list = MemberList([Member("John", 50), Member("Doe", 62), Member("Marilyn", 32)])

    Chain().add(FilterHandler(40)).process(member_list)

    assert Member("Marilyn", 32) not in member_list
