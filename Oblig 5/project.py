import tkinter as tk
import json
from PIL import ImageTk, Image

class Game:
    def __init__(self, title, release, score, developer, image):
        self.title = title
        self.release = release
        self.score = score
        self.developer = developer
        self.image = image


def add_game(title, release, score, developer, image):
    games.append(Game(title, release, score, developer, image).__dict__)
    save_to_file()


def edit_game(index, new_title, new_release, new_score, new_developer, new_image):
    games[index]["title"] = new_title
    games[index]["release"] = new_release
    games[index]["score"] = new_score
    games[index]["developer"] = new_developer
    games[index]["image"] = new_image
    save_to_file()


def display_game(event):
    pass


def save_to_file():
    with open("test.json", "w") as output_file:
        json.dump(games, output_file, indent=4)



def save_game():
    pass


games = []

# add_game("The Outer Wilds", 2019, 10, "blank", 2)
# add_game("Hollow Knight", 2017, 10, "Team Cherry", 2)

window = tk.Tk()

# Listbox og frame
listbox_frame = tk.Frame()
listbox = tk.Listbox(listbox_frame)

listbox.pack()
listbox_frame.pack(side=tk.LEFT)

listbox.bind("<<ListboxSelect>>", display_game)

# Legger til elementer i lista
with open("test.json", "r") as input_file:
    games_list = json.load(input_file)
    for i in range(len(games_list)):
        listbox.insert(i, games_list[i]["title"])


# Main frame
main_frame = tk.Frame()

# Cover
canvas = tk.Canvas(main_frame, width = 300, height = 300)
img = ImageTk.PhotoImage(Image.open("images/theouterwilds.jpg"))
canvas.create_image(20, 20, anchor="nw", image=img)

# Form labels
lbl_movie_title = tk.Label(main_frame, text="Title:")
lbl_movie_year = tk.Label(main_frame, text="Year:")
lbl_movie_duration = tk.Label(main_frame, text="Duration:")

# Form entries
ent_movie_title = tk.Entry(main_frame)
ent_movie_year = tk.Entry(main_frame)
ent_movie_duration = tk.Entry(main_frame)

btn_save = tk.Button(main_frame, text="Save", command=save_game)


canvas.grid(row=0, column=0, columnspan=2)
lbl_movie_title.grid(row=1, column=0)
lbl_movie_year.grid(row=2, column=0)
lbl_movie_duration.grid(row=3, column=0)
ent_movie_title.grid(row=1, column=1)
ent_movie_year.grid(row=2, column=1)
ent_movie_duration.grid(row=3, column=1)
btn_save.grid(row=4, column=0, columnspan=2)

main_frame.pack()


window.mainloop()
