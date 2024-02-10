# Beginner project 1 - madlibs
# string concatenation, meaning how to put strings together from different variable

adjective = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")

# Here we are using the "f string"
madlib = f"Computer programming is so {adjective}! It makes me so excited all the time.\
  I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)