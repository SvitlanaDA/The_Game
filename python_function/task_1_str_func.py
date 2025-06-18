def format_name(name, title):
    
    # Розділення рядка на слова
    first_name = name.split()[0]  # Беремо лише перше слово (ім'я)
    
    # Приведення в едину форму звернення
    if title in ("Mister", "mister", "Mr", "mr"):
        title = "Mr."
    if title in ("Missis", "Miss", "Ms", "missis", "miss", "ms"):
        title = "Ms."
    
    # Приведено до единого формату виведення повної інформації
    return f"Title: {title}, Name: {first_name}"

print(help(format_name))

# Перевірка функції
print(format_name("Alice", "Miss"))  
print(format_name("Alice Johnson", "Missis"))  
print(format_name("John Dr.", "Mister")) 
print(format_name("Bob Hight", "mister"))