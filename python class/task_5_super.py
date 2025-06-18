"""Перевизначення методів
Задача:

У Завданні 4, перевизначте метод __init__ класу ElectricCar, 
щоб ініціалізувати як атрибути Vehicle, так і ElectricCar (використовуючи super())
Викличте метод __init__ з ElectricCar і виведіть значення всіх атрибутів"""

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}" 

# Дочірній клас
class ElectricCar(Vehicle):
    def __init__(self, make, model, year, battery_size):
        # Виклик методу __init__ батьківського класу
        super().__init__(make, model, year)
        # Додавання нового атрибута
        self.battery_size = battery_size
    
    def get_info(self):
        return super().get_info() + f"\nBattery Size: {self.battery_size}"
    
# Створення екземпляра ElectricCar
my_tesla = ElectricCar("Tesla", "Model X", 2023, 120)
print(my_tesla.get_info())