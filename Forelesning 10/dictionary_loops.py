board_game = {
    "title": "Dixit",
    "playtime": 30,
    "age": 8
}

print("\nLoop that iterates through the dictionary")
for key in board_game:
    print(key)

print("\nLoop that iterates through the dictionary values")
for value in board_game.values():
    print(value)

print("\nLoop that iterates through the dictionary key-value pairs")
for key, value in board_game.items():
    print(f"{key} - {value}")
