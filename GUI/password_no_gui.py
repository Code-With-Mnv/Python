import re

def validate_password(password):
    # Regex pattern
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$'

    # Check match
    if re.match(pattern, password):
        return True
    else:
        return False

# --- Main Program ---
password = input("Enter your password: ")

if validate_password(password):
    print("✅ Password is valid!")
else:
    print("❌ Invalid Password.")
    print("Password must be at least 8 characters long and contain:")
    print("- At least one uppercase letter")
    print("- At least one lowercase letter")
    print("- At least one digit")
    print("- At least one special character")
