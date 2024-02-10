# add function
def add(a, b):
  answer = a + b
  print(f"{a} + {b} = {answer}")

# subtraction function
def subtraction(a, b):
  answer = a - b
  print(f"{a} - {b} = {answer}")

# multiplication function
def multiplication(a, b):
  answer = a * b
  print(f"{a} * {b} = {answer}")

# division function
def division(a, b):
  answer = a / b
  print(f"{a} / {b} = {answer}")

print("A. Addition\
       B. Subtraction\
       C. Multiplication\
       D. Division\
       E. Exit")

print("===WELCOME TO Basic Calculator===")
user_choice = input("Enter your choice: ").lower()

# flag variable
is_exist = False

# List of valid entries, otherwise invalid
valid_entry = ["a", "b", "c", "d", "e"]

# Here, the while will be forever true unless the user choice enters the valid entry
while True:
  if user_choice in valid_entry:
    # If user choice exists in the valid entry list, update the is_exist variable to True and break the loop
    is_exist = True
    break
  else:
    print("Enter valid input. Please try again.")

  # Until the user choice is not entering the valid entry, this loop will run forever
  user_choice = input("Enter your choice: ").lower()

# Now if is_exist is not equals to False, meaning True
if is_exist != False:
  # Run the while loop as long as the user_choice is not equals to "e" and "E"
  while user_choice != "E" and user_choice != "e":
    if user_choice == "a" or user_choice == "A":
      print("===Addition===")
      a = int(input("Enter first number: "))
      b = int(input("Enter second number: "))
      add(a, b)
    elif user_choice == "b" or user_choice == "B":
      print("===Subtraction===")
      a = int(input("Enter first number: "))
      b = int(input("Enter second number: "))
      subtraction(a, b)
    elif user_choice == "c" or user_choice == "C":
      print("===Multiplication===")
      a = int(input("Enter first number: "))
      b = int(input("Enter second number: "))
      multiplication(a, b)
    elif user_choice == "d" or user_choice == "D":
      print("===Division===")
      a = int(input("Enter first number: "))
      b = int(input("Enter second number: "))
      division(a, b)
      
    user_choice = input("Enter your choice: ")

  print("Exiting the program...")




    

