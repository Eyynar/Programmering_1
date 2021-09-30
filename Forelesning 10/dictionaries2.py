board_game = {
    "title": "Dixit",
    "playtime": 30,
    "age": 8
}

print(board_game["title"])
print(board_game.get("playtime"))


board_game["year"] = 2008
print(board_game)

year = board_game.pop("year")
print(f"After pop: {board_game}")

del board_game["playtime"]
print(f"After del {board_game}")

key = "year"
board_game[key] = year
print(f"After add: {board_game}")

print(board_game[key])


for key, value in board_game.items():
    print(f"{key}: {value}")