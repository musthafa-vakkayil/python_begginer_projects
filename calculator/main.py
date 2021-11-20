#impporting modules
from replit import clear
from art import logo

# addition
def add(n1, n2):
  return n1 + n2
# substraction
def subtract(n1, n2):
  return n1 - n2

# multiplication
def multiply(n1, n2):
  return n1 * n2

# division
def divide(n1, n2):
  if n2 ==0:
      return f"not possible" 
  return n1 / n2

# modulo
def modulo(n1,n2):
    return n1%n2

# power
def power(n1,n2):
    return n1**n2

# different operations
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "%": modulo,
  "**":power,
}

# calculator function
def calculator():
  print(logo)
  # taking first input
  num1 = float(input("What's the first number?: "))

  #printing operations
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    # asking the user wants to continue or not
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()
