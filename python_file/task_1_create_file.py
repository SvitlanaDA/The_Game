"""Запис введення користувача у файл
Задача: Створіть програму, яка запитує користувача ввести їхнє ім'я, 
вік і улюблений колір. 
Запишіть цю інформацію у файл user_info.txt у наступному форматі:

Приклад вводу:

Enter your name: Alice
Enter your age: 25
Enter your favorite color: Blue"""

from pathlib import Path

# Абсолютний шлях до базової папки
base_dir = Path(r"C:/Users/assto/PythonTasksProject/2_Git_Theory/python_file")

# Повний шлях до нової теки
target_folder = base_dir / "my_hw_file_py"

# Створюємо теку, якщо її немає
target_folder.mkdir(parents=True, exist_ok=True)

# Шлях до файлу user_info.txt всередині цієї теки
file_path = target_folder / "user_info.txt"

# Відкриваємо файл у режимі запису "w" (запис з очищенням попереднього вмісту)
with open(file_path, "w", encoding="utf-8") as file:
    
    # Додаємо приклади даних
    file.write(f"\n\tName: Alice\n \tAge: 25\n \tColor: Blue\n")
    file.write(f"\n\tName: Bob\n \tAge: 30\n \tColor: Yellow\n")

    # Запускаємо цикл для введення користувацьких даних
    while True:

        # Отримуємо  ім’я, вік, колір від користувача
        name = input("\n\tEnter your name: ").strip()
        age = int(input("\n\tEnter your age: "))
        color = input("\n\tEnter your favorite color: ").strip()

        # Записуємо введені дані у файл
        file.write(f"\n\tName: {name}\n \tAge: {age}\n \tColor: {color}\n")
        
        # Запит на продовження
        next_person = input("\n\tEnter Yes/No for enter next another person: ")

        # Якщо користувач не хоче продовжувати — виходимо з циклу
        if next_person.strip().lower() != "Yes":
            print("\n\tLogout.")
            break

# Закриття файла
# Читаємо весь вміст файлу після завершення запису (перевірка або перегляд)
with open(file_path, "r", encoding="utf-8") as file:
    print("\n\tЗбережені дані у файлі:")
    print(file.read())       