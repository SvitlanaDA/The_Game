"""Вилучення слів, що починаються з певної літери (filter і lambda)
Задача: Вам дано список слів і цільову літеру. 
Використовуйте лямбда-функцію та filter для створення нового списку, 
що містить лише слова, які починаються з заданої літери."""

words = ["apple", "banana", "cherry", "apricot", "blueberry"]

letter_words = filter(lambda word:  target_letter in word[0], words)
target_letter = "a"
print(letter_words.__doc__)
print(list(letter_words))