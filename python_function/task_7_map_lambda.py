"""Лямбда-функція та map для створення списку кортежів, де кожен кортеж містить ім'я та його довжину."""

names = ["Alice", "Bob", "Charlie"]
len_names = map(lambda name: (name, len(name)), names)

print(len_names.__doc__)

print(list(len_names))