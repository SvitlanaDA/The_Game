books = {
    "book1": {"title": "1984", "author": "George Orwell", "year": 1949},
    "book2": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960}
}

for category, details in books.items():
    print(category, details)

print("Other variante:")
for category, details in books.items():
    print(f"Category: {category}")
    
    if isinstance(details, dict):
        for key, value in details.items():
            print(f"  {key}: {value}")
    else:
        print(f"  {details}")