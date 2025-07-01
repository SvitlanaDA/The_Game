"""Базове створення класу та об'єкта
Задача:

Створіть клас Car з наступними атрибутами (використовуйте метод __init__):
make (рядок)
model (рядок)
year (ціле число)
Створіть екземпляр класу зі значеннями для make, model і year
Виведіть атрибути екземпляра"""

class Car:
     
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"\n\tMake: {self.make} \n\n\tModel: {self.model} \n\n\tYear: {self.year}")

my_car = Car(make = "Toyota", model = "Camry", year = 2020)
my_car.display_info() 