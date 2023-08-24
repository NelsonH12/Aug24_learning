# define the functions
def add(a, b):
  answer = a + b
  print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def subtract(a, b):
  answer = a - b
  print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def multiply(a, b):
  answer = a * b
  print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def divide(a, b):
  answer = a / b
  print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

#printing user options
while True:
  print("A.  Addition")
  print("B.  Subrtraction")
  print("C.  Multiplication")
  print("D.  Division")
  print("E.  Exit")
  
  Choice = input("input letter of your choice:  ")
  
  if Choice == "a" or Choice == "A":
    print("Addition")
    a = int(input("Enter first number:  "))
    b = int(input("Enter second number:  "))  #remember to convert to int
    add(a, b)  #REMEMBER TO CALL THE FUNCTION
  
  elif Choice == "b" or Choice == "B":
    print("Subtraction")
    a = int(input("Enter first number:  "))
    b = int(input("Enter second number:  "))
    subtract(a, b)
  
  elif Choice == "c" or Choice == "C":
    print("Multiplication")
    a = int(input("Enter first number:  "))
    b = int(input("Enter second number:  "))
    multiply(a, b)
    
  elif Choice == "d" or Choice == "D":
    print("Multiplication")
    a = int(input("Enter first number:  "))
    b = int(input("Enter second number:  "))
    divide(a, b)
  
  elif Choice == "e" or Choice == "E":
    print("Goodbye")
    quit()