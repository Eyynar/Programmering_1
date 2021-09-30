board_games = {
    "dixit2008": {
        "name": "Dixit",
        "playtime": 30,
        "age": 8,
        "year": 2008
    },
    "pandemic2008": {
        "name": "Pandemic",
        "playtime": 45,
        "age": 8,
        "year": 2008
    },

    "wingspan2019": {
        "name": "Wingspan",
        "playtime": 40,
        "age": 10,
        "year": 2019
    }
}

board_games["mysterium2015"] = {
        "name": "Mysterium",
        "playtime": 42,
        "age": 10,
        "year": 2015
    }

for board_game in board_games.values():
    print(f"{board_game['name']} was released in {board_game['year']}")