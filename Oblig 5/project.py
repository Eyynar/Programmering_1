import tkinter as tk
import json


class Game:
    def __init__(self, title, release, score, developer, image):
        self.title = title
        self.release = release
        self.score = score
        self.developer = developer
        self.image = image


def add_game(title, release, score, developer, image):
    games.append(Game(title, release, score, developer, image).__dict__)


def edit_game(index, new_title, new_release, new_score, new_developer, new_image):
    games[index]["title"] = new_title
    games[index]["release"] = new_release
    games[index]["score"] = new_score
    games[index]["developer"] = new_developer
    games[index]["image"] = new_image


def item_selected(*args):
    game_key = listbox_movies.get(listbox_movies.curselection())
    game = games[game_key]

    ent_game_title.delete(0, tk.END)
    ent_game_title.insert(0, game['title'])
    ent_movie_year.delete(0, tk.END)
    ent_movie_year.insert(0, game['year'])
    ent_movie_duration.delete(0, tk.END)
    ent_movie_duration.insert(0, game['duration'])


def save_game():
    pass


games = []

add_game("The Outer Wilds", 2019, 10, "blank", 2)


with open("test.json", "w") as output_file:
    json.dump(games, output_file, indent=4)


with open("test.json", "r") as input_file:
    print(json.load(input_file))

window = tk.Tk();

# List frame
list_frame = tk.Frame()

# TODO Fikse tittel på i listen
game_list = tk.StringVar(value=list(games))
listbox_movies = tk.Listbox(list_frame, listvariable=game_list)
listbox_movies.bind('<<ListboxSelect>>', item_selected)

listbox_movies.pack()
list_frame.pack(side=tk.LEFT)


# Main frame
main_frame = tk.Frame()

# Form labels
lbl_movie_title = tk.Label(main_frame, text="Title:")
lbl_movie_year = tk.Label(main_frame, text="Year:")
lbl_movie_duration = tk.Label(main_frame, text="Duration:")

# Form entries
ent_game_title = tk.Entry(main_frame)
ent_movie_year = tk.Entry(main_frame)
ent_movie_duration = tk.Entry(main_frame)

btn_save = tk.Button(main_frame, text="Save", command=save_game)


lbl_movie_title.grid(row=0, column=0)
lbl_movie_year.grid(row=1, column=0)
lbl_movie_duration.grid(row=2, column=0)
ent_game_title.grid(row=0, column=1)
ent_movie_year.grid(row=1, column=1)
ent_movie_duration.grid(row=2, column=1)
btn_save.grid(row=3, column=0, columnspan=2)

main_frame.pack()

window.mainloop()
