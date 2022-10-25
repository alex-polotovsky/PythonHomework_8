"""
Задание 2.
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Единственный класс этого проекта — одежда (класс Clothes).
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property
Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57
Два класса: абстрактный и Clothes
"""

from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    """
    Класс описывает интерфейс класса Clothes.
    """

    usage = 0

    @property
    @abstractmethod
    def height(self):
        """
        Функция должна позволять получить значение атрибута height.
        :return: __self.height
        """

    @height.setter
    @abstractmethod
    def height(self, height_suit):
        pass

    @property
    @abstractmethod
    def size(self):
        """
        Функция должна позволять получить значение атрибута size.
        :return: __self.size
        """

    @size.setter
    @abstractmethod
    def size(self, size_coat):
        pass

    @abstractmethod
    def coat_usage(self):
        """
        Функция должна подсчитывать расход ткани на пальто,
        а также добавлять этот расход к общему расходу.
        :return:
        """
        print('Расход ткани на пальто = ', self.usage)
        Clothes.usage += self.usage

    @abstractmethod
    def suit_usage(self):
        """
        Функция должна подсчитывать расход ткани на костюм,
        а также добавлять этот расход к общему расходу.
         :return:
         """
        print('Расход ткани на костюм = ', self.usage)
        Clothes.usage += self.usage


class Clothes(AbstractClothes):
    """
    Класс реализует учёт расхода ткани на отдельные пальто и костюмы,
    а также может отобразить общий расход ткани.
    """

    def __init__(self, height=0, size=0):
        self.__height = height
        self.__size = size

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    def coat_usage(self):
        self.usage = round(self.__size / 6.5 + 0.5, 2)
        super().coat_usage()

    def suit_usage(self):
        self.usage = round(2 * self.__height + 0.3, 2)
        super().suit_usage()


coat_1 = Clothes()
coat_1.size = 48
print(coat_1.size)
coat_1.coat_usage()

coat_2 = Clothes()
coat_2.size = 52
print(coat_2.size)
coat_2.coat_usage()

print('Общий расход ткани = ', Clothes.usage)
