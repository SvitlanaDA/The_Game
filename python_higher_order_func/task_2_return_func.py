"""Функція, що повертає функцію
Задача:

Створіть функцію make_adder(add_value), яка повертає функцію adder:
Повернута функція adder приймає число і додає до нього значення add_value, надане в make_adder
Використовуйте make_adder для створення функції-інкрементатора, яка збільшує число на 1. 
Перевірте її на вхідному значенні"""

def make_adder(add_value):
    """Повертаємо функцію, яка додає add_value до свого аргументу i."""
    def adder(i):
        return i + add_value
    return adder

increment  = make_adder(1)
value = 5
print(increment(value))
