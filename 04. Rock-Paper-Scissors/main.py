'''PYCODE'''

# ? 04. Rock-Paper-Scissors Game
# ? Features: Play against the computer with random choices.

# * Source Code
import random

rock, paper, scissors = 1, 2, 3

while True:
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    user = input("Enter your Choice: ")
    computer = random.choice([1, 2, 3])
    print(f"{user} -- {computer}")
    
    try:
        if int(user) == 1:
            if computer == 1:
                print("Draw")
            elif computer == 2:
                print("You Lost!")
            else:
                print("You Won!")
                
        elif int(user) == 2:
            if computer == 1:
                print("You Won!")
            elif computer == 2:
                print("Draw")
            else:
                print("You Lost!")
                
        elif int(user) == 3:
            if computer == 1:
                print("You Lost!")
            elif computer == 2:
                print("You Won!")
            else:
                print("Draw")
                
        else:
            print("Invalid Choice")
            
    except ValueError:
        user = 0
