import re

def load_common_passwords(filepath="common_passwords.txt"):
    with open(filepath, "r") as file:
        return set(line.strip() for line in file)

def check_password_strength(password, common_passwords):
    score = 0
    suggestions = []

    # This will check the length of the password
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 12 characters.")

    # Character variety
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")
    
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")
    
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add digits.")
    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add special characters.")

    # This will check if it's a known common or weak password
    if password.lower() in common_passwords:
        suggestions.append("Avoid common passwords.")
    else:
        score += 1

    return score, suggestions

def get_strength_level(score):
    if score <= 3:
        return "Weak"
    elif score <= 5:
        return "Moderate"
    else:
        return "Strong"

if __name__ == "__main__":
    common_passwords = load_common_passwords()

    password = input("Enter your password to analyze: ")
    score, suggestions = check_password_strength(password, common_passwords)

    print(f"\nPassword Score: {score}/8")
    print(f"Strength Level: {get_strength_level(score)}")

    if suggestions:
        print("\nSuggestions to improve your password:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
