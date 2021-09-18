tolkien_books = [
    "The Hobbit",
    "Farmer Giles of Ham",
    "The Fellowship of the Ring",
    "The Teo Towers",
    "The Return of the King",
    "The Adventures of Tom Bombadil",
    "Tree and Leaf"
]

length = len(tolkien_books)

print(f"{tolkien_books[0]}, {tolkien_books[1]}, {tolkien_books[length - 1]}, {tolkien_books[length - 2]}\n")

tolkien_books.append("The Silmarillion")
tolkien_books.append("Unfinished Tales")

tolkien_books[2] = "Lord of the Rings: The Fellowship of the Ring"
tolkien_books[3] = "Lord of the Rings: The Two Towers"
tolkien_books[4] = "Lord of the Rings: The Return of the King"

tolkien_books.sort()

for book in tolkien_books:
    print(book)