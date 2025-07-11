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

print(logo)

first_num = int(input("What is the first number?\n"))
print("+\n-\n*\n/")
operation = input("Pick an operation:\n")
next_num = int(input("What is the next number?\n"))
caculating = True

def calculate(num1, operator, num2):
    if operator == "+":
        res = num1 + num2
        return res
    elif operator == "-":
        res = num1 - num2
        return res
    elif operator == "*":
        res = num1 * num2
        return res
    else:
        res = num1 / num2
        return res
    
calculation = calculate(first_num, operation, next_num)

keep_calculating = input(f"Type 'y' to continue calulating with {calculation} or type 'n' to start a new calculation:\n")

while keep_calculating == "y":
    print(f"The current number is {calculation}")
    operation = input("Pick an operation:\n")
    next_num = int(input("What is the next number?\n"))
    calculation = calculate(calculation, operation, next_num)
    keep_calculating = input(f"Type 'y' to continue calulating with {calculation} or type 'n' to start a new calculation:\n")

print(f"The final result is {calculation}")