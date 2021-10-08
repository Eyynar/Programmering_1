def modify_list(list_name, title, year, rating=5.0, action="add"):
    if action == "add":
        list_name.append({"title": title, "year": year, "rating": rating})
    elif action == "remove":
        for i in range(len(list_movies)-1):
            if list_movies[i]["title"] == title:
                del list_movies[i]
    elif action == "change":
        for j in range(len(list_movies)):
            if list_movies[j]["title"] == title:
                list_movies[j]["year"] = year
                list_movies[j]["rating"] = rating


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

modify_list(list_movies, "Dune", 2021, 8.4)
modify_list(list_movies, "Dunkirk", 2021, 7.8)
modify_list(list_movies, "Upgrade", 2018)

modify_list(list_movies, "Dune", 20221, 7, "change")

print("\nList after adding more movies: ")
for element in list_movies:
    print(element)
