books = ["Harry Potter", "Matilda", "Diary"]
copies = [3, 0, 2]
library = dict(zip(books, copies))

print(list(filter(lambda b: library[b] > 0, books)))

fees = list(map(lambda f: f + 1, [2, 5, 3]))
print(fees)

chosen = input("Enter book: ")
for b in books:
    if b == chosen:
        print("Available" if library[b] > 0 else "Unavailable")
        break
else:
    print("Book not found")
