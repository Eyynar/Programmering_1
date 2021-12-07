e = 0
for i in range(9):
    e += 1
    print(e)
    e = e % 2
    print(f"{e}\n")


a = 4
b = 3
if a > b:
    print("A")
elif a > 0:
    print("B")
else:
    print("C")


def gjennomsnitt(tall1, tall2, tall3):
    return (tall1 + tall2 + tall3) / 3


def antall_nuller(array):
    teller = 0
    for element in array:
        if element == 0:
            teller += 1
    return teller


liste = [1, 0, 2, 0, 3, 67, 3, 9, 1, 0, 0, 0]

print(antall_nuller(liste))


arr1 = ["bil", "buss", "båt"]
arr2 = ["vrak", "henger", "tur"]

for element1 in arr1:
    for element2 in arr2:
        print(f"{element1}{element2}")


def sekunder_til_minutter(sekunder):
    minutt = sekunder // 60
    sekunder = sekunder % 60
    print(f"{minutt} minutter, {sekunder} sekunder.")


sekunder_til_minutter(5829)
