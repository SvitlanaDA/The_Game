"""Створення користувацького ітератора 
для послідовності Фібоначчі
Задача: Створіть користувацький клас ітератора 
FibonacciIterator, який генерує числа в послідовності Фібоначчі.
 Ітератор повинен приймати вхідне значення n, 
 яке визначає максимальну кількість чисел Фібоначчі для генерації.

Реалізуйте методи __iter__ і __next__, 
щоб зробити клас ітератором
Використовуйте ітератор для генерації та виведення послідовності 
Фібоначчі до n термінів
Приклад вводу:

fib = FibonacciIterator(5)
for num in fib:
    print(num)
Очікуваний вивід:

0
1
1
2
3
"""

class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1
        self.count = 0
    
    def __iter__(self):
        """Повертає об'єкт ітератора (self)."""
        self.a, self.b = 0, 1
        self.count = 0
        return self
    
    def __next__(self):
        """Повертає наступне число Фібоначчі."""
        if self.count >= self.limit:
            raise StopIteration
        
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return result
    
fib = FibonacciIterator(5)
for num in fib:
    print(num)