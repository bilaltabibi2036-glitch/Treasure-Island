print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o.__;__o.--"_o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o\o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
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
          
