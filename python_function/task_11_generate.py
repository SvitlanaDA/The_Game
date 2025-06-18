"""Генерація послідовності квадратів
Функція-генератор generate_squares, 
яка видає квадрати чисел, починаючи з 1 до заданого числа n (включно).

Використовується цикл for і ключове слово yield для створення генератора
Перевіряється генератор, перебираючи його та виводячи значення """


def generate_squares(n):
    """Generate squares numbers from 1 to n."""
    
    i = 1
    while i <= n:
        yield i**2
        i += 1

for square in generate_squares(5):
    print(square)
print()

"""Завдання-виклик: 
Використовуйте генератор з функцією sum(), 
наприклад, sum(generate_squares(4)) має повернути 30."""

print(sum(generate_squares(4)))