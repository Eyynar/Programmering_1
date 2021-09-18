import random

numbers = []

for i in range(660200):
    numbers.append(random.randint(0, 11935300))

print(sum(numbers))

for digits in str(sum(numbers)):
    print(digits)