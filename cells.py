"""
Задание 3.
Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка (Cell).
В его конструкторе инициализировать параметр (quantity),
соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (add()),
вычитание (sub()),
умножение (mul()),
деление (truediv()).
Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток.
При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки.
Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
"""


class Cell:
    """
    Класс реализует работу с органическими клетками.
    """
    def __init__(self, quantity: int):
        self.quantity = quantity

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity > other.quantity:
            return Cell(self.quantity - other.quantity)
        return 'Операция не может быть выполнена.'

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        if self.quantity > other.quantity:
            return Cell(self.quantity // other.quantity)
        return 'Клетка не может быть разделена.'

    def __str__(self):
        return f'{self.quantity}'

    def make_order(self, row):
        """
        Метод позволяет организовать ячейки экземпляра класса по рядам.
        Возвращается строка вида *****\n*****\n*****....

        :param self: Экземпляр класса.
        :param row: Количество ячеек в ряду.
        :return: Строка, разбитая на подстроки по row ячеек.
        """
        order_str = ''
        for i in range(self.quantity // row):
            order_str += "*" * row + "\n"
        return order_str + "*" * (self.quantity % row)


print("Создаем объекты клеток")
cell_1 = Cell(30)
cell_2 = Cell(25)
cell_3 = Cell(10)
cell_4 = Cell(15)
print()

print("Складываем:")
print(cell_1 + cell_2)
print()

print("Вычитаем:")
print(cell_2 - cell_1)
print(cell_4 - cell_3)
print()

print("Умножаем:")
print(cell_2 * cell_1)
print()

print("Делим:")
print(cell_1 / cell_2)
print()

print("Организация ячеек по рядам:")
print(cell_1.make_order(5))
print(cell_2.make_order(10))
