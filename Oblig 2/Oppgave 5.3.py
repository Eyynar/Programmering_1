import random

points_single = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
points_double = [2, 4, 6, 7, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
points_triple = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]
points_bullseye = [25, 50]


def throw():
    points_selection = random.randint(0, 3)
    points = 0

    if points_selection == 0:
        points = random.choice(points_single)
        
    if points_selection == 1:
        points = random.choice(points_double)

    if points_selection == 2:
        points = random.choice(points_triple)
        
    elif points_selection == 3:
        points = random.choice(points_bullseye)
        
    return points


def main():
    point = throw()
    print(point)


if __name__ == '__main__':
    main()

