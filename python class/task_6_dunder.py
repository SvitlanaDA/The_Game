"""Метод Dunder (str)
Задача:

Створіть клас Book з атрибутами title, author і year_published
Перевизначте метод __str__(), щоб повернути рядок у форматі: "[Title] by [Author] (Published: [Year])"
Створіть екземпляр Book і виведіть його, щоб побачити власне представлення рядка

The Great Gatsby by F. Scott Fitzgerald (Published: 1925)"""

class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published
    
    def __str__(self):
        """Повертає зручне для користувача рядкове представлення."""
        return f"{self.title} by {self.author} (Published: {self.year_published})"
    

# Створення Book
book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

# __str__ використовується функціями print() та str()
print(book)        # Виведе: The Great Gatsby by F. Scott Fitzgerald (Published: 1925)