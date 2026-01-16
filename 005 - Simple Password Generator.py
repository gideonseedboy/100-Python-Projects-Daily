
#  100 PYTHON PROJECTS — FROM BEGINNER TO ADVANCE WITH MySirGideon
# PROJECT 5 — SIMPLE PASSWORD GENERATOR

import random
import string
pword_length = int(input("How many characters should you password have (12 - 24)?: "))
generate_string = string.ascii_letters + string.digits
pw_characters = ""

while len(pw_characters)< pword_length:
    pw_characters += random.choice(generate_string)

print("Generated password: ", pw_characters)