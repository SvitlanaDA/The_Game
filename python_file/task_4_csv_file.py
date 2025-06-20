"""Читання та запис CSV-файлу
Задача: Створіть програму, яка робить наступне:

Записує CSV-файл з назвою students.csv 
з колонками: Name, Age та Grade
Заповніть його принаймні 3 рядками прикладних даних 
(наприклад, "Alice", 25, "A")
Прочитайте файл і обчисліть середній вік студентів
Відобразіть вміст CSV-файлу разом із середнім віком
Приклад вводу (дані в students.csv):

Name,Age,Grade
Alice,25,A
Bob,22,B
Charlie,24,A
Очікуваний вивід:

File content:
Name: Alice, Age: 25, Grade: A
Name: Bob, Age: 22, Grade: B
Name: Charlie, Age: 24, Grade: A

Average Age: 23.67"""

import csv
from pathlib import Path

# Всі дані студентів: один довгий рядок 
raw_data = "Alice,25,A Bob,22,B Charlie,24,A"

# Розбиваємо на окремі значення
tokens = raw_data.replace(",", " ").split()

# Групуємо кожні 3 значення як один рядок
rows = [tokens[i:i+3] for i in range(0, len(tokens), 3)]

# Абсолютний шлях до файлу
base_dir = Path(r"C:/Users/assto/PythonTasksProject/2_Git_Theory/python_file/my_hw_file_py")
file_path = base_dir / "students.csv"

# Перевіряємо, чи файл вже існує
if file_path.exists():
    print("The file exists")
else:
    print("The file does not exist. Creating new file...")

# Запис CSV, використовуючи словники
with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Grade"])
    writer.writerows(rows)
   

# Виводимо вміст файла
print("\n\tFile content:")

# Створення списку, для віку студентів
ages = [] 
# Читання CSV у словники
with open(file_path, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:

        # Обчислити вік студентів та додання до списку
        age = int(row["Age"])
        ages.append(age)

        # Виводимо вміст файла
        print(f"\tName: {row['Name']}, Age: {row['Age']}, Grade: {row['Grade']}")
    # Використання, обчислення середнього віку всіх студентів
    avrg_age = round(sum(ages) / len(ages), 2)

    # Виведення значення  середнього віку всіх студентів
    print(f"\n\tAverage Age: {avrg_age}")
    pass