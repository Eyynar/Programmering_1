def main():
    import math

    def calculate():
        check_int = False

        while not check_int:
            num = input("Enter an integer: ")

            try:
                try_int = int(num)

                if try_int <= 1:
                    print("The integer must be higher than or equal 2. ")
                    check_int = True
                    calculate()
                elif len(num) >= 17:
                    print("The integer can have 16 digits at most. Please choose another integer. ")
                    check_int = True
                    calculate()

                square_root = math.sqrt(int(num))
                i = 2

                while i <= float(square_root):
                    new_num = int(num) / int(i)
                    if float(new_num) == int(new_num):
                        print(num + " is not a primary number, as " + str(i) + " is a factor in the number. ")
                        i += int(num)
                        calculate()
                    elif float(new_num):
                        i += 1
                    else:
                        print("Something is wrong. ")
                        i += int(num)
                        calculate()

                print(num + " is a primary number. ")
                check_int = True

            except ValueError:
                print("This is not an acceptable input. Please choose an integer. ")
                calculate()


    calculate()


if __name__ == "__main__":
    main()