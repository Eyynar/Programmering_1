import random

number_of_players = int(input("Input the number of players: "))

for i in range(number_of_players):
    print(f"\n\n===== Player {i+1} ===== ")

    total = 0
    for j in range(3):
        score = random.randint(0, 60)
        print(f"Throw {j+1}: {score}")
        total += score

    print(f"\nTotal for player {i+1}: {total}")
    