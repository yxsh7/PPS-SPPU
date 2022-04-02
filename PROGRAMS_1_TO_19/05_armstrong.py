"""
To check whether input number is Armstrong number or not. An Armstrong number is an 
integer with three digits such that the sum of the cubes of its digits is equal to the number 
itself. Ex. 371
"""

# INPUT
number = int(input("Enter the number"))

#
sum = 0
temp = number

# CALCULATE

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp//=10

# CHECK

if number == sum:
    print(number,"is an Armstrong number")
else:
    print(number,"is not an Armstrong Number")

# GITHUB: yxsh7