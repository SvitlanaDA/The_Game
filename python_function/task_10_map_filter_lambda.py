"""Об'єднання map і filter
Дано список цілих чисел. Використовуючи lambda, map і filter разом, 
щоб спочатку подвоїти кожне число, а потім відфільтрувати числа, які більші за 10."""

numbers = [2, 4, 6, 8, 10]
doble_numbers = map(lambda x: x * 2, numbers)
selected_numbers = filter(lambda y: y <= 10, doble_numbers)

print(doble_numbers.__doc__)
print(selected_numbers.__doc__)
print()
print(list(selected_numbers))