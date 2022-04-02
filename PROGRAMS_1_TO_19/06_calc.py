"""
To  simulate  simple  calculator  that  performs  basic  tasks  such  as  addition,  subtraction, 
multiplication and division with special operations like computing xy and x!
"""

import math

# INPUT
operation = (input("WELCOME! \nEnter the Operation you want to perform \n Addition: + \
             \n Subtraction: - \n Divsion: / \n Multiplication: * \n Power: p \n Factorial: ! \n"))

if operation == '+' or operation == '-' or operation == '*' or operation == '/' or operation == '*' or operation == 'p':
    num1 = float(input("Enter First Number"))
    num2 = float(input("Enter Second Number"))
elif operation == '!':
    num1 = int(input("Enter Number"))
else:
    print("Invalid Input")

# CALCULATE
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
elif operation == 'p':
    result = num1 ** num2
elif operation == '!':
    if num1 < 0:
        print("Factorial does not exist for negative numbers")
        quit()
    elif num1 == 0:
        print("The factorial of 0 is 1")
        quit()
    else:
        result = 1
        for i in range(1, num1 +1):
            result = result * i
  # built-in function method below
  # result = math.factorial(num1)
else:
    print("Invalid Input")

#DISPLAY
print("Your Answer is", result)

# GITHUB: yxsh7