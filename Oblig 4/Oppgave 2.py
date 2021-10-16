class Film:
    def __init__(self, title, year, rating):
        self.title = title
        self.year = year
        self.rating = rating

    def print_film(self):
        print(f"\n{self.title} was released in {self.year}, with a rating of {self.rating}")


inception = Film("Inception", 2010, 8.8)
martian = Film("The Martian", 2015, 8.)
joker = Film("Joker", 2019, 8.4)

print(f"{inception.title} was released in {inception.year}, with a rating of {inception.rating}")
print(f"{martian.title} was released in {martian.year}, with a rating of {martian.rating}")
print(f"{joker.title} was released in {joker.year}, with a rating of {joker.rating}")

print("\nUsing method:")
inception.print_film()
martian.print_film()
joker.print_film()
