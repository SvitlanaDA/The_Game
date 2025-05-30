print("Вітаємо у менеджері плейлистів!")
# Кортежі з українськими піснями (назва, виконавець, тривалість)
song1 = ("Погляд", "Yaktak Feat. Sobol", 3.02)
song2 = ("Додому", "Wellboy", 2.50)
song3 = ("Дзвін", "Sanaria Feat. Skylerr", 3.13)
song4 = ("Різнокольорова", "Dorofeeva", 3.45)
song5 = ("Живи (Remix)", "Yuliya Roznen", 4.22)
song6 = ("Там У Тополі", "А. Пивоваров, NK", 3.36)
song7 = ("Фортеця", "Антитіла", 4.10)
song8 = ("Троянди", "100Лиця", 3.20)
song9 = ("Тримай Мене Міцно", "Без Обмежень", 3.55)
song10 = ("Двічі В Одну Річку Не Війде", "Океан Ельзи", 4.30)
song11 = ("Вечорниці", "Yaktak Feat. Sobol", 3.15)
song12 = ("Гуси", "Wellboy", 2.45)
song13 = ("Місто", "Sanaria Feat. Skylerr", 3.30)
song14 = ("Кохаю", "Dorofeeva", 3.40)
song15 = ("Ти моя", "Антитіла", 4.05)

# Список пісень (плейлист)
playlist = [song1, song2, song3, song4, song5, song6, song7,\
            song8, song9, song10, song11, song12, song13, song14, song15]

# Функція додавання пісень
def add_song():
    name_song = input("\nВведіть назву пісні: ").strip()
    art_song = input("Введіть виконавця: ").strip()
    time_song = float(input("Введіть тривалість (хв): "))
    playlist.append((name_song, art_song, time_song))
    print(f"Пісня '{name_song}' додана до плейлиста!\n")

# Функція сортування
def sort_playlist(attribute):
    index = {"назва": 0, "виконавець": 1, "тривалість": 2}.get(attribute, 0)
    playlist.sort(key=lambda song: song[index])
    print(f"\nПлейлист відсортовано за {attribute}!\n")

# Функція статистики
def playlist_stats():
    total_time = sum(song[2] for song in playlist)
    print(f"\nЗагальна кількість пісень: {len(playlist)}")
    print(f"Загальна тривалість: {total_time:.2f} хв\n")

# Головне меню CLI
while True:
    action = input("Введіть команду ('add', 'sort', 'stats', 'show', 'exit'): ").strip().lower()
    
    if action == "add":
        add_song()
    elif action == "sort":
        sort_type = input("Сортувати за 'назва', 'виконавець', 'тривалість': ").strip().lower()
        sort_playlist(sort_type)
    elif action == "stats":
        playlist_stats()
    elif action == "show":
        print("\nПлейлист:")
        for song in playlist:
            print(f"{song[0]} - {song[1]} ({song[2]} хв)")
        print("")
    elif action == "exit":
        print("Вихід із програми.")
        break
    else:
        print("Щось пійшло не так, спробуйте ще раз!")