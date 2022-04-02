"""
To accept N numbers from user. Compute and display maximum in list, minimum in list, 
sum and average of numbers.
"""

from decimal import Decimal

# INPUT
input_string =input("Enter all numbers seperated by a Space")

# CONVERT STRING TO LIST
num_list = input_string.split(" ")

# CALCULATE
maximum = max(num_list)
minimum = min(num_list)
# CANT ADD  INTEGERS AS STRINGS.......USE DECIMAL TO ADD INTEGERS AS STRINGS
total = sum(Decimal(i) for i in num_list)
length = len(num_list)
average = total/length

#PRINT
print("Maximum is", maximum,)
print("Minimum is", minimum)
print("Sum is", total)
print("Average is", average)

# GITHUB: yxsh7