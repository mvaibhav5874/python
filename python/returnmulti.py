from typing import Tuple


class Book:
    def __init__(self, name: str, price_per_unit: float, quantity: int = 0):
        self.name = name
        self.price_per_unit = price_per_unit
        self.quantity = quantity

    def total_cost(self) -> tuple[float, float]:
        return (self.price_per_unit * self.quantity,self.price_per_unit/self.quantity)
book2 = Book("Introduction to Data Science", 675, 7)
book = Book("rich dad and poor dad", 1002, 8)
print(book2.name)
print(book.name)
print(book.total_cost())
print(book2.total_cost())