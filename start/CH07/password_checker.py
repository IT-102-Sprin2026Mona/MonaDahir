"""
This is to check passwords and their strength base on length, complexity, and syntax.
"""

#Libraries utilized for this script
import re
import sys

#List of commonly used weak passwords
COMMON_PASSWORDS = [
    "password", "123456", "password123", "adim", "letmein", "qwerty", 
    "abc123", "welcome", "1234567890"
    
]


def check_password_strength(password):
    """
    Checks the password strength and returns feedback and score.

    +1 for length >= 8
    +1 for length >= 12
    +1 for uppercase and lowercase
    +1 for a digit
    +1 for one special character

    Deduction:
    -2 if password is in common password list
    """

    score = 0
    feedback = []

    # Check minimum length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Too short of a password. We need at least 8 characters.")

    # Check longer lenth
    if len(password) >= 12:
        score += 1
        feedback.append("Good length of 12+ characters.")
    else:
        feedback.append("Consider using 12+ characters for better security.")

    #Check uppercase and lowercase
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
        feedback.append("Contains both uppercase and lowercase letters")
    else:
        feedback.append("Please mix uppercase and lowercase letters")

    # Check uppercase and lowercase
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
        feedback.append("Contains both appercase and lowercase letters.")
    else:
        feedback.append("Please mix uppercase and lowercase letters")

    # Check for a digit
    if re.search('\d', password):
        score += 1
        feedback.append("Contains a digit or number.")
    else:
        feedback.append("Add at least one special chaaracter.")

    # Check common password list
    if password.lower() in  COMMON_PASSWORDS:
        score -= 2
        feedback.append("This is a common password.")

    # Determine password strength 
    score = max(score, 0)

    if score <= 1:
        strength = "Very weak"
    elif score == 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very strong"

    return score, strength, feedback

# Main function
def main():
    print("PASSWORD STREGTH CHECKER")

    # Accept password from command line
    if len(sys.argv) > 1:
        password = sys.argv[1]
    else:
        password = input("Enter your password to check: ")

    score, strength, feedback = check_password_strength(password)

    print(f"\nScore: {score}")
    print(f"Stength: {strength}")
    print("\nFeedback:")

    for line in feedback:
        print("f- {line}")

# Call main
if __name__ =="__main__":
    main()
