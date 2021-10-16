import tkinter as tk

window = tk.Tk()

window.title("Hello Tkinter!")

label1 = tk.Label(text="Label 1")
label1.pack()

label2 = tk.Label(text="Label 2", bg="black", fg="white")
label2.pack()

label3 = tk.Label(text="Label 3", bg="yellow", width=10, height=5)
label3.pack()

button1 = tk.Button(text="Button!", width=7, height=2)
button1.pack()

entry1 = tk.Entry(width=15)
entry1.pack()

text1 = tk.Text()
text1.pack()

window.mainloop()

