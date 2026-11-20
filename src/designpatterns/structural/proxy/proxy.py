from .real_subject import RealSubject
from .subject import Subject


class Proxy(Subject):

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject
        self._accessed = False

    def get_data(self) -> str:
        self._accessed = True
        return self._real_subject.get_data()

    def was_accessed(self) -> bool:
        return self._accessed
