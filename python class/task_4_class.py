"""Успадкування
Задача:

Створіть клас Vehicle з атрибутами make, model і year
Створіть підклас ElectricCar, який успадковується від Vehicle і додає атрибут battery_size (ціле число)
Створіть екземпляр ElectricCar і виведіть атрибути як з Vehicle, так і з ElectricCar"""

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
        Vehicle.__init__(self, make, model, year)
        # Додавання нового атрибута
        self.battery_size = battery_size
    
    def get_info(self):
        return Vehicle.get_info(self) + f"\nBattery Size: {self.battery_size}"
    
# Створення екземпляра ElectricCar
my_tesla = ElectricCar("Tesla", "Model S", 2022, 100)
print(my_tesla.get_info())