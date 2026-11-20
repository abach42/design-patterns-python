from .file_system_component import FileSystemComponent


# Composite
class Folder(FileSystemComponent):

    def __init__(self, name: str) -> None:
        self.name = name
        self.components: list[FileSystemComponent] = []

    def add_component(self, component: FileSystemComponent) -> None:
        self.components.append(component)

    def remove_component(self, component: FileSystemComponent) -> None:
        self.components.remove(component)

    def show_details(self) -> str:
        details = f"Folder: {self.name}\n"
        for component in self.components:
            details += "  " + component.show_details() + "\n"
        return details
