import string
import random

# Make a combined list of string, containing ascii letters, digits and random text
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

print("=== Welcome to password generator ===")

def generate_password():
  password_length = int(input("How long would you like your password? "))

  # shuffle the combined characters
  random.shuffle(characters)

  # Set a variable password here to store the random password
  password = []

  # Loop through the user entered password length
  for i in range(password_length):
    # Each iteration will append the random choice character to password variable
    password.append(random.choice(characters))

  # After loop, shuffle the appended password
  random.shuffle(password)

  # And lastly, join it without space
  password = "".join(password)

  print(password)

option = input("Do you want to generate a password? (Y/N): ")

if option != "Y":
  print("Thank you for visiting this app.")
  quit()
else:
  generate_password()