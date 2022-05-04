"""
To accept N numbers from user. Compute and display maximum in list, minimum in list, 
sum and average of numbers.
"""
numberofelements = int(input("Enter No. of elements: "))

num_list = []

for i in range(numberofelements):
    num = int(input("Enter a number: "))
    num_list.append(num)

maximum = max(num_list)
minimum = min(num_list)
sum_list = sum(num_list)
length = len(num_list)
average = sum_list/length

print("Maximum in list: ", maximum)
print("Minimum in list: ", minimum)
print("Sum of elements in list: ", sum_list)
print("Average of numbers: ", average)