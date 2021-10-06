def add_to_list(list_name, title, year, rating=5.0):
    list_name.append({"title": title, "year": year, "rating": rating})


def print_list(list_name):
    for element in list_name:
        print(f"{element['title']} - {element['year']} has a rating of {element['rating']}")


def avg_rating(list_name):
    rating_sum = 0
    for element in list_name:
        rating_sum += element['rating']
    average = rating_sum/len(list_name)
    print(f"\nThe titles in this list have an average rating of {round(average, 2)}\n")


def print_by_release(list_name, year):
    print(f"Movies released in or after {year}: ")
    for element in list_name:
        if element["year"] >= year:
            print(f"{element['title']} - {element['year']} has a rating of {element['rating']}")


def write_to_file(list_name, file_name):
    with open(file_name, "w") as file:
        for element in list_name:
            file.write(element["title"] + "\n")


def read_file(file_name):
    print("\nMovies read from file:")
    with open(file_name, "r") as file:
        content = file.read()
    print(content)


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

add_to_list(list_movies, "Dune", 2021, 8.4)
add_to_list(list_movies, "Dunkirk", 2021, 7.8)
add_to_list(list_movies, "Upgrade", 2018)

print_list(list_movies)

avg_rating(list_movies)

print_by_release(list_movies, 2016)

write_to_file(list_movies, "movie_titles.txt")

read_file("movie_titles.txt")
