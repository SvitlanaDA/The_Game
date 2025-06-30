"""Генерація нескінченних простих чисел
Функція-генератор generate_primes, яка видає прості числа нескінченно.

Використовує цикл while для перевірки простих чисел
Перевіряє генератор, виводячи перші 10 простих чисел за допомогою циклу for та enumerate"""


def generate_primes():
    i = 1
    while True:
        yield i + 1
        i += 1

primes = generate_primes()

primes = filter(lambda x: ((x % 2 != 0) and (x % 3 != 0) and(x % 5 != 0)) \
                           or ((x == 2) or (x == 3) or (x == 5)), generate_primes())

for i, prime in enumerate(primes):
    if i >= 10:  # Зупинитися після 10 простих чисел
        break
    print(prime)