
def main():
  text = "Welcome to Snakes on a Train, a Python parable. \n\nPlease select the what you would like to do:"
  options = "\nMath = M, Strings = S, Collections = C"
  print(text, options)
  user_input = input("Your selection: ")
  print(user_input)
  #breakpoint()
  if user_input == "M" :
    print("Its Math")
  else:
    print("Its not Math")


if __name__ == '__main__':
  main()
  print("Function has been called as main")
else:
  print("Called from another function")
    #functionA()
    #functionB()
