from art import logo
from os import system


# Calculator operations
# Add
def add(n1, n2):
  return n1 + n2
# Substract
def subtract(n1, n2):
  return n1 - n2
# Multiply
def multiply(n1, n2):
  return n1 * n2
# Divide
def divide(n1, n2):
  return n1 / n2
#
operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

# Calculator Function
def calculator():
  print(logo)
  num1 = float(input("What is the first number? "))
  
  for symbol in operations:
    print(symbol)
  
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Choose an operation: ")
    num2 = float(input("What is the next number? "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    user_input = input("Type 'y' to continue calculating or 'n' to start new calculation: ")
    if user_input == "y":
      num1 = answer
    else:
      should_continue = False
      system('cls')
      calculator()
  
calculator()