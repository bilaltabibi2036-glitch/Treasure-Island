
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
# Stage 1: Crossroads
choice1 = input('\nYou\'re at a crossroads. Where do you want to go? Type "left" or "right".\n').lower()

if choice1 == "left":
    # Stage 2: Lake
    choice2 = input('\nYou\'ve come to a lake. There is an island in the middle. Type "wait" to wait for a boat, or "swim" to swim across.\n').lower()

    if choice2 == "wait":
        # Stage 3: Castle doors
        choice3 = input('\nYou arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose?\n').lower()

        if choice3 == "red":
            print("\nIt's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("\nYou found the treasure! You Win! 🎉")
        elif choice3 == "blue":
            print("\nYou enter a room of beasts. Game Over.")
        else:
            print("\nThat door doesn't exist. Game Over.")

    else:
        print("\nAttacked by an electric eel! Game Over.")

else:
    print("\nYou fell into a hole. Game Over.")
          
