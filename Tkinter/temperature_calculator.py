import tkinter as tk

def convert(*args):
    fahrenheit = ent_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

window = tk.Tk()
window.title("Temperature converter")
window.resizable(width=False, height=True)

frm_entry = tk.Frame(master=window)
frm_entry.grid(row=0, column=0, padx=10)

ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temperature = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temperature.grid(row=0, column=1, sticky="w")

btn_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=convert)
btn_convert.grid(row=0, column=2, pady=10)

lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")
lbl_result.grid(row=0, column=3, padx=10)

window.bind("<Return>", convert)
window.mainloop()