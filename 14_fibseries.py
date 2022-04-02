"""
To accept from user the number of Fibonacci numbers to be generated and print 
the Fibonacci series.
"""

# INPUT
terms = int(input("Enter the number of terms to be generated"))

# DECLARE VARIABLES 
a = 0
b = 1
sum = 0
count = 0

# GENERATE
if terms < 0:
    print("Enter +ve Number")
elif terms == 1:
    print("Fibonacci series upto 1 term is")
    print(a)
else:
    print("Fibonacci series upto",terms,"terms is:")
    while(count < terms):
        print(sum)
        count += 1
        a = b
        b = sum
        sum = a + b


