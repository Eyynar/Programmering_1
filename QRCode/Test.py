from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        earth_gravity = 9.807
        moon_gravity = 1.622
        value = float(weight.get())
        moon_weight.set(int(value / earth_gravity * moon_gravity))
    except ValueError:
        pass

window = Tk()
window.title("Calculator")

frame = ttk.Frame(window)
frame.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

weight = StringVar()
weight_entry = ttk.Entry(frame, width=7, textvariable=weight)
weight_entry.grid(column=2, row=1, sticky=(W, E))

moon_weight = StringVar()
ttk.Label(frame, textvariable=moon_weight).grid(column=2, row=2, sticky=(W, E))

ttk.Button(frame, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(frame, text="earth weight").grid(column=3, row=1, sticky=W)
ttk.Label(frame, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(frame, text="moon weight").grid(column=3, row=2, sticky=W)

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)
weight_entry.focus()
window.bind("<Return>", calculate)



window.mainloop()