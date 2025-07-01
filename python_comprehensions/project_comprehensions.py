"""Проект з генераторами списків
Перетворювач даних
Мета: Створити інструменти для перетворення даних, 
використовуючи генератори списків, словників та множин.
    Функції:
Перетворювати списки, використовуючи різні критерії
Фільтрувати дані на основі умов
Створювати словники з існуючих даних
Генерувати вкладені структури даних
    Фокус реалізації:
Використовувати генератори списків для перетворень послідовностей
Реалізувати генератори словників для даних ключ-значення
Демонструвати фільтрацію з умовами в генераторах
Показати приклади вкладених генераторів
Інтерфейс користувача: Система на основі меню для вибору 
та застосування різних перетворень даних.
    Виклики:
Створювати читабельні вирази генераторів
Реалізувати ефективні перетворення даних
Демонструвати силу та лаконічність генераторів"""


def show_menu():
    print("\n\tПеретворювач даних\n")
    print("\t1. Створити список квадратів")
    print("\t2. Фільтрувати список")
    print("\t3. Створити словник")
    print("\t4. Вкладене перетворення")
    print("\t5. Генератор множини")
    print("\t6. Сортування після фільтрації")
    print("\t7. Генератор кортежів")
    print("\t8. Поміняти місцями ключі та значення")
    print("\t0. Вихід\n")

# 1. Створити список квадратів
def list_squares():
    squares = [n ** 2 for n in range(1, 11)]
    print("\n\tСтворений список квадратів:", squares)

# 2. Фільтрувати список
def filter_list():
    filt = [n for n in range(1, 11) if n % 2 == 0]
    print("\n\tПарні числа:", filt)

#3. Створити словник
def create_dict():
    square_dict = {n: n**2 for n in range(1, 11)}
    print("\n\tСловник квадратів:", square_dict)

# 4. Вкладене перетворення
def flatten_nested():
    nested_list = [[1, 2, 3], [4, 5], [6, 7], [8, 9, 10]]
    flattened = [item for sublist in nested_list for item in sublist]
    print("\n\tСплющений список:", flattened)

# 5. Генератор множини
def generate_set():
    nums = [2, 4, 6, 8, 10]
    result_set = {n**2 for n in nums if n % 2 == 0}
    print("\n\tМножина квадратів парних чисел:", result_set)

# 6. Сортування після фільтрації
def filter_sorted():
    nums = [3, 1, 7, 25, 2, 8, -7, 5]
    result = sorted([n for n in nums if n % 2 != 0])
    print("\n\tНепарні числа за зростанням:", result)

# 7. Генератор кортежів
def tuple_list():
    even_squares = {n: n ** 2 for n in range(1, 11) if n % 2 == 0}
    print("\n\tСписок кортежів (парне число і квадрат):", even_squares)    

# 8. Поміняти місцями ключі та значення (припускаючи, що значення унікальні)
def tuple_inventory():
    even_inventory = {n: n ** 2 for n in range(1, 11) if n % 2 == 0}
    inverted = {v: k for k, v in even_inventory.items()}
    print("\n\tСписок кортежів (квадрат і парне число):",inverted)

def main():
    while True:
        show_menu()
        choice = input("\n\tВаш вибір: ")
        if choice == "0":
            break
        elif choice == "1":
            list_squares()
        elif choice == "2":
            filter_list()
        elif choice == "3":
            create_dict()
        elif choice == "4":
            flatten_nested()
        elif choice == "5":
            generate_set()
        elif choice == "6":
            filter_sorted()
        elif choice == "7":
            tuple_list()
        elif choice == "8":
            tuple_inventory()
        else:
            print("\n\tНевірний вибір, спробуйте ще.")
main()