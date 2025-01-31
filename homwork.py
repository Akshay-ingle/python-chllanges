import random
import string

def generate_password(length=12):
    if length < 4:  # Ensuring the minimum length for a strong password
        raise ValueError("Password length should be at least 4 characters.")

    # Define character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits

    # Ensure at least one character from each category
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]

    # Fill the remaining length with random choices from all pools
    all_chars = lower + upper + digits
    password += random.choices(all_chars, k=length - len(password))

    # Shuffle the password to remove predictable patterns
    random.shuffle(password)

    return "".join(password)

# Example usage
print("Generated Password:", generate_password(12))
