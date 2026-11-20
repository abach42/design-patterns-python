from designpatterns.structural.composite.file import File
from designpatterns.structural.composite.folder import Folder


def test_composite_pattern() -> None:
    file1 = File("file1.txt", 120)
    file2 = File("file2.txt", 200)
    file3 = File("file3.txt", 50)
    folder1 = Folder("Folder1")
    folder2 = Folder("Folder2")

    # add files to folder1
    folder1.add_component(file1)
    folder1.add_component(file2)

    # add folder1 to folder2
    folder2.add_component(folder1)

    # add file3 directly to folder2
    folder2.add_component(file3)

    expected_details = (
        "Folder: Folder2\n"
        "  Folder: Folder1\n"
        "   File: file1.txt (Size: 120 KB)\n"
        "   File: file2.txt (Size: 200 KB)\n"
        "\n"
        "   File: file3.txt (Size: 50 KB)\n"
    )  # indent could be managed, but simplicity of the cheat sheet is more important

    assert folder2.show_details() == expected_details
