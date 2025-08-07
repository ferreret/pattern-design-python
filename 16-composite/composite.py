# Patrón de diseño de tipo estructural

# Creas estructuras complejas a partir de estructuras más simples

from abc import ABC, abstractmethod


class FileComponent(ABC):
    @abstractmethod
    def show(self, space=0):
        pass


class FileLeaf(FileComponent):
    def __init__(self, name):
        self.__name = name

    def show(self, space=0):
        print(" " * space + f"- Archivo{self.__name}")


class FolderComposite(FileComponent):
    def __init__(self, name):
        self.__name = name
        self.__children = []

    def add(self, child: FileComponent):
        self.__children.append(child)

    def remove(self, child: FileComponent):
        self.__children.remove(child)

    def show(self, space=0):
        print(" " * space + f"- Carpeta{self.__name}")
        for child in self.__children:
            child.show(space + 2)


file1 = FileLeaf("1.txt")
file2 = FileLeaf("2.txt")
file3 = FileLeaf("3.txt")

root = FolderComposite("root")
folder1 = FolderComposite("folder1")

root.add(folder1)
folder1.add(file1)
folder1.add(file2)
folder1.add(file3)

root.show()
