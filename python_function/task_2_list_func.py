"""Функція з кількома значеннями, що повертаються
Функція min_max_avg(numbers), яка приймає список чисел як аргумент"""
"""Функція обробляє крайні випадки, коли список порожній або має лише одне число"""

def min_max_avg(numbers):
    if not isinstance(numbers, list):  # Перевірка на порожній або не повний список
        return None, None, None

    min_val = min(numbers) # Мінімальне значення в списку
    max_val = max(numbers) # Максимальне значення в списку
    avg_val = sum(numbers) / len(numbers) \
        if len(numbers) > 1 else None # Середнє значення чисел, за усовою, що список містить більше 1 числа
    
    return min_val, max_val, avg_val

print(help(min_max_avg))

"""Перевірка коду: """
num_list1 = (5, 9, 10, 2, 2057, 0, 29)
print(num_list1)
min_val, max_val, avg_val = min_max_avg(num_list1)
print(f"Min: {min_val}, Max: {max_val}, Average: {avg_val}")

num_list2 = (3)
print(num_list2)
min_val, max_val, avg_val = min_max_avg(num_list2)
print(f"Min: {min_val}, Max: {max_val}, Average: {avg_val}")

num_list3 = ("hgfdhgmv", "hgmh", "h")
print(num_list3)
min_val, max_val, avg_val = min_max_avg(num_list3)
print(f"Min: {min_val}, Max: {max_val}, Average: {avg_val}")