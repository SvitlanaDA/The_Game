phone_book = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-123-4567"
}
alice_phone = phone_book.get("Alice", "Not available")
print(alice_phone)

del phone_book["Bob"]
print(phone_book)