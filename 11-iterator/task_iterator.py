from abc import ABC, abstractmethod
from typing import Any, List
import time


class Iterator(ABC):
    @abstractmethod
    def next(self) -> Any:
        """Return the next item in the collection."""
        pass

    @abstractmethod
    def has_next(self) -> bool:
        """Return True if there are more items in the collection."""
        pass


class IterableCollection(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        """Return an iterator for the collection."""
        pass


class TaskList(IterableCollection):
    def __init__(self, tasks: List[Any]):
        self.__tasks = tasks

    def create_iterator(self) -> Iterator:
        return TaskIterator(self)

    def get_tasks(self) -> List[Any]:
        return self.__tasks


class TaskIterator(Iterator):
    def __init__(self, task_list: TaskList):
        self.__task_list = task_list
        self.__index = 0

    def next(self) -> Any:
        if self.has_next():
            task = self.__task_list.get_tasks()[self.__index]
            self.__index += 1
            return task()

    def has_next(self) -> bool:
        return self.__index < len(self.__task_list.get_tasks())


def task1():
    time.sleep(1)
    return "Task 1 completed"


def task2():
    time.sleep(2)
    return "Task 2 completed"


def task3():
    time.sleep(1.5)
    return "Task 3 completed"


task_list = TaskList([task1, task2, task3])
iterator = task_list.create_iterator()

while iterator.has_next():
    print(iterator.next())
# Salida esperada:
# Task 1 completed
# Task 2 completed
# Task 3 completed
# (con tiempos de espera entre cada tarea)
