"""Декоратор з аргументами
Задача:

Створіть декоратор multiply_decorator, 
який приймає параметр factor і множить повернене значення функції на цей коефіцієнт
Застосуйте multiply_decorator до функції get_price(), яка повертає ціну (наприклад, 50)
Викличте декоровану функцію з коефіцієнтом 2 і виведіть результат"""

import operator

def multiply_decorator(factor):
    def decorator(func):
        def wrapper():
            result = operator.mul(func(), factor)  # func()  -  якщо без:  import operator
            return result # result * factor  -  якщо без:  import operator
        return wrapper
    return decorator

@multiply_decorator(2)
def get_price():
    return 50 

# Виклик декорованої функції
print(get_price())