import secrets
import string
import json
import os

FILE = "credintials.json"

def main():
    credintials = load_credintials()

    email = input("Enter your email: ")
    preferences = user_preference()
    password = generate_password(preferences, email)
    rate_password(password)


#Check is file exists
def load_credintials():
    if os.path.exists(FILE):
        with open(FILE) as file:
            return json.load(file)
    return {}


#Getting users preferences to be added to the password
def user_preference():
    pref = {}
    print("\nInput characters to be added to your password.")
    while True:
        try:
            pref["length"] = int(input("Length: "))
            break
        except ValueError:
            print("Length should be a number")
    pref["numbers"] = input("Numbers[y/n]: ").lower().strip()
    pref["symbols"] = input("Symbols[y/n]: ").lower().strip()
    pref["letters"] = input("letters[y/n]: ").lower().strip()

    return pref


def generate_password(pref, email):
    #Creating a character pool
    pool = ""

    for key, value in pref.items():
        if key == "numbers" and value == "y":
            pool += string.digits
        elif key == "symbols" and value == "y":
            pool += string.punctuation
        elif key == "letters" and value == "y":
            pool += string.ascii_letters

    #Creating a password
    password = "".join(secrets.choice(pool) for i in range(pref["length"]))
    print(f"\nYour password is: {password}")
    save_credintials({"email": email, "password": password})

    return password


def rate_password(password):
    has_numbers = False
    has_letters = False
    has_symbols = False

    for char in password:
        if char in string.digits:
            has_numbers = True
        elif char in string.ascii_letters:
            has_letters = True
        elif char in string.punctuation:
            has_symbols = True

    if has_numbers and has_letters and has_symbols and len(password) > 7:
        print("You've a strong password.")
    elif has_numbers and has_letters and len(password) > 7:
        print("You've a moderate password.")
    else:
        print("You've a weak password.")


def save_credintials(credintials):
    if credintials is None:
        print("First enter your credintials")
        return
    with open("credintials.json", "w") as file:
        json.dump(credintials,file, indent=4)


if __name__=="__main__":
    main()
