list_items = ("Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10",)
user_list = []

close = False


def operations(user_choice):
    if user_choice == "add":
        user_selection = int(input("\nWhich item do you want to add to the list? "))
        user_list.append(list_items[user_selection - 1])
        print("The item was added to your list.")

    elif user_choice == "delete":
        user_selection = int(input("\nWhich item do you want to delete from the list? "))
        user_list.remove(user_list[user_selection - 1])

    elif user_choice == "print":
        if len(user_list) > 0:

            print("\n=============== Your list ===============")

            for i in range(len(user_list)):
                print(f"{i + 1}. {user_list[i]}")

        else:
            print("\nThere are no items in your list.")

    elif user_choice == "stop":
        global close
        close = True

    else:
        print("\nPlease enter a valid option.")


def main():
    print("=============== Packing list ==============")

    for i in range(len(list_items)):
        print(f"{i + 1}. {list_items[i]}")

    print("\nDo you want to add an item to your list, delete an item from your list, print the list, "
          "or stop the program? (add/delete/print/stop): ")

    while not close:
        user_choice = input("\nEnter command: ")

        operations(user_choice)


if __name__ == '__main__':
    main()
