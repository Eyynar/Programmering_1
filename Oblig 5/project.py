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


def display_game(*args):
    game_key = listbox.curselection()[0]
    game = games_list[game_key]

    ent_title.delete(0, tk.END)
    ent_title.insert(0, game['title'])
    ent_release.delete(0, tk.END)
    ent_release.insert(0, game['release'])
    ent_score.delete(0, tk.END)
    ent_score.insert(0, game['score'])


def save_to_file():
    with open("test.json", "w") as output_file:
        json.dump(games, output_file, indent=4)


def save_game():
    pass


games = []

window = tk.Tk()

# Listbox og frame
listbox_frame = tk.Frame()
listbox = tk.Listbox(listbox_frame)

listbox.pack()
listbox_frame.pack(side=tk.LEFT)

listbox.bind("<<ListboxSelect>>", display_game)

# Inserts games from the list into the Listbox
with open("test.json", "r") as input_file:
    games_list = json.load(input_file)
    for i in range(len(games_list)):
        listbox.insert(i, games_list[i]["title"])


# Main frame
main_frame = tk.Frame()

# Cover
canvas = tk.Canvas(main_frame, width=300, height=300)
img = ImageTk.PhotoImage(Image.open(games_list[0]["image"]))
canvas.create_image(20, 20, anchor="nw", image=img)

# Form labels
lbl_title = tk.Label(main_frame, text="Title:")
lbl_release = tk.Label(main_frame, text="Released:")
lbl_score = tk.Label(main_frame, text="Score:")

# Form entries
ent_title = tk.Entry(main_frame)
ent_release = tk.Entry(main_frame)
ent_score = tk.Entry(main_frame)

btn_save = tk.Button(main_frame, text="Save", command=save_game)

canvas.grid(row=0, column=0, columnspan=2)
lbl_title.grid(row=1, column=0)
lbl_release.grid(row=2, column=0)
lbl_score.grid(row=3, column=0)
ent_title.grid(row=1, column=1)
ent_release.grid(row=2, column=1)
ent_score.grid(row=3, column=1)
btn_save.grid(row=4, column=0, columnspan=2)

main_frame.pack()

window.mainloop()
