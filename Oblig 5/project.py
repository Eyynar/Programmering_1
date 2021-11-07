import tkinter
import json


class Game:
    def __init__(self, title, release, score, developer, image):
        self.title = title
        self.release = release
        self.score = score
        self.developer = developer
        self.image = image


def add_game(title, release, score, developer, image):
    key = title
    games[key] = Game(title, release, score, developer, image).__dict__


def edit_game(key, new_title, new_release, new_score, new_developer, new_image):
    games[key]["title"] = new_title
    games[key]["release"] = new_release
    games[key]["score"] = new_score
    games[key]["developer"] = new_developer
    games[key]["image"] = new_image


games = {}

add_game("The Outer Wilds", 2019, 10, "blank", 2)


with open("test.json", "w") as output_file:
    json.dump(games, output_file, indent=4)


with open("test.json", "r") as input_file:
    print(json.load(input_file))

