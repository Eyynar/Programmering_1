#En dictionary som inneholder aller personenen og deres antall cookies
personer = {
    "person_1": 5,
    "person_2": 9,
    "person_3": 2.5,
    "person_4": 21,
    "person_5": 0

}

#Den totale mengden cookies
total = 0

#En for loop som går gjennom alle verdiene i personer og legger de sammen til en ny total
for x in personer.values():
    total += x

#En integer av gjennomsnittet blir funnet ved å dele totalen på antall personer.
avg = int(total / len(personer))

#Gjennomsnittet printes.
print("Gjennomsnittet er", avg)