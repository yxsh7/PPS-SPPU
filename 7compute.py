"""
To  accept  the  number  and  Compute  a)    square  root  of  number,  b)  Square  of  number,  c) 
Cube of number d) check for prime, d) factorial of number e) prime factors
"""
import math

#INPUT
operation = (input("WELCOME! \n Square root of number: a \n Square of number: b \n Cube of number: c \
    \n Check for prime: d \n Factorial of number: e \n Prime factors: f \n "))
number = float(input("Enter Number"))

# SQUARE ROOT OF NUMBER
if operation == 'a':
    result = number ** 0.5
# SQUARE OF NUMBER
elif operation == 'b':
    result = number * number
# CUBE OF NUMBER
elif operation == 'c':
    result = number * number * number
# CHECK FOR PRIME
elif operation == 'd':
    i=2
    number=int(number)
    if number > 1:
        for i in range(i,number):
            if (number % i == 0):
                print(number, "is not a Prime Number")
                quit()
        else:
            print(number,"is a Prime number")
            quit()
    # If the number is less than 1 it can't be Prime    
    else:
        print(number,"is not a Prime number")
        quit()
# FACTORIAL OF NUMBER
elif operation == 'e':
    if number < 0:
        print("Factorial does not exist for negative numbers")
        quit()
    elif number == 0:
        print("The factorial of 0 is 1")
        quit()
    else:
        result = 1
        number = int(number)
        for i in range(1, number +1):
            result = result * i
# PRIME FACTORS
elif operation == 'f':
    while number % 2 == 0:
      print (2),
      number = number / 2
    
   #number became odd
    for i in range(3,int(math.sqrt(number))+1,2):
     
      while (number % i == 0):
         print (i)
         number = number / i
    
    if number > 2:
      print (number)
    quit()
else:
    print("Invalid Input")

# DISPLAY 

print("Your Answer is", result)

     

