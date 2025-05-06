import json

from ciphers import *

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