"""Базова функція вищого порядку
Задача:

Створіть функцію вищого порядку apply_function(func, value), яка:
Приймає функцію func і значення value як аргументи
Застосовує функцію func до значення value і повертає результат
Перевірте apply_function, передавши просту функцію, наприклад lambda x: x * 3, і значення, наприклад 4"""


def apply_function(func, value):
    """Застосувати функцію func до кожного елемента value."""
    return (func(value))

result = apply_function(lambda x: x * 3, 4)
print(result)  