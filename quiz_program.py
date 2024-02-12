# A dictionary that contain questions and answers
# Have a variable that tracks the player's score
# Loop through dictionary using key value pairs
# Display each question to user and allow them to answer it
# Tell them if they are right or wrong
# Display the result

quiz = {
  "question1": {
    "question": "Who has the ability of 'Room' in One Piece anime?",
    "answer": "Law"
  },
  "question2": {
    "question": "Who has the ability of 'Gear-5' in One Piece anime?",
    "answer": "Luffy"
  },
  "question3": {
    "question": "Who has the ability of 'Divine Departure' in One Piece anime?",
    "answer": "Roger"
  },
  "question4": {
    "question": "Who has the ability of 'Killer of the Observation Haki' in One Piece anime?",
    "answer": "Shanks"
  },
  "question5": {
    "question": "Who has the ability that can destroy the world in One Piece anime?",
    "answer": "Whitebeard"
  }
}

score = 0
many_questions = len(quiz)

for key, value in quiz.items():
  # many_questions = many_questions + 1
  print(value['question'])
  answer = str(input("What is the answer? "))

  if answer.lower() != value['answer'].lower():
    print("Oops. Wrong!")
    print(f"The answer is {value['answer']}")
  else:
    score = score + 1
    print("You are correct!")
    print(f"Your score is: {score}")

print(f"Your total score is: {score}")

if score < many_questions // 2:
  print("You failed.")
else:
  print("You passed. Congratulations!")