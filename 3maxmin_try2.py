"""
To accept N numbers from user. Compute and display maximum in list, minimum in list, 
sum and average of numbers.
"""

from decimal import Decimal

# INPUT
input_string =input("Enter all numbers seperated by a Space")

# CONVERT STRING TO LIST
input_string = input_string.split()

num_list = []
for item in input_string: 
    num_list.append(int(item)) # CONVERT TO INT FROM STR

# CALCULATE
maximum = max(num_list)
minimum = min(num_list)
total = sum(num_list)
length = len(num_list)
average = total/length

#PRINT
print("Maximum is", maximum,)
print("Minimum is", minimum)
print("Sum is", total)
print("Average is", average)