from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, id, name):
        self._id = id
        self._name = name

    @abstractmethod
    def show_info(self):
        pass

class Student(Person):
    def __init__(self, id, name, class_name):
        super().__init__(id, name)
        self.__class_name = class_name

    @property
    def id(self):
        return self._id

    def show_info(self):
        print(
            f"{self._id} | {self._name} | {self.__class_name}"
        )