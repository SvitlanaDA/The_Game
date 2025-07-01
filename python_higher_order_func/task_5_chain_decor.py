"""Ланцюжок декількох декораторів
Задача:

Створіть два декоратори:
double_decorator: Подвоює результат функції, яку він декорує
add_five_decorator: Додає 5 до результату функції, яку він декорує
Застосуйте обидва декоратори до функції get_value(), яка повертає 10
Викличте декоровану функцію і виведіть результат"""

import operator

def double_decorator(func):
    def wrapper():
        return operator.mul(func(), 2)
    return wrapper

def add_five_decorator(func):
    def wrapper():
        return operator.add(func(), 5)
    return wrapper

"""Декоратори в ланцюжку виконують дії в зворотньому напрямку.
Тобто с початку @double_decorator, а потім @add_five_decorator"""

@add_five_decorator # 2
@double_decorator   # 1
def get_value():
    return 10

# Виклик декорованої функції
print(get_value())