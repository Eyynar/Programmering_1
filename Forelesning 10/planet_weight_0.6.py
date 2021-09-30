def calculate_weight(your_weight, planet_gravity, original_planet_gravity=9.807):
    calculated_weight = (your_weight / original_planet_gravity) * planet_gravity
    return round(calculated_weight, 2)


planets = [
    {
        "name": "Mercury",
        "gravity": 3.7
    },

    {
        "name": "Venus",
        "gravity": 8.87
    },

    {
        "name": "Earth",
        "gravity": 9.807
    },

    {
        "name": "Mars",
        "gravity": 3.721
    },

    {
        "name": "Jupiter",
        "gravity": 24.79
    },

    {
        "name": "Saturn",
        "gravity": 10.44
    },

    {
        "name": "Uranus",
        "gravity": 8.87
    },

    {
        "name": "Neptune",
        "gravity": 11.15
    }
]

for index, planet in enumerate(planets):
    print(f"{index+1} - {planet['name']}")

planet_number = int(input("Pick planet: "))
chosen_planet = planets[planet_number]
user_weight = int(input("Your weight: "))

calculated_weight = calculate_weight(user_weight, chosen_planet["gravity"])

print(f"Your weight on {chosen_planet['name']} is {calculated_weight}kg")