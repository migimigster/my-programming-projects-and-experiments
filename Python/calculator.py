#Calculator
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  num1 = float(input("Input number?: "))
  for symbol in operations:
    print(symbol)
  calculator_done = False
  while not calculator_done:

    #Here we select symbols
    operation_symbol = input("Pick an operation: ") 
    num2 = float(input("Input other number?: "))
    calculation_function = operations[operation_symbol]
    answer = float(calculation_function(num1, num2))

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    continue_calc=input("Do you want to continue calculating? y if yes. c if you want to restart or n if you want to stop? ")
    if continue_calc=='y':
          num1=answer
    elif continue_calc=='c':
      calculator_done = True
      calculator()
    elif continue_calc=='n':
      return
 

print("Welcome to migimigster's basic calculator! ")
zzz=input("Press any letter or number to start! ")
if zzz:
  calculator()