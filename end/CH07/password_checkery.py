"""
This is to check password and their strength based on length on length, complexity, and syntax
"""

#Libraries utilized for this scripr are
import re
import sys

#List of commonly used passwords
COMMON_PASSWORDS = [
    "password", "23456", "password123", "admin", "letmein", 
    "qwerty", "abc123", "welcome", "1234567890"
]

def check_password_strength(password):
    """
    Checks password strength and returns feedback and score
    +1 length >= 8
    +2 length >= 12
    +1 uppercase + lowercase
    +1 digit
    +1 special character
    -2 if common password
    """
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
        feedback.append("Good length (8+ characters)")
    else:
        feedback.append("Password is too short (minimum 8 characters)")

    if len(password) >= 12:
        score += 1
        feedback.append("Good length (12+ characters)")
    else:
        feedback.append("Consider using 12+ characters for better security")

    # Check for uppercase and lowercase
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
        feedback.append("Good mix of uppercase and lowercase letters")   
    else:
        feedback.append("Use a mix of uppercase and lowercase letters")

    # Check for digits
    if re.search(r"\d", password):
        score += 1
        feedback.append("Good use of digits")
    else:
        feedback.appenc("Add at least one number")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
        feedback.append("Contains special characters")
    else:
        feedback.append("Add at least one special character")

    # Check weak password list
    if password.lower() in COMMON_PASSWORDS:
        score -= 2
        feedback.append("This is a very common weak password")

    # Determine strength
    score = max(score, 0)

    if score <= 1:
        strength = "Very weak"
    elif score == 2:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very strong"

    return score, strength, feedback
def main():
    print("PASSWORD STRENGTH CHECKER")

    # Accapt password from command line or input
    if len(sys.argv) > 1:
        password = sys.argv[1]
    else:
        password = input("Enter a password to check: ")

    score, strength, feedback = check_password_strength(password)

    print("\nRESULT:")
    print("Srength:", strength)
    print("Score:", score)
    print("\nFeedback:")

    print(f" Score: {score}")
    print(f" Strength: {strength}")
    print("\n Feedback:")
    for line in feedback:
        print("-", line)
      
if __name__ == "__main__":
    main()