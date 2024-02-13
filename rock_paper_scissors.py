import random

def is_win(player, opponent):
  if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
    return True

user_score = 0
computer_score = 0
def play():
  global user_score
  global computer_score

  valid_entry = ['r', 'p', 's']

  # User choice
  user = input(f"'r' for rocks, 'p' for paper, 's' for scissors ")

  # flag variable
  is_exist = False

  while True:
    if user in valid_entry:
      # If user choice exists in the valid entry list, update the is_exist variable to True and break the loop
      is_exist = True
      break
    else:
      break

  # Computer choice6
  if is_exist != False:
    computer = random.choice(valid_entry)
    if user == computer:
      return "It's a tie"

    if is_win(user, computer):
      user_score = user_score + 1
      return 'You won!'
    
    computer_score = computer_score + 1
    return 'You lost!'
  else:
    print("Enter valid input. Please try again.")
  

# r > s, s > p, p > r
def round(round):
  round_count = 0
  while round_count < round:
    round_count = round_count + 1
    print(play())

round(10)

if user_score > computer_score:
  print("You won against computer!")
elif user_score < computer_score:
  print("You lose to a computer.")
else:
  print("It's a tie overall.")

print(f"Your score: {user_score}")
print(f"Computer opponent score: {computer_score}")
