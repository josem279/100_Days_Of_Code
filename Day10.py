# More work with functions -> functions with outputs

logo = '''
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def mult(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": mult,
    "/": div
}

print(logo)
num1 = float(input("What is the first number?\n"))

for symbol in operations:
    print(symbol, "\n")

operation_symbol = input("Pick an operation:\n")
num2 = float(input("What is the next number?\n"))

caculating = True

def calculate(num1, operator, num2):
    res = operations[operator](num1, num2)
    return res
    
calculation = calculate(num1, operation_symbol, num2)

keep_calculating = input(f"Type 'y' to continue calulating with {calculation} or type 'n' to start a new calculation:\n")

while keep_calculating == "y":
    print(f"The current number is {calculation}")
    operation = input("Pick an operation:\n")
    next_num = float(input("What is the next number?\n"))
    calculation = calculate(calculation, operation, next_num)
    keep_calculating = input(f"Type 'y' to continue calulating with {calculation} or type 'n' to start a new calculation:\n")

print(f"The final result is {calculation}")