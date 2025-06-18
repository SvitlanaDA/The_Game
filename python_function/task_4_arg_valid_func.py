"""Функція з іменованими аргументами та валідацією
Функцію create_user(username, email, password, **kwargs), яка:
Приймає username, email та password як обов'язкові параметри
Приймає будь-які додаткові дані користувача через **kwargs (наприклад, вік, адреса)

Якщо валідація успішна, повертає словник з даними користувача,  
або повідомлення про помилку, якщо валідація не вдалася"""

"""Запит для вводу данних користувачем"""
username = input("Введить ім'я не менше 5 символів: ")
email = input("Введить email: ")
password = input("Введить пароль не менше 8 символів: ")

errors = []  # Список для збереження помилок

def create_user(username, email, password, **kwargs):

    # Валідація параметрів
    if len(username) < 5:  # Перевіряє чи ім'я користувача має довжину не менше 5 символів
        errors.append("Error: Username must be at least 5 characters long.")

    if "@" not in email:  # Перевіряє чи електронна пошта містить @
        errors.append("Error: Email must contain '@'.")

    if len(password) < 8:  # Перевіряє чи пароль має довжину не менше 8 символів
        errors.append("Error: Password must be at least 8 characters long.")

    # Якщо є помилки, повертаємо список помилок
    if errors:
        return f"Error: {', '.join(errors)}"

    # Формування словника користувача
    user_data = {
        "username": username,
        "email": email,
        "password": password
    }

    # Додавання додаткових даних
    user_data.update(kwargs)

    return user_data

print(create_user(username, email, password, age=30, adres="Ukraina, Kiev"))
print()
print("Перевірка функції")
print(create_user("john123", "john@example.com", "securePass123", age=30))  
# {'username': 'john123', 'email': 'john@example.com', 'password': 'securePass123', 'age': 30}

print(create_user("tim", "timexample.com", "pass"))  
# "Error: Username must be at least 5 characters long."