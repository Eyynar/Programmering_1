user_input = ""

with open("text_files/my_novel.txt", "a") as file:
    while user_input != "q":
        user_input = input(": ")
        file.write(user_input + "\n")