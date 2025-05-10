import re
import random
import string

password_requirements = [
        r"[A-Z]",
        r"[a-z]",
        r"[0-9]",
        f"[{re.escape(string.punctuation)}]"
]

# Caesar cipher encryption and decryption functions (pre-implemented)
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Password strength checker function (optional)
def is_strong_password(password):
    if len(password) < 8:
        return False

    for pattern in password_requirements:
       if not re.search(pattern, password):
           return False

    return True

# Password generator function (optional)
def generate_password(length):
    """
    Generate a random strong password of the specified length.

    Args:
        length (int): The desired length of the password.

    Returns:
        str: A random strong password.
    """
    if length < 8:
        length = 8  # Enforce minimum strength

    # Generate at least one of the mandatory characters
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    punct = random.choice(string.punctuation)

    # Fill the rest and shuffle
    characters = string.ascii_letters + string.digits + string.punctuation
    remaining = random.choices(characters, k=length - 4)
    password = list(lower + upper + digit + punct + ''.join(remaining))

    random.shuffle(password)

    return ''.join(password)