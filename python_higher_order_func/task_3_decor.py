"""Базовий декоратор
Задача:

Створіть декоратор uppercase_decorator, який модифікує поведінку функції так, 
щоб вона завжди повертала результат у верхньому регістрі
Застосуйте uppercase_decorator до функції greet(), яка повертає "Hello" """

def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "Hello"

# Виклик декорованої функції
print(greet())