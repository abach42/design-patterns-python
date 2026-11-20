from unittest.mock import MagicMock

from designpatterns.behavioral.chain.context.abstract_handler import (
    AbstractHandler,
    Member,
    MemberList,
)
from designpatterns.behavioral.chain.context.filter_handler import FilterHandler
from designpatterns.behavioral.chain.context.sort_by_age_handler import SortByAgeHandler


def test_chain_not_handles_if_empty() -> None:
    member_list = MemberList()
    handler_mock = MagicMock(spec=AbstractHandler)
    handler_mock.handle.assert_not_called()

    subject = AbstractHandler.initialize_chain(handler_mock)

    subject.handle()
    assert member_list == []


def test_chain_sorts_data() -> None:
    member_list = MemberList([Member("Doe", 62), Member("Marilyn", 32), Member("John", 50)])

    subject = AbstractHandler.initialize_chain(SortByAgeHandler(member_list))

    subject.handle()
    assert member_list[0] == Member("Marilyn", 32)


def test_chain_filters_data() -> None:
    member_list = MemberList([Member("Doe", 62), Member("John", 50), Member("Marilyn", 32)])

    subject = AbstractHandler.initialize_chain(FilterHandler(member_list, 40))

    subject.handle()

    assert Member("Marilyn", 32) not in member_list
