planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_gravity = [3.7, 8.87, 9.807, 3.721, 24.79, 10.44, 8.87, 11.15]

close = False
while not close:
    print("\n=============================================================================")
    print("====================What is your weight on other planets?====================")
    print("=============================================================================")

    for planet_number in range(len(planets)):
        print(f"{planet_number + 1} - {planets[planet_number]}")

    planet_number = input("\n Pick a planet by typing a number: ")
    planet_number = int(planet_number) - 1

    print(f"\nYou picked: {planets[planet_number]}")

    your_weight = float(input("\nType in your weight in kg: "))

    earth_gravity = planets_gravity[2]

    your_weight_on_other_planet = (your_weight / earth_gravity) * planets_gravity[planet_number]

    print(f"\nYour weight on {planets[planet_number]} is {round(your_weight_on_other_planet, 2)}kg")

    answer = input("Would you like to run the program again? (y/n)")

    if answer.lower != "y":
        close = True
