from strings import *


#TODO test framework

def main():
  text = "Welcome to Snakes on a Train, a Python parable. \n\nPlease select the what you would like to do:"
  options = "\nMath = M, Strings = S, Classes = C"
  print(text, options)
  user_input = input("Your selection: ")
  #breakpoint()
  
  if user_input == "M" :
    print("TODO make math module")
  elif user_input == "S":
    string_machine()
  elif user_input == "C":
    print("TODO make Class/Inheritance module")
  else:
    print("No idea what you're prattling on about mate")


if __name__ == '__main__':
  main()
  print("Function has been called as main")
else:
  print("Called from another function")
    #functionA()
    #functionB()
