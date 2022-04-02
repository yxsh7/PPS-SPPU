"""
Write  a  python  program  that  accepts  a  string  from  user  and  perform  following  string 
operations
1.Calculate  length  of  string
2.String  reversal
3.Equality  check  of  two strings 
4.Check palindrome
5.Check substring
"""

# INPUT
str = input("Enter First string:")
str2 = input("Enter second string to check Equality & Substring:")

# LENGTH OF STRING
counter = 0
for s in str:
      counter = counter+1
print("Length of the First string is:", counter, "\n")

# REVSERSE OF STRING
print("Reverse of the First string is:",(str[::-1]), "\n")

# CHECK PALINDROME
reverse = str[::-1]
if str == reverse:
    print("First String is Palindrome \n")
else:
    print("First String is not Palindrome \n")

# CHECK SUBSTRING
if str.find(str2) != -1:
    # If find() doesn't find a match, it returns -1, otherwise it returns the left-most index of the substring in the larger string.
    print("Found Substring \n")
else:
    print("No Substring Found \n ")

# CHECK EQUALITY
if str == str2:
    print("Both strings are equal \n")
else:
    print("Both strings are unequal \n")

# GITHUB: yxsh7