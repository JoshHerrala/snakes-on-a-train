text = "Welcome to Snakes on a Train, a Python parable. \n\nPlease select the what you would like to do:"
options = "\nMath = M, Strings = S, Collections = C"
print(text, options)


user_input = input("Your selection: ")
print(user_input)

math = "M"

breakpoint()

if user_input == math :
  print("Its Math")
else:
  print("Its not Math")



