"""Проект з керуванням файлами
Простий нотатник
Мета: Створити програму для ведення нотаток з базовим керуванням файлами.
    Функції:
Створювати та зберігати текстові нотатки у файлах
Читати існуючі нотатки
Перераховувати доступні нотатки
Шукати нотатки за ключовими словами
    Фокус реалізації:
Використовувати операції з файлами для читання та запису
Створювати відповідні угоди з іменування файлів
Реалізувати керування директоріями
Граціозно обробляти помилки файлів
Інтерфейс користувача: Інтерфейс командного рядка для створення, 
перегляду, переліку та пошуку нотаток.
    Виклики:
Реалізувати надійне збереження та завантаження файлів
Створити організовану структуру файлів
Обробляти потенційні помилки файлів
Реалізувати ефективний пошук нотаток"""

from pathlib import Path
from datetime import datetime

# Абсолютний шлях до базової папки
base_dir = Path(r"C:/Users/assto/PythonTasksProject/2_Git_Theory/python_file")
target_folder = base_dir / "notes_files_py"  # Повний шлях до нової теки
target_folder.mkdir(parents=True, exist_ok=True) # Створюємо теку, якщо її немає

def create_note():
    # Абсолютний шлях до базової папки
    base_dir_note = Path(r"C:/Users/assto/PythonTasksProject/2_Git_Theory/python_file/notes_files_py")

    # Повний шлях до нової теки
    today = datetime.now().strftime("%Y-%m-%d")
    daily_folder = target_folder / today
    daily_folder.mkdir(parents=True, exist_ok=True) # Створюємо теку, якщо її немає


    title = input("\n\tВведи назву нотатки: ").strip()
    content = input("\n\tВведи текст нотатки:\n")
    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S") # Поточний час у потрібному форматі
    file_name = f"{title}_{timestamp}.txt"
    file_path = daily_folder / file_name # Шлях до файлу note_data.csv всередині цієї теки

    # Перевірка наявності файла
    first_time = not file_path.exists()
    if first_time:
        print(f"\n\t{file_path} created.")

    # Відкриваємо файл у режимі запису "w" (запис з очищенням попереднього вмісту)
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
    except PermissionError:
        print("You don't have permission to access this file")

    print(f"\n\tНотатку '{title}' збережено як {file_name}")

# Перелічити в списку всі папки та їх нотатки та інформвцію про кожну
def list_notes():
    print("\n\tСписок усіх нотаток:")

    for folder in target_folder.glob("*"): 
        if folder.is_dir(): 
            print(f"\n\tDirectory: {folder.name}") 
            for note in folder.glob("*.txt"):
                try:
                    stat = note.stat()
                    print(f"Is file: {note.name}")
                    print(f"Is directory: {'Catalog' if note.is_dir() else 'File'}")
                    print(f"Size: {note.stat().st_size} bytes")
                    print(f"Last modified: {datetime.fromtimestamp(note.stat().st_mtime).\
                                strftime('%Y-%m-%d %H:%M:%S')}")
                except Exception as e:
                    print(f"\n\tНе вдалося прочитати {note.name}: {e}")

# Прочитати зміст нотатки
def read_note():
    list_notes()
    name = input("\n\tВведи точну назву файлу нотатки: ").strip()
    matches  = list(target_folder.rglob(name))
    if matches:
        try:
            with open(matches[0], "r", encoding="utf-8") as file:
                print("\n\tВміст нотатки:")
                print(file.read())
        except FileNotFoundError:
            print("The file does not exist")
        except PermissionError:
            print("You don't have permission to read this file")
        except IOError as e:
            print(f"An I/O error occurred: {e}")
    else:
        print("\n\tТакої нотатки не знайдено.")

# Пошуківарка нотаток в списку   
def search_notes():
    keyword = input("\n\tВведи ключове слово для пошуку: ").lower()
    print("\n\tРезультати пошуку:")
    found = False
    for note in target_folder.rglob("*.txt"):
        try:
            content = note.read_text(encoding="utf-8").lower()
            if keyword in content:
                print(f"\n\tЗнайдено в: {note}")
                found = True
        except Exception as e:
            print(f"\n\tНе вдалося прочитати {note.name}: {e}")
    if not found:
        print("\n\tНотаток з таким словом не знайдено.")

# Інтерфейс користувача: 
def menu():
    while True:
        print("\n\tМеню:")
        print("\t1. Створити нотатку")
        print("\t2. Переглянути нотатку")
        print("\t3. Перелічити всі нотатки")
        print("\t4. Пошук нотаток за 'словом'")
        print("\t5. Вихід")
        choice = input("\n\tОбери дію (1–5): ").strip()

        if choice == "5":
            print("\n\tВихід з нотатника!")
            break
        elif choice == "1":
            create_note()
        elif choice == "2":
            read_note()
        elif choice == "3":
            list_notes()
        elif choice == "4":
            search_notes()
        else:
            print("\n\tНевідома опція!")

menu()