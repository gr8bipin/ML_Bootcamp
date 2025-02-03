"""
Task for 27 Jan, 2025:

[A] Create same FRIDGE Simulation App using functions for all 6 features.
    Create a Python Program, which must be menu driven and that is simulation of a fridge.
    In the program, user must be able to:
    1. Add an item to the fridge.
    2. Remove an item from the fridge.
    3. Check if an item is in the fridge.
    4. Check all items in the fridge.
    5. Exit.

"""
print("======================== Welcome to the menu driven app ============================")
fridge = []
while True:
    choice = input("Enter your choice: ")
    if choice == "1":
        def add(item):
            fridge.append(item)
            print(f"{item} is added in the fridge.")
        add("apple")
    elif choice == "2":
        def remove(item):
            fridge.remove(item)
            print(f"{item} is removed from the fridge.")
        remove("apple")
    elif choice == "3":
        for item in fridge:
            if item in fridge:
                print(f"{item} is in the fridge.")
            else:
                print(f"{item} is not in the fridge.")  
    elif choice == "4":
        for item in fridge:
            print(item)                
    elif choice == "5":
        print("Program exited.")
        exit()
        break
    else:
        print()
