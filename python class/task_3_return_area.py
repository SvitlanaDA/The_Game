"""Метод екземпляра
Задача:

Модифікуйте клас Rectangle із Завдання 2, щоб включити метод area(), 
який обчислює та повертає площу прямокутника (ширина * висота)
Створіть екземпляр і викличте метод area(), щоб отримати площу прямокутника"""

class Rectangle:
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)

    def area(self):
        """Обчислити та повернути площу прямокутника."""
        return self.width * self.height
    
    def display_info(self):
            print(f"Area: {self.area()}")
    
my_rectangle = Rectangle(5, 10)
my_rectangle.display_info()
           