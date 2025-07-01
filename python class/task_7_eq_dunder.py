"""Метод Dunder (eq)
Задача:

Створіть клас Person з атрибутами name і age
Перевизначте метод __eq__(), щоб порівнювати два об'єкти Person на основі їхніх імен і віку
Створіть два екземпляри Person і перевірте, чи вони рівні, використовуючи оператор ==

Are they equal? True"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        """Визначає оператор ==."""
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.age == other.age
    

# Створення екземплярів Person
person1 = Person("Alice", 30)
person2 = Person("Alice", 30)
person3 = Person("Bob", 25)

# Порівняння на рівність
print(f"\nAre they equal? {person1 == person2}")  # Виведе: True
print(f"\nAre they equal? {person1 == person3}")  # Виведе: False        