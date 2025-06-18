print("Вітаємо у менеджері контактів!")

manager_contact = {
    "Dmytro": {"phone": "128-962-1588", "email": "ghvn@gchmg.ij"},
    "Alice": {"phone": "+48-153-482-235", "email": "ghcmghv@mnmgj.ty"},
    "Ivan": {"phone": "246-158-158", "email": "bvhgc@bnjhg.yu"},
    "Юлія": {"phone": "23-258-482-157", "email": "gcfhn@hgjj.hg"},
    "Олексій": {"phone": "23-147-158-155887", "email": "bbvhgncv@ghfhm.bjhg"},
    "Uliana": {"phone": "123-456-4566", "email": "hggtd@mnbgjh.mjkl"},
    "Світлана": {"phone": "2147-56-12557", "email": "hvjghv@nbh.uh"},
    "Олександр": {"phone": "23581587", "email": "hgjfvf@knkjhg.com"},
    "Дмитрій": {"phone": "23587-1235", "email": "gghfdjrfd@jhkj.yt"},
    "Ivanna": {"phone": "25487-12-25", "email": "hjfghc@jgjhgv.hggfd"},
    "Іван": {"phone": "2354-25-25-25", "email": "hhvghcv@bmvb.jhgfr"},
    "Роман": {"phone": "+39-254-254-24", "email": "hgvjhgdcfgb2@bjhlvj.jhvf"},
    "Борис": {"phone": "254-458-485", "email": "hgjgdu65utkujgv68i@jkhgf.vgjk"},
    "Оксана": {"phone": "23-25-555-878", "email": "hjkvfhgxc34554r67b@bjk.byg"},
    "Таня": {"phone": "22-587-257-165", "email": "hjvjhv@klkj.rty"},
}

# Виведення контактів у форматі таблиці
print("\n Контактний список:")
for contact, details in manager_contact.items():
    print(f"{contact}: {details['phone'], details['email']}")

    
# Функція перевірки контакту
def check_contact(name):
    return name in  manager_contact

# Функція додавання нового контакту
def add_contact():
    name = input("\nВведіть ім'я контакту: ").strip()
    
    # Перевірка, чи контакт вже існує
    if check_contact(name):
        print(f"Контакт '{name}' вже існує! Данні контакту: {manager_contact[name]}")
        #                        details.get('phone', 'Немає телефону'), details.get('email', 'Немає email')}")
        return
    
    else:
        phone = input("Введіть номкр телефону контакта: ").strip()
        email = input("Введіть email: ").strip()
        manager_contact[name] = {"phone": phone, "email": email}
    
        print(f"Контакт '{name}' додано!")

# Функція сортування

def sort_contact(attribute):
    attribute_ind = {"1": "name", "2": "phone", "3": "email"}
    sort_key = attribute_ind.get(attribute, "name")  

    sorted_contacts = dict(sorted(manager_contact.items(), \
                    key=lambda item: item[0] if sort_key == "name" else item[1][sort_key]))
    
    print(f"\n Контакти відсортовано за {sort_key}!\n")
    return sorted_contacts

# Виклик функції для перевірки або додавання
while True:
    action = input("\n Введіть команду ('check', 'add', 'sort', 'show', 'exit'): ").strip().lower()
    
    if action == "check":
        name = input("Введіть ім'я для перевірки: ").strip()
        contact = check_contact(name)
        if contact:
            print(f"{name}: {details['phone']}, email: {details['email']}")
        else:
            print(f"Контакт '{name}' не знайдено!")
    
    elif action == "add":
        add_contact()

    elif action == "sort":
        attribute = input("Сортувати за 'назва - 1', 'номером телефона - 2', 'email - 3': ").strip()
        manager_contact = sort_contact(attribute)

    elif action == "show":
        print("\n Контактний список:")
        for contact, details in manager_contact.items():
            print(f"{contact}: {details.get('phone', 'Немає телефону')}, {details.get('email', 'Немає email')}")
    
    elif action == "exit":
        print("Вихід з програми.")
        break
    else:
        print("Невідома команда, спробуйте ще раз!")