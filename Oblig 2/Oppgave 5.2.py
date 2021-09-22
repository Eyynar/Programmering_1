import random

points = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
          [2, 4, 6, 7, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
          [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],
          [25, 50]]

number_of_players = int(input("Input the number of players: "))
number_of_rounds = int(input("Input the number of round the players will play: "))
number_of_throws = int(input("Input number of throws each player throws per round? "))

for h in range(number_of_rounds):
    print(f"\n\n=============== Round {h + 1} ===============")

    for i in range(number_of_players):
        print(f"\n\n===== Player {i + 1} ===== ")

        total = 0
        for j in range(number_of_throws):
            point_selection = random.choice(points)
            score = random.choice(point_selection)
            print(f"Throw {j + 1}: {score}")
            total += score

        print(f"\nTotal for player {i + 1}: {total}")
