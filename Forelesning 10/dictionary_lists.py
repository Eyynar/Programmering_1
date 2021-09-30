board_games = [
    {
        "name": "Dixit",
        "playtime": 30,
        "age": 8,
        "year": 2008
    },
    {
        "name": "Pandemic",
        "playtime": 45,
        "age": 8,
        "year": 2008
    },

    {
        "name": "Wingspan",
        "playtime": 40,
        "age": 10,
        "year": 2019
    }
]

print("\nBoard games loop from list:")

for game in board_games:
    print(f"{game.get('name')} has an average playtime of {game.get('playtime')} minutes.")

board_games.append({"name": "Mysterium", "playtime": 42})
print(board_games)

wingspan = board_games[2]
print(f"\n{wingspan}")
