#  100 Python Projects — From Beginner to Advanced with MySirGideon
#  PROJECT 3 — NUMBER GUESSING GAME  

import random
random_number = random.randint(1, 10)
guessed_number = int(input("Guess a numer btween 1 and 10: "))

while guessed_number != random_number:
    print("Try again!")
    guessed_number = int(input("Guess a number between 1 and 10"))

print("Congratulations! You guessed it!")