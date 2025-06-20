"""Підрахунок слів у файлі
Задача: Напишіть програму, яка читає вміст текстового файлу sample.txt, 
підраховує кількість слів у ньому та відображає загальну кількість слів.

Створіть текстовий файл sample.txt з будь-яким вмістом 
(наприклад, "Hello world! This is a file.")
Відкрийте файл у режимі читання, підрахуйте слова та виведіть результат
Приклад вводу в sample.txt:

Hello world! This is a file."""

from pathlib import Path
from functools import reduce

# Абсолютний шлях до базової папки
base_dir = Path(r"C:/Users/assto/PythonTasksProject/2_Git_Theory/python_file/my_hw_file_py")

# Створюємо об'єкт шляху до файла
file_path = base_dir / "sample.txt"

# Перевіряємо, чи файл вже існує
if file_path.exists():
    print("The file exists")
else:
    print("The file does not exist. Creating new file...")

# Відкриваємо файл у режимі запису "w" (запис з очищенням попереднього вмісту)
with open(file_path, "w", encoding="utf-8") as file:
    
    # Додаємо приклад даних
    file.write(f"\n\tHello world! This is a file.")

# Закриття файла
# Читаємо весь вміст файлу після завершення запису (перевірка або перегляд)
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    print("\n\tЗбережені дані у файлі:")
    print(content) 

    # Рахуємо кількість слів у файлі
    def count_words(word):
        return reduce(lambda count, _: count + 1, word.split(), 0)
    
    # Виводимо загальну кількість слів
    total_words = count_words(content)
    print(f"\n\tThe file contains {total_words} words.")