import random

# User guess
def guess(x):
  print(f"=====WELCOME TO Guess Number game!=====")
  
  # the random number will from 1 to arguments (depends on the argument pass down in the function parameter)
  random_number = random.randint(1, x)
  print(f"You will be guessing the number from 1 to {x}")

  # Enter the guess of the user here
  user_guess = int(input("Enter your guess here: "))

  # While the user guess number is not equals to random number, this loop will run continuously
  while user_guess != random_number:
    if user_guess < random_number:
      print("You guessed it wrong. Try to guess higher number.")
      user_guess = int(input("Enter your guess here: "))
    elif user_guess > random_number:
      print("You guessed it wrong. Try to guess lower number.")
      user_guess = int(input("Enter your guess here: "))

  print(f"You guessed it right, {user_guess}!")

# Call the guess function
# guess(100)

# Computer guess
def computer_guess(x):
  low = 1
  high = x
  feedback = ''
  while feedback.lower() != 'c':
    if low != high:
      guess = guess = random.randint(1, x)
    else:
      guess = low
    
    feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)")
    if feedback.lower() == 'h':
      high = guess - 1
    elif feedback.lower() == 'l':
      low = guess + 1
    
  print(f"Yes! The computer guessed your number, {guess}, correctly!")

computer_guess(100)