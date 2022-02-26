"""
To accept list of N integers and partition list into two sub lists even and odd numbers.
"""

input_string = input("Enter Numbers seperated by a Space \n")

input_string = input_string.split()

num_list = []

for item in input_string:
    num_list.append(int(item))

even_numbers = []
odd_numbers = []

for item in num_list:
    if (item % 2) == 0:
        even_numbers.append(int(item))
    else:
        odd_numbers.append(int(item))

print(even_numbers, odd_numbers)