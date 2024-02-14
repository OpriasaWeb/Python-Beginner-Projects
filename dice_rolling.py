# Import random
# Manually drawing the dice 

import random

def roll_dice():

  print("=== Welcome to Dice Rolling ===")
  
  # Dictionary - can access through key value pairs loop
  dice_drawing = {
    1: (
      "---------------",
      "'      1      '",
      "'             '",
      "'      ○      '",
      "'             '",
      "'             '",
      "---------------"
    ),
    2: (
      "---------------",
      "'      2      '",
      "'    ○        '",
      "'             '",
      "'        ○    '",
      "'             '",
      "---------------"
    ),
    3: (
      "---------------",
      "'      3      '",
      "'    ○        '",
      "'      ○      '",
      "'        ○    '",
      "'             '",
      "---------------"
    ),
    4: (
      "---------------",
      "'             '",
      "'    ○   ○    '",
      "'      4      '",
      "'    ○   ○    '",
      "'             '",
      "---------------"
    ),
    5: (
      "---------------",
      "'      5      '",
      "'    ○   ○    '",
      "'      ○      '",
      "'    ○   ○    '",
      "'             '",
      "---------------"
    ),
    6: (
      "---------------",
      "'      6      '",
      "'    ○   ○    '",
      "'    ○   ○    '",
      "'    ○   ○    '",
      "'             '",
      "---------------"
    )
  }

  roll = input("Roll the dice? (Yes/No): ")

  while roll.lower() == "Yes".lower():
    roll_dice = random.randint(1, 6)

    print(f"The result is {roll_dice}")
    print("\n".join(dice_drawing[roll_dice]))

    roll = input("Roll the dice again? (Yes/No): ")
  
  print("Thank you, I hope you enjoy!")

roll_dice()