"""Додавання та відображення вмісту файлу
Задача: Створіть програму, яка додає новий рядок до файлу
 log.txt з поточною датою та часом. 
 Потім прочитайте та відобразіть весь вміст файлу.

Якщо файл не існує, створіть його
Додайте поточну дату та час у форматі: РРРР-ММ-ДД ГГ:ХХ:СС
Виведіть весь вміст файлу після додавання нового рядка"""

from pathlib import Path
from datetime import datetime

# Абсолютний шлях до базової папки
base_dir = Path(r"C:/Users/assto/PythonTasksProject/2_Git_Theory/python_file/my_hw_file_py")

# Створюємо об'єкт шляху до файла
file_path = base_dir / "log.txt"

# Перевірка наявності файла
first_time = not file_path.exists()
if first_time:
    print("log.txt created.")

# Поточний час у потрібному форматі
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Відкриваємо файл у режимі запису "a" (запис з додаванням нижче до  попереднього вмісту)
with open(file_path, "a", encoding="utf-8") as file:

    # Додаемо рядок у файл
    file.write(timestamp + "\n")

print(f"Appended: {timestamp}")

# Виводимо вміст файла
print("\nFile content:")
# Читаємо весь вміст файлу після завершення запису (перевірка або перегляд)
with open(file_path, "r", encoding="utf-8") as file:
    print(file.read())