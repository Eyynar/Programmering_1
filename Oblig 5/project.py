import tkinter as tk
import json
from PIL import ImageTk, Image


class Game:
    def __init__(self, title, genre, release, score, developer, image):
        self.title = title
        self.genre = genre
        self.release = release
        self.score = score
        self.developer = developer
        self.image = image


def add_game(title, genre, release, score, developer, image):
    games.append(Game(title, genre, release, score, developer, image).__dict__)
    save_to_file()


def edit_game(index, new_title, new_genre, new_release, new_score, new_developer, new_image):
    games[index]["title"] = new_title
    games[index]["genre"] = new_genre
    games[index]["release"] = new_release
    games[index]["score"] = new_score
    games[index]["developer"] = new_developer
    games[index]["image"] = new_image
    save_to_file()


def display_game(*args):
    global img_path
    game_key = listbox.curselection()[0]
    game = games_list[game_key]

    img_path = ImageTk.PhotoImage(Image.open(games_list[game_key]["image"]))
    canvas.itemconfigure(cover_img, image=img_path)

    ent_title.delete(0, tk.END)
    ent_title.insert(0, game['title'])
    ent_genre.delete(0, tk.END)
    ent_genre.insert(0, game['genre'])
    ent_release.delete(0, tk.END)
    ent_release.insert(0, game['release'])
    ent_score.delete(0, tk.END)
    ent_score.insert(0, game['score'])
    ent_dev.delete(0, tk.END)
    ent_dev.insert(0, game['developer'])


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
    for game in games_list:
        listbox.insert(tk.END, game["title"])


# Main frame
main_frame = tk.Frame()

# Cover
canvas = tk.Canvas(main_frame, width=225, height=225)
img_path = ImageTk.PhotoImage(Image.open(games_list[0]["image"]))
cover_img = canvas.create_image(0, 0, anchor="nw", image=img_path)

# Form labels
lbl_title = tk.Label(main_frame, text="Title:")
lbl_genre = tk.Label(main_frame, text="Genre:")
lbl_release = tk.Label(main_frame, text="Released:")
lbl_score = tk.Label(main_frame, text="Score:")
lbl_dev = tk.Label(main_frame, text="Developed by:")

# Form entries
ent_title = tk.Entry(main_frame)
ent_genre = tk.Entry(main_frame)
ent_release = tk.Entry(main_frame)
ent_score = tk.Entry(main_frame)
ent_dev = tk.Entry(main_frame)

btn_save = tk.Button(main_frame, text="Save", command=save_game)

canvas.grid(row=0, column=0, columnspan=2)
lbl_title.grid(row=1, column=0)
lbl_genre.grid(row=2, column=0)
lbl_release.grid(row=3, column=0)
lbl_score.grid(row=4, column=0)
lbl_dev.grid(row=5, column=0)
ent_title.grid(row=1, column=1)
ent_genre.grid(row=2, column=1)
ent_release.grid(row=3, column=1)
ent_score.grid(row=4, column=1)
ent_dev.grid(row=5, column=1)
btn_save.grid(row=6, column=0, columnspan=2)

main_frame.pack()

window.mainloop()
