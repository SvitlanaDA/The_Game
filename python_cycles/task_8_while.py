"""Симуляція циклу 

Do-While в Python
Задача: Python не має вбудованого циклу do-while, але ви можете симулювати його. 
Напишіть програму, яка багаторазово просить користувача ввести число, 
доки вони не введуть значення від 1 до 10. 
Переконайтеся, 
що перший запит виконується принаймні один раз, навіть якщо користувач вводить недійсне значення."""

while True:

    try:
        num = int(input(f"\nEnter a number between 1 and 10: "))
        if (1 <= num <= 10):  # Перевіряємо, чи число входить в діапазон
            print(f"Thank you! Your number is  {num}.") 
            break  # Завершуємо цикл
        else:
            print("Invalid input. Try again.")

    except ValueError:
        print("Invalid input. Try again.")