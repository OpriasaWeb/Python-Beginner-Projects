
def email_slicer():
  print("=== Welcome to email slicer ===")
  print(" ")

  email_input = input("Enter your email here: ")

  (username, domain) = email_input.split("@")
  (username, extension) = email_input.split(".")

  print(f"""Username: {username} 
          Domain: {domain}
          Extension: {extension}""")

email_slicer()