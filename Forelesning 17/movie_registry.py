import tkinter as tk
import tkinter_helper as tkh


def save_movie():
    title = ent_movie_title.get()
    year = int(ent_movie_year.get())
    duration = int(ent_movie_duration.get())

    key = f"({year}) {title}"
    movies[key] = {'title': title, 'year': year, 'duration': duration}
    listbox_movies.insert(tk.END, key)


def item_selected(*args):
    movie_key = listbox_movies.get(listbox_movies.curselection())
    movie = movies[movie_key]

    ent_movie_title.delete(0, tk.END)
    ent_movie_title.insert(0, movie['title'])
    ent_movie_year.delete(0, tk.END)
    ent_movie_year.insert(0, movie['year'])
    ent_movie_duration.delete(0, tk.END)
    ent_movie_duration.insert(0, movie['duration'])



movies = {
    '(2020) Soul':
        {
            'title': 'Soul',
            'year': 2020,
            'duration': 100
        },

    '(2021) Dune':
        {
            'title': 'Dune',
            'year': 2021,
            'duration': 156
        }
}

window = tk.Tk()
tkh.create_big_ui(32)

# List frame
list_frame = tk.Frame()

movie_list = tk.StringVar(value=list(movies))
listbox_movies = tk.Listbox(list_frame, listvariable=movie_list)
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
ent_movie_title = tk.Entry(main_frame)
ent_movie_year = tk.Entry(main_frame)
ent_movie_duration = tk.Entry(main_frame)

btn_save = tk.Button(main_frame, text="Save", command=save_movie)


lbl_movie_title.grid(row=0, column=0)
lbl_movie_year.grid(row=1, column=0)
lbl_movie_duration.grid(row=2, column=0)
ent_movie_title.grid(row=0, column=1)
ent_movie_year.grid(row=1, column=1)
ent_movie_duration.grid(row=2, column=1)
btn_save.grid(row=3, column=0, columnspan=2)

main_frame.pack()

window.mainloop()
