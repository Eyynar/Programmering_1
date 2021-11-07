import tkinter
import json


class Game:
    def __init__(self, title, release, score, developer, image):
        self.title = title
        self.release = release
        self.score = score
        self.developer = developer
        self.image = image


def add_to_list(title, release, score, developer, image):
    game_list.append(Game(title, release, score, developer, image).__dict__)


game_list = []

add_to_list("The Outer Wilds", 2019, 10, "blank", 2)


with open("test.json", "w") as output_file:
    json.dump(game_list, output_file, indent=4)


with open("test.json", "r") as input_file:
    print(json.load(input_file))

