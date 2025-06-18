"""Завдання-виклик:

Розширте ітератор, щоб він генерував виняток StopIteration, 
коли досягнуто максимального значення n
Використовуйте ітератор з функцією list(), 
наприклад, list(FibonacciIterator(7)) 
має вивести [0, 1, 1, 2, 3, 5, 8]"""

class FibonacciIterator:
    def __init__(self, max_n):
        self.a, self.b = 0, 1
        self.max_n = max_n
    
    def __iter__(self):
        """Повертає об'єкт ітератора (self)."""
        return self
    
    def __next__(self):
        """Повертає наступне число Фібоначчі."""
        if self.a > self.max_n:
            raise StopIteration
        
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result
    
# Використання ітератора з list()
fib_sequence = list(FibonacciIterator(7))
print(fib_sequence)