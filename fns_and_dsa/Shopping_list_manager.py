shopping_list = []

def display_menu():
    print("\nShopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item = input("Enter item to add: ").strip()
        if item:
            shopping_list.append(item)
            print(f"'{item}' added to the shopping list.")
        else:
            print("Item name cannot be empty.")
    elif choice == "2":
        item = input("Enter item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' removed from the shopping list.")
        else:
            print(f"'{item}' not found in the shopping list.")
    elif choice == "3":
        if shopping_list:
            print("\nCurrent Shopping List:")
            for idx, item in enumerate(shopping_list, 1):
                print(f"{idx}. {item}")
        else:
            print("Shopping list is empty.")
    elif choice == "4":
        print("Exiting Shopping List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to")