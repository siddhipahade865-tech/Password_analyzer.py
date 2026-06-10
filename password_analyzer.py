import re
import datetime


# Function to calculate password strength
def calculate_strength(password):
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check for numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2
    else:
        feedback.append("Add at least one special character.")

    # Check against common passwords
    common_passwords = [
        "password", "123456", "12345678",
        "password123", "admin", "qwerty",
        "welcome", "abc123"
    ]

    if password.lower() in common_passwords:
        score = 0
        feedback.append("This is a commonly used password and is highly insecure!")

    return score, feedback


# Function to return both file-friendly and display-friendly labels
def strength_label(score):
    if score <= 2:
        return "Very Weak", "🔴 Very Weak"
    elif score <= 4:
        return "Weak", "🟠 Weak"
    elif score <= 6:
        return "Moderate", "🟡 Moderate"
    else:
        return "Strong", "🟢 Strong"


# Save analysis history to a file
def save_history(password, result):
    with open("password_history.txt", "a", encoding="utf-8") as file:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        hidden_password = "*" * len(password)  # Hide actual password
        file.write(f"{current_time} | {hidden_password} | {result}\n")


# Main function
def main():
    print("=" * 55)
    print("         🔐 PASSWORD STRENGTH ANALYZER")
    print("           Cyber Security Mini Project")
    print("=" * 55)

    while True:
        password = input("\nEnter a password to analyze: ")

        score, feedback = calculate_strength(password)

        # Get labels
        save_result, display_result = strength_label(score)

        # Display results
        print("\n----------- Analysis Report -----------")
        print(f"Password Length : {len(password)}")
        print(f"Security Rating : {display_result}")
        print(f"Score           : {score}/8")

        if feedback:
            print("\nSuggestions to Improve:")
            for item in feedback:
                print(f"• {item}")
        else:
            print("\n✅ Excellent! Your password follows good security practices.")

        # Save to history file
        save_history(password, save_result)

        # Ask user if they want to continue
        choice = input("\nDo you want to test another password? (y/n): ").strip().lower()

        if choice != "y":
            print("\nThank you for using Password Strength Analyzer!")
            print("Your analysis history has been saved in 'password_history.txt'.")
            break


# Run the program
if __name__ == "__main__":
    main()