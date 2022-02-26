"""
To accept a number from user and print digits of number in a reverse order
"""

num = int(input("Enter the number you want to reverse"))

reverse = (str(num)[::-1])

print("Reversed number is", reverse)