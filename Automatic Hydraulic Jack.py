# Automatic-Hydraulic-Jack
# Automatic Hydraulic Jack - Simple Python Program

height = 0

while True:
    print("\n--- Automatic Hydraulic Jack ---")
    print("1. Raise Jack")
    print("2. Lower Jack")
    print("3. Show Height")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if height < 100:
            height += 10
            print("Jack is raising...")
            print("Height:", height, "cm")
        else:
            print("Maximum height reached!")

    elif choice == "2":
        if height > 0:
            height -= 10
            print("Jack is lowering...")
            print("Height:", height, "cm")
        else:
            print("Jack is already at the bottom!")

    elif choice == "3":
        print("Current Jack Height:", height, "cm")

    elif choice == "4":
        print("Hydraulic Jack stopped.")
        break

    else:
        print("Invalid choice!")
