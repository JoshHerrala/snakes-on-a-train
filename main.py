from strings import *


def main():
  text = "Welcome to Snakes on a Train, a Python parable. \n\nPlease select the what you would like to do:"
  options = "\nMath = M, Strings = S, Collections = C"
  print(text, options)
  user_input = input("Your selection: ")
  print(user_input)
  #breakpoint()
  
  if user_input == "M" :
    print("TODO make math module")
  elif user_input == "S":
    string_machine()
  elif user_input == "C":
    print("TODO make collection module")
  else:
    print("No idea what you're prattling on about mate")


if __name__ == '__main__':
  main()
  print("Function has been called as main")
else:
  print("Called from another function")
    #functionA()
    #functionB()
