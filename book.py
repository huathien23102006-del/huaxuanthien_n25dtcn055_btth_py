from abc import ABC, abstractmethod


class PersonOrObject(ABC):
    @abstractmethod
    def show_info(self):
        pass

class Book(PersonOrObject):
    def __init__(self, id, title, author, quantity):
        self.__id = id
        self.__title = title
        self.__author = author
        self.__quantity = quantity

    @property
    def id(self):
        return self.__id

    @property
    def quantity(self):
        return self.__quantity

    def borrow(self):
        if self.__quantity > 0:
            self.__quantity -= 1
            return True
        return False

    def return_book(self):
        self.__quantity += 1

    def show_info(self):
        print(
            f"{self.__id} | {self.__title} | {self.__author} | {self.__quantity}"
        )