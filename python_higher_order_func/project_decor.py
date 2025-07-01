""" Проект з функціями вищого порядку
        Конструктор функцій
Мета: Створити систему, яка демонструє композицію функцій та функції вищого порядку.
    Функції:
Базові математичні функції (подвоїти, квадрат, додати, заперечити)
Можливість композиції функцій
Послідовне застосування функцій
Користувацькі послідовності операцій
    Фокус реалізації:
Створення функцій, які приймають та повертають інші функції
Реалізація функції композиції для ланцюжка функцій
Демонстрація послідовностей застосування функцій
Показ того, як функції вищого порядку забезпечують повторне використання коду
Інтерфейс користувача: Інтерактивна система для застосування та 
компонування функцій до вхідних значень.
    Виклики:
Зрозуміти логіку композиції функцій
Створити чіткі демонстрації функцій вищого порядку
Забезпечити гнучке послідовне виконання функцій"""

import operator

# математична функція - подвоїти
def multiply(func):
    def wrapper():
        return operator.mul(func(), 2)
    return wrapper

# математична функція - квадрат
def kwadr(func):
    def wrapper():
        return operator.pow(func(), 2)
    return wrapper

# математична функція - додати
def added(func):
    def wrapper():
        x = float(input("Введити число для додавання: "))
        return operator.add(func(), x)
    return wrapper

# заперечити - помножити на -1
def object(func):
    def wrapper():
        return operator.mul(func(), -1)
    return wrapper


# Комбінатор декораторів
def compose_decor(func_list):
    def composed(x):
        for func in func_list:
            x = func(x)
        return x
    return composed

# Основна логіка
def values():
    value = float(input("\n\tВітаємо у Конструкторі функцій!\n\tВведіть число для обчислення: "))

    # Виклик декорованої функції
    def get_value():
        return value

    # Словник декораторів
    decorators = {
        1: multiply,
        2: kwadr,
        3: added,
        4: object
    }

    operations = []
    while True:

        action = int(input("\n\tОберить дію: \n\t1 - подвоїти, \n\t2 - квадрат, \n\t3 - додати,"\
                    "\n\t4 - заперечити, \n\t5 - Вивід результатів, \n\t6 - вихід з системи "\
                    "\n\tВведіть команду: "))
        
        if action == 6:
            print("Вихід із програми.")
            break

        elif action == 5:
            if operations:
                composed_func = compose_decor(operations)(get_value)
                print("\n\tРезультат:", composed_func())
            else:
                print("\tНемає вибраних дій.")
            operations.clear()

        elif action in decorators:
            operations.append(decorators[int(action)])
            print(f"\tДія додана: {decorators[int(action)].__name__}")
                        
        else:
            print("\tНемає вибраних дій.")
            break

values()
