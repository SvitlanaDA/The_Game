"""Симулятор домашніх тварин
Мета: Створити простий симулятор домашніх тварин, 
використовуючи об'єктно-орієнтоване програмування.

Функції:

Клас тварини з атрибутами (ім'я, тип, голод, щастя)
Методи для взаємодії з тваринами (годувати, грати)
Звітування про стан благополуччя тварини
Фокус реалізації:

Створення визначення класу з атрибутами
Реалізація методів для різних дій
Використання змінних екземпляра для відстеження стану тварини
Демонстрація створення екземплярів та викликів методів
Інтерфейс користувача: Текстовий інтерфейс 
для створення віртуальної домашньої тварини та взаємодії з нею.

Виклики:

Розробити інтуїтивну структуру класу
Реалізувати зміни стану через методи
Створити захоплюючу поведінку домашніх тварин"""


class Animal:
    def __init__(self, name, hunger=50, happiness=50):
        self.name = name
        self.hunger = hunger
        self.happiness = happiness

    def eat(self):
        self.hunger -= 20 
        self.happiness += 20
        print(f"{self.name} біжить до миски! Hunger: {self.hunger}, happiness: {self.happiness}")

    def play(self):
        self.hunger += 20
        self.happiness -= 20
        print(f"{self.name} грається! Hunger: {self.hunger}, happiness: {self.happiness}")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"

# Запуск симулятора
print("\nВітаємо у Симуляторі домашніх тварин!")

while True:
    # Вибір тварини
    choice = input("\nОберіть тварину:\n1 - Собака\n2 - Кішка\n3 - Качка\n4 - Вихід\nВаш вибір: ")

    if choice == "4":
        print("Дякуємо, що скористалися симулятором!")
        break

    if choice in ["1", "2", "3"]:
        name = input("Введіть ім'я тварини: ")
        pet = Dog(name) if choice == "1" else Cat(name) if choice == "2" else Duck(name)

        print(f"{pet.name} каже: {pet.speak()}")

        while True:
            action = input("\nЩо будемо робити?\n1 - Годувати\n2 - Гратися\n3 - Вийти\nВаш вибір: ")
            if action == "1":
                pet.eat()
            elif action == "2":
                pet.play()
            elif action == "3":
                break
            else:
                print("Невірний вибір, спробуйте ще раз.")