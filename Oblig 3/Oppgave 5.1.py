def add_to_list(list_name, title, year, rating=5.0):
    list_name.append({"title": title, "year": year, "rating": rating})


list_movies = [
    {
        "title": "Inception",
        "year": 2010,
        "rating": 8.7
    },
    {
        "title": "Inside Out",
        "year": 2015,
        "rating": 8.1
    },
    {
        "title": "Con Air",
        "year": 1997,
        "rating": 6.9
    }
]

for element in list_movies:
    print(element)

add_to_list(list_movies, "Dune", 2021, 8.4)
add_to_list(list_movies, "Dunkirk", 2021, 7.8)
add_to_list(list_movies, "Upgrade", 2018)

print("\nList after adding more movies: ")
for element in list_movies:
    print(element)
