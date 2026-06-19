"""
Password Generator
Create a secure passowrd with user-defined options
Minimum length is 8
"""

import random
import string

#Characeter pools
UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
DIGITS = string.digits

#FIXED SPECIAL CHARACTERS (safe version)
SPECIAL = "!@#$%^&*()_-|;<>"

MIN_LENGTH = 8


def get_yes_or_no(prompt: str) -> bool:
    while True:
        answer = input(prompt).strip().lower()

        if answer in ("y", "yes"):
            return True
        
        if answer in ("n", "no"):
            return False
        
        print("Please enter yes or no (y/n).")


def get_password_length() -> int:
    while True:
        try:
            length = int(input("How long do you want the password?"))

            if length >= MIN_LENGTH:
                return length
            
            print("Password must be at least 8 characters.")

        except ValueError:
            ("Please enter a valid whole number.")
        

def get_criteria() -> dict:

    length = get_password_length()

    critia = {
        "length": length,
        "uppercase": get_yes_or_no("Include uppercase letters? (y/n): "),
        "lowecase": get_yes_or_no("Include lowercase letters? (y/n): "),
        "digits": get_yes_or_no("Include numbers? (y/n): "),
        "special": get_yes_or_no("Include special charcters? (y/n?): ")

    }

    if not any(critia.values()):
        print("You must select at least one character typ. ")

    return critia
    

def build_pool(criteria: dict) -> tuple[str, list[str]]:

    pool = ""
    requird = []

    if criteria["uppercase"]:
        pool += UPPERCASE
        requird.append(random.choice(UPPERCASE))

    if criteria["lowercase"]:
        pool += LOWERCASE
        requird.append(random.choice(LOWERCASE))

    if criteria["digits"]:
        pool += DIGITS
        requird.append(random.choice(DIGITS))
    
    if criteria["special"]:
        pool += SPECIAL
        requird.append(random.choice(SPECIAL))

    return pool, requird

def generate_password(criteria: dict) -> str:
    
    length = criteria["length"]

    remaining_count = length - len(required)

    remaining = [random.choice(pool) for  _ in range(remaining_count)]

    password_chars = required + remaining
    random.shuffle(password_chars)


def main():

    while True:

        criteria = get_criteria()
        password = get_password(criteria)
        print("\nGenerated password:")
        print(password)

        if not get_yes_or_no("\nGenerate another password? (y/n): "):
            print("Stay secure.")
            break

if __name__ == "__main__":
    main()
    