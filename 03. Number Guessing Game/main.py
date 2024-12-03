'''PYCODE'''

# ? 3. Number Guessing Game
# ? Features: Random number generation, hints for guesses.

# * Source Code
import random

wins = 0
while True:
    computer = random.randint(0, 100)
    
    print(f"Hint: The number starts with {str(computer)[0]}")
    
    try:
        user = int(input("Guess the Number: "))
    except ValueError:
        user = 0
    
    if computer == user:
        print("Cigar!! You Won")
        wins += 1
        
    elif abs(computer - user) < 3:
        print("Close but not the Cigar")
        
    else:
        print("Very Far")
        
    print(f"Wins: {wins}")

    
