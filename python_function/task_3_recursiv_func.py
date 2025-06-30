"""Рекурсивна функція для обчислення факторіалу
Рекурсивна функція factorial(n), яка обчислює факторіал числа n (тобто n!)
Функція повертає 1, коли n дорівнює 0 або 1, і рекурсивно множе число на факторіал n-1 для значень більше 1"""

def factorial(n):
    """Calculate n! recursively."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(help(factorial))

print(f"5! = {factorial(5)}")
print(f"6! = {factorial(6)}")
print(f"7! = {factorial(7)}")