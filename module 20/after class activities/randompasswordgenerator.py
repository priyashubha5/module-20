import random
import string

def generate_password(length):
    # Define possible characters for password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    
    # Ensure password contains at least one of each character type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]
    
    # Fill the rest of the password length with random choices from all types
    all_characters = lowercase + uppercase + digits
    password += random.choices(all_characters, k=length - 3)
    
    # Shuffle to randomize the character order
    random.shuffle(password)
    
    # Join list into a single string to create the final password
    return ''.join(password)

# Specify the desired password length
password_length = int(input("Enter the desired password length: "))
print("Generated Password:", generate_password(password_length))
