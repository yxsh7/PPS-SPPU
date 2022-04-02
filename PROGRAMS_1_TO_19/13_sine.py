"""
To accept the number of terms a finds the sum of sine series.
"""

import math

a = int(input("Enter a in degrees:"))
n = int(input("Number of terms:"))
s = 0

for i in range(n):
    sign = (-1)**i
    pi = 22/ 7
    y = a*(pi/180)
    s = s + ((y**(2.0*i+1))/math.factorial(2*i+1))*sign
print(round(s,2))

# GITHUB: yxsh7


