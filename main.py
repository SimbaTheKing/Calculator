#calculator
# Add
from art import logo
def add(n1, n2):
  return n1 + n2
#subtract
def subract(n1, n2):
  return n1 - n2
#multiply
def multiply(n1, n2):
  return n1 * n2
#Divide
def divide(n1, n2):
  return n1/n2

operations = {
  "+": add,
  "-": subract,
  "/": divide,
  "*": multiply,
  
}
def calculator():
  print(logo)
  num1 = float(input("what the first number?: "))
  
  
  for symbol in operations:
    print(symbol)
  should_continue = True
  while should_continue:
    operations_symbol = input("Pick an operation: ")
    num2 = float(input("what the next number?: "))
    calculation_function = operations[operations_symbol]
    answer = calculation_function (num1, num2)
        
    
    print(f"{num1} {operations_sysmbol} {num2} = {answer}" )
    continue_calculations =input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    if continue_calculations == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()
    
calculator()