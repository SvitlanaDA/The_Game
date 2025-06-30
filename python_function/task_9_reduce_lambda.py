"""Створення накопичувальної суми (reduce і lambda)
Дано список чисел. Використовуя лямбда-функцію та reduce 
для створення одного списку, який представляє накопичувальну суму."""

from functools import reduce   # Завантажуємо словник Python

numbers = [1, 2, 3, 4]

sum_numbers = reduce(lambda x, y: x + y, numbers)

print(sum_numbers.__doc__)
print()
print(sum_numbers)