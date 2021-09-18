import random

list_of_numbers = []

for i in range(100):
    list_of_numbers.insert(i, random.randint(0, 100))

sorted_list = sorted(list_of_numbers)

print(list_of_numbers)
print(sorted_list)

sum_av_tall = 0
for num in list_of_numbers:
    sum_av_tall += num

print(f"\nSum: {sum_av_tall}")

