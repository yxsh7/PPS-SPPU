"""
To  accept  two  numbers  from  user  and  compute  smallest  divisor  and  Greatest  Common 
Divisor of these two numbers
"""

import math

num1 = int(input("Enter First Number"))
num2 = int(input("Enter Second Number"))

lcm = math.lcm(num1,num2)
gcd = math.gcd(num1,num2)

print("LCM of the numbers is", lcm, "GCD of the numbers is", gcd)





