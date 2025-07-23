from typing import Any, List
import time


class TaskList:
    def __init__(self, tasks: List[Any]):
        self.__tasks = tasks

    def __iter__(self):
        return TaskIterator(self)

    def get_tasks(self) -> List[Any]:
        return self.__tasks


class TaskIterator:
    def __init__(self, task_list: TaskList):
        self.__task_list = task_list
        self.__index = 0

    def __next__(self) -> Any:
        if self.has_next():
            task = self.__task_list.get_tasks()[self.__index]
            self.__index += 1
            return task()
        else:
            raise StopIteration

    def has_next(self) -> bool:
        return self.__index < len(self.__task_list.get_tasks())


def task1():
    time.sleep(1)
    return "Task 1 completed"


def task2():
    time.sleep(2)
    return "Task 2 completed"


def task3():
    time.sleep(3)
    return "Task 3 completed"


tasks = TaskList([task1, task2, task3])

for task in tasks:
    print(task)
# Salida esperada:
# Task 1 completed
# Task 2 completed
# Task 3 completed
