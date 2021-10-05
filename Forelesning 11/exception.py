try:
    number1 = int(input("Enter a whole number: "))
    number2 = int(input("Enter another whole number: "))
    answer = number1 / number2
except ValueError:
    print("\nYou have to enter a valid number.")
except ZeroDivisionError:
    print("You can not divide by zero.")
else:
    print(f"{number1} / {number2} = {answer}")
    