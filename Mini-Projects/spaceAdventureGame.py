username = input("Enter your username: ")

print(f"Welcome to the Voyage of the Lost Star: Interactive Space Adventure, {username}!\n")
print(f"You are Captain {username}, commander of the starship Lost Star, stranded in an uncharted galaxy after a mysterious energy wave leaves your ship damaged. Fuel and time are running out—your choices will decide if you and your crew make it home.")

print("\nThe ship's scanners pick up two signals in the distance. One is a faint distress beacon; the other shows signs of a nearby asteroid belt with potential resources.")
choice = input("1. Follow the distress beacon.\n2. Head toward the asteroid belt.\nSelect your choice: ")

if choice == '1':
    print("\nYou arrive at an abandoned ship drifting silently in space. You detect two options:")
    choice = input("1. Board the ship to look for fuel.\n2. Download the ship’s logs remotely for navigation data.\nSelect your choice: ")
    
    if choice == '1':
        print("\nYou find a small cache of fuel cells, enough to get you home.\nEnding: Escape with Fuel – You manage to power up your ship and chart a course back to known space. Your mission is a success!")
    elif choice == '2':
        print("\nThe logs reveal an undiscovered star system with vital resources, but it’s far from home.\nEnding: New Discovery – You decide to explore this new star system, gaining valuable resources but remaining in uncharted territory.")
    else:
        print("\nInvalid input! Transmission Lost...\nThe Lost Star drifts on, a silent relic of the unknown, lost to the endless depths of space.")
        quit()

elif choice == '2':
    print("\nThe asteroid belt has potential resources but poses unknown dangers.")
    choice = input("1. Search for resources carefully.\n2. Abandon the belt and continue forward.\nSelect your choice: ")

    if choice == '1':
        print("\nWhile gathering resources, hostile alien drones attack, and your ship sustains damage. With limited power, you’re left drifting.\nEnding: Lost in Space – Your journey ends as your crew drifts endlessly in the dark.")
    elif choice == '2':
        print("\nFurther ahead, you spot a wormhole that may lead back to known space.")
        choice = input("1. Enter the wormhole for a risky shortcut.\n2. Stay on your current path, avoiding the unknown.\nSelect your choice: ")

        if choice == '1':
            print("\nThe wormhole pulls you through and transports you to a familiar sector.\nEnding: Home through the Wormhole – You safely return to known space, celebrated for your courage and discoveries.")
        elif choice == '2':
            print("\nAvoiding the wormhole, you continue forward but eventually run out of fuel, lost in space.\nEnding: Lost in Space – Without enough resources, your ship fades into the silent darkness of space.")
        else:
            print("\nInvalid input! Transmission Lost...\nThe Lost Star drifts on, a silent relic of the unknown, lost to the endless depths of space.")
            quit()

    else:
        print("\nInvalid input! Transmission Lost...\nThe Lost Star drifts on, a silent relic of the unknown, lost to the endless depths of space.")
        quit()

else:
    print("\nInvalid input! Transmission Lost...\nThe Lost Star drifts on, a silent relic of the unknown, lost to the endless depths of space.")
    quit()

print(f"\n\nThank you for playing, {username}!")