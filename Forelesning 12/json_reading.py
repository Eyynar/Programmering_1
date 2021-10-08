import json

with open("planets.json", "r") as file:
    planets_file = json.load(file)

    for planet in planets_file:
        print(planet)


json_string = '''{
    "animal" : "dog",
    "name" : "Fido",
    "age" : "12"
}'''

dog = json.loads(json_string)
print(f"{dog['name']} is a {dog['animal']}")
