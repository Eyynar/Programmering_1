print("========What is your weight on another planet?========")

your_weight = input("Whats your weight (in whole kg)? ")
your_weight = int(your_weight)

if your_weight <= 0:
    print(f"Your weight {your_weight}kg is not positive. Please enter a positive weight next time.")
    exit()
elif your_weight > 700:
    print(f"{your_weight}kg cant be right...")

planet_gravity = input("What's the gravity on the planet?")
planet_gravity = float(planet_gravity)
if planet_gravity <= 0:
    print(f"{planet_gravity} can't be a negative number.")
    exit()

planet_name = input("Enter the name of the planet: ")
if planet_name == "Pluto".lower():
    print("Pluto is not a planet")
    exit()
else:
    earth_gravity = 9.607
    your_mass = your_weight / earth_gravity
    weight_on_other_planet = your_mass * planet_gravity

    print(f"\n\nYour weight on {planet_name} is {weight_on_other_planet}")