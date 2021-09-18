tolkien_books = [
    'Farmer Giles of Ham',
    'Lord of the Rings: The Fellowship of the Ring',
    'Lord of the Rings: The Return of the King',
    'Lord of the Rings: The Two Towers',
    'The Adventures of Tom Bombadil',
    'The Hobbit',
    'The Silmarillion',
    'Tree and Leaf',
    'Unfinished Tales'
]

new_list = []

for book in tolkien_books:
    if "Lord of the Rings" in book:
        new_list.append(book)

for i in range(len(new_list)):
    print(new_list[i])