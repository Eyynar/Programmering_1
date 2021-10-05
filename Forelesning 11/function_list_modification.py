import random


def print_list(list_to_print):
    for element in list_to_print:
        print(element)


def pick_random_board_game(boardgames):
    board_game_index = random.randrange(len(boardgames))
    return boardgames.pop(board_game_index)


board_games = ["Ubungo", "Pandemic", "Ticket to Ride", "Monopoly", "Mysterium"]

print("The original list")
print_list(board_games)

picked_board_game = pick_random_board_game(board_games[:])
print(f"\nYou got {picked_board_game}. Have fun playing")

print("\nThe list after we picked a game:")

print_list(board_games)