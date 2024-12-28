import os
import random

pool = list(range(1,101))
#List of possible numbers

def intro():
    hit = random.choice(pool)
    #computer chooses the number randomly from the ranged list above
    return hit
    
print("\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100\n")

difficulty_chances = {0:99,1:10, 2:5, 3:3, 4:1}
choice = int(input("Please select the difficulty level:\n\n0. Baby (99 chances)\n\n1. Easy (10 Chances)\n\n2. Medium (5 Chances)\n\n3. Hard (3 Chances)\n\n4. Impossible (1 Chance)\n\n Enter your choice: "))

chances = difficulty_chances.get(choice,1)

print(f"Great! You have {chances} chances!\nLet's start the game!")


hit = intro()

while chances > 0:
    #The amount of guesses is higer than 0, indicates beginning of game
    guess = int(input("Enter your guess: "))
    chances -= 1
    #After your first guess it subtracts 1 from the amount of guesses you have

    if guess < hit:
        #if the number you guessed is lower than the number the computer chose
        print(f"Incorrect! The number is HIGHER... You have {chances} chances left")
        #it is incorrect, so a hint is given, and it lists the amount of chances you have left
    elif guess > hit:
        print(f"Incorrect! The number is LOWER...You have {chances} chances left")
                #it is incorrect, so a hint is given, and it lists the amount of chances you have left
    else:
        print(f"Congratulations! You guessed the correct number with {chances} attempts remaining")
        #It is the correct answer, so there is no need to to lower you chances, as the game is ended.
        break
    #game ended

if guess != hit:
    print(f"Game Over! The correct number was {hit}")
    #You lost all your chances, you have lost the game. The number the computer chose is shown.