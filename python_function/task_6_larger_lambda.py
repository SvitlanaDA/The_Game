"""Знаходе більше з двох чисел
Лямбда-функція для порівняння двох чисел і повернення більшого."""

larger = lambda x, y: max(x, y) 

print(f"larger(10, 20): {larger(10, 20)}")
print(f"larger(-5, -10): {larger(-5, -10)}")  
print(f"larger(8, 8): {larger(8, 8)}")