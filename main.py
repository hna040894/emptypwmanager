import json
import re
import random
import string

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
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
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

    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if is_strong_password(password):
            return password

# Initialize empty lists to store encrypted passwords, websites, and usernames
encrypted_passwords = []
websites = []
usernames = []

# Function to add a new password 
def add_password():
    """
    Add a new password to the password manager.

    This function should prompt the user for the website, username,  and password and store them to lists with same index. Optionally, it should check password strength with the function is_strong_password. It may also include an option for the user to
    generate a random strong password by calling the generate_password function.

    Returns:
        None
    """
    website = input("Enter website: ")
    username = input("Enter username: ")
    use_generated = input("Do you want to generate a strong password? (yes/no): ").lower()

    if use_generated == "yes":
        length = int(input("Enter password length: "))
        password = generate_password(length)
        print(f"Generated password: {password}")
    else:
        password = input("Enter password: ")
        if not is_strong_password(password):
            print("Warning: Password is weak!")

    encrypted_password = caesar_encrypt(password, 3)

    websites.append(website)
    usernames.append(username)
    encrypted_passwords.append(encrypted_password)

# Function to retrieve a password 
def get_password():
    """
    Retrieve a password for a given website.

    This function should prompt the user for the website name and
    then display the username and decrypted password for that website.

    Returns:
        None
    """
    website = input("Enter website to retrieve: ")

    if website in websites:
        index = websites.index(website)
        username = usernames[index]
        encrypted_password = encrypted_passwords[index]
        decrypted_password = caesar_decrypt(encrypted_password, 3)

        print(f"Username: {username}")
        print(f"Password: {decrypted_password}")
    else:
        print("Website not found.")

# Function to save passwords to a JSON file 
def save_passwords():
    """
    Save the password vault to a file.

    This function should save passwords, websites, and usernames to a text
    file named "vault.txt" in a structured format.

    Returns:
        None
    """
    data = []
    for i in range(len(websites)):
        entry = {
            "website": websites[i],
            "username": usernames[i],
            "password": encrypted_passwords[i]
        }
        data.append(entry)

    with open("vault.txt", "w") as file:
        json.dump(data, file)

# Function to load passwords from a JSON file 
def load_passwords():
    """
    Load passwords from a file into the password vault.

    This function should load passwords, websites, and usernames from a text
    file named "vault.txt" (or a more generic name) and populate the respective lists.

    Returns:
        None
    """
    global websites, usernames, encrypted_passwords

    try:
        with open("vault.txt", "r") as file:
            data = json.load(file)

            websites = [entry["website"] for entry in data]
            usernames = [entry["username"] for entry in data]
            encrypted_passwords = [entry["password"] for entry in data]
    except FileNotFoundError:
        print("No saved vault found. Starting fresh.")

# Main method
def main():
    # implement user interface 

    while True:
        print("\nPassword Manager Menu:")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Save Passwords")
        print("4. Load Passwords")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_password()
        elif choice == "2":
            get_password()
        elif choice == "3":
            save_passwords()
        elif choice == "4":
            load_passwords()
            print("Passwords loaded successfully!")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

# Execute the main function when the program is run
if __name__ == "__main__":
    main()
