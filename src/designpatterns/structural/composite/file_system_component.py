from typing import Protocol


class FileSystemComponent(Protocol):

    def show_details(self) -> str: ...
