import random
import string

def generate_password(length):
    if length < 6:
        return "Password length should be at least 6 characters."

    # Combination of characters: letters (uppercase and lowercase), digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    print("Password Generator")
    
    while True:
        try:
            length = int(input("Enter the desired password length (or 0 to exit): "))
            if length == 0:
                print("Exiting password generator.")
                break
            print(f"Generated password: {generate_password(length)}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
