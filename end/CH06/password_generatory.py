"""
Password Generator

A secure password generator that has a minimum length of 8
"""

# Libraries utilized
import random
import string

#defive character pools
UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
DIGITS = string.digits
SPECIAL = r"!@#$%^&*()_-|\;<>" #fixed string

# Minimum password length
MIN_LENGTH = 8

# Help function
def get_yes_or_no(prompt: str) -> bool:
    """Ask the user for a yes or no question"""
    while True:
        answer = input(prompt).lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter 'y' or 'n'.")

def get_password_length() -> int:
    """Ask the user for a valid password length"""
    while True:
        try:
            length = int(input("Enter desired password length (minimum 8): "))
            if length >= MIN_LENGTH:
                return length
            print("Password must be at least 8 chartacters long.")
        except ValueError:
            print("Please enter a valid number.")

def get_criteria() -> dict:

    """Take length , uppercas, lowercase, digits, special input user"""
    length = get_password_length()

    criteria ={
        "length": length,
        "uppercase": get_yes_or_no("Include uppercase letters? (y/n): "),
        "lowercase": get_yes_or_no("Include lowercase letters? (y/n): "),
        "digits": get_yes_or_no("Include digits? (y/n): "),
        "special": get_yes_or_no("Include special characters? (y/n): ")
    }

    # validator
    if not any ([criteria["uppercase"],
                criteria["digits"], ["special"]]):
        print("You must select at least one character type")
        return get_criteria()
    
    return criteria

def build_pool(criteria: dict) -> tuple[str, list[str]]:
    """Build character pool"""
    pool = ""
    required = []
    if criteria["uppercase"]:
        pool += UPPERCASE
        required.append(random.choice(UPPERCASE))
    if criteria["lowercase"]:
        pool += LOWERCASE
        required.append(random.choice(LOWERCASE))

    if criteria["digits"]:
        pool += DIGITS
        required.append(random.choice(DIGITS))

    if criteria["special"]:
        pool += SPECIAL
        required.append(random.choice(SPECIAL))

    return pool, required
def generate_password(criteria: dict) -> str:
    """Generate password"""
    pool, required = build_pool(criteria)
    length = criteria["length"]

    remaining_count = length - len(required)
    remaining = [random.choice(pool) for _ in range(remaining_count)]

    password_chars = required + remaining
    random.shuffle(password_chars)

    return "".join(password_chars)

def main():
    while True:
        criteria = get_criteria()
        password = generate_password(criteria)

        print("This is your generated password:")
        print(password)

        if not get_yes_or_no("Generate another password? (y/n): "):
            print("Stay secure")
            break

if __name__ == "__main__":
    main()



