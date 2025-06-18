"""Метод конструктора (init)
Задача:

Створіть клас Rectangle з наступними атрибутами:
width (ціле число)
height (ціле число)
Використовуйте метод __init__ для ініціалізації атрибутів при створенні об'єкта
Створіть екземпляр Rectangle і виведіть його ширину та висоту"""

class Rectangle:
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)

    def display_info(self):
            print(f"\n\tWidth: {self.width} \n\tHeight: {self.height}")
    
my_rectangle = Rectangle(5, 10)
my_rectangle.display_info()