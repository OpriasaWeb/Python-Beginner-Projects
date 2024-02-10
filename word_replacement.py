def replace_word():
  str = "Hello, good good good good morning everyone!"
  print(str)
  word_to_replace = input("Enter the word you wish to replace: ")
  word_replacement = input("Enter the word replacement: ")

  # ---------- Built-in function ----------
  # print(str.replace(word_to_replace, word_replacement))
  # ---------- Built-in function ----------

  # ---------- Manual coding ----------
  split_str = str.split()
  result = ''
  for split in split_str:
    if split == word_to_replace:
      # change string
      result += word_replacement + " "
    else:
      result += split + " "
  print(result)
  # ---------- Manual coding ----------
    


# call the function
replace_word()
