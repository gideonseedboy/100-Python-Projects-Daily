
#  100 PYTHON PROJECTS — FROM BEGINNER TO ADVANCE WITH MySirGideon
# PROJECT 4 — DICE ROLLING SIMULATOR

import random
dice_roll = input("Role the dice? (yes/no): ")

while dice_roll == "yes":
    dice_outcome = random.randint(1, 6)
    print("You rolled: ", dice_outcome)
    dice_roll = input("Roll again? (yes/no): ")

print("Game ended.")