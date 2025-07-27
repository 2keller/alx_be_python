

def display_menu():
    # This part tells the helper what choices it has for us.
    print("Shopping List Manager")
    print("1. Add Item (Put something in the basket)")
    print("2. Remove Item (Take something out of the basket)")
    print("3. View List (See everything in the basket)")
    print("4. Exit (Stop playing with the helper)")

def main():
    # This is our empty basket where we'll put our things.
    shopping_list = []

    # This is like playing a game with the helper until we say "stop."
    while True:
        # First, the helper shows us all the choices.
        display_menu()

        # Then, we tell the helper what we want to do!
        choice = input("Enter your choice: ")

        # If we pick '1', it means we want to add something!
        if choice == '1':
            item_to_add = input("What would you like to add? ") # We tell the helper the name of the thing.
            shopping_list.append(item_to_add) # The helper puts it in our basket!
            print(f"{item_to_add} has been added!") # The helper tells us it did it.

        # If we pick '2', it means we want to take something out!
        elif choice == '2':
            item_to_remove = input("What would you like to remove? ") # We tell the helper the name of the thing.
            if item_to_remove in shopping_list: # The helper checks if that thing is really in the basket.
                shopping_list.remove(item_to_remove) # If it is, the helper takes it out!
                print(f"{item_to_remove} has been removed!") # The helper tells us it did it.
            else:
                print(f"Oops! {item_to_remove} is not in your list.") # If it's not there, the helper tells us.

        # If we pick '3', it means we want to see everything in the basket!
        elif choice == '3':
            print("\n--- Your Shopping List ---") # The helper tells us it's showing the list.
            if not shopping_list: # The helper checks if the basket is empty.
                print("Your basket is empty. Time to add some fun things!")
            else:
                # The helper shows us each thing, one by one.
                for item in shopping_list:
                    print(f"- {item}")
            print("------------------------\n")

        # If we pick '4', it means we want to stop playing!
        elif choice == '4':
            print("Goodbye! See you next time!")
            break # The helper stops.

        # If we pick something silly, the helper tells us to pick again!
        else:
            print("That's not a choice. Please pick 1, 2, 3, or 4.")

# This line just makes sure our helper starts working when we open the recipe book.
if __name__ == "__main__":
    main()
