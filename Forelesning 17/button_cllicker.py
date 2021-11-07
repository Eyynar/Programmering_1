import tkinter as tk
import tkinter_helper as tkh


def increment(*args):
    number.set(number.get() + 1)


def number_changed(*args):
    print(f"We changed! New value: {number.get}")


window = tk.Tk()
window.title("Button clicker!")

tkh.create_big_ui(32)

number = tk.IntVar(0)
number.trace("w", callback=increment)
lbl_number = tk.Label(textvariable=number)
btn_increment = tk.Button(text="Click me!", command=increment)
# btn_increment.bind("<Button-1>", func=increment)

lbl_number.pack()
btn_increment.pack(padx=20, pady=(0, 10))

window.mainloop()
