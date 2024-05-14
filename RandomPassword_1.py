import random as r
import string as s

def generate_password(length, include_characters=True, include_digits=True):
    characters = ''
    if include_characters:
        characters += s.ascii_letters
    if include_digits:
        characters += s.digits

    if not characters:
        print("Error: You must include at least characters or digits.")
        return None

    password = ''.join(r.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    include_characters = input("Include characters? (yes/no): ").lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").lower() == 'yes'

    password = generate_password(length, include_characters, include_digits)
    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()