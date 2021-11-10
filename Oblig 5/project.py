import tkinter as tk
from tkinter import ttk
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


def edit_game(*args):
    try:
        index = listbox.curselection()[0]
    except IndexError:
        index = 0

    new_title = ent_title.get()
    new_genre = ent_genre.get()
    new_release = ent_release.get()
    new_score = ent_score.get()
    new_developer = ent_dev.get()
    # new_image = ent_ima.get()

    games[index]["title"] = new_title
    games[index]["genre"] = new_genre
    games[index]["release"] = new_release
    games[index]["score"] = new_score
    games[index]["developer"] = new_developer
    # games[index]["image"] = new_image
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


def delete_game():
    try:
        game_key = listbox.curselection()[0]
        del games[game_key]
        listbox.delete(game_key)
        save_to_file()
    except IndexError:
        pass


# List that contains all stored games
games = []

window = tk.Tk()
window.resizable(False, False)

# The parent for all tabs
frame_parent = ttk.Notebook(window)

# Main and info tabs
main_frame = tk.Frame(frame_parent)
add_frame = tk.Frame(frame_parent)

frame_parent.add(main_frame, text="All games")
frame_parent.add(add_frame, text="Add games")

frame_parent.pack(fill=tk.BOTH, expand=1)

# Widgets for the "All games" page
# Frame for listbox and delete button
listbox_frame = tk.Frame(main_frame)
listbox_frame.pack(side=tk.LEFT)

# Listbox
listbox = tk.Listbox(listbox_frame, height=20)
listbox.bind("<<ListboxSelect>>", display_game)

# Listbox scrollbar
listbox_scrollbar = tk.Scrollbar(listbox_frame)

listbox.config(yscrollcommand=listbox_scrollbar.set)
listbox_scrollbar.config(command=listbox.yview)

# Delete button
btn_delete = tk.Button(listbox_frame, text="Delete selected", command=delete_game)

# Placing the widgets in the grid
listbox.grid(row=0, column=0)
listbox_scrollbar.grid(row=0, column=1, sticky="NS")
btn_delete.grid(row=1, column=0)


# Inserts games from the list into the Listbox
with open("test.json", "r") as input_file:
    games_list = json.load(input_file)
    for game in games_list:
        games.append(game)
        listbox.insert(tk.END, game["title"])


# Frame that contains all the game info
info_frame = tk.Frame(main_frame)

# Cover
canvas = tk.Canvas(info_frame, width=225, height=225)
img_path = ImageTk.PhotoImage(Image.open(games_list[0]["image"]))
cover_img = canvas.create_image(0, 0, anchor="nw", image=img_path)

# Form labels
lbl_title = tk.Label(info_frame, text="Title:")
lbl_genre = tk.Label(info_frame, text="Genre:")
lbl_release = tk.Label(info_frame, text="Released:")
lbl_score = tk.Label(info_frame, text="Score:")
lbl_dev = tk.Label(info_frame, text="Developed by:")

# Form entries
ent_title = tk.Entry(info_frame)
ent_genre = tk.Entry(info_frame)
ent_release = tk.Entry(info_frame)
ent_score = tk.Entry(info_frame)
ent_dev = tk.Entry(info_frame)

# Save button
btn_save = tk.Button(info_frame, text="Save", command=edit_game)

# Positioning all of the elements in the grid.
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

info_frame.pack()

# Inserts details form the first game onto the page.
ent_title.insert(0, games[0]['title'])
ent_genre.insert(0, games[0]['genre'])
ent_release.insert(0, games[0]['release'])
ent_score.insert(0, games[0]['score'])
ent_dev.insert(0, games[0]['developer'])


# Widgets for the "Add games" page
form_frame = tk.Frame(add_frame)

window.mainloop()
