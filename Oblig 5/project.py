import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
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


def add_game():
    title = ent_add_title.get()
    genre = ent_add_genre.get()
    release = ent_add_release.get()
    score = ent_add_score.get()
    developer = ent_add_dev.get()
    image = ent_add_img.get()

    if not title:
        tk.messagebox.showerror("Error", "You can not create a blank game. At the least, it needs a title.")
    else:
        games.append(Game(title, genre, release, score, developer, image).__dict__)

    ent_add_title.delete(0, tk.END)
    ent_add_genre.delete(0, tk.END)
    ent_add_release.delete(0, tk.END)
    ent_add_score.delete(0, tk.END)
    ent_add_dev.delete(0, tk.END)
    ent_add_img.delete(7, tk.END)

    save_to_file()
    display_game_info()
    update_listbox(listbox_info)
    update_listbox(listbox_edit)


def edit_game(*args):
    try:
        index = int(listbox_edit.curselection()[0])
    except IndexError:
        tk.messagebox.showerror("Error", "Could not edit entry, please select a game from the list and try again.")
    else:
        if not ent_edit_title.get():
            tk.messagebox.showerror("Error", "The title cannot be blank.")
        else:
            games[index]["title"] = ent_edit_title.get()
            games[index]["genre"] = ent_edit_genre.get()
            games[index]["release"] = ent_edit_release.get()
            games[index]["score"] = ent_edit_score.get()
            games[index]["developer"] = ent_edit_dev.get()
            games[index]["image"] = ent_edit_img.get()

        save_to_file()
        display_game_info()
        update_listbox(listbox_info)
        update_listbox(listbox_edit)


def display_game_info(*args):
    global img_path
    try:
        game_key = listbox_info.curselection()[0]
        selected_game = dict(games[game_key])
    except IndexError:
        if games:
            selected_game = dict(games[0])
        else:
            selected_game = {}
    finally:
        title_text.set(selected_game['title'])
        genre_text.set(selected_game['genre'])
        release_text.set(selected_game['release'])
        score_text.set(selected_game['score'])
        dev_text.set(selected_game['developer'])

    try:
        img_path = ImageTk.PhotoImage(Image.open(selected_game["image"]))
    except FileNotFoundError:
        img_path = ImageTk.PhotoImage(Image.open(error_image))
    except PermissionError:
        img_path = ImageTk.PhotoImage(Image.open(error_image))
    except KeyError:
        img_path = ImageTk.PhotoImage(Image.open(error_image))
    finally:
        canvas.itemconfigure(cover_img, image=img_path)


def display_edit_info(*args):
    try:
        game_key = listbox_edit.curselection()[0]
        selected_game = dict(games[game_key])

        ent_edit_title.delete(0, tk.END)
        ent_edit_title.insert(0, selected_game['title'])
        ent_edit_genre.delete(0, tk.END)
        ent_edit_genre.insert(0, selected_game['genre'])
        ent_edit_release.delete(0, tk.END)
        ent_edit_release.insert(0, selected_game['release'])
        ent_edit_score.delete(0, tk.END)
        ent_edit_score.insert(0, selected_game['score'])
        ent_edit_dev.delete(0, tk.END)
        ent_edit_dev.insert(0, selected_game['developer'])
        ent_edit_img.delete(0, tk.END)
        ent_edit_img.insert(0, selected_game['image'])
    except IndexError:
        pass


def clear_edit(*args):
    ent_edit_title.delete(0, tk.END)
    ent_edit_genre.delete(0, tk.END)
    ent_edit_release.delete(0, tk.END)
    ent_edit_score.delete(0, tk.END)
    ent_edit_dev.delete(0, tk.END)
    ent_edit_img.delete(0, tk.END)


def save_to_file():
    with open("test.json", "w") as output_file:
        json.dump(games, output_file, indent=4)


def delete_game():
    try:
        game_key = listbox_info.curselection()[0]
        del games[game_key]
        listbox_info.delete(game_key)
        save_to_file()
    except IndexError:
        pass
    update_listbox(listbox_info)
    update_listbox(listbox_edit)
    display_game_info()


def update_listbox(listbox):
    listbox.delete(0, tk.END)
    for game in games:
        listbox.insert(tk.END, game["title"])


# List that contains all stored games
games = []
error_image = "images/error.png"

with open("test.json", "r") as input_file:
    games_list = json.load(input_file)
for game in games_list:
    games.append(game)

window = tk.Tk()
window.title("Games database")
window.resizable(False, False)

# The parent for all tabs
tab_parent = ttk.Notebook(window)

# Main and info tabs
main_frame = tk.Frame(tab_parent)
add_frame = tk.Frame(tab_parent)
edit_frame = tk.Frame(tab_parent)

tab_parent.add(main_frame, text="All games")
tab_parent.add(add_frame, text="Add game")
tab_parent.add(edit_frame, text="Edit games")
tab_parent.bind("<<NotebookTabChanged>>", clear_edit)

tab_parent.pack(fill=tk.BOTH, expand=1)


# ------------Widgets for the "All games" page------------

# Frame for listbox and delete button
listbox_frame = tk.Frame(main_frame)

# Listbox
listbox_info = tk.Listbox(listbox_frame, height=20)
listbox_info.bind("<<ListboxSelect>>", display_game_info)

# Listbox scrollbar
listbox_scrollbar = tk.Scrollbar(listbox_frame)

listbox_info.config(yscrollcommand=listbox_scrollbar.set)
listbox_scrollbar.config(command=listbox_info.yview)

# Delete button
btn_delete = tk.Button(listbox_frame, text="Delete selected", command=delete_game)

# Placing the widgets in the grid
listbox_info.grid(row=0, column=0)
listbox_scrollbar.grid(row=0, column=1, sticky="NS")
btn_delete.grid(row=1, column=0)

# Packing the frame into the main_frame
listbox_frame.pack(side=tk.LEFT)

# Inserts games from the list into the Listbox
update_listbox(listbox_info)


# Frame that contains the game's cover and information
info_frame = tk.Frame(main_frame)

# Cover
canvas = tk.Canvas(info_frame, width=256, height=256)
try:
    img_path = ImageTk.PhotoImage(Image.open(games[0]["image"]))
except FileNotFoundError:
    img_path = ImageTk.PhotoImage(Image.open(error_image))
except IndexError:
    img_path = ImageTk.PhotoImage(Image.open(error_image))
except PermissionError:
    img_path = ImageTk.PhotoImage(Image.open(error_image))
finally:
    cover_img = canvas.create_image(128, 128, anchor="center", image=img_path)

# Labels
lbl_title = tk.Label(info_frame, text="Title:")
lbl_genre = tk.Label(info_frame, text="Genre:")
lbl_release = tk.Label(info_frame, text="Released:")
lbl_score = tk.Label(info_frame, text="Score:")
lbl_dev = tk.Label(info_frame, text="Developed by:")

# Variables to be used to insert text into read-only entry boxes
title_text = tk.StringVar()
genre_text = tk.StringVar()
release_text = tk.StringVar()
score_text = tk.StringVar()
dev_text = tk.StringVar()

# Entries
ent_title = tk.Entry(info_frame, state="readonly", textvariable=title_text)
ent_genre = tk.Entry(info_frame, state="readonly", textvariable=genre_text)
ent_release = tk.Entry(info_frame, state="readonly", textvariable=release_text)
ent_score = tk.Entry(info_frame, state="readonly", textvariable=score_text)
ent_dev = tk.Entry(info_frame, state="readonly", textvariable=dev_text)

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

# Packing the frame into the main_frame
info_frame.pack()

# Inserts details from the first game onto the page on startup.
try:
    title_text.set(games[0]['title'])
    genre_text.set(games[0]['genre'])
    release_text.set(games[0]['release'])
    score_text.set(games[0]['score'])
    dev_text.set(games[0]['developer'])
except IndexError:
    pass


# -----------Widgets for the "Add games" page-----------

# Frame for the form
add_form_frame = tk.Frame(add_frame)


# Labels
lbl_add_title = tk.Label(add_form_frame, text="Title:")
lbl_add_genre = tk.Label(add_form_frame, text="Genre:")
lbl_add_release = tk.Label(add_form_frame, text="Release year:")
lbl_add_score = tk.Label(add_form_frame, text="Review score:")
lbl_add_dev = tk.Label(add_form_frame, text="Developer:")
lbl_add_img = tk.Label(add_form_frame, text="Image path: \n256x256")

# Entries
ent_add_title = tk.Entry(add_form_frame)
ent_add_genre = tk.Entry(add_form_frame)
ent_add_release = tk.Entry(add_form_frame)
ent_add_score = tk.Entry(add_form_frame)
ent_add_dev = tk.Entry(add_form_frame)
ent_add_img = tk.Entry(add_form_frame)
ent_add_img.insert(0, "images/")

# Add button
btn_add_game = tk.Button(add_form_frame, text="Add game", command=add_game)

# Grid placement
lbl_add_title.grid(row=0, column=0, pady=5)
lbl_add_genre.grid(row=1, column=0, pady=5)
lbl_add_release.grid(row=2, column=0, pady=5)
lbl_add_score.grid(row=3, column=0, pady=5)
lbl_add_dev.grid(row=4, column=0, pady=5)
lbl_add_img.grid(row=5, column=0, pady=5)

ent_add_title.grid(row=0, column=1)
ent_add_genre.grid(row=1, column=1)
ent_add_release.grid(row=2, column=1)
ent_add_score.grid(row=3, column=1)
ent_add_dev.grid(row=4, column=1)
ent_add_img.grid(row=5, column=1)

btn_add_game.grid(row=6, column=0, columnspan=2)

# Packing the frame into the tab
add_form_frame.pack()


# -----------Widgets for the "Edit games" page-----------

# Frame for the listbox used ti select titles
listbox_edit_frame = tk.Frame(edit_frame)

# Listbox
listbox_edit = tk.Listbox(listbox_edit_frame, height=20)
listbox_edit.bind("<<ListboxSelect>>", display_edit_info)

# Listbox scrollbar
listbox_edit_scrollbar = tk.Scrollbar(listbox_edit_frame)

listbox_edit.config(yscrollcommand=listbox_edit_scrollbar.set)
listbox_edit_scrollbar.config(command=listbox_edit.yview)

# Placing the widgets in the grid
listbox_edit.grid(row=0, column=0)
listbox_edit_scrollbar.grid(row=0, column=1, sticky="NS")

# Packing the listbox-frame into the page-frame
listbox_edit_frame.pack(side=tk.LEFT)

# Updating the listbox with titles from the games-list
update_listbox(listbox_edit)


# Frame for the edit form
edit_form_frame = tk.Frame(edit_frame)
edit_form_frame.pack()

# Labels
lbl_edit_title = tk.Label(edit_form_frame, text="Title:")
lbl_edit_genre = tk.Label(edit_form_frame, text="Genre:")
lbl_edit_release = tk.Label(edit_form_frame, text="Released:")
lbl_edit_score = tk.Label(edit_form_frame, text="Score:")
lbl_edit_dev = tk.Label(edit_form_frame, text="Developed by:")
lbl_edit_img = tk.Label(edit_form_frame, text="Image path:")

# Entries
ent_edit_title = tk.Entry(edit_form_frame)
ent_edit_genre = tk.Entry(edit_form_frame)
ent_edit_release = tk.Entry(edit_form_frame)
ent_edit_score = tk.Entry(edit_form_frame)
ent_edit_dev = tk.Entry(edit_form_frame)
ent_edit_img = tk.Entry(edit_form_frame)

# Save button
btn_edit_game = tk.Button(edit_form_frame, text="Save", command=edit_game)

# Grid placement
lbl_edit_title.grid(row=0, column=0)
lbl_edit_genre.grid(row=1, column=0)
lbl_edit_release.grid(row=2, column=0)
lbl_edit_score.grid(row=3, column=0)
lbl_edit_dev.grid(row=4, column=0)
lbl_edit_img.grid(row=5, column=0)

ent_edit_title.grid(row=0, column=1, pady=5)
ent_edit_genre.grid(row=1, column=1, pady=5)
ent_edit_release.grid(row=2, column=1, pady=5)
ent_edit_score.grid(row=3, column=1, pady=5)
ent_edit_dev.grid(row=4, column=1, pady=5)
ent_edit_img.grid(row=5, column=1, pady=5)

btn_edit_game.grid(row=6, column=0, columnspan=2)

window.mainloop()
