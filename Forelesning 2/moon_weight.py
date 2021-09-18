moon = "Moon"

earth_gravity = 9.807
moon_gravity = 1.622

#my_earth_weight = 85
def weight_calculator():
    my_earth_weight = input("Enter your weight:")

    if my_earth_weight.isnumeric() == True:
        weight = float(my_earth_weight)
        # weight / earth_grav * moon_grav
        my_lunar_weight = weight / earth_gravity * moon_gravity

        print(f"My weight on the moon is: {round(my_lunar_weight, 3)}kg")

    else:
        print("Enter a number")
        weight_calculator()

weight_calculator()