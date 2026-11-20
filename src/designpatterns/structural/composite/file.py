from .file_system_component import FileSystemComponent


# Leaf
class File(FileSystemComponent):

    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    def show_details(self) -> str:
        return f" File: {self.name} (Size: {self.size} KB)"
