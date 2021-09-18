print("==============================================================")
print("=========== WHat is your weight on another planet? ===========")
print("==============================================================")

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_gravity = [3.7, 8.87, 9.807, 3.72, 24.79, 10.44, 8.87, 11.15]

print("===== Planets =====")
print(f"1 - {planets[0]}")
print(f"2 - {planets[1]}")
print(f"3 - {planets[2]}")
print(f"4 - {planets[3]}")
print(f"5 - {planets[4]}")
print(f"6 - {planets[5]}")
print(f"7 - {planets[6]}")
print(f"8 - {planets[7]}")
print("==================")

planet_number = int(input("Pick a planet by typing a number:"))

chosen_planet = planet_number -1
print(f"\nYou picked {planets[chosen_planet]} ")

weight = int(input("Enter your weight in kg: "))

mass = weight / planets_gravity[2]

weight_on_another_planet = mass * planets_gravity[chosen_planet]

print(f"Your weight on {planets[chosen_planet]} is {weight_on_another_planet.__round__(2)}kg.")