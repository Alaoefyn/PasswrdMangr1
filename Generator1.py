import random
import string

# Give a length to desired password.
while True:
    try:
        length = int(input("Enter password length (1-135): "))
        if length < 1 or length > 135:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 135.")

# You can choose yes or no by type y/n and decide rules of your password.
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
include_special = input("Include special characters? (y/n): ").lower() == 'y'
include_random_words = input("Include random words in password? (y/n): ").lower() == 'y'

if include_random_words:
    while True:
        try:
            random_word_chance = int(input("Enter the chance of including a random word (0-100): "))
            if random_word_chance < 0 or random_word_chance > 100:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 100.")

# Generating password
characters = ''
if include_uppercase:
    characters += string.ascii_uppercase
if include_lowercase:
    characters += string.ascii_lowercase
if include_numbers:
    characters += string.digits
if include_special:
    characters += string.punctuation

password = ''
for i in range(length):
    if include_random_words and random.randint(1, 100) <= random_word_chance:
        # Generate random word and add it to the password (Give percentage of random word occur)
        random_word = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(3, 10)))
        password += random_word
    else:
        password += random.choice(characters)

# Prints generated new password
print("Generated password:", password)
